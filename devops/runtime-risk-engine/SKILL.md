---
name: runtime-risk-engine
description: Implement and review CYBOU risk engine that combines matched policy rules, risk floors, side effects, environment, sensitive data and activity classes.
---

# Runtime Risk Engine

Computes final risk from matched rule risk, risk floors, side effects, environment, sensitive data and activity policy.

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
