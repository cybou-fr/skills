---
name: task-classification
description: Classify DevOps or SecOps requests, select candidate skills, determine default mode, and identify risk signals
  before execution. Use for ambiguous operational tasks, infrastructure, security, CI/CD, logs, incidents, deployments, cloud,
  database, network, or repository requests.
---

# Task Classification

## Purpose

Classify the user request before selecting operational skills.

## Do not use for

- Pure conceptual explanation.
- General tutorials without an operational target.
- Non-DevOps/SecOps writing tasks.

## Procedure

1. Identify task domain:
   - DevOps diagnostic;
   - DevOps change;
   - SecOps review;
   - SecOps incident;
   - repository/code review;
   - cloud/infrastructure;
   - database;
   - network;
   - deployment;
   - unknown.

2. Identify environment:
   - local sandbox;
   - development;
   - staging;
   - production;
   - customer environment;
   - unknown.

3. Identify data sensitivity:
   - public;
   - internal;
   - confidential;
   - secret;
   - regulated/customer data;
   - unknown.

4. Detect risk triggers:
   - production;
   - delete/remove/destroy;
   - secrets/tokens/keys;
   - IAM/admin/root/sudo;
   - database writes;
   - firewall/security groups;
   - external message;
   - deploy/restart/rollback;
   - incident/breach/compromise.

5. Select candidate skills from `registry.yaml`.

## Routing examples

| User request | Candidate skills |
|---|---|
| CI failed | `cicd-failure-analysis` |
| Pod is CrashLoopBackOff | `kubernetes-readonly-triage`, `devops-incident-triage` |
| Terraform plan review | `terraform-plan-review` |
| Token leaked | `secret-detection`, `secret-rotation-playbook`, `secops-incident-response` |
| Suspicious login | `security-log-review`, `secops-incident-response` |
| Review Dockerfile | `docker-diagnostics`, `container-security-review` |
| Database migration | `database-safety`, `deployment-planning` |

## Classification output

```yaml
task_type:
environment:
environment_confidence:
data_sensitivity:
production_impact:
requires_credentials:
requires_network:
requires_write_access:
risk_level:
approval_required:
selected_skills:
do_not_execute_reason:
```

## Required output

End with:
- summary;
- evidence;
- risk level;
- actions taken;
- recommended next steps;
- approval required, if any.

## Safety notes

If the task touches production, secrets, IAM, data deletion, database writes, firewall rules, external communication, or destructive commands, stop before write actions and request approval.

If a tool policy conflicts with this skill, the tool policy wins.
