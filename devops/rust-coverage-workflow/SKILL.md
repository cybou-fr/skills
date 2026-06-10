---
name: rust-coverage-workflow
description: Configure Rust coverage workflow using cargo-llvm-cov or tarpaulin, coverage thresholds, report generation, CI upload, and exclusions.
---

# Rust Coverage Workflow

## Purpose

Measure useful Rust test coverage without gaming the metric.

## Tools

- `cargo llvm-cov`
- `cargo tarpaulin`
- coverage reports
- CI artifacts

## Procedure

1. Choose coverage tool.
2. Define workspace command.
3. Exclude generated code and non-testable glue only when justified.
4. Define minimum threshold.
5. Track coverage trend.
6. Use coverage to find missing tests, not as a vanity metric.

## Recommended CYBOU command

```bash
cargo llvm-cov --workspace --all-features --lcov --output-path lcov.info
```

## Important

Coverage is not security assurance. Policy engine and adapters need targeted tests even if line coverage looks high.

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
