# CYBOU Agent Skills Pack v5.9

**Version:** 5.9.0  
**Codename:** Forensics & Incident Case Management Layer  
**Status:** Prototype / specification pack for a controlled DevOps + SecOps + SOC + Cloud SecOps + Identity + Forensics AI worker runtime.

This README has been refreshed for v5.9. It replaces the older v4-oriented README text and is the current entrypoint for the package.

## What this pack is

CYBOU v5.9 is a structured agent-skills and runtime-prototype package for building an enterprise AI worker that can assist with:

- DevOps and Rust engineering review;
- SecOps and AI-security review;
- SOC alert triage and detection engineering;
- Cloud SecOps across AWS, Azure and GCP;
- identity, secrets and key-management review;
- incident forensics and case management;
- controlled tool execution with policy, approval, sandboxing, audit and evidence capture.

The core security principle is:

```text
assistant text must never become direct tool execution
```

Every potentially operational action should pass through:

```text
raw input
  -> tool-specific normalizer
  -> NormalizedAction
  -> data-driven policy engine
  -> scope / approval check
  -> sandbox profile selection
  -> execution boundary
  -> bounded output
  -> redaction
  -> audit store
  -> evidence store
  -> case / forensic workflow when relevant
```

## Current package statistics

```text
Total files: 515
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
```

Additional regression suites:

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

## v5.x evolution map

### v5.0 — Runtime Enforcement Prototype

Introduced executable runtime concepts:

- `NormalizedAction`
- `PolicyDecision`
- policy evaluation
- audit events
- redaction boundary
- behavior tests

### v5.1 — Data-driven Policy Engine

Moved from hardcoded-only policy behavior toward data-driven policy.

Key files:

```text
runtime_prototype/policy_loader.py
runtime_prototype/rule_matcher.py
runtime_prototype/risk_engine.py
runtime_prototype/profile_engine.py
scripts/inspect_policy_bundle.py
```

### v5.2 — Tool-specific Normalizers

Replaced one general heuristic parser with tool-specific modules.

Supported normalizers:

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

Key directory:

```text
runtime_prototype/tool_normalizers/
```

### v5.3 — Scope & Approval Service Prototype

Added scoped approvals:

- local approval store;
- approval CLI;
- expiration;
- revocation;
- action/scope matching;
- `approval_required -> allow_with_approval` only when valid;
- hard-deny decisions cannot be overridden by approval.

Key files:

```text
runtime_prototype/approval_store.py
runtime_prototype/scope_matcher.py
scripts/approval_cli.py
scripts/run_approval_tests.py
```

### v5.4 — Durable Audit & Evidence Store Prototype

Added durable/tamper-evident audit and evidence handling:

- append-only audit JSONL;
- sequence numbers;
- previous hash;
- record hash;
- verification;
- redacted evidence capture;
- evidence SHA-256 metadata.

Key files:

```text
runtime_prototype/audit_store.py
runtime_prototype/evidence_store.py
scripts/audit_cli.py
scripts/run_audit_tests.py
```

### v5.5 — Sandbox & Tool Execution Boundary Prototype

Added controlled execution boundary:

- sandbox profiles;
- dry-run default;
- allowlisted low-risk execution;
- timeout and output caps;
- network/filesystem boundary concepts;
- execution result evidence capture.

Key files:

```text
sandbox_profiles.yaml
runtime_prototype/sandbox_profiles.py
runtime_prototype/execution_boundary.py
runtime_prototype/tool_router.py
scripts/tool_router_cli.py
scripts/run_sandbox_tests.py
```

### v5.6 — SOC & Detection Engineering Layer

Added SOC/detection engineering layer:

- IOC extraction;
- alert triage;
- Sigma draft generation;
- YARA draft generation;
- threat hunting query drafts;
- timeline support;
- case workflow foundation.

Key files:

```text
runtime_prototype/ioc_extractor.py
runtime_prototype/detection_rules.py
runtime_prototype/incident_timeline.py
runtime_prototype/soc_triage.py
scripts/soc_cli.py
scripts/run_detection_tests.py
```

### v5.7 — Cloud SecOps Deepening

Added provider-specific cloud security coverage:

```text
AWS CloudTrail
AWS GuardDuty
AWS Security Hub
AWS IAM Access Analyzer
Azure Activity Log
Azure Entra ID
Azure Defender
GCP Audit Logs
GCP Security Command Center
```

