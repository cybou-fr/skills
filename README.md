# Cybou Core Integration Pack v6.6

**Version:** 6.6.0  
**Role:** signed-release/provenance-ready external skills/policies/evals corpus for Cybou.  
**Target:** `cybou-core`, especially `skills sync`, enterprise trust mode, release verification and supply-chain hardening.

v6.6 adds **Release Signing & Provenance** on top of v6.5 eval runner/adversarial immunity tests.

## Core rule

```text
The pack must never execute tools directly.
```

## What changed in v6.6

```text
Added signing policy.
Added trusted publishers manifest.
Added provenance manifest.
Added signature status.
Added release signature placeholder.
Added enterprise trust mode documentation.
Added release signing validator.
```

## Package statistics

```text
Total files: 504
Skill files: 207
Registry skills: 207
Output templates: 139
Policy rule files: 13
Activity policy files: 2
Tool adapter files: 74
Scope object files: 6
Schema JSON files: 38
Schema total files: 40
Eval files: 43
Eval scenarios: 240
Immunity mapping files: 7
```

## Signing status

```text
status: unsigned_placeholder
community behavior: warn_and_metadata_only
enterprise behavior: deny_until_signed
```

This generated artifact defines the signing contract but is not cryptographically signed.

## Validate

```bash
python scripts/validate_pack_v6_1.py
python scripts/validate_loader_contract_v6_2.py
python scripts/validate_immunity_compat_v6_3.py
python scripts/validate_supply_chain_v6_4.py
python scripts/validate_skill_vetting_rules_v6_4.py
python scripts/validate_command_patterns_v6_4.py
python scripts/validate_eval_contract_v6_5.py
python scripts/validate_adversarial_immunity_v6_5.py
python scripts/validate_release_signing_v6_6.py
```
