#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse, time
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.forensics_case import CaseStore, reconstruct_timeline_from_text
from runtime_prototype.audit_store import AuditStore
from runtime_prototype.evidence_store import EvidenceStore

def main():
    parser = argparse.ArgumentParser(description="CYBOU forensics incident case prototype")
    parser.add_argument("--case-store", default=str(ROOT / ".cybou_cases.json"))
    parser.add_argument("--audit-store", default=str(ROOT / ".cybou_audit.jsonl"))
    parser.add_argument("--evidence-dir", default=str(ROOT / ".cybou_evidence"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("create")
    c.add_argument("--title", required=True)
    c.add_argument("--severity", default="medium")
    c.add_argument("--owner", default="analyst")

    n = sub.add_parser("note")
    n.add_argument("--case-id", required=True)
    n.add_argument("--text", required=True)
    n.add_argument("--author", default="analyst")

    e = sub.add_parser("evidence")
    e.add_argument("--case-id", required=True)
    e.add_argument("--source", required=True)
    e.add_argument("--content", required=True)
    e.add_argument("--collector", default="analyst")
    e.add_argument("--type", default="log")

    t = sub.add_parser("timeline")
    t.add_argument("--case-id", required=True)
    t.add_argument("--summary", required=True)
    t.add_argument("--source", required=True)
    t.add_argument("--timestamp", type=float, default=None)
    t.add_argument("--confidence", default="medium")

    imp = sub.add_parser("import-timeline")
    imp.add_argument("--case-id", required=True)
    imp.add_argument("--text", required=True)

    x = sub.add_parser("export")
    x.add_argument("--case-id", required=True)

    l = sub.add_parser("list")

    args = parser.parse_args()
    store = CaseStore(args.case_store)
    audit = AuditStore(args.audit_store)
    evidence = EvidenceStore(args.evidence_dir, audit)

    if args.cmd == "create":
        case = store.create_case(args.title, args.severity, args.owner)
        audit.append({"event_type": "case_created", "case_id": case["case_id"], "title": args.title}, "case_event")
        print(json.dumps(case, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "list":
        print(json.dumps(store.load(), indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "note":
        rec = store.add_note(args.case_id, args.text, args.author)
        audit.append({"event_type": "case_note_added", "case_id": args.case_id, "note_id": rec["note_id"]}, "case_event")
        print(json.dumps(rec, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "evidence":
        rec = store.attach_evidence(args.case_id, args.source, args.content, args.collector, args.type)
        audit_rec = audit.append({"event_type": "case_evidence_attached", "case_id": args.case_id, "evidence": rec}, "case_event")
        evidence.capture_text(json.dumps(rec, indent=2, ensure_ascii=False), "case_evidence_metadata", {"audit_record_id": audit_rec["record_id"], "case_id": args.case_id})
        print(json.dumps(rec, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "timeline":
        rec = store.add_timeline_event(args.case_id, args.timestamp or time.time(), args.summary, args.source, args.confidence)
        audit.append({"event_type": "case_timeline_event_added", "case_id": args.case_id, "event_id": rec["event_id"]}, "case_event")
        print(json.dumps(rec, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "import-timeline":
        imported = []
        for ev in reconstruct_timeline_from_text(args.case_id, args.text):
            imported.append(store.add_timeline_event(args.case_id, ev["timestamp"], ev["summary"], ev["source"], ev["confidence"]))
        audit.append({"event_type": "case_timeline_imported", "case_id": args.case_id, "count": len(imported)}, "case_event")
        print(json.dumps(imported, indent=2, ensure_ascii=False, sort_keys=True)); return 0

    if args.cmd == "export":
        exp = store.export_case(args.case_id)
        audit.append({"event_type": "case_exported", "case_id": args.case_id}, "case_event")
        print(json.dumps(exp, indent=2, ensure_ascii=False, sort_keys=True)); return 0

if __name__ == "__main__":
    raise SystemExit(main())
