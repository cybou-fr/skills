# Cybou Core Integration Pack v6

**Version:** 6.0.0  
**Role:** external skills / policies / templates / evals corpus for the real Cybou Rust + MicroVM worker.  
**Target project:** Cybou (`cybou-core`, `cybou-guest`, `cybou-proto`).

This is not a standalone runtime. It is the integration-ready version of the v5.9 skills pack, adapted to the actual Cybou architecture.

## One-line definition

```text
Cybou core = authoritative Rust worker runtime + MicroVM execution boundary.
This pack = external procedural knowledge + safety policy + eval corpus.
```

## Core rule

```text
The pack must never execute tools directly.
```

Execution authority stays in Cybou:

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

## Package statistics

```text
Total files: 568
Skill files: 207
Registry skills: 207
Output templates: 139
Policy rule files: 13
Activity policy files: 2
Tool adapter files: 74
Scope object files: 6
Schema files: 19
Test scenario files: 29
Test scenarios: 171
Behavior scenarios: 171
Strict runtime scenarios: 21
Eval files: 41
```

Regression/eval suites:

```text
Normalizer scenarios: 16
Approval scenarios: 6
Audit scenarios: 4
Sandbox scenarios: 5
Detection scenarios: 5
Cloud SecOps scenarios: 5
Identity/secrets scenarios: 6
Forensics scenarios: 4
```

## Start here

```text
docs/CYBOU_CORE_INTEGRATION.md
docs/POLICY_TO_IMMUNITY_MAPPING.md
docs/SKILL_VETTING.md
docs/EVAL_TO_LEARNING_LOOP.md
docs/MICROVM_BOUNDARY_MODEL.md
docs/REPOSITORY_LAYOUT.md
```

Machine-readable integration manifests:

```text
integration/cybou_core_mapping.yaml
integration/policy_to_immunity_matrix.yaml
integration/skill_trust_levels.yaml
integration/eval_to_learning_loop.yaml
```

## How Cybou should use this pack

```text
sync-skills.sh
  -> memory/skills.rs parses compact metadata
  -> memory/vetting.rs vets external content
  -> agent/mod.rs selects relevant skills
  -> decision.rs adds compact hints
  -> immunity.rs enforces deterministic safety
  -> guest.rs sends approved commands over vsock
  -> audit.rs records AgentEvent stream
  -> memory learns facts / skills / lessons
```

## v6 change from v5.9

v5.9 was a broad standalone reference prototype.  
v6 is an integration corpus for the real Rust/MicroVM project.

The directory `runtime_prototype/` is retained as reference material only.

## Suggested implementation milestone

```text
CIP039 — Skills Pack v6 Integration
```

Tasks:

```text
1. Implement registry loader in memory/skills.rs.
2. Connect SkillVetter before full skill body access.
3. Compile selected policy_rules into immunity/risk tables.
4. Add SkillSelected and PolicyMatched AgentEvent variants.
5. Convert evals into Cybou Testing-as-Learning runner.
6. Add skill trust levels to audit records.
7. Add policy compatibility check to CI.
```
