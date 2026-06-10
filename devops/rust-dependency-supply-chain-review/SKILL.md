---
name: rust-dependency-supply-chain-review
description: 'Review Rust dependencies and Cargo supply chain: crates, features, licenses, build scripts, transitive risk,
  MSRV, advisories, and dependency minimization.'
---

# Rust Dependency and Supply Chain Review

## Review checklist

- direct dependencies;
- transitive dependency risk;
- default features;
- build scripts;
- native dependencies;
- license compatibility;
- maintenance status;
- security advisories;
- unnecessary dependencies;
- duplicate versions;
- MSRV impact.

## CYBOU dependency policy

- core crates should be dependency-light;
- build scripts require review;
- crypto/security crates require extra review;
- network/runtime crates should be centralized;
- dependencies that execute code during build are high risk.

## Output

- dependency risk summary;
- crates to remove or replace;
- feature flag changes;
- license notes;
- approval required.

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
