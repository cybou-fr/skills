#!/usr/bin/env python3
from pathlib import Path
import sys, json, argparse
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.tool_router import ToolRouter

def main():
    parser = argparse.ArgumentParser(description="CYBOU tool router execution boundary prototype")
    parser.add_argument("--workdir", default=str(ROOT))
    parser.add_argument("--audit-store", default=str(ROOT / ".cybou_audit.jsonl"))
    parser.add_argument("--evidence-dir", default=str(ROOT / ".cybou_evidence"))
    parser.add_argument("--execute", action="store_true", help="execute allowlisted low-risk commands; default is dry-run")
    parser.add_argument("command")
    args = parser.parse_args()

    router = ToolRouter(ROOT, args.workdir, args.audit_store, args.evidence_dir)
    result = router.route(args.command, dry_run=not args.execute)
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
