---
name: runtime-git-normalizer
description: Implement and review Git normalizer for fetch/status/diff/log versus commit/push/reset/clean/rebase risks, remote targets and branch references.
---

# Runtime Git Normalizer

Separates read-only operations from write/history rewriting operations. Detects `push --force`, `reset --hard`, `clean -fd`, remote operations and branch targets.

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
