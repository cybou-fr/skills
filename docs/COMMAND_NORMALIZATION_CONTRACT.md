# Command Normalization Contract

v6.7 defines the command normalization contract for Cybou immunity.

## Core principle

```text
Regex is metadata.
Rust normalizer is authority.
```

The Rust normalizer should parse argv, identify wrappers, extract nested interpreter payloads, detect pipelines, normalize tool-specific verbs and emit structured `NormalizedAction` records.
