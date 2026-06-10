---
name: rust-miri-unsafe-validation
description: Use Miri and unsafe review to validate Rust unsafe code, undefined behavior risks, aliasing, memory model assumptions,
  and concurrency-sensitive unsafe boundaries.
---

# Rust Miri and Unsafe Validation

## Purpose

Review and test Rust unsafe code and UB-sensitive logic.

## Tools

- `cargo miri test`;
- unsafe code review;
- `cargo geiger` if available;
- targeted unit tests.

## Procedure

1. Inventory unsafe blocks.
2. Require justification and invariants.
3. Check whether safe abstraction boundary is sound.
4. Run or propose Miri for relevant tests.
5. Avoid unsafe in CYBOU runtime paths unless strongly justified.
6. Add comments documenting invariants.

## CYBOU default

- no unsafe in policy engine unless unavoidable;
- no unsafe in command normalization;
- no unsafe in redaction;
- unsafe in adapters requires senior review.

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
