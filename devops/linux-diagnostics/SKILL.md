---
name: linux-diagnostics
description: Diagnose Linux host issues safely using read-only commands first. Use for operational troubleshooting of service
  down, high CPU, high memory, disk full, inode exhaustion, systemd failures, port conflicts, permissions, DNS symptoms, file
  descriptors, and server health.
---

# Linux Diagnostics

## Default mode

Read-only.

## Read-only commands

```bash
hostname
uptime
date
df -h
df -i
free -m
ps aux --sort=-%mem | head
ps aux --sort=-%cpu | head
ss -tulpn
journalctl -p err --since "1 hour ago" --no-pager
systemctl status SERVICE --no-pager
journalctl -u SERVICE --since "1 hour ago" --no-pager
ulimit -n
```

## Decision tree

### Disk usage above 90 percent
- Do not delete files.
- Identify largest directories.
- Check log growth.
- Check inode exhaustion with `df -i`.
- Recommend cleanup candidates.
- Ask approval before deletion.

### Service failed
- Check status and recent logs.
- Look for config, permission, port, dependency, or crash errors.
- Propose restart only after approval.

### Port conflict
- Identify process using port.
- Do not kill process without approval.

### File descriptor exhaustion
- Check service logs and limits.
- Recommend limit review, not immediate change.

## Approval required

- restart service;
- stop service;
- kill process;
- delete files;
- change permissions;
- install packages.

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
