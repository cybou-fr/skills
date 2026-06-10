# Cybou Core Integration Pack v6.3

**Version:** 6.3.0  
**Role:** loader-compatible external skills/policies/evals corpus with Rust immunity compatibility assets.  
**Target:** `cybou-core`, especially `immunity.rs`, `risk.rs`, `approval.rs`, `audit.rs`.

v6.3 adds direct **Immunity Compatibility Mapping** on top of the v6.2 loader contract.

## Core rule

```text
The pack must never execute tools directly.
```

Execution authority remains in Cybou:

```text
CybouDecision
  -> immunity.rs
  -> approval.rs
  -> risk.rs / dryrun.rs / snapshot.rs
  -> GuestExecutor
  -> vsock
  -> cybou-guest
  -> MicroVM shell
  -> AgentEvent
  -> audit.rs
```

## What changed in v6.3

```text
Added immunity_mapping/.
Added Rust-facing immunity manifest.
Added decision/risk/tool class mappings for immunity.rs.
Added command pattern mapping for deterministic safety checks.
Added sensitive target mapping.
Added Rust contract sketch.
Added immunity compatibility validator.
```

## Package statistics

```text
Total files: 464
Skill files: 207
Registry skills: 207
Output templates: 139
Policy rule files: 13
Activity policy files: 2
Tool adapter files: 74
Scope object files: 6
Schema JSON files: 27
Schema total files: 29
Eval files: 41
Eval scenarios: 222
Immunity mapping files: 6
```

## Immunity compatibility files

```text
immunity_mapping/immunity_manifest.yaml
immunity_mapping/decision_mapping.yaml
immunity_mapping/risk_mapping.yaml
immunity_mapping/tool_class_mapping.yaml
immunity_mapping/command_pattern_mapping.yaml
immunity_mapping/sensitive_targets.yaml
```

## Runtime verdicts

All rich policy labels compile into:

```text
Allow
Deny
NeedsApproval
```

## Matching policy

```text
Deny overrides NeedsApproval.
NeedsApproval overrides Allow.
Highest risk wins.
Approval cannot override Deny.
```

## Validate

```bash
python scripts/validate_pack_v6_1.py
python scripts/validate_loader_contract_v6_2.py
python scripts/validate_immunity_compat_v6_3.py
```

Expected result:

```text
status: pass
errors: []
```

## Suggested Cybou implementation step

CIP039 Phase 4–5 can now start:

```text
policy compatibility checker
  -> immunity_mapping validation
  -> compile command patterns
  -> compile sensitive targets
  -> map policy decisions to ImmunityVerdict
  -> emit PolicyMatched / ImmunityEvaluated AgentEvent
```
