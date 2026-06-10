---
name: rust-docs-and-api-contracts
description: Create Rust documentation and API contracts: rustdoc, doc tests, examples, ADRs, crate-level docs, public API stability, and generated docs policy.
---

# Rust Docs and API Contracts

## Purpose

Ensure Rust APIs are understandable, stable, and tested.

## Tools

- `cargo doc`;
- doc tests;
- examples;
- ADRs;
- README;
- crate-level `//!` docs.

## Procedure

1. Identify public APIs.
2. Add examples.
3. Add doc tests for stable behavior.
4. Document error semantics.
5. Document security and approval boundaries.
6. Add ADRs for architectural decisions.
7. Keep generated docs free of secrets.

## CYBOU docs priorities

- policy engine API;
- tool adapter contract;
- skill pack format;
- approval state model;
- audit event schema.

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
