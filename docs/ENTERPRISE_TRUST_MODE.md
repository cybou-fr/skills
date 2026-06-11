# Enterprise Trust Mode

Enterprise mode must fail closed.

## Rules

```text
unsigned release -> deny
bad signature -> deny
unknown publisher -> deny
hash mismatch -> deny
critical vetting failure -> deny
```

## Allowed without signature

Nothing beyond local, manually supplied development fixtures should be trusted in enterprise mode.

## Community behavior

Community mode may allow unsigned packs only in metadata-only mode with warnings:

```text
warn_and_metadata_only
```

Full body access and live policy compilation should require a signed release or explicit local developer override.
