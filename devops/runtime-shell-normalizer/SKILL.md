---
name: runtime-shell-normalizer
description: Implement and review shell command normalizer with wrapper detection, pipe-to-shell detection, destructive command classification, environment hints and sensitive output hints.
---

# Runtime Shell Normalizer

Handles `sh`, `bash`, `zsh`, wrapper commands, pipe-to-shell, shell metacharacters and destructive command markers.

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
