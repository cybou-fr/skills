---
name: linux-diagnostics
description: Diagnose Linux guest system issues (high CPU, disk full, OOM, memory, service status, journalctl logs).
description_fr: Diagnostiquer les problèmes système Linux (CPU élevé, disque plein, OOM, mémoire, état des services, journaux journalctl).
category: devops
triggers: linux, systemctl, journalctl, disk full, high cpu, memory, inode, service down
risk: low
---

# Linux System Diagnostics

## 1. Use when

Use this skill when checking guest VM system health, troubleshooting slow services, investigating disk space exhaustion, high CPU utilization, memory pressure, or OOM crashes.

## 2. Command templates & Diagnostic steps

### CPU & System Load
To check load averages and CPU consumption:
```bash
uptime
top -b -n 1 | head -30
ps aux --sort=-%cpu | head -15
```

### Memory & OOM investigation
To check free memory and inspect if services were terminated by the Out-Of-Memory (OOM) killer:
```bash
free -m
vmstat 1 5
dmesg -T | grep -i -E 'oom|kill|out of memory' | tail -10
journalctl -kt oom-killer --no-pager | tail -10
```

### Disk Space & Inodes
To inspect disk usage, mounted file systems, and inode usage:
```bash
df -h
df -i
# Find the top 10 largest files in a directory (e.g. /var/log)
find /var/log -type f -exec du -h {} + | sort -rh | head -10
```

### Services & System Logs
To check failed systemd services and view logs:
```bash
systemctl --failed --no-pager
systemctl list-units --state=failed --no-pager
journalctl -xb -p err..emerg --no-pager | tail -50
```

## 3. Stop / block conditions

Do not write or modify files or services during diagnostics. This skill is strictly read-only for triage. If repairs are needed, hand off to `safe-file-authoring` or service management skills.

## 4. Verification

After diagnosing, summarize the system state (CPU load, free memory, disk availability, failed services) to provide a clear diagnostic report.