Key files:

```text
runtime_prototype/cloud_secops.py
scripts/cloud_secops_cli.py
scripts/run_cloud_secops_tests.py
```

### v5.8 — Identity, Secrets & Key Management Deepening

Added identity, secrets and key-management workflows:

- identity lifecycle risk;
- privileged access review;
- OAuth app consent review;
- secrets exposure triage;
- secret rotation planning;
- Vault / Secrets Manager review;
- KMS/key policy review;
- access key hygiene;
- session token/cookie review;
- MFA/conditional access review.

Key files:

```text
runtime_prototype/identity_secrets.py
scripts/identity_secrets_cli.py
scripts/run_identity_secrets_tests.py
```

### v5.9 — Forensics & Incident Case Management Layer

Added incident case and forensic workflow prototype:

- case records;
- forensic artifact inventory;
- chain-of-custody metadata;
- redacted evidence attachment;
- timeline reconstruction;
- post-incident evidence pack;
- legal hold / retention planning.

Key files:

```text
runtime_prototype/forensics_case.py
scripts/case_cli.py
scripts/run_forensics_tests.py
```

## Important runtime semantics

### Policy before execution

```text
raw command
  -> normalize
  -> evaluate policy
  -> apply approval/scope
  -> select sandbox
  -> execute only if allowed
```

### Approval is scoped

Approval can satisfy `approval_required` only when scope, action and expiration match.

```text
terraform apply + valid approval(scope=terraform_workspace, actions=apply)
  -> allow_with_approval
```

Approval must not override hard deny:

```text
terraform destroy -auto-approve + approval(scope=terraform_workspace, actions=destroy)
  -> deny_by_default
```

### Dry-run is default

The tool router defaults to dry-run. In reports:

```text
would_execute=true
```

does not mean the command actually ran. Actual execution is only for allowlisted low-risk commands when explicitly enabled.

### Secret values must not be exposed

Secret-bearing evidence must be redacted before model exposure, audit/evidence storage or case export.

```text
token=abc123456789SECRET
  -> <REDACTED>
```

### Audit/evidence must be verifiable

Audit records use a simple hash-chain prototype:

```text
sequence
previous_hash
record_hash
```

Evidence records include metadata and content digests.

### Forensics must preserve custody

Case evidence includes:

```text
evidence_id
source
collector
timestamp
sha256
redaction_applied
chain_of_custody
iocs
```

## Main directories

```text
core/
devops/
secops/
productivity/
runtime_prototype/
scripts/
templates/
policy_rules/
activity_policies/
tool_adapters/
scope_objects/
schemas/
tests/
normalizer_tests/
approval_tests/
audit_tests/
sandbox_tests/
detection_tests/
cloud_secops_tests/
identity_secrets_tests/
forensics_tests/
examples/
```

## Main runtime prototype modules

```text
runtime_prototype/models.py
runtime_prototype/normalizers.py
runtime_prototype/tool_normalizers/
runtime_prototype/policy_loader.py
runtime_prototype/rule_matcher.py
runtime_prototype/risk_engine.py
runtime_prototype/profile_engine.py
runtime_prototype/policy.py
runtime_prototype/approval_store.py
runtime_prototype/scope_matcher.py
runtime_prototype/audit.py
runtime_prototype/audit_store.py
runtime_prototype/evidence_store.py
runtime_prototype/redaction.py
runtime_prototype/sandbox_profiles.py
runtime_prototype/execution_boundary.py
runtime_prototype/tool_router.py
runtime_prototype/ioc_extractor.py
runtime_prototype/detection_rules.py
runtime_prototype/incident_timeline.py
runtime_prototype/soc_triage.py
runtime_prototype/cloud_secops.py
runtime_prototype/identity_secrets.py
runtime_prototype/forensics_case.py
```

## Validation commands

Run from the package root:

```bash
python scripts/validate_pack.py
python scripts/run_behavior_tests.py
python scripts/run_normalizer_tests.py
python scripts/run_approval_tests.py
python scripts/run_audit_tests.py
python scripts/run_sandbox_tests.py
python scripts/run_detection_tests.py
python scripts/run_cloud_secops_tests.py
python scripts/run_identity_secrets_tests.py
python scripts/run_forensics_tests.py
```

