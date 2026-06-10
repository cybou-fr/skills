---
name: rust-linting-and-formatting
description: Configure and enforce Rust formatting/linting: rustfmt, rustfmt.toml, clippy, clippy.toml, workspace lint levels, CI gates, and exception policy.
---

# Rust Linting and Formatting

## Purpose

Make Rust formatting and linting consistent, strict, and practical.

## Tools

- `cargo fmt`
- `cargo clippy`
- `rustfmt.toml`
- `clippy.toml`
- workspace lints in `Cargo.toml`

## Procedure

1. Run or propose `cargo fmt --all -- --check`.
2. Run or propose `cargo clippy --workspace --all-targets --all-features -- -D warnings`.
3. Define allowed lint exceptions.
4. Keep clippy exceptions local and justified.
5. Add CI gates.
6. Avoid silencing lints globally.

## Recommended CYBOU gates

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
```

## Review focus

- needless clones;
- unwrap/expect in runtime paths;
- blocking in async contexts;
- large error enums;
- unsafe or undocumented unsafe;
- missed trait derives;
- needless public visibility.

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
