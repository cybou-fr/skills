# Changelog


## v5.5.0 — Sandbox & Tool Execution Boundary Prototype

### Added

- Sandbox profiles:
  - `sandbox_profiles.yaml`
- Sandbox profile engine:
  - `runtime_prototype/sandbox_profiles.py`
- Tool execution boundary:
  - `runtime_prototype/execution_boundary.py`
- Tool router execution prototype:
  - `runtime_prototype/tool_router.py`
- Tool router CLI:
  - `scripts/tool_router_cli.py`
- Sandbox regression tests:
  - `sandbox_tests/`
  - `scripts/run_sandbox_tests.py`
- New skills:
  - `runtime-sandbox-profile-engine`
  - `runtime-tool-execution-boundary`
  - `runtime-filesystem-boundary`
  - `runtime-network-boundary`
  - `runtime-output-limit-boundary`
  - `runtime-tool-router-execution-prototype`
  - `runtime-sandbox-regression-suite`

### Improved

- Dry-run is default.
- Execution is allowlist-based.
- Denied and approval-required actions do not execute.
- Execution results are captured into evidence store and linked to audit records.
- Output is bounded and redacted.

### Limitation

This is still a Python prototype. Production requires OS/container sandboxing, seccomp/AppArmor or equivalent, credential isolation, WORM audit storage and Rust implementation.



## v5.4.0 — Durable Audit & Evidence Store Prototype

### Added

- Durable audit store:
  - `runtime_prototype/audit_store.py`
- Evidence store:
  - `runtime_prototype/evidence_store.py`
- Audit CLI:
  - `scripts/audit_cli.py`
- Audit test runner:
  - `scripts/run_audit_tests.py`
- Audit fixtures:
  - `audit_tests/`
- New skills:
  - `runtime-durable-audit-store`
  - `runtime-evidence-store`
  - `runtime-audit-cli`
  - `runtime-tamper-evidence`
  - `runtime-evidence-redaction-integration`
  - `runtime-audit-regression-suite`

### Improved

- Audit events can be appended to JSONL with sequence, previous hash and record hash.
- Audit verification detects modification/reordering/deletion through hash-chain checks.
- Evidence capture stores redacted text plus metadata and SHA-256 digest.
- CLI supports append/list/verify/export/capture-evidence/evaluate.

### Limitation

This is a prototype. Production needs authenticated durable storage, WORM/append-only controls, signed audit records, retention policies and secure export controls.



## v5.3.0 — Scope & Approval Service Prototype

### Added

- Scope matcher:
  - `runtime_prototype/scope_matcher.py`
- Approval store prototype:
  - `runtime_prototype/approval_store.py`
- Approval CLI:
  - `scripts/approval_cli.py`
- Approval test runner:
  - `scripts/run_approval_tests.py`
- Approval fixtures:
  - `approval_tests/`
- New skills:
  - `runtime-scope-matcher`
  - `runtime-approval-store`
  - `runtime-approval-cli`
  - `runtime-approval-policy-integration`
  - `runtime-approval-regression-suite`

### Improved

- Approval can change `approval_required` into `allow_with_approval` only when scope/action/expiration match.
- Hard-deny decisions cannot be overridden by approval.
- Tests cover valid approval, wrong action, wrong scope, expired approval and hard-deny-not-overridden.

### Limitation

This remains a local JSON approval-store prototype. Production needs authenticated durable approval service, signed audit trail and UI/API approval flow.



## v5.2.0 — Tool-specific Normalizers

### Added

- Tool-specific normalizer package:
  - `runtime_prototype/tool_normalizers/`
- Normalizers:
  - shell
  - cargo
  - kubectl
  - terraform
  - docker
  - git
  - database
  - http_fetch
- Compatibility wrapper:
  - `runtime_prototype/normalizers.py`
- Normalizer regression runner:
  - `scripts/run_normalizer_tests.py`
- Normalizer regression fixtures:
  - `normalizer_tests/`
- Strict runtime behavior test:
  - `tests/tool_specific_normalizers_v5_2.yaml`
