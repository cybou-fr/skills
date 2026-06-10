---
name: kubernetes-readonly-triage
description: Triage Kubernetes issues using read-only kubectl and optional Helm commands. Use for operational troubleshooting of pods, deployments, services, ingress, CrashLoopBackOff, ImagePullBackOff, Pending, OOMKilled, NodeNotReady, PVC Pending, RBAC Forbidden, and cluster diagnostics.
---

# Kubernetes Read-only Triage

## Default mode

Read-only.

## Safety

Do not run:
- `kubectl apply`;
- `kubectl delete`;
- `kubectl edit`;
- `kubectl patch`;
- `kubectl scale`;
- `kubectl rollout restart`.

Do not show raw secret values. Avoid `kubectl get secret -o yaml`.

ConfigMaps may contain sensitive values. Redact if displayed.

## Read-only command set

```bash
kubectl config current-context
kubectl get nodes
kubectl get pods -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl get deploy -n NAMESPACE
kubectl get svc -n NAMESPACE
kubectl get endpoints -n NAMESPACE
kubectl get ingress -n NAMESPACE
kubectl get pvc -n NAMESPACE
kubectl get networkpolicy -n NAMESPACE
kubectl describe pod POD -n NAMESPACE
kubectl logs POD -n NAMESPACE --tail=100
kubectl logs POD -n NAMESPACE --previous --tail=100
kubectl top pods -n NAMESPACE
kubectl auth can-i get pods -n NAMESPACE
```

## Optional Helm read-only commands

If Helm release is involved, use `helm-readonly-triage`.

## Decision tree

### CrashLoopBackOff
Check previous logs, env/config errors, missing configmap/secret, healthcheck, startup command.

### ImagePullBackOff
Check image name, tag, registry access, pull secret, network.

### Pending
Check resources, node capacity, taints, node selectors, PVC binding.

### OOMKilled
Check memory limit, peak usage, recent traffic, memory leak signs.

### Service unreachable
Check selector, endpoints, pod labels, ingress, network policy.

### RBAC Forbidden
Use `kubectl auth can-i`. Do not escalate permissions.

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
