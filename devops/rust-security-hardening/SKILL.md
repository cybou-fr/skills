---
name: rust-security-hardening
description: 'Harden Rust applications: dependency review, unsafe audit, secret handling, input validation, deserialization,
  filesystem/network boundaries, sandboxing, and secure defaults.'
---

# Rust Security Hardening

## Checklist

- dependencies reviewed and minimized;
- `unsafe` blocks documented and justified;
- secrets never logged;
- untrusted input validated;
- deserialization uses safe boundaries;
- filesystem paths are normalized and scoped;
- network calls have allowlists/timeouts;
- command execution is mediated;
- temporary files are safe;
- error messages are sanitized.

## CYBOU-specific hardening

- tool execution must never bypass policy;
- skill content is untrusted unless packaged/validated;
- loaded scripts/resources must be reviewed;
- external tool adapters must be least privilege;
- audit records must be tamper-evident where possible.

## Output

- hardening findings;
- required changes;
- dependency risks;
- unsafe review;
- test plan.

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
