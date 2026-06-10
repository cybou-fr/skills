#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.identity_secrets import classify_secret, review_oauth_app, review_key_policy, review_identity

ORDER = {"low":1, "medium":2, "high":3, "critical":4}

def load_yaml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def main():
    errors = []
    total = 0
    for path in sorted((ROOT / "identity_secrets_tests").glob("*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            exp = sc["expected"]
            if "secret_text" in sc:
                result = classify_secret(sc["secret_text"])
                if ORDER[result["severity"]] < ORDER[exp["severity"]] or result["finding_count"] < exp["finding_count_min"]:
                    errors.append({"scenario":sc["id"],"expected":exp,"actual":result})
            elif "oauth_app" in sc:
                result = review_oauth_app(sc["oauth_app"])
                if ORDER[result["severity"]] < ORDER[exp["severity"]] or len(result["risky_scopes"]) < exp["risky_scope_min"]:
                    errors.append({"scenario":sc["id"],"expected":exp,"actual":result})
            elif "key_policy" in sc:
                result = review_key_policy(sc["key_policy"])
                if ORDER[result["severity"]] < ORDER[exp["severity"]] or result["finding_count"] < exp["finding_count_min"]:
                    errors.append({"scenario":sc["id"],"expected":exp,"actual":result})
            elif "principal" in sc:
                result = review_identity(sc["principal"])
                if ORDER[result["severity"]] < ORDER[exp["severity"]] or exp["reason"] not in result["reasons"]:
                    errors.append({"scenario":sc["id"],"expected":exp,"actual":result})
    print(json.dumps({"status":"pass" if not errors else "fail","identity_secrets_scenarios":total,"errors":errors}, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
