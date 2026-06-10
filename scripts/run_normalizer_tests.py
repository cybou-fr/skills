#!/usr/bin/env python3
from pathlib import Path
import json, yaml, sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime_prototype.normalizers import normalize

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    full = "--full" in sys.argv
    errors = []
    results = []
    total = 0
    for path in sorted((ROOT / "normalizer_tests").glob("runtime_normalizers_*.yaml")):
        data = load_yaml(path)
        for sc in data.get("scenarios", []):
            total += 1
            exp = sc.get("expected_normalized_action", {}) or {}
            action = normalize(sc.get("input", ""), exp.get("tool"))
            actual = action.to_dict()
            mismatches = []
            for key, expected in exp.items():
                if key == "side_effects_contains":
                    missing = [x for x in expected if x not in actual.get("side_effects", [])]
                    if missing:
                        mismatches.append({"field": key, "missing": missing, "actual": actual.get("side_effects")})
                elif key == "args_contains":
                    for ak, av in expected.items():
                        if actual.get("args", {}).get(ak) != av:
                            mismatches.append({"field": f"args.{ak}", "expected": av, "actual": actual.get("args", {}).get(ak)})
                else:
                    if actual.get(key) != expected:
                        mismatches.append({"field": key, "expected": expected, "actual": actual.get(key)})
            if mismatches:
                errors.append({"file": path.name, "scenario": sc.get("id"), "mismatches": mismatches})
            if full:
                results.append({"file": path.name, "id": sc.get("id"), "input": sc.get("input"), "actual": actual, "mismatches": mismatches})
    report = {"status": "pass" if not errors else "fail", "normalizer_scenarios": total, "errors": errors}
    if full:
        report["results"] = results
    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
