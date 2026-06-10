---
name: rust-testing-strategy
description: 'Design Rust testing strategy: unit, integration, property, snapshot, fuzz-like safe tests, contract tests, policy
  tests, tool adapter tests, and regression suites.'
---

# Rust Testing Strategy

## Test layers

- unit tests for pure functions;
- integration tests for crate boundaries;
- contract tests for adapters;
- policy tests for decisions;
- snapshot tests for reports;
- property tests for parsers and normalizers;
- regression tests for bugs;
- end-to-end dry-run tests.

## CYBOU required tests

- command normalization;
- policy decision;
- approval state;
- skill registry validation;
- tool adapter contract;
- scope enforcement;
- redaction;
- audit event creation;
- behavior test scenario mapping.

## Output

- test matrix;
- fixtures;
- mock strategy;
- CI commands;
- coverage gaps.

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
