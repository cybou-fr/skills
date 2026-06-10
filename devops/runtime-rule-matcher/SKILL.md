---
name: runtime-rule-matcher
description: Implement and review rule matching for CYBOU runtime policy files, including regex matching, decision mapping,
  risk extraction, matched rule reporting and safe fallback.
---

# Runtime Rule Matcher

Compiles and evaluates `policy_rules/*.yaml` against normalized action raw input and tool operation. It reports matched rule IDs, strongest risk and most restrictive decision.

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
