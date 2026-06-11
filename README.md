# Cybou Skills Corpus v6.8

**Version:** 6.8.0  
**Role:** public/private skills corpus for Cybou.  
**Repository boundary:** skills, policies, evals, schemas, trust/signing metadata and documentation only.

This repository does **not** contain Cybou runtime implementation code.

## Core rule

```text
Skills improve reasoning.
Rust decides safety.
MicroVM contains execution.
Audit records everything.
```

## What changed in v6.8

```text
Finalized skills-only repository boundary.
Removed Rust contract sketch artifact.
Confirmed no cybou-core patch/scaffold directories.
Added CONTRIBUTING.md.
Added SECURITY.md.
Added SKILL_AUTHORING_GUIDE.md.
Added RELEASE.md.
Added repository boundary docs.
Renamed runtime-* skill ids to cybou-core-*.
Added public repository cleanup validator.
```

## Package statistics

```text
Total files: 531
Skill files: 207
Registry skills: 207
Output templates: 139
Policy rule files: 13
Activity policy files: 2
Tool adapter files: 74
Scope object files: 6
Schema JSON files: 42
Schema total files: 44
Eval files: 44
Eval scenarios: 254
Immunity mapping files: 11
```

## Canonical directories

```text
core/
devops/
secops/
productivity/
policy_rules/
activity_policies/
tool_adapters/
scope_objects/
schemas/
evals/
integration/
immunity_mapping/
docs/
examples/
scripts/
```

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
python scripts/validate_policy_hardening_v6_7.py
python scripts/validate_public_repository_cleanup_v6_8.py
```

## Signing status

This generated artifact may still be unsigned placeholder unless signed by the real `cybou-fr` release key.

Enterprise mode must deny unsigned releases.
