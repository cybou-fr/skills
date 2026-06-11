#!/usr/bin/env python3
from pathlib import Path
import yaml, json

ROOT = Path(__file__).resolve().parents[1]
def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
def main():
    errors, warnings = [], []
    manifest_path = ROOT / "evals" / "manifest.yaml"
    if not manifest_path.exists():
        errors.append("missing evals/manifest.yaml")
        print(json.dumps({"status":"fail","errors":errors,"warnings":warnings}, indent=2)); return 1
    manifest = load_yaml(manifest_path)
    suite_ids, total = set(), 0
    for suite in manifest.get("suites", []):
        sid, path = suite.get("id"), suite.get("path")
        if not sid or not path:
            errors.append(f"malformed suite entry: {suite}"); continue
        if sid in suite_ids: errors.append(f"duplicate suite id: {sid}")
        suite_ids.add(sid)
        sp = ROOT / path
        if not sp.exists():
            errors.append(f"suite path missing: {path}"); continue
        suite_total = 0
        for f in sp.rglob("*.yaml"):
            data = load_yaml(f)
            for sc in data.get("scenarios", []):
                suite_total += 1
                if not sc.get("id"): errors.append(f"{f.relative_to(ROOT)} scenario missing id")
        if suite_total == 0: warnings.append(f"suite has no scenarios: {sid}")
        total += suite_total
    required = {"eval_run_id", "suite_id", "scenario_id", "result", "duration_ms"}
    must = set(manifest.get("runner_contract", {}).get("must_record", []))
    if required - must: errors.append(f"runner_contract missing required fields: {sorted(required-must)}")
    if manifest.get("runner_contract", {}).get("success_does_not_imply_trust") is not True: errors.append("success_does_not_imply_trust must be true")
    if manifest.get("runner_contract", {}).get("learning_requires_gate") is not True: errors.append("learning_requires_gate must be true")
    result = {"status":"pass" if not errors else "fail","errors":errors,"warnings":warnings,"suites":len(suite_ids),"scenarios":total}
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True)); return 1 if errors else 0
if __name__ == "__main__":
    raise SystemExit(main())
