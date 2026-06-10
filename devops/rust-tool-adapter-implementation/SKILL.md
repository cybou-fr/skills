---
name: rust-tool-adapter-implementation
description: Design and implement Rust tool adapters for CYBOU: normalized actions, policy checks, execution boundary, timeout, output capture, redaction, and audit events.
---

# Rust Tool Adapter Implementation

## Purpose

Create safe Rust implementations of CYBOU tool adapters.

## Adapter contract

Each adapter should:

1. Accept a typed request.
2. Normalize into `NormalizedAction`.
3. Ask policy engine for `PolicyDecision`.
4. Stop if denied or approval is missing.
5. Execute only if allowed.
6. Capture bounded output.
7. Redact sensitive data.
8. Emit audit event.
9. Return typed result.

## Adapter design

```text
trait ToolAdapter {
    type Request;
    type Output;
    fn normalize(&self, request: Self::Request) -> NormalizedAction;
    async fn execute(&self, request: Self::Request, ctx: ToolContext) -> Result<Self::Output, ToolError>;
}
```

## CYBOU priority adapters

- shell;
- git;
- docker;
- kubectl;
- terraform;
- http_fetch;
- repo_api;
- log_reader;
- secrets_manager.

## Output

- adapter trait design;
- request/output types;
- policy integration;
- test plan;
- audit events.

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
