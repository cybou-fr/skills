#!/usr/bin/env python3
from pathlib import Path
import yaml, json, re

ROOT = Path(__file__).resolve().parents[1]
RANK = {"Allow": 1, "NeedsApproval": 2, "Deny": 3}
def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
def evaluate(command, patterns):
    matches = [p for p in patterns if re.search(p["regex"], command)]
    if not matches:
        return {"verdict": "Allow", "pattern": None, "matches": []}
    best = sorted(matches, key=lambda p: RANK[p["verdict"]], reverse=True)[0]
    return {"verdict": best["verdict"], "pattern": best["id"], "matches": [m["id"] for m in matches]}
def main():
    errors, warnings = [], []
    required = [
        "immunity_mapping/argv_normalization_contract.yaml",
        "immunity_mapping/destructive_command_tests.yaml",
        "immunity_mapping/cloud_cli_dangerous_ops.yaml",
        "immunity_mapping/package_publish_policy.yaml",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"missing v6.7 hardening file: {rel}")
    contract = load_yaml(ROOT / "immunity_mapping" / "argv_normalization_contract.yaml")
    if contract.get("core_principle") != "Regex is metadata. Rust normalizer is authority.":
        errors.append("argv normalization core principle mismatch")
    if contract.get("on_parse_failure") != "NeedsApproval":
        errors.append("on_parse_failure must be NeedsApproval")
    patterns = load_yaml(ROOT / "immunity_mapping" / "command_pattern_mapping.yaml").get("patterns", [])
    ids = set()
    for pat in patterns:
        pid = pat.get("id")
        if pid in ids:
            errors.append(f"duplicate command pattern id {pid}")
        ids.add(pid)
        try:
            re.compile(pat.get("regex", ""))
        except Exception as e:
            errors.append(f"{pid}: invalid regex {e}")
    tests = load_yaml(ROOT / "immunity_mapping" / "destructive_command_tests.yaml").get("scenarios", [])
    for sc in tests:
        res = evaluate(sc["command"], patterns)
        if res["verdict"] != sc["expected_verdict"]:
            errors.append({"id": sc["id"], "field": "verdict", "expected": sc["expected_verdict"], "actual": res})
        exp = sc.get("expected_pattern")
        if exp is not None and exp not in res["matches"]:
            errors.append({"id": sc["id"], "field": "pattern", "expected": exp, "actual": res})
        if exp is None and res["pattern"] is not None:
            errors.append({"id": sc["id"], "field": "pattern", "expected": None, "actual": res})
    cloud = load_yaml(ROOT / "immunity_mapping" / "cloud_cli_dangerous_ops.yaml")
    if cloud.get("normalizer_required") is not True:
        errors.append("cloud_cli_dangerous_ops must require normalizer")
    package = load_yaml(ROOT / "immunity_mapping" / "package_publish_policy.yaml")
    if not package.get("publish_operations"):
        errors.append("package_publish_policy missing publish_operations")
    result = {"status": "pass" if not errors else "fail", "errors": errors, "warnings": warnings, "destructive_scenarios": len(tests), "command_patterns": len(patterns), "cloud_ops": len(cloud.get("dangerous_operations", [])), "publish_ops": len(package.get("publish_operations", []))}
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0
if __name__ == "__main__":
    raise SystemExit(main())
