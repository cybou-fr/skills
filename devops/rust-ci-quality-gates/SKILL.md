---
name: rust-ci-quality-gates
description: Design CI quality gates for Rust projects: fmt, clippy, test, nextest, coverage, audit, deny, MSRV, docs, semver, feature matrix, and release checks.
---

# Rust CI Quality Gates

## Purpose

Create practical CI gates for CYBOU Rust development.

## Recommended baseline

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-features
cargo nextest run --workspace --all-features
cargo audit
cargo deny check
cargo doc --workspace --no-deps
```

## Advanced gates

- `cargo llvm-cov`;
- `cargo hack check --feature-powerset`;
- `cargo msrv verify`;
- `cargo semver-checks`;
- `cargo miri test` for unsafe-sensitive crates;
- fuzz scheduled job.

## CYBOU gates by crate

- `cybou-policy`: property tests + fuzz targets;
- `cybou-tools`: adapter contract tests;
- `cybou-skills`: registry validation fixtures;
- `cybou-runtime`: async cancellation/backpressure tests;
- `cybou-audit`: serialization and redaction tests.

## CYBOU dogfooding rule

When this skill is used for CYBOU itself:

- keep changes small and reviewable;
- add or update tests with implementation;
- prefer dry-run/read-only commands first;
- do not add dependencies without supply-chain review;
- do not publish, release, deploy, or modify production without explicit approval;
- document quality gates in CI.

## Required output

End with:

- toolchain decision;
- config/files affected;
- commands to run;
- CI quality gates;
- risks;
- approval required, if any.
