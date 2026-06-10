---
name: rust-workspace-and-crate-design
description: Design Rust Cargo workspaces, crate boundaries, feature flags, dependency direction, public APIs, module layout, and versioning policy.
---

# Rust Workspace and Crate Design

## Procedure

1. Identify domains and runtime boundaries.
2. Split stable domain types from infrastructure adapters.
3. Define crate dependency direction.
4. Define feature flags and optional integrations.
5. Keep public APIs small.
6. Avoid cyclic conceptual dependencies.
7. Add workspace-level lint/test commands.

## CYBOU recommendations

- `cybou-core` should be dependency-light.
- `cybou-policy` should be test-heavy and deterministic.
- `cybou-tools` should expose traits and adapter implementations separately.
- `cybou-runtime` orchestrates but should not embed tool-specific logic.
- `cybou-api` converts external requests into domain commands.
- `cybou-cli` should use same public APIs as runtime.

## Anti-patterns

- one giant crate;
- policy logic inside tool implementations;
- persistence models leaking into domain logic;
- feature flags that change semantics invisibly.

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
