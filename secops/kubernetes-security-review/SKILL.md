---
name: kubernetes-security-review
description: Review Kubernetes manifests and cluster resources for security risks. Use for Pod securityContext, RBAC, NetworkPolicy, Secrets exposure, privileged workloads, admission policy, service accounts, hostPath, hostNetwork, and namespace security review.
---

# Kubernetes Security Review

## Default mode

Read-only review.

## Review areas

- Pod security context;
- privileged containers;
- hostPath mounts;
- hostNetwork;
- hostPID;
- service account permissions;
- RBAC bindings;
- network policies;
- secrets usage;
- image tags;
- resource limits;
- admission policies.

## Red flags

- `privileged: true`;
- `hostNetwork: true`;
- broad ClusterRoleBinding;
- default service account with elevated permissions;
- no NetworkPolicy in sensitive namespace;
- secrets mounted unnecessarily;
- `latest` image tag;
- no resource limits.

## Approval required

- patching resources;
- applying manifests;
- deleting bindings;
- changing network policies.

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
