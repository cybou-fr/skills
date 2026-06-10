---
name: environment-detection
description: Determine whether the worker is operating in local, development, staging, production, customer, or unknown environment.
  Use before deployments, restarts, database work, Kubernetes, cloud, IAM, or any write action.
---

# Environment Detection

## Default

Unknown environment means read-only mode.

Low confidence environment means read-only mode.

## Detection signals

Check:
- hostname;
- Kubernetes context;
- namespace;
- cloud account/project/subscription;
- branch name;
- environment variables;
- deployment labels;
- database name;
- URL/domain;
- CI/CD environment;
- user-provided context.

## Confidence scoring

```yaml
environment:
confidence: low|medium|high
evidence:
  - ...
default_mode:
risk_modifier:
```

## Environment risk

| Environment | Default mode |
|---|---|
| local sandbox | low-risk actions may be allowed |
| development | cautious write with approval if needed |
| staging | approval recommended for changes |
| production | approval required for changes |
| customer environment | approval required |
| unknown | read-only only |

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
