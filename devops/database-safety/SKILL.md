---
name: database-safety
description: Safely inspect databases and review SQL or migrations. Use for database diagnostics, SQL review, migrations, slow queries, backup-before-change checks, read-only query safety, and preventing destructive database actions.
---

# Database Safety

## Default mode

Read-only.

## Recommendation

Prefer read-only credentials for diagnostics.

## Safe operations

Usually safe:
- `SELECT` with limits;
- `EXPLAIN`;
- schema inspection;
- migration review;
- backup status check.

## Dangerous operations

Approval required:
- `INSERT`;
- `UPDATE`;
- `DELETE`;
- `ALTER`;
- `CREATE INDEX`;
- migrations;
- restore.

Denied by default:
- `DROP DATABASE`;
- `TRUNCATE`;
- `DELETE` without `WHERE`;
- `UPDATE` without `WHERE`;
- destructive migration without backup.

## Query safety

1. Add `LIMIT` when inspecting data.
2. Do not output PII.
3. Prefer aggregates over raw rows.
4. Explain query purpose.
5. Check transaction/rollback plan.
6. Confirm backup before migration.

## Transaction review

For proposed writes, draft transaction plan only unless approved:

```sql
BEGIN;
-- proposed change
-- verify affected rows
ROLLBACK;
```

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
