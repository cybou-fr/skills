---
name: cybou-policy-engine-implementation
description: Design and implement CYBOU policy engine in Rust: normalized action evaluation, rule matching, risk floors, approval state, profile matrix, and auditable decisions.
---

# CYBOU Policy Engine Implementation

## Purpose

Implement deterministic policy decisions before any side effect.

## Inputs

- normalized action;
- runtime profile;
- scope object;
- environment;
- approval state;
- risk matrix;
- tool policy;
- activity policy;
- profile decision matrix.

## Output object

```text
PolicyDecision {
  decision,
  risk,
  matched_rules,
  approval_required,
  approval_scope,
  redaction_required,
  audit_required,
  reason
}
```

## Implementation rules

- deterministic and testable;
- no tool execution inside policy engine;
- support risk floors;
- explain every decision;
- deny unknown high-risk operations;
- approval is scoped and expiring;
- unknown environment limits autonomy.

## Required tests

- destructive shell commands;
- terraform destroy;
- kubectl delete namespace;
- secret reveal;
- AI jailbreak generation;
- out-of-scope pentest;
- expired approval;
- profile restrictions.

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
