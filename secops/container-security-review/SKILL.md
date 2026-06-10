---
name: container-security-review
description: Review container images, Dockerfiles, Docker Compose, Kubernetes securityContext, runtime privileges, image vulnerabilities, SBOM, provenance, and container hardening. Use when security-reviewing containers rather than debugging them.
---

# Container Security Review

## Default mode

Read-only.

## Review areas

### Image
- base image;
- pinned versions;
- known CVEs;
- unnecessary packages;
- secrets in layers;
- root user;
- build tools in runtime.

### Runtime
- privileged mode;
- capabilities;
- seccomp/apparmor;
- read-only filesystem;
- resource limits;
- host networking;
- Docker socket;
- hostPath.

## Kubernetes hardening draft

```yaml
securityContext:
  runAsNonRoot: true
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop: ["ALL"]
```

Do not blindly set `readOnlyRootFilesystem` if the app writes to filesystem; propose a temporary volume.

## Red flags

- `privileged: true`;
- root user;
- Docker socket mount;
- host network;
- no resource limits;
- hardcoded secret;
- `latest` tag in production;
- no image scanning;
- no SBOM.

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
