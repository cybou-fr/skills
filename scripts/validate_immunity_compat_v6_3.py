#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json, re

ROOT = Path(__file__).resolve().parents[1]
RISK = {"low", "medium", "high", "critical"}
VERDICTS = {"Allow", "Deny", "NeedsApproval"}

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    errors = []
    warnings = []

    manifest_path = ROOT / "immunity_mapping" / "immunity_manifest.yaml"
    if not manifest_path.exists():
        errors.append("missing immunity_mapping/immunity_manifest.yaml")
        print(json.dumps({"status":"fail","errors":errors,"warnings":warnings}, indent=2))
        return 1

    manifest = load_yaml(manifest_path)
    for k, rel in manifest.get("files", {}).items():
        if not (ROOT / rel).exists():
            errors.append(f"manifest references missing file {k}: {rel}")

    decision_mapping = load_yaml(ROOT / "immunity_mapping" / "decision_mapping.yaml").get("mapping", {})
    for src, dst in decision_mapping.items():
        if dst not in VERDICTS:
            errors.append(f"decision mapping {src} maps to invalid verdict {dst}")

    risk_mapping = load_yaml(ROOT / "immunity_mapping" / "risk_mapping.yaml").get("risk_levels", {})
    for risk, cfg in risk_mapping.items():
        if risk not in RISK:
            errors.append(f"invalid risk level {risk}")
        if cfg.get("runtime_default") not in VERDICTS:
            errors.append(f"risk {risk} invalid runtime_default {cfg.get('runtime_default')}")

    cmd = load_yaml(ROOT / "immunity_mapping" / "command_pattern_mapping.yaml")
    ids = set()
    for pat in cmd.get("patterns", []):
        pid = pat.get("id")
        if not pid:
            errors.append("command pattern missing id")
            continue
        if pid in ids:
            errors.append(f"duplicate command pattern id {pid}")
        ids.add(pid)
        if pat.get("verdict") not in VERDICTS:
            errors.append(f"{pid}: invalid verdict {pat.get('verdict')}")
        if pat.get("risk") not in RISK:
            errors.append(f"{pid}: invalid risk {pat.get('risk')}")
        try:
            re.compile(pat.get("regex", ""))
        except Exception as e:
            errors.append(f"{pid}: invalid regex: {e}")
        if pat.get("risk") == "critical" and pat.get("verdict") == "Allow":
            errors.append(f"{pid}: critical risk cannot map to Allow")

    sensitive = load_yaml(ROOT / "immunity_mapping" / "sensitive_targets.yaml")
    target_ids = set()
    for tgt in sensitive.get("targets", []):
        tid = tgt.get("id")
        if not tid:
            errors.append("sensitive target missing id")
            continue
        if tid in target_ids:
            errors.append(f"duplicate sensitive target id {tid}")
        target_ids.add(tid)
        if tgt.get("verdict") not in VERDICTS:
            errors.append(f"{tid}: invalid verdict {tgt.get('verdict')}")
        if tgt.get("risk") not in RISK:
            errors.append(f"{tid}: invalid risk {tgt.get('risk')}")
        if tgt.get("risk") == "critical" and tgt.get("verdict") == "Allow":
            errors.append(f"{tid}: critical target cannot map to Allow")

    # Ensure policy rule decisions are represented in immunity decision mapping.
    for p in (ROOT / "policy_rules").glob("*.yaml"):
        data = load_yaml(p)
        for rule in data.get("rules", []):
            dec = rule.get("decision")
            if dec and dec not in decision_mapping:
                errors.append(f"{p.relative_to(ROOT)}:{rule.get('id')}: policy decision not mapped for immunity: {dec}")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "command_patterns": len(cmd.get("patterns", [])),
        "sensitive_targets": len(sensitive.get("targets", [])),
        "decision_mappings": len(decision_mapping),
        "risk_levels": len(risk_mapping),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
