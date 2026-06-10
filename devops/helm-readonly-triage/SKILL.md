---
name: helm-readonly-triage
description: Inspect Helm releases safely using read-only commands. Use for Helm deployment history, release status, rendered values review, rollback planning, chart version investigation, and Kubernetes incidents involving Helm-managed resources.
---

# Helm Read-only Triage

## Default mode

Read-only.

## Safe commands

```bash
helm list -n NAMESPACE
helm status RELEASE -n NAMESPACE
helm history RELEASE -n NAMESPACE
helm get values RELEASE -n NAMESPACE
helm get manifest RELEASE -n NAMESPACE
```

## Caution

Helm values may contain secrets. Redact sensitive output.

## Use cases

- determine last deployed revision;
- inspect failed release;
- compare chart/app versions;
- prepare rollback plan without executing rollback;
- identify generated Kubernetes resources.

## Approval required

- `helm upgrade`;
- `helm rollback`;
- `helm uninstall`;
- changing values;
- applying manifests.

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
