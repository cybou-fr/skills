# Cybou Core Integration Pack v6.4

**Version:** 6.4.0  
**Role:** supply-chain aware external skills/policies/evals corpus for Cybou.  
**Target:** `cybou-core`, especially `memory/skills.rs`, `memory/vetting.rs`, `immunity.rs`, `audit.rs`.

v6.4 adds **Skill Vetting & Supply Chain Trust** on top of v6.3 immunity compatibility.

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

## What changed in v6.4

```text
Added supply-chain manifest and file hashes.
Added machine-readable vetting rules.
Added quarantine policy.
Added command-pattern regression tests.
Fixed rm-rf-root detection for rm -rf / variants.
Added supply-chain, vetting and command-pattern validators.
```

## Package statistics

```text
Total files: 479
Skill files: 207
Registry skills: 207
Output templates: 139
Policy rule files: 13
Activity policy files: 2
Tool adapter files: 74
Scope object files: 6
Schema JSON files: 31
Schema total files: 33
Eval files: 41
Eval scenarios: 222
Immunity mapping files: 7
```

## Validate

```bash
python scripts/validate_pack_v6_1.py
python scripts/validate_loader_contract_v6_2.py
python scripts/validate_immunity_compat_v6_3.py
python scripts/validate_supply_chain_v6_4.py
python scripts/validate_skill_vetting_rules_v6_4.py
python scripts/validate_command_patterns_v6_4.py
```
