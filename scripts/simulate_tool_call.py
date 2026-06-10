#!/usr/bin/env python3
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy
from runtime_prototype.audit import audit_from_decision
from runtime_prototype.redaction import redact
if len(sys.argv)<2:
    print("Usage: simulate_tool_call.py '<command>' [mock_output]", file=sys.stderr); raise SystemExit(2)
a=normalize(sys.argv[1]); d=evaluate_policy(a, policy_root=ROOT); out,red=redact(sys.argv[2] if len(sys.argv)>2 else "mock output")
print(json.dumps({"would_execute":d.decision in ["allow_read_only","allow_read_only_and_redact","allow_with_approval"],"normalized_action":a.to_dict(),"policy_decision":d.to_dict(),"mock_output":out,"redaction_applied":red,"audit_event":audit_from_decision(d).to_dict()},indent=2,ensure_ascii=False,sort_keys=True))
