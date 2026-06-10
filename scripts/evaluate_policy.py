#!/usr/bin/env python3
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy
from runtime_prototype.audit import audit_from_decision
if len(sys.argv)<2:
    print("Usage: evaluate_policy.py '<command>' [tool_hint]", file=sys.stderr); raise SystemExit(2)
a=normalize(sys.argv[1], sys.argv[2] if len(sys.argv)>2 else None); d=evaluate_policy(a, policy_root=ROOT); ev=audit_from_decision(d)
print(json.dumps({"normalized_action":a.to_dict(),"policy_decision":d.to_dict(),"audit_event":ev.to_dict()},indent=2,ensure_ascii=False,sort_keys=True))
