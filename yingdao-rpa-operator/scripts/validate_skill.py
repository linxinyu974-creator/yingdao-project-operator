#!/usr/bin/env python3
"""Validate the consolidated skill and an optional installed copy."""
from __future__ import annotations
import argparse, ast, hashlib, json, re
from pathlib import Path

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def files(root):
    return [path for path in root.rglob('*') if path.is_file() and '.git' not in path.parts]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--installed', type=Path)
    args = parser.parse_args()
    root = args.root
    errors = []
    skill = root / 'SKILL.md'
    text = skill.read_text(encoding='utf-8')
    if not re.match(r'^---\s*\nname:\s*\S+\s*\ndescription:\s*.+?\nversion:\s*\S+\s*\n---', text, re.S):
        errors.append('invalid frontmatter')
    for reference in re.findall(r'\]\((references/[^)]+|scripts/[^)]+)', text):
        if not (root / reference).is_file():
            errors.append('missing resource: ' + reference)
    for path in (root / 'scripts').glob('*.py'):
        try:
            ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        except Exception as exc:
            errors.append(f'syntax {path}: {exc}')
    result = {'ok': not errors, 'errors': errors, 'root': str(root),
              'file_count': len(files(root))}
    if args.installed:
        local = {str(path.relative_to(root)): digest(path) for path in files(root)}
        installed = {str(path.relative_to(args.installed)): digest(path)
                     for path in files(args.installed)}
        result.update(missing_in_installed=sorted(set(local) - set(installed)),
                      extra_in_installed=sorted(set(installed) - set(local)),
                      different_files=sorted(key for key in local.keys() & installed.keys()
                                             if local[key] != installed[key]))
        result['copies_equal'] = not any(result[key] for key in (
            'missing_in_installed', 'extra_in_installed', 'different_files'))
        result['ok'] = result['ok'] and result['copies_equal']
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
