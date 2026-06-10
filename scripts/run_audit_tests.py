#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys, tempfile
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.audit_store import AuditStore
from runtime_prototype.evidence_store import EvidenceStore
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy
from runtime_prototype.audit import audit_from_decision

def load_yaml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def main():
    errors = []
    total = 0
    for path in sorted((ROOT / "audit_tests").glob("*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            with tempfile.TemporaryDirectory() as td:
                audit = AuditStore(Path(td) / "audit.jsonl")
                evidence = EvidenceStore(Path(td) / "evidence", audit)
                if "actions" in sc:
                    for a in sc["actions"]:
                        if "append" in a:
                            audit.append(a["append"], "audit_event")
                    result = audit.verify()
                    if result["valid"] != sc["expected"]["valid"] or result["record_count"] != sc["expected"]["record_count"]:
                        errors.append({"scenario": sc["id"], "actual": result})
                elif "evidence_text" in sc:
                    rec = evidence.capture_text(sc["evidence_text"])
                    ev = evidence.verify()
                    if rec["redaction_applied"] != sc["expected"]["redaction_applied"] or ev["valid"] != sc["expected"]["evidence_valid"]:
                        errors.append({"scenario": sc["id"], "record": rec, "verify": ev})
                elif "command" in sc:
                    action = normalize(sc["command"])
                    decision = evaluate_policy(action, policy_root=ROOT)
                    audit.append(audit_from_decision(decision).to_dict(), "policy_decision")
                    ver = audit.verify()
                    if ver["valid"] != sc["expected"]["audit_valid"] or decision.decision != sc["expected"]["decision"]:
                        errors.append({"scenario": sc["id"], "decision": decision.decision, "verify": ver})
                elif sc.get("tamper"):
                    audit.append({"event_type": "test", "message": "original"}, "audit_event")
                    # Modify line without recomputing hash.
                    p = Path(td) / "audit.jsonl"
                    line = p.read_text(encoding="utf-8")
                    p.write_text(line.replace("original", "tampered"), encoding="utf-8")
                    ver = audit.verify()
                    if ver["valid"] != sc["expected"]["valid"]:
                        errors.append({"scenario": sc["id"], "verify": ver})
    print(json.dumps({"status": "pass" if not errors else "fail", "audit_scenarios": total, "errors": errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
