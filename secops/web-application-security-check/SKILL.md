---
name: web-application-security-check
description: Perform safe, authorized web application security checks without destructive exploitation. Use for reviewing
  headers, cookies, TLS, authentication flow observations, access control evidence from provided accounts, input validation
  review, and OWASP-style finding triage.
---

# Web Application Security Check

## Default mode

Safe checks only.

## Preconditions

Use `pentest-scope-and-authorization` first.

## Safe checks

- security headers;
- cookie flags;
- TLS/certificate configuration;
- exposed debug pages;
- verbose error messages;
- authentication and session behavior observations;
- access control checks with provided authorized test accounts;
- input validation review using harmless probes;
- CORS configuration review;
- rate-limit observation without stress.

## Not allowed by default

- SQL injection exploitation;
- command injection exploitation;
- XSS payload delivery to real users;
- SSRF exploitation;
- file upload weaponization;
- brute force;
- DoS;
- credential harvesting;
- testing outside scope.

## Evidence handling

- redact tokens/cookies;
- do not include live session IDs;
- avoid storing sensitive responses;
- stop if customer data appears.

## Output

```md
## Web application security check
Target:
Scope:
Checks performed:
Findings:
Evidence:
Risk:
Recommended remediation:
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