- New skills:
  - `runtime-shell-normalizer`
  - `runtime-cargo-normalizer`
  - `runtime-kubectl-normalizer`
  - `runtime-terraform-normalizer`
  - `runtime-docker-normalizer`
  - `runtime-git-normalizer`
  - `runtime-database-normalizer`
  - `runtime-http-fetch-normalizer`
  - `runtime-normalizer-regression-suite`

### Improved

- Normalization moved from one general heuristic parser to tool-specific modules.
- Dispatcher keeps backward-compatible `normalize()` API.
- Normalizer tests verify tool, operation, target, environment, side effects and sensitive-data detection.

### Limitation

This is still a Python prototype. Production implementation should port normalizers to Rust and make shell/kubectl/terraform parsers AST-like where possible.



## v5.1.0 — Data-driven Policy Engine

### Added

- Data-driven runtime policy modules:
  - `runtime_prototype/policy_loader.py`
  - `runtime_prototype/rule_matcher.py`
  - `runtime_prototype/risk_engine.py`
  - `runtime_prototype/profile_engine.py`
- Policy bundle inspector:
  - `scripts/inspect_policy_bundle.py`
- Data-driven examples:
  - `examples/data_driven_policy/`
- Strict data-driven policy tests:
  - `tests/data_driven_policy_v5_1.yaml`
- New runtime skills:
  - `runtime-policy-loader`
  - `runtime-rule-matcher`
  - `runtime-risk-engine`
  - `runtime-profile-scope-engine`
  - `runtime-policy-regression-suite`

### Improved

- `runtime_prototype/policy.py` now loads policy bundle data from the package.
- Rule matching reports YAML rule IDs when they match.
- Risk engine applies risk floors, side effects, environment and sensitive data.
- Profile/scope engine participates in policy decisions.
- Hardcoded logic is now a safe fallback rather than the only behavior.

### Limitation

This is still a prototype. Production implementation should move these components into Rust crates and replace regex-only matching with tool-specific AST-like normalizers.



## v5.0.0 — DevOps Runtime Enforcement Prototype

### Added

- Executable Python runtime prototype:
  - `runtime_prototype/models.py`
  - `runtime_prototype/normalizers.py`
  - `runtime_prototype/policy.py`
  - `runtime_prototype/audit.py`
  - `runtime_prototype/redaction.py`
- CLI scripts:
  - `scripts/normalize_command.py`
  - `scripts/evaluate_policy.py`
  - `scripts/route_task.py`
  - `scripts/simulate_tool_call.py`
- Strict v5 runtime behavior tests:
  - `tests/runtime_enforcement_v5.yaml`
- Runtime enforcement skills:
  - `runtime-normalized-action-engine`
  - `runtime-policy-decision-engine`
  - `runtime-approval-state-manager`
  - `runtime-audit-event-pipeline`
  - `runtime-redaction-boundary`
  - `runtime-tool-router`
  - `runtime-behavior-test-engine`
- Example normalized action / policy decision / audit event outputs.

### Improved

- Behavior runner now strictly checks v5 runtime scenarios and keeps older scenarios as routing/safety coverage.
- Runtime prototype can normalize commands, evaluate policy, simulate tool calls, redact mock output and emit audit event objects.

### Limitation

This is a prototype, not a production sandbox. Real production use still requires hardened parsers, process isolation, credential boundaries, persistent audit storage and a real approval service.



## v4.5.0 — Rust Toolchain Mastery

### Added

- Full Rust toolchain skills:
  - `rust-toolchain-management`
  - `rust-linting-and-formatting`
  - `rust-test-infrastructure`
  - `rust-coverage-workflow`
  - `rust-benchmarking-and-profiling`
  - `rust-fuzzing-and-property-testing`
  - `rust-miri-unsafe-validation`
  - `rust-ci-quality-gates`
  - `rust-docs-and-api-contracts`
  - `rust-release-and-semver`
  - `rust-feature-matrix-and-hack`
  - `rust-dead-code-and-dependency-hygiene`
- New adapters for nextest, llvm-cov, tarpaulin, miri, fuzz, hack, udeps, msrv, semver-checks, Criterion, flamegraph, bloat and geiger.
- `rust_toolchain_quality_matrix.yaml`
- Rust config templates:
  - `templates/rust-toolchain.toml`
  - `templates/rustfmt.toml`
  - `templates/clippy.toml`
  - `templates/deny.toml`
