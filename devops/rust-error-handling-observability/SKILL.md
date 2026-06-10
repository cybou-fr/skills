---
name: rust-error-handling-observability
description: 'Design Rust error handling and observability: thiserror/anyhow boundaries, tracing spans, structured logs, metrics,
  audit events, and user-safe error messages.'
---

# Rust Error Handling and Observability

## Error model

- domain errors are typed;
- infrastructure errors carry context;
- user-facing errors are sanitized;
- secrets are never included in errors;
- retryable vs permanent errors are distinguishable.

## Observability model

- structured logs;
- tracing spans;
- metrics for queues/tool calls/policies;
- audit events for decisions;
- correlation IDs;
- redaction at logging boundary.

## CYBOU-specific events

- task received/classified;
- skill selected;
- normalized action created;
- policy decision created;
- approval requested/received/expired;
- tool call allowed/blocked/executed;
- redaction applied;
- task completed/failed/cancelled.

## Output

- error type plan;
- observability events;
- metrics;
- tracing strategy;
- redaction controls.

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
