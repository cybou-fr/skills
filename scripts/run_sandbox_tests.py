#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys, tempfile
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.tool_router import ToolRouter

def load_yaml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def main():
    errors = []
    total = 0
    for path in sorted((ROOT / "sandbox_tests").glob("*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            with tempfile.TemporaryDirectory() as td:
                router = ToolRouter(ROOT, ROOT, Path(td)/"audit.jsonl", Path(td)/"evidence")
                result = router.route(sc["command"], dry_run=True)
                exp = sc["expected"]
                mismatches = []
                if result["sandbox_profile"] != exp["sandbox_profile"]:
                    mismatches.append({"field":"sandbox_profile","expected":exp["sandbox_profile"],"actual":result["sandbox_profile"]})
                if result["execution_result"]["would_execute"] != exp["would_execute"]:
                    mismatches.append({"field":"would_execute","expected":exp["would_execute"],"actual":result["execution_result"]["would_execute"]})
                if "executed" in exp and result["execution_result"]["executed"] != exp["executed"]:
                    mismatches.append({"field":"executed","expected":exp["executed"],"actual":result["execution_result"]["executed"]})
                if not result["audit_verification"]["valid"] or not result["evidence_verification"]["valid"]:
                    mismatches.append({"field":"verification","audit":result["audit_verification"],"evidence":result["evidence_verification"]})
                if mismatches:
                    errors.append({"scenario":sc["id"],"mismatches":mismatches})
    print(json.dumps({"status":"pass" if not errors else "fail","sandbox_scenarios":total,"errors":errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
