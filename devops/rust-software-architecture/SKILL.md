---
name: rust-software-architecture
description: Design Rust software architecture for CYBOU and similar systems: crates, modules, boundaries, domain model, runtime services, adapters, traits, persistence, observability, and evolution strategy.
---

# Rust Software Architecture

## Purpose

Design or review architecture for Rust systems, especially CYBOU itself.

## Architecture dimensions

- workspace/crate boundaries;
- domain model;
- runtime services;
- trait boundaries;
- adapter boundaries;
- persistence model;
- plugin/skill loading;
- policy engine;
- tool router;
- API surface;
- event/audit model;
- error model;
- observability;
- testing strategy.

## CYBOU target architecture

Recommended conceptual crates:

```text
cybou-core          # domain types, task model, skill model
cybou-runtime       # orchestration, task state, profiles
cybou-policy        # policy decision engine
cybou-tools         # tool adapter traits and implementations
cybou-skills        # skill registry, loaders, validators
cybou-audit         # audit events and evidence records
cybou-api           # HTTP/gRPC API
cybou-cli           # operator/developer CLI
cybou-agent         # worker loop
cybou-ui            # optional frontend integration boundary
```

## Design rules

- core crates must not depend on infrastructure crates;
- domain types should be serializable and versioned;
- side effects go through adapters;
- policy engine runs before tool execution;
- audit events are emitted for blocked and allowed actions;
- errors are typed at boundaries and contextual internally.

## Output

- proposed crate/module structure;
- dependency direction;
- interfaces/traits;
- state model;
- migration path;
- risks and trade-offs.

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
