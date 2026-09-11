#!/usr/bin/env python3
"""Read-only ShadowBot capability/state probe."""
from __future__ import annotations
import argparse,hashlib,json,os,re,shutil,subprocess
from pathlib import Path
def candidates():
    out=[]; found=shutil.which("shadowbot.shell-cli.exe") or shutil.which("shadowbot.shell-cli")
    if found: out.append(Path(found))
    for root in (os.environ.get("ProgramFiles"),os.environ.get("ProgramW6432")):
        if root: out.extend(Path(root).glob("ShadowBot/*/shadowbot.shell-cli.exe"))
    return list(dict.fromkeys(p for p in out if p.is_file()))
def run(cli,args,timeout=20):
    env=os.environ.copy()
    if args and args[0]=="studio": env["SWITCH_STUDIO_MCP_CLI_SUPPORT"]="1"
    try:
        p=subprocess.run([str(cli),*args],capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=timeout,env=env)
        return p.returncode,(p.stdout or p.stderr).strip()
    except Exception as e: return 99,f"{type(e).__name__}: {e}"
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return h.hexdigest()
def obj(s):
    try: return json.loads(s)
    except Exception: return None
def quota(path):
    text=path.read_text(encoding="utf-8",errors="replace"); records=[]
    pat=r"(?P<ts>\d{4}-\d\d-\d\d[^\r\n]*?)(?:\[QuotaGate\].*?usedToday=(?P<u>\d+),\s*dailyLimit=(?P<l>\d+).*?Allowed=(?P<a>True|False))"
    for m in re.finditer(pat,text):
        records.append({"timestamp":m.group("ts")[:19],"usedToday":int(m.group("u")),"dailyLimit":int(m.group("l")),"allowed":m.group("a")=="True"})
    if not records:return {"found":False,"status":"unknown"}
    r=records[-1]; r.update(found=True,remaining_observed=r["dailyLimit"]-r["usedToday"],status="allowed" if r["allowed"] else "denied",note="observed log entry, not a live quota query"); return r
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--cli"); ap.add_argument("--live",action="store_true"); ap.add_argument("--quota-log",type=Path); n=ap.parse_args()
    cs=[Path(n.cli)] if n.cli else candidates(); cs=[p for p in cs if p.is_file()]
    out={"tool":"operator_probe","read_only":True,"candidate_count":len(cs),"candidates":[{"path":str(p),"sha256":digest(p)} for p in cs]}
    if len(cs)==1:
        c=cs[0]; out.update(cli=str(c),version=run(c,["--version"])[1]); out["help_contracts"]={}
        for a in (["--help"],["studio","open","--help"],["console","task","run","--help"],["studio","codeflow","edit","--help"]):
            rc,s=run(c,a); out["help_contracts"][" ".join(a)]={"returncode":rc,"has_output":bool(s)}
        if n.live:
            for k,a in (("health",["system","health"]),("state",["system","state"]),("auth",["auth","current"])):
                rc,s=run(c,a); x=obj(s); d=x.get("data") if isinstance(x,dict) else {}
                if k=="state" and isinstance(d,dict): d={z:d.get(z) for z in ("hasRunningTask","hasStudioOpened","isStudioBusy","isIdle","currentMode","currentModule","networkStatus") if z in d}
                else: d={"ok":x.get("ok") if isinstance(x,dict) else None,"message":x.get("message") if isinstance(x,dict) else None}
                out[k]={"returncode":rc,"data":d}
    if n.quota_log: out["quota"]=quota(n.quota_log)
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
