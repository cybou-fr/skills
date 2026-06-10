# Validation Report

Generated: 2026-06-10T20:25:57.667647+00:00

## Structural validation

- Total files: 491
- Skill files: 195
- Registry skills: 195
- Output templates: 137
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 69
- Scope object files: 6
- Schema files: 19
- Test scenario files: 28
- Test scenarios: 167
- Validation errors: 0
- Validation warnings: 0

## Regression tests

- Normalizer scenarios: 16
- Approval scenarios: 6
- Audit scenarios: 4
- Sandbox scenarios: 5
- Detection scenarios: 5
- Cloud SecOps scenarios: 5
- Identity/secrets scenarios: 6
- Behavior scenarios: 167
- Strict runtime scenarios: 21

## Demo Identity/Secrets/KMS

```json
{
  "secret_aws_key": {
    "finding_count": 1,
    "severity": "critical",
    "findings": [
      {
        "kind": "aws_access_key_id",
        "start": 8,
        "end": 28,
        "value_redacted": true,
        "preview": "<REDACTED>"
      }
    ],
    "read_only_next_steps": [
      "identify storage location and exposure window",
      "map consumers/dependencies",
      "check recent use logs without printing secret",
      "prepare rotation/revocation plan"
    ],
    "approval_required_actions": [
      "rotate secret",
      "revoke session/token",
      "delete exposed credential",
      "update dependent applications"
    ]
  },
  "oauth_high_risk": {
    "app_id": "app-1",
    "publisher": "Unknown",
    "severity": "high",
    "risky_scopes": [
      "User.ReadWrite.All",
      "offline_access"
    ],
    "reasons": [
      "high_risk_scopes",
      "insecure_redirect_uri",
      "unverified_publisher"
    ],
    "approval_required_actions": [
      "remove consent",
      "disable app",
      "delete app credential"
    ]
  },
  "kms_wildcard": {
    "severity": "high",
    "finding_count": 2,
    "findings": [
      {
        "risk": "high",
        "issue": "wildcard_principal_or_action"
      },
      {
        "risk": "high",
        "issue": "kms:*"
      }
    ],
    "read_only_next_steps": [
      "collect key usage metadata",
      "review grants/bindings",
      "verify rotation and deletion window"
    ],
    "approval_required_actions": [
      "change key policy",
      "disable/delete key",
      "revoke grant",
      "change rotation schedule"
    ]
  },
  "identity_admin_no_mfa": {
    "principal": "admin@example.com",
    "severity": "high",
    "reasons": [
      "privileged_without_mfa"
    ],
    "approval_required_actions": [
      "disable principal",
      "remove role",
      "revoke sessions",
      "rotate/delete service account key"
    ]
  },
  "audit_valid": true,
  "evidence_valid": true
}
```

## Commands

```bash
python scripts/identity_secrets_cli.py classify-secret --text "token=abc123456789SECRET"
python scripts/identity_secrets_cli.py oauth-review --app-json '{"app_id":"app-1","scopes":["User.ReadWrite.All","offline_access"],"publisher_verified":false}'
python scripts/identity_secrets_cli.py key-policy-review --policy-json '{"Statement":[{"Effect":"Allow","Principal":"*","Action":"kms:*","Resource":"*"}]}'
python scripts/identity_secrets_cli.py identity-review --principal-json '{"id":"admin@example.com","privileged":true,"mfa_enabled":false}'
python scripts/run_identity_secrets_tests.py
```
