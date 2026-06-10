---
name: rust-feature-matrix-and-hack
description: Validate Rust feature flags and workspace combinations using cargo-hack, feature powerset, no-default-features, all-features, and dependency minimization.
---

# Rust Feature Matrix and Cargo Hack

## Purpose

Ensure feature flags do not create broken or unsafe configurations.

## Tools

- `cargo hack`;
- `--no-default-features`;
- `--all-features`;
- feature powerset;
- workspace package selection.

## Procedure

1. Inventory features.
2. Identify mutually exclusive features.
3. Test default, no-default, all-features.
4. Test feature powerset for critical crates.
5. Check docs for feature semantics.
6. Avoid features that silently change security behavior.

## CYBOU priority

Policy/security semantics should not change invisibly behind features.

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
