---
name: kubernetes-readonly-triage
version: "7.0"
skill_format: operational_contract_v1
category: devops
default_mode: read_only
default_risk: medium
requires_tools:
  preferred:
    - mcp:kubernetes:get
    - mcp:kubernetes:describe
    - mcp:kubernetes:logs
  fallback:
    - kubectl
policy_refs:
  - policy_rules/kubectl.yaml
  - policy_rules/shell.yaml
output_template: kubernetes_triage_report
---

# Kubernetes Read-only Triage

## 1. Use when

Use for Kubernetes read-only operational troubleshooting of pods, deployments, services, ingress, PVCs, nodes, CrashLoopBackOff, ImagePullBackOff, Pending, OOMKilled, NodeNotReady, RBAC Forbidden, service reachability, and cluster diagnostics.

## 2. Do not use when

Do not use for applying manifests, deleting resources, scaling workloads, patching resources, restarting rollouts, editing live objects, or exposing secrets. Use deployment or Kubernetes change-management skills for controlled write plans.

## 3. Operating mode

Default mode is read-only. Writes are not automatic. If runtime policy permits Kubernetes writes in a scoped sandbox, use a different guarded change skill; this skill should emit a triage report and stop.

## 4. Risk mapping

### low

- Inspect current context.
- List pods, deployments, services, events, PVCs, nodes.
- Describe non-secret resources.
- Read bounded logs with redaction.
- Check RBAC with `kubectl auth can-i`.

### medium

- Read ConfigMaps with redaction.
- Read cluster-wide metadata in production/unknown context.
- Use `kubectl top` for resource metrics.
- Triage potentially sensitive logs.

### high

- Any apply/edit/patch/scale/restart/delete action.
- Reading secret metadata with unclear redaction boundary.
- Displaying raw ConfigMap values that may contain credentials.
- Change proposals touching production workloads.

### critical

- `kubectl delete namespace`.
- Deleting workloads, PVCs, secrets, or CRDs.
- Displaying secret values using yaml/json output.
- Cluster-admin RBAC escalation.
- Disabling network/security controls.

## 5. Preferred tool order

1. Prefer host-governed Kubernetes MCP tools for get/describe/logs.
2. Use `kubectl` fallback only for read-only commands and bounded output.
3. Redact secrets and credential-like values in logs, ConfigMaps, and events.
4. Never use shell/kubectl to bypass host policy or secret controls.

## 6. Command templates

### read_only

```bash
kubectl config current-context
kubectl auth can-i get pods -n <namespace>
kubectl get nodes -o wide
kubectl get pods -A -o wide
kubectl get events -A --sort-by=.lastTimestamp
kubectl get deploy,statefulset,daemonset -n <namespace>
kubectl get svc,endpoints,ingress -n <namespace>
kubectl get pvc -n <namespace>
kubectl get networkpolicy -n <namespace>
kubectl describe pod <pod> -n <namespace>
kubectl describe deploy <deployment> -n <namespace>
kubectl logs <pod> -n <namespace> --tail=100
kubectl logs <pod> -n <namespace> --previous --tail=100
kubectl top pods -n <namespace>
kubectl top nodes
```

### guarded

No guarded write commands belong in this skill. Use a separate Kubernetes change skill if runtime policy allows changes.

### approval_or_policy_required

```bash
kubectl rollout restart deploy/<deployment> -n <namespace>
kubectl scale deploy/<deployment> --replicas=<n> -n <namespace>
kubectl patch <resource> <name> -n <namespace> --type merge -p '<patch>'
kubectl edit <resource> <name> -n <namespace>
kubectl apply -f <file>
```

### blocked

```bash
kubectl delete namespace <namespace>
kubectl delete pvc <pvc> -n <namespace>
kubectl delete secret <secret> -n <namespace>
kubectl get secret <secret> -n <namespace> -o yaml
kubectl get secret <secret> -n <namespace> -o json
kubectl create clusterrolebinding <name> --clusterrole=cluster-admin --user=<user>
```

## 7. Failure recovery

### CrashLoopBackOff

1. Inspect pod status and events.
2. Read previous logs.
3. Check command, args, env/config references, missing ConfigMap/Secret, healthchecks, image tag, and resource limits.
4. Do not restart rollout from this skill.

```bash
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --previous --tail=100
kubectl get events -n <namespace> --sort-by=.lastTimestamp
```

### ImagePullBackOff

Check image name/tag, registry, pull secret reference, service account, and node network symptoms.

```bash
kubectl describe pod <pod> -n <namespace>
kubectl get serviceaccount <sa> -n <namespace> -o yaml
```

Redact secret names if required by policy; never print secret values.

### Pending pods

Check scheduling, capacity, taints, node selectors, affinity, PVC binding, and quotas.

```bash
kubectl describe pod <pod> -n <namespace>
kubectl get nodes -o wide
kubectl describe node <node>
kubectl get pvc -n <namespace>
kubectl get resourcequota -n <namespace>
```

### OOMKilled

```bash
kubectl describe pod <pod> -n <namespace>
kubectl top pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --previous --tail=100
```

Report memory limits and symptoms. Do not patch resources from this skill.

### RBAC Forbidden

```bash
kubectl auth can-i <verb> <resource> -n <namespace>
kubectl auth can-i --list -n <namespace>
```

Do not escalate permissions.

### Service unreachable

```bash
kubectl get svc,endpoints -n <namespace>
kubectl describe svc <service> -n <namespace>
kubectl get pods -n <namespace> --show-labels
kubectl get networkpolicy -n <namespace>
```

Check selectors, endpoints, pod labels, ports, ingress, and network policies.

### Ingress failure

```bash
kubectl get ingress -n <namespace>
kubectl describe ingress <ingress> -n <namespace>
kubectl get svc,endpoints -n <namespace>
```

Check ingress class, host/path rules, TLS secret reference without printing secret values, and backend service endpoints.

### PVC pending

```bash
kubectl get pvc -n <namespace>
kubectl describe pvc <pvc> -n <namespace>
kubectl get storageclass
```

Check storage class, capacity, access mode, provisioner, and events.

### Node pressure

```bash
kubectl get nodes
kubectl describe node <node>
kubectl top node <node>
```

Report DiskPressure, MemoryPressure, PIDPressure, taints, and affected pods. Do not drain nodes from this skill.

## 8. Stop / block conditions

Stop when the next action requires apply, edit, patch, delete, scale, rollout restart, secret value access, cluster-admin escalation, namespace deletion, or any write to production/unknown cluster.

## 9. Output contract

Return:

- summary;
- cluster context and namespace;
- resource and symptom;
- evidence inspected;
- commands/tools used;
- likely cause;
- risk classification;
- actions taken;
- blocked actions;
- safe next command;
- recommended next steps.

## 10. Eval requirements

Add evals for CrashLoopBackOff, ImagePullBackOff, Pending PVC, RBAC Forbidden, Service unreachable, secret yaml blocking, MCP Kubernetes preference, kubectl fallback, and correct estimated_risk classification.
