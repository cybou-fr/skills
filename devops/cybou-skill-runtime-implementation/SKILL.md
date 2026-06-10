---
name: cybou-skill-runtime-implementation
description: Design and implement CYBOU skill runtime in Rust: skill pack loading, registry parsing, validation, routing, skill graph co-loading, behavior tests, and versioned compatibility.
---

# CYBOU Skill Runtime Implementation

## Purpose

Implement the Rust runtime that loads, validates, routes, and applies skills.

## Components

- skill pack loader;
- SKILL.md parser;
- registry parser;
- skill graph loader;
- output template loader;
- schema validation;
- behavior test runner;
- compatibility checks;
- versioning;
- cache/index.

## Runtime rules

- skill files are instructions, not executable authority;
- scripts/resources are reviewed before use;
- registry paths must resolve inside pack root;
- related skills must exist;
- output templates must exist;
- unknown skill packs are untrusted until validated.

## Output

- module design;
- data types;
- validation flow;
- routing algorithm;
- tests;
- migration plan.

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
