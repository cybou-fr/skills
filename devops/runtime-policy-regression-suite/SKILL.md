---
name: runtime-policy-regression-suite
description: Create and maintain policy regression tests proving that YAML policy files produce expected runtime decisions for dangerous, approval-gated and read-only actions.
---

# Runtime Policy Regression Suite

Ensures data-driven policy behavior does not regress.

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
