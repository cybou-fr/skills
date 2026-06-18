---
name: linux-diagnostics
version: "7.0"
skill_format: operational_contract_v1
category: devops
default_mode: read_only
default_risk: low
requires_tools:
  preferred:
    - mcp:host:metrics
    - mcp:filesystem:read_file
  fallback:
    - shell
policy_refs:
  - policy_rules/shell.yaml
output_template: linux_diagnostics_report
---

# Linux Diagnostics

## 1. Use when

Use for Linux host diagnostics: service down, high CPU, high memory, disk full, inode exhaustion, systemd failure, journal/log issues, port conflicts, permissions, DNS symptoms, file descriptor exhaustion, and general server health.

## 2. Do not use when

Do not use for destructive cleanup, production restart, package installation, firewall mutation, or persistence changes. Use deployment/incident skills when the task is an incident response or production change plan.

## 3. Operating mode

Default mode is read-only. VM-local reversible recovery may be guarded only when runtime policy allows it. Unknown or production writes are high risk and must be blocked or emitted as a host-policy approval artifact.

## 4. Risk mapping

### low

- Host baseline inspection.
- Read logs and status.
- Inspect disk, inode, memory, CPU, sockets, and service status.
- Identify largest directories without deleting files.

### medium

- VM-local bounded retry or restart of a synthetic/non-production service when policy permits.
- Create a patch proposal for config fixes.
- Rotate or truncate logs only in an isolated sandbox fixture when policy permits.

### high

- Restart/stop/kill unknown or production services.
- Delete logs or application data.
- Change permissions/ownership.
- Install packages.
- Modify systemd units or network/firewall configuration.

### critical

- Recursive destructive delete.
- Purge logs in an incident context.
- Disable security/audit services.
- Kill critical system processes.
- Modify production system state without policy scope.

## 5. Preferred tool order

1. Prefer host metrics/log MCP tools if available.
2. Use `mcp:filesystem:read_file` for known mounted logs/configs.
3. Use shell fallback only for VM-local inspection with bounded output.
4. Never use shell to bypass host policy, secret redaction, or approval boundaries.

## 6. Command templates

### read_only

#### host baseline

```bash
hostname
uptime
date
whoami
id
uname -a
```

#### disk usage

```bash
df -h
df -i
journalctl --disk-usage
du -xhd1 / 2>/dev/null | sort -h | tail -20
du -sh /var/log/* 2>/dev/null | sort -rh | head -20
find /var/log -type f -size +100M -printf '%s %p\n' 2>/dev/null | sort -nr | head -20
```

#### memory and CPU

```bash
free -m
ps aux --sort=-%mem | head -20
ps aux --sort=-%cpu | head -20
vmstat 1 5 2>/dev/null
```

#### service failure

```bash
systemctl status <service> --no-pager
systemctl cat <service> --no-pager
journalctl -u <service> -n 80 --no-pager
journalctl -p err --since "1 hour ago" --no-pager
```

#### port conflicts and networking basics

```bash
ss -tulpn
ss -tulpn | grep -E ':(<port>)\b'
ip addr
ip route
resolvectl status 2>/dev/null || cat /etc/resolv.conf
```

#### file descriptors and limits

```bash
ulimit -n
cat /proc/sys/fs/file-nr
ls -l /proc/<pid>/fd 2>/dev/null | wc -l
```

### guarded

```bash
systemctl restart <service>
systemctl reload <service>
```

Guarded only for VM-local/non-production service when policy permits. Verify once after the action and stop.

### approval_or_policy_required

```bash
systemctl stop <service>
kill <pid>
chmod <mode> <path>
chown <user>:<group> <path>
apt install <package>
```

### blocked

```bash
rm -rf /
rm -rf /var/log/*
journalctl --vacuum-size=1M
systemctl disable auditd
systemctl stop auditd
```

Blocked commands must not be executed automatically.

## 7. Failure recovery

### disk usage above 90 percent

1. Inspect filesystem usage and inode usage.
2. Identify largest directories and log growth using read-only commands.
3. Do not delete files automatically.
4. Recommend cleanup candidates and classify deletion as high/critical depending on environment.

### inode exhaustion

```bash
df -i
find / -xdev -printf '%h\n' 2>/dev/null | sort | uniq -c | sort -nr | head -20
```

Do not delete files automatically. Report top directories and likely source.

### service failed

```bash
systemctl status <service> --no-pager
journalctl -u <service> -n 80 --no-pager
systemctl cat <service> --no-pager
```

Classify config error, permission error, missing dependency, crash, OOM, or port conflict. VM-local guarded restart is allowed only if policy permits. Unknown/production restart is high risk.

### port already in use

```bash
ss -tulpn | grep -E ':(<port>)\b'
ps -fp <pid>
```

Do not kill the process automatically. Report owner, command, and safer alternatives.

### permission denied

Inspect path, owner, group, mode, service user, and SELinux/AppArmor hints if present. Do not chmod/chown automatically.

### journal unavailable

```bash
systemctl status systemd-journald --no-pager
ls -ld /var/log/journal /run/log/journal 2>/dev/null
```

If journal is unavailable, fall back to service-specific log paths only when known.

### OOM symptoms

```bash
journalctl -k --since "2 hours ago" --no-pager | grep -i -E 'out of memory|oom|killed process'
free -m
ps aux --sort=-%mem | head -20
```

Report memory pressure and suspect process. Do not kill processes automatically.

## 8. Stop / block conditions

Stop before writes when environment is unknown or production, when action deletes logs/data, kills processes, modifies permissions, installs packages, changes firewall/networking, disables security services, or purges evidence.

## 9. Output contract

Return:

- summary;
- environment;
- evidence inspected;
- commands/tools used;
- risk classification;
- likely cause;
- actions taken;
- blocked actions;
- safe next step;
- recommended next steps.

## 10. Eval requirements

Add evals for disk pressure, inode exhaustion, service failure with port conflict, permission denied, OOM symptoms, blocked log deletion, MCP metrics preference, shell fallback, and correct estimated_risk classification.
