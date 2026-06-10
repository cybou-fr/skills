---
name: rust-senior-code-review
description: 'Review Rust code like a senior engineer: ownership, lifetimes, error handling, async correctness, trait design,
  module boundaries, unsafe usage, testing, performance, and maintainability.'
---

# Rust Senior Code Review

## Purpose

Review Rust code for correctness, maintainability, safety, performance, and architecture fit.

## Review checklist

### Correctness
- ownership and borrowing are clear;
- lifetimes are not overcomplicated;
- error paths are handled;
- no hidden panics in runtime paths;
- boundary conditions are tested.

### API design
- public APIs are minimal and stable;
- types encode invariants;
- error types are meaningful;
- traits are not over-generalized;
- generics improve clarity, not complexity.

### Async/concurrency
- no blocking in async runtime;
- cancellation behavior is considered;
- shared state is explicit;
- locks are scoped tightly;
- backpressure exists where needed.

### Security
- no secret logging;
- inputs are validated;
- unsafe blocks are justified;
- dependency changes are reviewed;
- deserialization boundaries are controlled.

### Tests
- unit tests for pure logic;
- integration tests for boundaries;
- property tests for parsers/policies where useful;
- regression tests for bugs.

## Output

Provide:
- blocking issues;
- high-priority issues;
- maintainability notes;
- suggested patch plan;
- test additions.

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
