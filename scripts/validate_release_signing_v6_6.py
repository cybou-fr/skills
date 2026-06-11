#!/usr/bin/env python3
from pathlib import Path
import yaml, json

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    errors = []
    warnings = []

    required = [
        "integration/signing_policy.yaml",
        "integration/trusted_publishers.yaml",
        "integration/provenance_manifest.yaml",
        "integration/signature_status.yaml",
        "integration/release_signature.placeholder",
        "schemas/signing_policy.schema.json",
        "schemas/trusted_publishers.schema.json",
        "schemas/provenance_manifest.schema.json",
        "schemas/signature_status.schema.json",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"missing release-signing file: {rel}")

    if errors:
        print(json.dumps({"status": "fail", "errors": errors, "warnings": warnings}, indent=2, ensure_ascii=False))
        return 1

    policy = load_yaml(ROOT / "integration" / "signing_policy.yaml")
    publishers = load_yaml(ROOT / "integration" / "trusted_publishers.yaml")
    provenance = load_yaml(ROOT / "integration" / "provenance_manifest.yaml")
    status = load_yaml(ROOT / "integration" / "signature_status.yaml")

    if policy.get("signature_required", {}).get("enterprise") is not True:
        errors.append("enterprise signature_required must be true")
    if policy.get("loader_policy", {}).get("enterprise_unsigned") != "deny":
        errors.append("enterprise_unsigned policy must be deny")
    if policy.get("loader_policy", {}).get("enterprise_bad_signature") != "deny":
        errors.append("enterprise_bad_signature policy must be deny")
    if policy.get("loader_policy", {}).get("community_unsigned") != "warn_and_metadata_only":
        errors.append("community_unsigned policy must be warn_and_metadata_only")

    if not publishers.get("publishers"):
        errors.append("trusted_publishers must list at least one publisher")

    if provenance.get("integrity", {}).get("file_hashes") != "integration/file_hashes.yaml":
        errors.append("provenance must reference integration/file_hashes.yaml")
    if provenance.get("integrity", {}).get("signature_policy") != "integration/signing_policy.yaml":
        errors.append("provenance must reference integration/signing_policy.yaml")

    if status.get("status") == "unsigned_placeholder":
        warnings.append("release is unsigned_placeholder; enterprise loader must deny until signed")
        if status.get("enterprise_loader_behavior") != "deny_until_signed":
            errors.append("unsigned placeholder must set enterprise_loader_behavior=deny_until_signed")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "publishers": len(publishers.get("publishers", [])),
        "signature_status": status.get("status"),
        "enterprise_requires_signature": policy.get("signature_required", {}).get("enterprise"),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
