---
name: cybou-core-profile-scope-engine
description: Implement and review profile and scope enforcement for CYBOU runtime, combining autonomy profile, profile decision
  matrix, scope objects and approval state.
---

# Runtime Profile and Scope Engine

Evaluates whether selected runtime profile and scope allow, block or require approval for a normalized action.

## Runtime enforcement rule

This skill belongs to the data-driven policy layer.

The runtime must load policy data from pack files, compile the applicable rules, evaluate normalized actions, produce auditable policy decisions, and avoid hardcoded-only behavior except as a safe fallback.

## Required output

End with:

- policy data source;
- compiled rule behavior;
- risk decision;
- profile/scope/approval impact;
- tests required;
- migration notes.