- `tests/rust_toolchain_mastery.yaml`

### Improved

- Rust senior architect profile now covers the full quality toolchain.
- Cargo publish/install/fuzz/profiling operations remain approval-gated.
- CYBOU self-development can now use complete Rust quality gates.



## v4.4.0 — Rust Senior Developer / Software Architect

### Added

- Rust senior developer and software architect skills for building CYBOU itself.
- CYBOU self-hosting development loop.
- CYBOU Rust architecture map.
- Cargo and rust-analyzer tool adapters.
- Cargo policy rules.
- Rust architect autonomy profile.
- Rust architecture and implementation test scenarios.

### New Rust/CYBOU skills

- `rust-senior-code-review`
- `rust-software-architecture`
- `rust-workspace-and-crate-design`
- `rust-async-runtime-design`
- `rust-error-handling-observability`
- `rust-api-design`
- `rust-security-hardening`
- `rust-performance-engineering`
- `rust-testing-strategy`
- `rust-dependency-supply-chain-review`
- `rust-tool-adapter-implementation`
- `cybou-policy-engine-implementation`
- `cybou-skill-runtime-implementation`
- `cybou-self-hosting-development-loop`

### Safety

CYBOU self-development is treated as high-value internal development. New dependencies, policy engine changes, tool adapter changes, publishing, and production deployment remain approval-gated.



## v4.3.0 — Upstream Catalog Adapters

### Added

- `upstream_catalog_mapping.yaml`
- CYBOU-native adapters inspired by public Anthropic and OpenAI skills catalogs.
- Document/artifact workflows: DOCX, PDF, PPTX, XLSX, screenshots.
- Design/frontend workflows: brand guidelines, frontend review, web artifacts, themes, Figma handoff, image briefs.
- Developer platform workflows: MCP builder, skill creator/installer, CLI creator, OpenAI/Claude API integration, ChatGPT apps.
- Deployment/repo workflows: static platform deploy, GitHub comment triage, CI fix proposal, Sentry issue triage, issue tracker workflow.
- Productivity/research workflows: goal definition, meeting intelligence, knowledge capture, research docs, notebooks, speech/transcription.
- Security governance workflows: security best practices, ownership map, threat modeling.
- Additional external tools and adapters: Figma, issue tracker, deployment platform, Sentry, notebook runtime, audio processor.

### Note

This release does not vendor or copy upstream skill contents. It adds CYBOU-native compatible workflows based on observed public catalog categories and folder names.



## v4.2.0 — Runtime Completeness

### Added

- `external_tools.yaml`
- Additional tool adapters for abstract/external tools.
- Runtime schemas for tool adapters, skill graph, autonomy profiles, policy decisions, normalized actions, task state and tool-call state.
- `runtime/runtime_objects.yaml`
- `profile_decision_matrix.yaml`
- AI security scope objects.
- `tests/runtime_completeness.yaml`
- Compact behavior test runner with optional `--full` output.

### Improved

- External and abstract tools are explicitly cataloged.
- Runtime policy decisions and normalized actions now have formal schemas.
- Behavior runner emits compact risk/decision summaries.
- Runtime manifest now requires normalized actions, policy decisions and external tool catalog.



## v4.1.0 — AI Security / LLM AppSec skills

### Added

- New AI security activity policy:
  - `activity_policies/ai_security_assessment.yaml`
- New AI security controls map:
  - `ai_security_controls.yaml`
- New policy/tool adapter:
  - `policy_rules/ai_security.yaml`
  - `tool_adapters/ai_security.yaml`
- New schema:
  - `schemas/ai_security_test_case.schema.json`
- New tests:
  - `tests/ai_security.yaml`
- New skills:
  - `ai-jailbreak-defense`
  - `indirect-prompt-injection-assessment`
  - `ai-agent-tool-abuse-review`
  - `rag-poisoning-defense`
  - `model-data-leakage-review`
  - `model-denial-of-service-cost-abuse`
  - `ai-supply-chain-review`
  - `ai-evaluation-and-redteam-reporting`
  - `ai-memory-and-context-safety`
  - `ai-output-handling-review`

### Safety

