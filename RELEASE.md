# Release Process

Generated unsigned artifacts may be used only in metadata-only mode.

```text
community_unsigned -> warn_and_metadata_only
enterprise_unsigned -> deny
enterprise_bad_signature -> deny
hash_mismatch -> deny
```

## Release checklist

```bash
python scripts/validate_all.py
```

Then verify:

```text
status: pass
failed: 0
file hashes updated
provenance manifest updated
signature status correct
release archive generated
```

A production enterprise release must be signed outside the artifact generation environment with the real `cybou-fr` release key.
