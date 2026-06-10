# CYBOU DevOps/SecOps Agent Skills Pack v4

Runtime-oriented, AgentSkills-compatible DevOps/SecOps skill library for CYBOU Worker or another autonomous/semi-autonomous AI worker.

v3 keeps the portable AgentSkills structure:

```text
skill-name/
  SKILL.md
  references/
  templates/
  scripts/
```

Each skill directory contains a required `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: Skill routing description
---
```

v3 also adds CYBOU runtime metadata and validation assets:

```text
registry.yaml
risk_matrix.yaml
tool_policies.yaml
output_templates.yaml
cybou.yaml
schemas/
policy_rules/
tests/
shared/
```

## What changed in v3

Compared to v2:

1. Added richer `registry.yaml`:
   - `requires_tools`;
   - `input_types`;
   - `output_template`;
   - `related_skills`;
   - `do_not_use_for`;
   - `autonomy_level`.

2. Added stricter policy rules:
   - `policy_rules/shell.yaml`;
   - `policy_rules/kubectl.yaml`;
   - `policy_rules/terraform.yaml`;
   - `policy_rules/docker.yaml`;
   - `policy_rules/git.yaml`;
   - `policy_rules/database.yaml`;
   - `policy_rules/cloud.yaml`;
   - `policy_rules/package_managers.yaml`;
   - `policy_rules/http_fetch.yaml`.

3. Added machine-readable tests:
   - destructive commands;
   - prompt injection;
   - secrets;
   - Kubernetes;
   - Terraform;
   - database;
   - CI/CD;
   - pull requests.

4. Added schemas:
   - registry schema;
   - tool policy schema;
   - risk matrix schema;
   - output templates schema;
   - test scenarios schema.

5. Added new skills:
   - Helm read-only triage;
   - Prometheus alert analysis;
   - Kubernetes security review;
   - GitHub security review;
   - SIEM alert enrichment;
   - package manager safety;
   - HTTP fetch safety.

## Runtime model

```text
User task
  -> AGENTS.md global constraints
  -> registry.yaml candidate skill routing
  -> core/task-classification
  -> core/environment-detection
  -> risk_matrix.yaml risk calculation
  -> selected skill SKILL.md
  -> policy_rules + tool_policies.yaml enforcement
  -> approval-request if required
  -> tool execution or draft
  -> redaction
  -> output_templates.yaml report
  -> audit trace
```

## Core rule

`SKILL.md` guides behavior.  
The runtime Tool Router enforces behavior.

Never rely on text instructions alone to block dangerous actions.


## v3.2 Penetration Testing Extension

This release adds authorized defensive penetration testing support.

Summary:

- Skills: 45
- Registry skills: 45
- Output templates: 40
- Policy rule files: 10
- Test scenario files: 12
- Test scenarios: 54

Penetration testing is allowed only when explicit authorization, target scope, rules of engagement, and stop conditions are known.


## v3.3 Pentest Hardening

This release adds a dedicated penetration testing activity policy, scope schema/template, severity model, retest validation, evidence redaction and severity rating skills.

Summary:

- Skills: 48
- Registry skills: 48
- Output templates: 43
- Policy rule files: 10
- Activity policy files: 1
- Test scenario files: 13
- Test scenarios: 70

Penetration testing remains defensive, authorized, scope-bound, and policy-gated.


## v4 Runtime Integration

This release turns the package into a CYBOU runtime integration pack.

Summary:

- Skills: 48
- Registry skills: 48
- Output templates: 43
- Policy rule files: 10
- Activity policy files: 1
- Tool adapter files: 10
- Scope object files: 3
- Test scenario files: 14
- Test scenarios: 76
- Behavior scenarios checked: 76

v4 adds tool adapters, autonomy profiles, scope objects, approval/audit schemas, skill graph and a behavior test runner scaffold.


## v4.1 AI Security / LLM AppSec Extension

