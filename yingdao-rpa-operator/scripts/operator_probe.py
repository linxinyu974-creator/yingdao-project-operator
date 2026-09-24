#!/usr/bin/env python3
"""Read-only ShadowBot capability/state probe for the consolidated skill."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess
from pathlib import Path

def candidates():
    found = shutil.which('shadowbot.shell-cli.exe') or shutil.which('shadowbot.shell-cli')
    out = [Path(found)] if found else []
    for root in (os.environ.get('ProgramFiles'), os.environ.get('ProgramW6432')):
        if root:
            out.extend(Path(root).glob('ShadowBot/*/shadowbot.shell-cli.exe'))
    return list(dict.fromkeys(p for p in out if p.is_file()))

def run(cli, args, timeout=20):
    env = os.environ.copy()
    if args and args[0] == 'studio':
        env['SWITCH_STUDIO_MCP_CLI_SUPPORT'] = '1'
    try:
        p = subprocess.run([str(cli), *args], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=timeout, env=env)
        return p.returncode, (p.stdout or p.stderr).strip()
    except Exception as exc:
        return 99, f'{type(exc).__name__}: {exc}'

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()

def quota(path):
    text = path.read_text(encoding='utf-8', errors='replace')
    records = []
    pattern = (r'(?P<ts>\d{4}-\d\d-\d\d[^\r\n]*?)(?:\[QuotaGate\].*?'
               r'usedToday=(?P<u>\d+),\s*dailyLimit=(?P<l>\d+).*?'
               r'Allowed=(?P<a>True|False))')
    for match in re.finditer(pattern, text):
        records.append({'timestamp': match.group('ts')[:19],
                        'usedToday': int(match.group('u')),
                        'dailyLimit': int(match.group('l')),
                        'allowed': match.group('a') == 'True'})
    if not records:
        return {'found': False, 'status': 'unknown'}
    record = records[-1]
    record.update(found=True,
                  remaining_observed=record['dailyLimit'] - record['usedToday'],
                  status='allowed' if record['allowed'] else 'denied',
                  note='observed log entry, not a live quota query')
    return record

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cli')
    parser.add_argument('--live', action='store_true')
    parser.add_argument('--quota-log', type=Path)
    args = parser.parse_args()
    paths = [Path(args.cli)] if args.cli else candidates()
    paths = [path for path in paths if path.is_file()]
    output = {'tool': 'operator_probe', 'read_only': True,
              'candidate_count': len(paths),
              'candidates': [{'path': str(path), 'sha256': digest(path)} for path in paths]}
    if len(paths) == 1:
        cli = paths[0]
        output['cli'] = str(cli)
        output['version'] = run(cli, ['--version'])[1]
        output['help_contracts'] = {}
        for command in (['--help'], ['studio', 'open', '--help'],
                        ['console', 'task', 'run', '--help'],
                        ['studio', 'codeflow', 'edit', '--help']):
            code, text = run(cli, command)
            output['help_contracts'][' '.join(command)] = {'returncode': code,
                                                            'has_output': bool(text)}
        if args.live:
            for name, command in (('health', ['system', 'health']),
                                  ('state', ['system', 'state']),
                                  ('auth', ['auth', 'current'])):
                code, text = run(cli, command)
                try:
                    payload = json.loads(text)
                except json.JSONDecodeError:
                    payload = {}
                data = payload.get('data', {}) if isinstance(payload, dict) else {}
                if name == 'state' and isinstance(data, dict):
                    data = {key: data.get(key) for key in (
                        'hasRunningTask', 'hasStudioOpened', 'isStudioBusy',
                        'isIdle', 'currentMode', 'currentModule', 'networkStatus')
                            if key in data}
                else:
                    data = {'ok': payload.get('ok') if isinstance(payload, dict) else None,
                            'message': payload.get('message') if isinstance(payload, dict) else None}
                output[name] = {'returncode': code, 'data': data}
    if args.quota_log:
        output['quota'] = quota(args.quota_log)
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