- The package supports defensive AI security assessment only.
- Jailbreak prompt generation, bypass instructions, exploit optimization, secret exfiltration, malware/phishing generation, and third-party testing without authorization are denied by default.
- AI security testing should use synthetic fixtures, placeholders, and approved evaluation harnesses.



## v4.0.0 — CYBOU Runtime Integration Pack

### Added

- `runtime/integration_manifest.yaml`
- `runtime/decision_enums.yaml`
- `autonomy_profiles.yaml`
- `skill_graph.yaml`
- `tool_adapters/`
- `scope_objects/`
- `schemas/scope_object.schema.json`
- `schemas/approval_state.schema.json`
- `schemas/audit_event.schema.json`
- `scripts/run_behavior_tests.py`
- `tests/runtime_integration.yaml`

### Improved

- Added boot sequence and runtime component contract.
- Added tool adapter layer for shell, kubectl, terraform, docker, git, database, http_fetch, GitHub, cloud and pentest activities.
- Added autonomy profiles for readonly, local dev, staging, production, SecOps incident and authorized pentest workflows.
- Added generic scope objects for production changes, incidents and pentest.
- Added skill graph for co-loading and escalation.
- Added behavior test runner scaffold.
- Extended validation to runtime integration files.

### Safety

- Tool calls must be intercepted before execution.
- Unknown environment limits autonomy to read-only.
- High/critical actions require scoped approval.
- Activity policies and tool adapters are now separated.
- Pentest remains authorized, scope-bound and policy-gated.



## v3.3.0 — Pentest hardening

### Added

- `activity_policies/penetration_testing.yaml`
- `schemas/pentest_scope.schema.json`
- `schemas/activity_policy.schema.json`
- `schemas/severity_model.schema.json`
- `templates/pentest_scope.yaml`
- `severity_model.yaml`
- New skills:
  - `pentest-retest-validation`
  - `pentest-evidence-redaction`
  - `pentest-severity-rating`
- New tests:
  - `tests/penetration_testing_hardening.yaml`

### Improved

- Added machine-readable penetration testing activity classes.
- Added pentest scope object template.
- Added severity rating model for findings.
- Added risk floors for stealth/evasion, malware, phishing/social engineering, third-party targets and out-of-scope assets.
- Strengthened validator for activity policy and pentest scope template presence.

### Safety

- Active and invasive testing remains approval-required.
- DoS, credential theft, persistence, malware, stealth/evasion, social engineering, and out-of-scope testing remain denied by default.



## v3.2.0 — Authorized penetration testing extension

### Added

- New penetration testing skills:
  - `pentest-scope-and-authorization`
  - `passive-reconnaissance`
  - `safe-vulnerability-validation`
  - `web-application-security-check`
  - `api-security-check`
  - `pentest-finding-report`
  - `pentest-retainer-triage`
- New `policy_rules/pentest.yaml`.
- New `tests/penetration_testing.yaml`.
- New pentest output templates.
- Pentest-specific risk floors and approval policy.

### Safety model

- Penetration testing requires explicit authorization and scope.
- Active scanning requires approval, scope, and rate limits.
- DoS, credential theft, persistence, stealth, malware, and out-of-scope testing are denied by default.


## v3.1.0 — Consistency and validation release

### Fixed

- Added all missing output templates referenced by `registry.yaml`.
- Updated package version metadata to `3.1.0`.
- Added deeper validation script at `scripts/validate_pack.py`.
- Updated `VALIDATION_REPORT.md` to include cross-reference checks.
- Expanded test scenarios from 16 to 50.
- Added additional test files for approval, cloud, and supply chain scenarios.

### Improved

- Added `risk_floor`, `approval_policy`, and `environment_rules` to `risk_matrix.yaml`.
- Strengthened runtime consistency expectations.
- Added validation for:
  - registry path existence;
  - registry id matching SKILL.md frontmatter name;
  - related skills existence;
  - output template existence;
  - policy regex compilation;
  - test required skills existence.

## v3.0.0 — Runtime pack

- Added schemas, policy rules, tests, CYBOU manifest, and expanded skills.

## v2.0.0 — AgentSkills-compatible pack

- Converted flat Markdown documents into AgentSkills-compatible skill directories.

## v1.0.0 — Initial Markdown pack

- Initial DevOps/SecOps skill notes and procedures.
