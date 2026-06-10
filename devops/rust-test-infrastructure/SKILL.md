---
name: rust-test-infrastructure
description: Design Rust test infrastructure: cargo test, cargo-nextest, fixtures, integration tests, workspace test matrix, doc tests, flaky test policy, and CI test gates.
---

# Rust Test Infrastructure

## Purpose

Build a reliable Rust test system for CYBOU.

## Tools

- `cargo test`
- `cargo nextest run`
- doctests
- integration tests
- fixture directories
- mock adapters
- test containers if needed

## Test layers

- unit tests;
- integration tests;
- adapter contract tests;
- policy decision tests;
- behavior tests;
- API tests;
- doc tests;
- regression tests.

## Recommended CYBOU commands

```bash
cargo test --workspace --all-features
cargo nextest run --workspace --all-features
cargo test --doc --workspace
```

## Rules

- policy engine tests must be deterministic;
- tool adapter tests should support dry-run/mocks;
- tests involving secrets use placeholders only;
- flaky tests are quarantined and fixed, not ignored.

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
