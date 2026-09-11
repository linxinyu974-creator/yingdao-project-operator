#!/usr/bin/env python3
"""Offline regression tests for operator tools."""
from __future__ import annotations
import importlib.util,tempfile
from pathlib import Path
p=Path(__file__).with_name("operator_probe.py"); s=importlib.util.spec_from_file_location("probe",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def main():
 with tempfile.TemporaryDirectory() as td:
  f=Path(td)/"log"; f.write_text("2026-09-10 09:58:26 [QuotaGate] runId=x, usedToday=4, dailyLimit=5, tipText=x Allowed=True\n",encoding="utf-8")
  q=m.quota(f); assert q["status"]=="allowed" and q["remaining_observed"]==1
  f.write_text("2026-09-10 [QuotaGate] usedToday=5, dailyLimit=5, Allowed=False\n",encoding="utf-8"); assert m.quota(f)["status"]=="denied"
  f.write_text("business error only",encoding="utf-8"); assert m.quota(f)["status"]=="unknown"
 print("offline operator tools: PASS")
if __name__=="__main__": main()
