---
name: api-security-check
description: Perform safe, authorized API security checks. Use for OpenAPI/Swagger review, authentication and authorization review with provided test credentials, rate-limit observation, error handling, sensitive data exposure review, and non-destructive API finding triage.
---

# API Security Check

## Default mode

Safe, non-destructive API review.

## Preconditions

- API target in scope.
- Test credentials provided or no-auth endpoint authorized.
- Rate limits respected.
- Data handling rules known.

## Safe checks

- OpenAPI/Swagger review;
- authentication requirement review;
- authorization checks using authorized test accounts;
- method exposure review;
- error message review;
- object-level authorization evidence;
- sensitive field exposure;
- CORS and headers;
- rate-limit observation without stress.

## Not allowed by default

- brute force;
- token theft;
- fuzzing at high volume;
- destructive POST/PUT/PATCH/DELETE;
- accessing real customer data;
- bypassing auth outside explicit scope.

## Output

```md
## API security check
API:
Scope:
Auth context:
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
