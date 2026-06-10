---
name: passive-reconnaissance
description: Perform passive reconnaissance for authorized targets using non-invasive sources only. Use for domain inventory,
  certificate transparency review, DNS records, public metadata, exposed documentation, technology fingerprinting from provided
  data, and attack surface mapping without active probing.
---

# Passive Reconnaissance

## Default mode

Passive only.

## Preconditions

Use `pentest-scope-and-authorization` first.

## Allowed activities

- review provided asset inventory;
- inspect public DNS records;
- inspect certificate transparency records if tool/source is available;
- review public security headers from provided responses;
- identify public documentation exposure;
- map domains/subdomains from provided or authorized data;
- summarize visible technologies from provided headers/pages.

## Not allowed without explicit scope

- active port scanning;
- brute force;
- login attempts;
- directory brute forcing;
- vulnerability exploitation;
- bypass attempts;
- scraping at scale.

## Output

```md
## Passive reconnaissance summary
Scope:
Assets reviewed:
Public exposure:
Potential risks:
Recommended safe next checks:
Approval required:
```

## Required output

End with:
- scope/authorization status;
- summary;
- evidence;
- risk level;
- actions taken;
- recommended next steps;
- approval required, if any.

## Safety notes

Only perform penetration testing activities inside an explicitly authorized scope.

If authorization, ownership, scope, time window, or target identity is unclear, stop and request clarification.

Do not perform destructive exploitation, persistence, credential theft, malware deployment, stealth, evasion, denial-of-service, phishing, or data exfiltration.

If a policy rule conflicts with this skill, the policy rule wins.
