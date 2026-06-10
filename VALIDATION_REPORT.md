# Validation Report

Generated: 2026-06-10T21:02:05.111663+00:00

README was refreshed for v5.9 and no longer presents v4 as the current package.

## README patch validation

- Missing registry skill paths: 0
- Missing output templates: 0
- Registry skills: 207
- Skill files: 207
- Source package previous validation: errors 0, warnings 0


# Validation Report

Generated: 2026-06-10T20:55:18.337224+00:00

## Structural validation

- Total files: 515
- Skill files: 207
- Registry skills: 207
- Output templates: 139
- Policy rule files: 13
- Activity policy files: 2
- Tool adapter files: 74
- Scope object files: 6
- Schema files: 19
- Test scenario files: 29
- Test scenarios: 171
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
- Forensics scenarios: 4
- Behavior scenarios: 171
- Strict runtime scenarios: 21

## Demo Forensics Case

```json
{
  "case_id": "7c36e022-5558-42b3-bd7a-85d5f78f9186",
  "evidence_id": "75a8526b-3c83-4e4d-bf7c-e5dd330ec666",
  "evidence_redaction_applied": true,
  "note_redaction_applied": true,
  "timeline_event_count": 1,
  "evidence_count": 1,
  "chain_of_custody_valid": true,
  "audit_valid": true,
  "evidence_store_valid": true
}
```

## Commands

```bash
python scripts/case_cli.py create --title "Suspicious IAM Activity" --severity high --owner soc
python scripts/case_cli.py evidence --case-id <case_id> --source cloudtrail --content "2026-06-10T12:00:00Z CreateAccessKey from 203.0.113.7"
python scripts/case_cli.py timeline --case-id <case_id> --summary "CreateAccessKey event" --source cloudtrail
python scripts/case_cli.py export --case-id <case_id>
python scripts/run_forensics_tests.py
```
