---
name: log-analysis
description: Analyze operational logs, group errors, build timelines, detect reliability and security patterns, and summarize
  likely root causes. Use for application logs, system logs, container logs, CI logs, incident timelines, and redacted pattern
  analysis.
---

# Log Analysis

## Default mode

Read-only. Redact sensitive values.

## Procedure

1. Normalize timestamp, service, severity, trace ID, user/session, host/pod.
2. Group by error type, endpoint, status code, host, deployment version.
3. Build timeline.
4. Identify reliability patterns.
5. Identify security indicators.
6. Summarize evidence and likely cause.

## Structured pattern output

```yaml
patterns:
  - type:
    count:
    first_seen:
    last_seen:
    example_redacted:
```

## Reliability patterns

- timeout;
- connection refused;
- DNS NXDOMAIN;
- TLS handshake failure;
- OOM;
- disk full;
- migration failed;
- rate limited;
- upstream 502/503;
- dependency unavailable.

## Security patterns

- repeated 401/403;
- SQL injection strings;
- path traversal;
- SSRF attempts;
- command injection;
- brute force;
- user enumeration;
- token replay.

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
