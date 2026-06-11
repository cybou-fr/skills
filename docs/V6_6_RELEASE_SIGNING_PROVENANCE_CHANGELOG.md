# v6.6 Release Signing & Provenance Changelog

## Added

- `integration/signing_policy.yaml`
- `integration/trusted_publishers.yaml`
- `integration/provenance_manifest.yaml`
- `integration/signature_status.yaml`
- `integration/release_signature.placeholder`
- `schemas/signing_policy.schema.json`
- `schemas/trusted_publishers.schema.json`
- `schemas/provenance_manifest.schema.json`
- `schemas/signature_status.schema.json`
- `docs/RELEASE_SIGNING.md`
- `docs/ENTERPRISE_TRUST_MODE.md`
- `scripts/validate_release_signing_v6_6.py`

## Purpose

Define how Cybou should treat signed vs unsigned external skills packs in community and enterprise modes.

## Note

This artifact is not cryptographically signed. It includes the signing contract and an unsigned placeholder status.
