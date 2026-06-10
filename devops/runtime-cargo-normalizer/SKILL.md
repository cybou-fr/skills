---
name: runtime-cargo-normalizer
description: Implement and review Cargo/Rust command normalizer for cargo check/test/fmt/clippy/audit/deny/publish/install/update and Rust toolchain commands.
---

# Runtime Cargo Normalizer

Extracts Cargo operation, package/workspace target, feature flags, channel/toolchain hints, publish/install/update risks and read-only quality gate commands.

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
