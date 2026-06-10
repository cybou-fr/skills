#!/usr/bin/env python3

from pathlib import Path
import sys,json,yaml
ROOT=Path(__file__).resolve().parents[1]
def y(p): return yaml.safe_load(open(p,encoding="utf-8"))
if len(sys.argv)<2:
    print("Usage: route_task.py '<task>'", file=sys.stderr); raise SystemExit(2)
text=sys.argv[1].lower(); reg=y(ROOT/"registry.yaml"); scored=[]
for s in reg.get("skills",[]):
    score=sum(5 for t in s.get("triggers",[]) if t.lower() in text)+sum(1 for part in s["id"].split("-") if part in text)
    if score: scored.append((score,s["id"]))
print(json.dumps({"task":sys.argv[1],"selected_skills":[sid for _,sid in sorted(scored,reverse=True)[:8]] or ["task-classification","risk-and-approval"]},indent=2,ensure_ascii=False))
