---
name: cybou-core-sandbox-profile-engine
description: Implement and review sandbox profiles for local readonly commands, repository checks, CI-quality commands, network
  fetches and denied/high-risk operations.
---

# Runtime Sandbox Profile Engine

Selects a sandbox profile from normalized action, policy decision and tool type.

Profiles include `no_execution`, `readonly_local`, `repo_quality`, `network_fetch_restricted`, `approval_required_execution` and `blocked`.

## Runtime enforcement rule

This skill belongs to sandbox and tool execution boundary.

No tool may execute directly from assistant text. Every execution must pass through normalization, policy evaluation, approval validation if needed, sandbox profile selection, timeout/output limits, redaction and audit/evidence capture.

## Required output

End with:

- sandbox profile;
- allowed filesystem roots;
- network mode;
- timeout/output limits;
- policy decision;
- execution mode;
- audit/evidence impact;
- tests required.
