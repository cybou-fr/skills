---
name: cybou-core-policy-loader
description: Implement and review CYBOU policy loader that reads risk matrix, tool policies, policy rules, activity policies,
  autonomy profiles, profile decision matrix and scope objects.
---

# Runtime Policy Loader

Loads CYBOU policy data from YAML files.

Inputs: `risk_matrix.yaml`, `tool_policies.yaml`, `policy_rules/*.yaml`, `activity_policies/*.yaml`, `autonomy_profiles.yaml`, `profile_decision_matrix.yaml`, `scope_objects/*.yaml`.

Rules: malformed policy fails closed; unknown tool uses safe fallback; policy loader never executes tools.

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
