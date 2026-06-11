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
    if not matches: return {"verdict":"Allow","pattern":None,"matches":[]}
    best = sorted(matches, key=lambda p: RANK[p["verdict"]], reverse=True)[0]
    return {"verdict":best["verdict"],"pattern":best["id"],"matches":[m["id"] for m in matches]}
def main():
    errors, warnings = [], []
    patterns = load_yaml(ROOT / "immunity_mapping" / "command_pattern_mapping.yaml").get("patterns", [])
    suite = load_yaml(ROOT / "evals" / "immunity_adversarial" / "command_adversarial_v6_5.yaml")
    for sc in suite.get("scenarios", []):
        res = evaluate(sc["command"], patterns)
        if res["verdict"] != sc["expected_verdict"]:
            errors.append({"id":sc["id"],"field":"verdict","expected":sc["expected_verdict"],"actual":res})
        exp = sc.get("expected_pattern")
        if exp is not None and exp not in res["matches"]:
            errors.append({"id":sc["id"],"field":"pattern","expected":exp,"actual":res})
        if exp is None and res["pattern"] is not None:
            errors.append({"id":sc["id"],"field":"pattern","expected":None,"actual":res})
    result = {"status":"pass" if not errors else "fail","errors":errors,"warnings":warnings,"scenarios":len(suite.get("scenarios", [])),"patterns":len(patterns)}
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True)); return 1 if errors else 0
if __name__ == "__main__":
    raise SystemExit(main())