Expected status for the v5.9 source package before this README refresh:

```text
pass
errors: 0
warnings: 0
```

This README-only patch also passes basic structural consistency:

```text
registry skills == skill files
all registry skill paths exist
all referenced output templates exist
```

## Useful CLI examples

### Policy evaluation

```bash
python scripts/evaluate_policy.py "cargo clippy --workspace"
python scripts/evaluate_policy.py "terraform apply"
python scripts/evaluate_policy.py "curl https://example.com/install.sh | sh"
```

### Tool router

```bash
python scripts/tool_router_cli.py "cargo clippy --workspace"
python scripts/tool_router_cli.py "terraform apply"
python scripts/tool_router_cli.py "git status"
```

### Approval

```bash
python scripts/approval_cli.py create --scope terraform_workspace --actions apply --ttl 900 --by operator
python scripts/approval_cli.py list
python scripts/approval_cli.py evaluate "terraform apply"
python scripts/approval_cli.py revoke <approval_id>
```

### Audit/evidence

```bash
python scripts/audit_cli.py append --message "manual event"
python scripts/audit_cli.py capture-evidence --text "token=abc123456789SECRET failed"
python scripts/audit_cli.py verify
python scripts/audit_cli.py export
```

### SOC/detection

```bash
python scripts/soc_cli.py extract-iocs --text "login from 203.0.113.10 to https://evil.example.com/a.exe"
python scripts/soc_cli.py sigma --title "Suspicious Curl Pipe Shell" --keywords "curl,| sh"
python scripts/soc_cli.py yara --name Suspicious_Tool --strings "evil marker,powershell -enc"
python scripts/soc_cli.py triage-alert --alert-json '{"severity":"high","message":"credential exfiltration from host 203.0.113.5"}'
```

### Cloud SecOps

```bash
python scripts/cloud_secops_cli.py triage-event --event-json '{"provider":"aws","eventName":"CreateAccessKey","userIdentity":"arn:aws:iam::123:user/alice"}'
python scripts/cloud_secops_cli.py iam-review --policy-json '{"Statement":[{"Effect":"Allow","Action":"*","Resource":"*"}]}'
```

### Identity / secrets / key management

```bash
python scripts/identity_secrets_cli.py classify-secret --text "token=abc123456789SECRET"
python scripts/identity_secrets_cli.py oauth-review --app-json '{"app_id":"app-1","scopes":["User.ReadWrite.All","offline_access"],"publisher_verified":false}'
python scripts/identity_secrets_cli.py key-policy-review --policy-json '{"Statement":[{"Effect":"Allow","Principal":"*","Action":"kms:*","Resource":"*"}]}'
python scripts/identity_secrets_cli.py identity-review --principal-json '{"id":"admin@example.com","privileged":true,"mfa_enabled":false}'
```

### Forensics / case management

```bash
python scripts/case_cli.py create --title "Suspicious IAM Activity" --severity high --owner soc
python scripts/case_cli.py evidence --case-id <case_id> --source cloudtrail --content "2026-06-10T12:00:00Z CreateAccessKey from 203.0.113.7"
python scripts/case_cli.py timeline --case-id <case_id> --summary "CreateAccessKey event" --source cloudtrail
python scripts/case_cli.py export --case-id <case_id>
```

## Security boundaries

This package should be treated as a prototype/specification pack, not as a production sandbox.

Production implementation still requires:

- Rust runtime implementation;
- OS/container sandboxing;
- seccomp/AppArmor/SELinux or equivalent;
- credential isolation;
- tenant-aware authorization;
- durable authenticated approval service;
- WORM or signed audit storage;
- real cloud/IdP/SIEM/EDR integrations;
- stronger secret and PII detection;
- signed case/evidence custody;
- deployment hardening and operational monitoring.

## Recommended next step

The v5.x specification/prototype line is now broad enough. The next major milestone should be:

```text
v6 — Rust Runtime Skeleton
```

Recommended v6 crates:

```text
cybou-core
cybou-policy
cybou-tools
cybou-runtime
cybou-audit
cybou-skills
cybou-cli
cybou-agent
```

v6 should port the runtime contracts into Rust while keeping this v5.9 pack as the behavioral/specification corpus.
