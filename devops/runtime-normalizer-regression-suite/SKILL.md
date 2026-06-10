---
name: runtime-normalizer-regression-suite
description: Create and maintain normalizer regression tests for shell, cargo, kubectl, terraform, docker, git, database and http_fetch inputs.
---

# Runtime Normalizer Regression Suite

Tests tool-specific normalizers independently from policy evaluation.

## Runtime enforcement rule

This skill belongs to the tool-specific normalizer layer.

The normalizer must produce a deterministic `NormalizedAction` before policy evaluation. It must preserve raw input, extract tool/operation/target/environment, detect side effects, detect sensitive data hints, and avoid executing anything.

## Required output

End with:

- tool normalizer;
- parsed operation;
- target/environment extraction;
- side effects;
- sensitive data flag;
- tests required;
- known parser limitations.
