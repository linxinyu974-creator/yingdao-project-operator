#!/usr/bin/env python3
"""Offline regression tests for the consolidated operator scripts."""
from pathlib import Path
import importlib.util
import tempfile

path = Path(__file__).with_name('operator_probe.py')
spec = importlib.util.spec_from_file_location('probe', path)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

def main():
    with tempfile.TemporaryDirectory() as folder:
        log = Path(folder) / 'log'
        log.write_text('2026-09-10 09:58:26 [QuotaGate] runId=x, usedToday=4, dailyLimit=5, tipText=x Allowed=True\n', encoding='utf-8')
        result = probe.quota(log)
        assert result['status'] == 'allowed' and result['remaining_observed'] == 1
        log.write_text('2026-09-10 [QuotaGate] usedToday=5, dailyLimit=5, Allowed=False\n', encoding='utf-8')
        assert probe.quota(log)['status'] == 'denied'
        log.write_text('business error only', encoding='utf-8')
        assert probe.quota(log)['status'] == 'unknown'
    print('consolidated operator tools: PASS')

if __name__ == '__main__':
    main()
