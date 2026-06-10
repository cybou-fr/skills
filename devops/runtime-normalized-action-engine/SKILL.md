---
name: runtime-normalized-action-engine
description: Implement and review CYBOU NormalizedAction engine for shell, cargo, kubectl, terraform, git, docker, database,
  http_fetch and abstract tools.
---

# Runtime Normalized Action Engine

Transforms raw tool requests into typed `NormalizedAction` objects before policy evaluation.

Required fields: `tool`, `operation`, `raw_input`, `args`, `target`, `environment`, `scope`, `side_effects`, `sensitive_data_possible`.

Must detect shell wrappers, pipe-to-shell, destructive operations, production hints and sensitive data hints.

## Runtime enforcement rule

Skills may recommend. Runtime decides. Tool Router enforces.

Runtime flow:

```text
raw request -> NormalizedAction -> PolicyDecision -> approval/scope check -> audit -> execution only if allowed -> redaction
```

## Required output

End with:
- runtime component;
- normalized action impact;
- policy decision impact;
- tests required;
- audit/redaction impact;
- approval required, if any.
