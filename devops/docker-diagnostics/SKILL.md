---
name: docker-diagnostics
description: Diagnose Docker and Docker Compose problems. Use for operational troubleshooting of failed containers, container
  exits, build failures, logs, image issues, port conflicts, volume permissions, Docker Compose services, and runtime debugging.
---

# Docker Diagnostics

## Default mode

Read-only.

## Read-only diagnostics

```bash
docker ps -a
docker images
docker logs CONTAINER --tail 100
docker inspect CONTAINER
docker stats --no-stream
docker compose ps
docker compose logs --tail=100
docker compose config
```

## Caution

`docker inspect` may expose environment variables and secrets. Redact output.

## Common cases

### Container exits immediately
Check exit code, logs, command/entrypoint, missing env/config, permission errors.

### Port conflict
Check published ports and host listeners.

### Volume permission issue
Check container user, mounted path, ownership, read-only mount.

### Build failure
Check first failing Dockerfile step, `.dockerignore`, dependency install failure, registry/network issue.

## Escalate to `container-security-review` if

- privileged container;
- Docker socket mount;
- host network;
- root user;
- hardcoded secret;
- `latest` tag in production.

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
