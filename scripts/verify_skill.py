#!/usr/bin/env python3
"""Read-only validation of one skill and optional installed copy."""
from __future__ import annotations
import argparse,ast,hashlib,json,re
from pathlib import Path
def digest(p):
 h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def files(root):
 return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts and "structured-thinking-toolkit" not in p.parts and "__pycache__" not in p.parts]
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--root",type=Path,required=True); ap.add_argument("--installed",type=Path); n=ap.parse_args(); root=n.root; errors=[]
 t=(root/"SKILL.md").read_text(encoding="utf-8")
 if not re.match(r"^---\s*\nname:\s*\S+\s*\ndescription:\s*.+?\n",t,re.S): errors.append("invalid frontmatter")
 for ref in re.findall(r"\]\((references/[^)]+|scripts/[^)]+)",t):
  if not (root/ref).is_file(): errors.append("missing resource: "+ref)
 for p in (root/"scripts").glob("*.py") if (root/"scripts").is_dir() else []:
  try: ast.parse(p.read_text(encoding="utf-8"),filename=str(p))
  except Exception as e: errors.append(f"syntax {p}: {e}")
 out={"ok":not errors,"errors":errors,"root":str(root),"file_count":len(files(root))}
 if n.installed:
  a={str(p.relative_to(root)):digest(p) for p in files(root)}; b={str(p.relative_to(n.installed)):digest(p) for p in files(n.installed)}
  out.update(missing_in_installed=sorted(set(a)-set(b)),extra_in_installed=sorted(set(b)-set(a)),different_files=sorted(k for k in a.keys()&b.keys() if a[k]!=b[k]))
  out["copies_equal"]=not(out["missing_in_installed"] or out["extra_in_installed"] or out["different_files"]); out["ok"]=out["ok"] and out["copies_equal"]
 print(json.dumps(out,ensure_ascii=False,indent=2)); return 0 if out["ok"] else 1
if __name__=="__main__": raise SystemExit(main())
