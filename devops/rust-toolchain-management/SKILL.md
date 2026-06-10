---
name: rust-toolchain-management
description: 'Manage Rust toolchain configuration for senior projects: rust-toolchain.toml, MSRV policy, stable/beta/nightly
  split, components, targets, CI matrix, and reproducibility.'
---

# Rust Toolchain Management

## Purpose

Define and maintain reproducible Rust toolchain configuration.

## Files

- `rust-toolchain.toml`
- `.cargo/config.toml`
- CI matrix
- `Cargo.toml` `rust-version`
- workspace documentation

## Procedure

1. Identify project MSRV and current Rust channel.
2. Decide stable vs nightly requirements.
3. Define components:
   - rustfmt;
   - clippy;
   - llvm-tools-preview if using cargo-llvm-cov;
   - miri if applicable;
   - rust-src if needed.
4. Define target platforms.
5. Align `Cargo.toml` `rust-version`.
6. Add CI matrix for MSRV and stable.
7. Document upgrade policy.

## CYBOU defaults

- stable channel by default;
- nightly only for miri/fuzz-specific workflows if needed;
- MSRV explicit;
- toolchain pinned for CI reproducibility;
- rustfmt/clippy required in CI.

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
