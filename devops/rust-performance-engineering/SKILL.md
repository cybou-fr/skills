---
name: rust-performance-engineering
description: Analyze Rust performance: allocation, cloning, async overhead, lock contention, parsing performance, memory usage, profiling plan, benchmarks, and regression prevention.
---

# Rust Performance Engineering

## Review areas

- unnecessary clones;
- allocation hotspots;
- string parsing overhead;
- lock contention;
- async task overhead;
- channel backpressure;
- serialization costs;
- memory growth;
- startup time;
- benchmark coverage.

## CYBOU performance targets

- policy decisions should be deterministic and fast;
- command normalization should be bounded;
- skill registry lookup should be cheap;
- audit logging should not block critical path;
- behavior tests should run quickly;
- tool output processing should be bounded by size/time limits.

## Output

- suspected bottlenecks;
- measurement plan;
- benchmark plan;
- patch suggestions;
- regression tests.

## CYBOU dogfooding rule

When this skill is used to develop CYBOU itself:

- treat CYBOU repository changes as high-value internal changes;
- prefer small reviewable patches;
- preserve auditability;
- add tests before or with implementation;
- avoid irreversible migrations without approval;
- avoid adding dependencies without supply-chain review;
- document architecture decisions.

## Required output

End with:

- architecture/development decision;
- files/modules affected;
- proposed patch plan;
- tests required;
- security/performance risks;
- review checklist;
- approval required, if any.
