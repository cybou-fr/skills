# Release Process

This repository uses versioned releases.

## Release checklist

```text
run all validators
update package version
update registry version
update file hashes
update provenance manifest
verify signing policy
create signed release for enterprise use
```

## Community mode

Unsigned releases may be used only in metadata-only mode with warnings.

```text
community_unsigned -> warn_and_metadata_only
```

## Enterprise mode

Enterprise mode must fail closed.

```text
enterprise_unsigned -> deny
enterprise_bad_signature -> deny
hash_mismatch -> deny
```

## Signing

v6.8 still contains a placeholder signature status when built without a real private key. Production releases must be signed outside the artifact generation environment.
