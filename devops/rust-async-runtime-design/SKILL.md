---
name: rust-async-runtime-design
description: Design and review Rust async systems: Tokio runtime boundaries, cancellation, backpressure, timeouts, channels, worker pools, graceful shutdown, and avoiding blocking work.
---

# Rust Async Runtime Design

## Review checklist

- clear runtime ownership;
- no blocking calls inside async tasks;
- cancellation is handled;
- timeouts exist on network/tool calls;
- channels have bounded capacity;
- backpressure is explicit;
- shutdown is graceful;
- task spawning is controlled;
- tracing spans cross async boundaries.

## CYBOU-specific concerns

CYBOU worker runtime must:

- time-limit every tool call;
- cancel child tasks on task cancellation;
- avoid unbounded queues;
- keep audit events even when a task is cancelled;
- separate long-running tool processes from the main runtime;
- isolate per-tenant or per-user jobs.

## Output

- runtime topology;
- async risks;
- timeout/backpressure plan;
- shutdown plan;
- test plan.

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
