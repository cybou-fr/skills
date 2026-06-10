---
name: cybou-self-hosting-development-loop
description: Use CYBOU to develop CYBOU itself safely: task intake, architecture decision, patch planning, code review, test selection, policy simulation, and release notes.
---

# CYBOU Self-hosting Development Loop

## Purpose

Dogfood CYBOU as its own development assistant without bypassing safety or review.

## Loop

1. Define development task.
2. Select architecture/runtime skills.
3. Produce small patch plan.
4. Identify affected crates/modules.
5. Generate or edit code only within scope.
6. Run or propose tests.
7. Review security and performance.
8. Update docs and changelog.
9. Produce audit/release notes.

## Rules

- CYBOU cannot approve its own high-risk side effects.
- Production deploys require human approval.
- New tools/adapters require security review.
- New dependencies require supply-chain review.
- Policy bypasses are blocking issues.

## Output

- task decomposition;
- selected skills;
- patch plan;
- tests;
- review checklist;
- release note.

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
