---
name: rust-dead-code-and-dependency-hygiene
description: Use cargo-udeps and code review to identify unused dependencies, dead code, unnecessary features, stale modules, and architecture drift.
---

# Rust Dead Code and Dependency Hygiene

## Purpose

Keep Rust workspace lean and maintainable.

## Tools

- `cargo udeps`;
- `cargo tree`;
- clippy;
- code review;
- module ownership map.

## Procedure

1. Find unused dependencies.
2. Find duplicate or stale crates.
3. Remove unnecessary features.
4. Identify dead modules.
5. Check if dependency removal changes behavior.
6. Add regression tests before cleanup when needed.

## Safety

Dependency removal can break optional integrations. Check feature matrix.

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
