---
name: network-diagnostics
description: Diagnose network, DNS, TLS, port, ingress, egress, proxy, timeout, connection refused, firewall, and service connectivity problems using safe read-only checks. Use for operational troubleshooting, not aggressive scanning.
---

# Network Diagnostics

## Default mode

Read-only.

## Procedure

1. Identify source and destination.
2. Check DNS.
3. Check port reachability.
4. Check TLS.
5. Check routing/proxy.
6. Check service listener.
7. Check firewall/security group/network policy.
8. Summarize likely failure layer.

## Read-only examples

```bash
dig example.com
nslookup example.com
curl -Iv https://example.com
ss -tulpn
ip route
openssl s_client -connect example.com:443 -servername example.com
```

## Caution

- Do not run aggressive scans without approval.
- `curl` output may expose headers/cookies. Redact.

## Approval required

- firewall changes;
- security group changes;
- DNS changes;
- proxy config changes;
- ingress apply/patch.

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
