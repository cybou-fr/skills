#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.audit_store import AuditStore
from runtime_prototype.evidence_store import EvidenceStore
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy
from runtime_prototype.audit import audit_from_decision

def main():
    parser = argparse.ArgumentParser(description="CYBOU durable audit/evidence store prototype")
    parser.add_argument("--audit-store", default=str(ROOT / ".cybou_audit.jsonl"))
    parser.add_argument("--evidence-dir", default=str(ROOT / ".cybou_evidence"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("append")
    a.add_argument("--event-type", default="manual_event")
    a.add_argument("--message", required=True)

    sub.add_parser("list")
    sub.add_parser("verify")
    sub.add_parser("export")

    e = sub.add_parser("capture-evidence")
    e.add_argument("--text", required=True)
    e.add_argument("--type", default="tool_output")

    ev = sub.add_parser("evaluate")
    ev.add_argument("command")

    args = parser.parse_args()
    audit = AuditStore(args.audit_store)

    if args.cmd == "append":
        rec = audit.append({"event_type": args.event_type, "message": args.message}, "audit_event")
        print(json.dumps(rec, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "list":
        print(json.dumps(audit.list(), indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "verify":
        evidence = EvidenceStore(args.evidence_dir)
        print(json.dumps({"audit": audit.verify(), "evidence": evidence.verify()}, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "export":
        evidence = EvidenceStore(args.evidence_dir)
        print(json.dumps({"audit": audit.export(), "evidence": evidence.list(), "evidence_verification": evidence.verify()}, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "capture-evidence":
        evidence = EvidenceStore(args.evidence_dir, audit)
        rec = evidence.capture_text(args.text, args.type)
        print(json.dumps(rec, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "evaluate":
        action = normalize(args.command)
        decision = evaluate_policy(action, policy_root=ROOT)
        event = audit_from_decision(decision)
        rec = audit.append(event.to_dict(), "policy_decision")
        print(json.dumps({"normalized_action": action.to_dict(), "policy_decision": decision.to_dict(), "audit_record": rec}, indent=2, ensure_ascii=False, sort_keys=True)); return 0

if __name__ == "__main__":
    raise SystemExit(main())
