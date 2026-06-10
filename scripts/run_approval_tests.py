#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys, tempfile
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.approval_store import ApprovalStore
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy

def load_yaml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def main():
    errors = []
    total = 0
    for path in sorted((ROOT / "approval_tests").glob("*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            with tempfile.TemporaryDirectory() as td:
                store = ApprovalStore(Path(td) / "approvals.json")
                adef = sc["approval"]
                store.create(adef["scope"], adef["approved_actions"], adef.get("ttl_seconds", 900), "test", sc["id"])
                action = normalize(sc["command"])
                approval = store.find_valid_for(action)
                decision = evaluate_policy(action, approval=approval, policy_root=ROOT)
                if decision.decision != sc["expected_decision"]:
                    errors.append({"scenario": sc["id"], "expected": sc["expected_decision"], "actual": decision.decision, "approval_used": approval.__dict__ if approval else None})
    print(json.dumps({"status": "pass" if not errors else "fail", "approval_scenarios": total, "errors": errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
