#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.identity_secrets import classify_secret, review_oauth_app, review_key_policy, review_identity
from runtime_prototype.audit_store import AuditStore
from runtime_prototype.evidence_store import EvidenceStore

def emit(result, audit, evidence, event_type):
    rec = audit.append({"event_type": event_type, "result": result}, "identity_secret_event")
    evidence.capture_text(json.dumps(result, indent=2, ensure_ascii=False), event_type, {"audit_record_id": rec["record_id"]})
    print(json.dumps({"result": result, "audit_record": rec, "audit_verification": audit.verify(), "evidence_verification": evidence.verify()}, indent=2, ensure_ascii=False, sort_keys=True))

def main():
    parser = argparse.ArgumentParser(description="CYBOU identity/secrets/key-management prototype")
    parser.add_argument("--audit-store", default=str(ROOT / ".cybou_audit.jsonl"))
    parser.add_argument("--evidence-dir", default=str(ROOT / ".cybou_evidence"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("classify-secret")
    s.add_argument("--text", required=True)

    o = sub.add_parser("oauth-review")
    o.add_argument("--app-json", required=True)

    k = sub.add_parser("key-policy-review")
    k.add_argument("--policy-json", required=True)

    i = sub.add_parser("identity-review")
    i.add_argument("--principal-json", required=True)

    args = parser.parse_args()
    audit = AuditStore(args.audit_store)
    evidence = EvidenceStore(args.evidence_dir, audit)

    if args.cmd == "classify-secret":
        return emit(classify_secret(args.text), audit, evidence, "secret_exposure_triage")
    if args.cmd == "oauth-review":
        return emit(review_oauth_app(json.loads(args.app_json)), audit, evidence, "oauth_app_review")
    if args.cmd == "key-policy-review":
        return emit(review_key_policy(json.loads(args.policy_json)), audit, evidence, "kms_key_policy_review")
    if args.cmd == "identity-review":
        return emit(review_identity(json.loads(args.principal_json)), audit, evidence, "identity_review")

if __name__ == "__main__":
    raise SystemExit(main())
