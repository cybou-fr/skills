# Release Signing

v6.6 defines the signing and provenance contract for the external Cybou skills repository.

## Why signing matters

`cybou-fr/skills` is a supply-chain input. Hashes inside the package are useful, but they do not prove who produced the package. Release signing adds publisher identity and provenance.

## Files

```text
integration/signing_policy.yaml
integration/trusted_publishers.yaml
integration/provenance_manifest.yaml
integration/signature_status.yaml
integration/release_signature.placeholder
```

## Loader behavior

```text
community unsigned release -> warn and metadata-only mode
community bad signature -> quarantine
enterprise unsigned release -> deny
enterprise bad signature -> deny
hash mismatch -> deny
```

## Current artifact

This generated artifact is intentionally marked:

```text
status: unsigned_placeholder
```

because no private signing key exists in this environment.

## Future signing target

The release signature should cover:

```text
integration/provenance_manifest.yaml
integration/file_hashes.yaml
```

and should be verified before full-body skills or policy compilation are enabled.
