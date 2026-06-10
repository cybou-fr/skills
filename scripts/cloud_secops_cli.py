#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.cloud_secops import triage_cloud_event, least_privilege_review
from runtime_prototype.audit_store import AuditStore
from runtime_prototype.evidence_store import EvidenceStore

def main():
    parser = argparse.ArgumentParser(description="CYBOU Cloud SecOps prototype")
    parser.add_argument("--audit-store", default=str(ROOT / ".cybou_audit.jsonl"))
    parser.add_argument("--evidence-dir", default=str(ROOT / ".cybou_evidence"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("triage-event")
    t.add_argument("--event-json", required=True)

    p = sub.add_parser("iam-review")
    p.add_argument("--policy-json", required=True)

    args = parser.parse_args()
    audit = AuditStore(args.audit_store)
    evidence = EvidenceStore(args.evidence_dir, audit)

    if args.cmd == "triage-event":
        event = json.loads(args.event_json)
        result = triage_cloud_event(event)
        rec = audit.append({"event_type":"cloud_secops_triage","result":result}, "cloud_secops_event")
        evidence.capture_text(json.dumps(result, indent=2, ensure_ascii=False), "cloud_secops_triage", {"audit_record_id": rec["record_id"]})
        print(json.dumps({"result":result, "audit_record":rec, "audit_verification":audit.verify(), "evidence_verification":evidence.verify()}, indent=2, ensure_ascii=False, sort_keys=True))
        return 0

    if args.cmd == "iam-review":
        policy = json.loads(args.policy_json)
        result = least_privilege_review(policy)
        rec = audit.append({"event_type":"cloud_iam_review","result":result}, "cloud_secops_event")
        evidence.capture_text(json.dumps(result, indent=2, ensure_ascii=False), "cloud_iam_review", {"audit_record_id": rec["record_id"]})
        print(json.dumps({"result":result, "audit_record":rec, "audit_verification":audit.verify(), "evidence_verification":evidence.verify()}, indent=2, ensure_ascii=False, sort_keys=True))
        return 0

if __name__ == "__main__":
    raise SystemExit(main())
