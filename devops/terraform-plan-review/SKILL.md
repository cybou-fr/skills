---
name: terraform-plan-review
version: "7.0"
skill_format: operational_contract_v1
category: devops
default_mode: read_only
default_risk: high
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - mcp:git:diff
    - mcp:terraform:plan_reader
  fallback:
    - terraform
    - shell
    - git
policy_refs:
  - policy_rules/terraform.yaml
  - policy_rules/shell.yaml
  - policy_rules/git.yaml
output_template: terraform_plan_review_report
---

# Terraform Plan Review

## 1. Use when

Use for Terraform/OpenTofu plan review, `.tf` diffs, infrastructure-as-code blast-radius analysis, cloud resource changes, IAM changes, networking changes, database/storage changes, public exposure, production IaC review, and destructive-change prevention.

## 2. Do not use when

Do not use to apply, destroy, force-unlock state, import resources, or mutate production infrastructure. Use a deployment/change-management skill for approved execution planning.

## 3. Operating mode

Default mode is read-only review. Never apply from this skill. If the next action exceeds runtime policy, emit a blocked/high-risk or critical decision and provide a safer review-only alternative.

## 4. Risk mapping

### low

- Read `.tf` files and plan output.
- Run format check and validation without backend access.
- Parse plan JSON.
- Count create/update/delete/replace actions.

### medium

- Generate local review notes.
- Run static scanners such as Checkov/tfsec/Terrascan in local workspace.
- Run `terraform plan` only with safe constraints in non-production and without applying changes.

### high

- Plan touches production.
- Plan touches IAM, security groups, firewall, public exposure, databases, storage, backups, KMS/keys, logs, monitoring, or networking.
- Replacement of stateful resources.
- Backend/state access with write lock risk.

### critical

- `terraform destroy`.
- `terraform apply` of destructive plan.
- `terraform force-unlock` without scoped incident process.
- Delete/replace database, cluster, storage, backup, KMS key, audit logs, or IAM admin controls.

## 5. Preferred tool order

1. Prefer MCP filesystem/git tools for `.tf` diffs and plan artifacts.
2. Prefer MCP Terraform plan reader if available.
3. Use Terraform CLI fallback only for read-only checks with safe backend constraints.
4. Never use Terraform commands to bypass host policy, state policy, or approval boundaries.

## 6. Command templates

### read_only

```bash
terraform fmt -check -recursive
terraform init -backend=false
terraform validate
terraform show -json <planfile> > tfplan.json
jq '[.resource_changes[]? | {address, type, name, actions: .change.actions}]' tfplan.json
jq '[.resource_changes[]? | select(.change.actions | index("delete")) | {address, type, actions: .change.actions}]' tfplan.json
jq '[.resource_changes[]? | select(.change.actions == ["delete","create"] or .change.actions == ["create","delete"]) | {address, type, actions: .change.actions}]' tfplan.json
git diff -- '*.tf' '*.tfvars' '.terraform.lock.hcl'
```

If a local non-production plan is explicitly permitted:

```bash
terraform plan -refresh=false -out=tfplan
terraform show -json tfplan > tfplan.json
```

### guarded

No infrastructure writes belong in this skill. Static scanners may be run locally:

```bash
checkov -d .
tfsec .
terrascan scan -t terraform
conftest test .
```

### approval_or_policy_required

```bash
terraform plan -out=tfplan
terraform import <address> <id>
terraform state mv <source> <destination>
terraform state rm <address>
```

### blocked

```bash
terraform apply
terraform apply -auto-approve
terraform destroy
terraform destroy -auto-approve
terraform force-unlock <lock-id>
rm -rf .terraform terraform.tfstate terraform.tfstate.backup
```

## 7. Failure recovery

### provider init failure

Run backend-free init and report provider/version issue. Do not modify provider constraints automatically.

```bash
terraform init -backend=false
terraform providers
```

### backend access required

Do not obtain credentials or access remote state automatically. Ask the host policy layer for scoped state access or request an uploaded plan artifact.

### state lock

Do not run force-unlock automatically. Report lock holder, environment, and required coordination.

### variable missing

Report missing variables and source files. Do not invent production values.

```bash
terraform validate
git diff -- '*.tfvars' '*.tf'
```

### plan contains destroy

Classify at least high; critical if production/stateful/security/audit resources are affected. Extract resource addresses and data-loss/downtime risk.

### plan contains replacement

Identify replacement actions and whether resources are stateful or public-facing. Treat database/storage/cluster replacement as critical unless proven sandbox.

### plan touches IAM/security/networking

Classify high. Flag admin privileges, wildcard policies, public ingress `0.0.0.0/0`, disabled encryption, disabled logs, and KMS/key changes.

### plan touches production

Block execution. Produce review-only report and required approval scope.

## 8. Stop / block conditions

Stop before apply, destroy, force-unlock, state mutation, import, production write, destructive plan, IAM/admin escalation, public exposure, or deletion of backups/audit logs/KMS keys.

## 9. Output contract

Return:

- summary;
- environment;
- evidence inspected;
- commands/tools used;
- action counts: create/update/delete/replace;
- blast radius;
- dangerous changes;
- data loss risk;
- downtime risk;
- security exposure;
- risk classification;
- actions taken;
- blocked actions;
- recommendation.

## 10. Eval requirements

Add evals for safe plan parsing, provider init failure, backend access block, destroy detection, stateful replacement, IAM/networking high-risk classification, apply/destroy blocking, MCP diff preference, CLI fallback, and correct estimated_risk classification.