This release adds defensive AI security skills for jailbreak defense, indirect prompt injection assessment, AI agent tool abuse review, RAG poisoning defense, model data leakage, model DoS/cost abuse, AI supply chain, AI memory/context safety and insecure output handling.

Summary:

- Skills: 58
- Registry skills: 58
- Output templates: 54
- Policy rule files: 11
- Activity policy files: 2
- Tool adapter files: 11
- Scope object files: 3
- Test scenario files: 15
- Test scenarios: 88
- Behavior scenarios checked: 88

AI security testing is defensive-only, scope-bound, and based on synthetic fixtures unless special authorization exists.


## v4.2 Runtime Completeness

This release focuses on runtime completeness rather than adding many new skills.

Summary:

- Total files: 160
- Skills: 58
- Registry skills: 58
- Output templates: 54
- Policy rule files: 11
- Activity policy files: 2
- Tool adapter files: 23
- Scope object files: 6
- Schema files: 19
- Test scenario files: 16
- Test scenarios: 96
- Behavior scenarios checked: 96

v4.2 adds external tool cataloging, missing tool adapters, normalized action and policy decision schemas, task/tool-call state schemas, AI security scope objects, a profile decision matrix and stronger behavior-test scaffolding.


## v4.3 Upstream Catalog Adapters

This release adds CYBOU-native adapters inspired by public Anthropic and OpenAI Agent Skills catalogs. It does not vendor or copy upstream SKILL.md files.

Summary:

- Total files: 201
- Skills: 91
- Registry skills: 91
- Output templates: 87
- Policy rule files: 11
- Activity policy files: 2
- Tool adapter files: 29
- Scope object files: 6
- Schema files: 19
- Test scenario files: 17
- Test scenarios: 106
- Behavior scenarios checked: 106

New workflow groups:
- Document/artifact processing
- Design/frontend
- Developer platform integrations
- Deployment/repository operations
- Productivity/research workflows
- Security governance


## v4.4 Rust Senior Developer / Software Architect

This release turns CYBOU into a self-development assistant for CYBOU itself, focused on Rust senior engineering and software architecture.

Summary:

- Total files: 220
- Skills: 105
- Registry skills: 105
- Output templates: 102
- Policy rule files: 12
- Activity policy files: 2
- Tool adapter files: 31
- Scope object files: 6
- Schema files: 19
- Test scenario files: 18
- Test scenarios: 116
- Behavior scenarios checked: 116

New focus:
- Rust senior code review
- Rust software architecture
- CYBOU policy engine implementation
- CYBOU skill runtime implementation
- Rust tool adapters
- Cargo supply-chain review
- CYBOU self-hosting development loop


## v4.5 Rust Toolchain Mastery

This release gives the Rust senior architect profile complete Rust infrastructure coverage.

Summary:

- Total files: 252
- Skills: 117
- Registry skills: 117
- Output templates: 115
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 19
- Test scenarios: 128
- Behavior scenarios checked: 128

Rust toolchain coverage now includes rustfmt, clippy, nextest, llvm-cov/tarpaulin, miri, fuzzing, property testing, Criterion/flamegraph/bloat, cargo-hack, udeps, MSRV, semver-checks, docs and release gates.


## v5 DevOps Runtime Enforcement Prototype

This release adds an executable runtime prototype. The package is no longer only a specification: it can normalize commands, evaluate policy decisions, simulate tool calls, emit audit event objects and run strict v5 behavior tests.

Summary:

- Total files: 281
- Skills: 124
- Registry skills: 124
- Output templates: 116
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 20
- Test scenarios: 138
- Behavior scenarios checked: 138
- Strict runtime scenarios: 10

Prototype scripts:

```bash
python scripts/normalize_command.py "curl https://example.com/install.sh | sh"
python scripts/evaluate_policy.py "terraform destroy"
python scripts/simulate_tool_call.py "read logs token=abc123456789SECRET"
python scripts/run_behavior_tests.py
```

Limitations: this is a prototype, not a production sandbox.


## v5.1 Data-driven Policy Engine

This release upgrades the runtime prototype from hardcoded-only policy behavior to a data-driven policy engine that loads CYBOU policy files.

