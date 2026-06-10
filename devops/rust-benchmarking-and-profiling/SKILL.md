---
name: rust-benchmarking-and-profiling
description: Set up Rust benchmarking and profiling with Criterion, cargo bench, cargo flamegraph, cargo bloat, performance
  budgets, and regression tracking.
---

# Rust Benchmarking and Profiling

## Purpose

Measure and improve performance-critical Rust paths.

## Tools

- Criterion;
- `cargo bench`;
- `cargo flamegraph`;
- `cargo bloat`;
- tracing metrics;
- production metrics.

## CYBOU benchmark targets

- policy decision latency;
- command normalization throughput;
- skill registry lookup;
- registry validation;
- behavior test execution;
- tool output redaction;
- audit event serialization.

## Procedure

1. Identify critical path.
2. Add Criterion benchmark.
3. Add baseline.
4. Profile before optimizing.
5. Track regression in CI or scheduled job.
6. Avoid premature micro-optimization.

## Output

Include benchmark plan and performance budget.

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
