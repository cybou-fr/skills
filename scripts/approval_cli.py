#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.approval_store import ApprovalStore
from runtime_prototype.normalizers import normalize
from runtime_prototype.policy import evaluate_policy
from runtime_prototype.audit import audit_from_decision

def main():
    parser = argparse.ArgumentParser(description="CYBOU approval store prototype")
    parser.add_argument("--store", default=str(ROOT / ".cybou_approvals.json"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("create")
    c.add_argument("--scope", required=True)
    c.add_argument("--actions", required=True)
    c.add_argument("--ttl", type=int, default=900)
    c.add_argument("--by", default="operator")
    c.add_argument("--text", default="")

    sub.add_parser("list")

    r = sub.add_parser("revoke")
    r.add_argument("approval_id")

    e = sub.add_parser("evaluate")
    e.add_argument("command")

    args = parser.parse_args()
    store = ApprovalStore(args.store)

    if args.cmd == "create":
        approval = store.create(args.scope, [x.strip() for x in args.actions.split(",") if x.strip()], args.ttl, args.by, args.text)
        print(json.dumps(approval.__dict__, indent=2, ensure_ascii=False, sort_keys=True)); return 0
    if args.cmd == "list":
        print(json.dumps([a.__dict__ for a in store.load()], indent=2, ensure_ascii=False, sort_keys=True)); return 0
    if args.cmd == "revoke":
        print(json.dumps({"approval_id": args.approval_id, "revoked": store.revoke(args.approval_id)}, indent=2, ensure_ascii=False)); return 0
    if args.cmd == "evaluate":
        action = normalize(args.command)
        approval = store.find_valid_for(action)
        decision = evaluate_policy(action, approval=approval, policy_root=ROOT)
        audit = audit_from_decision(decision)
        print(json.dumps({"approval_used": approval.__dict__ if approval else None, "normalized_action": action.to_dict(), "policy_decision": decision.to_dict(), "audit_event": audit.to_dict()}, indent=2, ensure_ascii=False, sort_keys=True)); return 0

if __name__ == "__main__":
    raise SystemExit(main())
