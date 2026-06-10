#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.cloud_secops import triage_cloud_event, least_privilege_review

ORDER = {"low":1, "medium":2, "high":3, "critical":4}

def load_yaml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def main():
    errors = []
    total = 0
    for path in sorted((ROOT / "cloud_secops_tests").glob("*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            exp = sc["expected"]
            if "event" in sc:
                result = triage_cloud_event(sc["event"])
                if result["provider"] != exp["provider"] or ORDER[result["severity"]] < ORDER[exp["severity"]]:
                    errors.append({"scenario":sc["id"],"expected":exp,"actual":result})
            elif "policy" in sc:
                result = least_privilege_review(sc["policy"])
                if result["finding_count"] < exp["finding_count_min"]:
                    errors.append({"scenario":sc["id"],"expected":exp,"actual":result})
    print(json.dumps({"status":"pass" if not errors else "fail","cloud_secops_scenarios":total,"errors":errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