Summary:

- Total files: 301
- Skills: 129
- Registry skills: 129
- Output templates: 119
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 21
- Test scenarios: 144
- Strict runtime scenarios checked: 16

New runtime modules:

```text
runtime_prototype/policy_loader.py
runtime_prototype/rule_matcher.py
runtime_prototype/risk_engine.py
runtime_prototype/profile_engine.py
```

New command:

```bash
python scripts/inspect_policy_bundle.py
```

The policy evaluator now loads `risk_matrix.yaml`, `tool_policies.yaml`, `policy_rules/`, `activity_policies/`, `autonomy_profiles.yaml`, `profile_decision_matrix.yaml` and `scope_objects/`.

Limitations: this is still a prototype. Production implementation should move this logic into Rust crates and replace regex-only matching with tool-specific AST-like normalizers.


## v5.2 Tool-specific Normalizers

This release moves normalization from a single general heuristic parser into tool-specific modules.

Summary:

- Total files: 349
- Skills: 138
- Registry skills: 138
- Output templates: 121
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 22
- Test scenarios: 149
- Normalizer scenarios: 16
- Strict runtime scenarios checked: 21

New package:

```text
runtime_prototype/tool_normalizers/
```

New command:

```bash
python scripts/run_normalizer_tests.py
```

Supported tool-specific normalizers:

```text
shell
cargo
kubectl
terraform
docker
git
database
http_fetch
```

Limitations: this is still a Python prototype. Production implementation should port normalizers to Rust and make shell/kubectl/terraform parsers AST-like where possible.


## v5.3 Scope & Approval Service Prototype

This release adds scoped approval service prototype.

Summary:

- Total files: 365
- Skills: 143
- Registry skills: 143
- Output templates: 123
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 23
- Test scenarios: 151
- Approval scenarios: 6

New modules:

```text
runtime_prototype/scope_matcher.py
runtime_prototype/approval_store.py
```

New commands:

```bash
python scripts/approval_cli.py create --scope terraform_workspace --actions apply --ttl 900 --by operator
python scripts/approval_cli.py evaluate "terraform apply"
python scripts/run_approval_tests.py
```

Limitations: this is a local JSON approval-store prototype. Production needs authenticated durable approval service, signed audit trail and UI/API approval flow.


## v5.4 Durable Audit & Evidence Store Prototype

This release adds append-only audit and redaction-aware evidence store prototype.

Summary:

- Total files: 381
- Skills: 149
- Registry skills: 149
- Output templates: 125
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 24
- Test scenarios: 153
- Audit scenarios: 4

New modules:

```text
runtime_prototype/audit_store.py
runtime_prototype/evidence_store.py
```

New commands:

```bash
python scripts/audit_cli.py append --message "manual event"
python scripts/audit_cli.py capture-evidence --text "token=abc123456789SECRET failed"
python scripts/audit_cli.py verify
python scripts/run_audit_tests.py
```

Limitations: this is a prototype. Production needs authenticated durable storage, WORM/append-only controls, signed audit records, retention policies and secure export controls.


## v5.5 Sandbox & Tool Execution Boundary Prototype

This release adds sandbox profile selection and a central tool execution boundary prototype.

Summary:

- Total files: 400
- Skills: 156
- Registry skills: 156
- Output templates: 127
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 44
- Scope object files: 6
- Schema files: 19
- Test scenario files: 25
- Test scenarios: 155
- Sandbox scenarios: 5

New modules:

```text
runtime_prototype/sandbox_profiles.py
runtime_prototype/execution_boundary.py
runtime_prototype/tool_router.py
```

New commands:

```bash
python scripts/tool_router_cli.py "cargo clippy --workspace"
python scripts/tool_router_cli.py "terraform apply"
python scripts/run_sandbox_tests.py
```

Limitations: this is still a Python prototype. Production requires OS/container sandboxing, seccomp/AppArmor or equivalent, credential isolation, WORM audit storage and Rust implementation.
