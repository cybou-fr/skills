---
name: database-safety
version: "7.0"
skill_format: operational_contract_v1
category: devops
default_mode: read_only
default_risk: high
requires_tools:
  preferred:
    - mcp:database:metadata
    - mcp:database:readonly_query
    - mcp:filesystem:read_file
  fallback:
    - database
    - shell
policy_refs:
  - policy_rules/database.yaml
  - policy_rules/shell.yaml
output_template: database_safety_report
---

# Database Safety

## 1. Use when

Use for database diagnostics, SQL review, migration review, slow query analysis, backup-before-change checks, read-only query safety, transaction planning, and destructive database action prevention.

## 2. Do not use when

Do not use for automatic production writes, destructive schema changes, unauthorized data access, credential extraction, or bulk data export. Use incident/evidence skills when preserving forensic state is the main objective.

## 3. Operating mode

Default mode is read-only. Writes, schema changes, migrations, restores, and destructive commands are not automatic. If an action exceeds runtime policy or environment is unknown/production, emit a blocked/high-risk decision or approval_request artifact.

## 4. Risk mapping

### low

- Inspect database version and connection metadata without secrets.
- List schemas/tables/indexes.
- Run `EXPLAIN` without execution where supported.
- Run bounded aggregate or metadata queries.

### medium

- Read-only `SELECT` on indexed columns with strict `LIMIT` in non-production.
- Create local/sandbox backup dump when policy permits.
- Draft transaction-wrapped write plan without execution.
- Review migration file diffs.

### high

- `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `CREATE INDEX`, migrations, restore.
- Backup/export of production or customer data.
- Long-running query that may lock or overload database.
- Reading PII/raw customer rows.

### critical

- `DROP DATABASE`, `DROP SCHEMA`, `DROP TABLE`.
- `TRUNCATE`.
- `DELETE` or `UPDATE` without `WHERE`.
- Destructive migration without verified backup and rollback.
- Production write in unknown scope.

## 5. Preferred tool order

1. Prefer MCP database metadata/read-only query tools using read-only credentials.
2. Prefer MCP filesystem/git tools for migration diffs.
3. Use database CLI fallback only with explicit target and bounded output.
4. Never print secrets, credentials, raw PII, or unrestricted query results.

## 6. Command templates

### read_only

#### PostgreSQL

```bash
psql "$DATABASE_URL" -c "select version();"
psql "$DATABASE_URL" -c "select current_database(), current_user;"
psql "$DATABASE_URL" -c "select schemaname, tablename from pg_tables where schemaname not in ('pg_catalog','information_schema') order by 1,2 limit 100;"
psql "$DATABASE_URL" -c "select relname, n_live_tup from pg_stat_user_tables order by n_live_tup desc limit 20;"
psql "$DATABASE_URL" -c "explain <SELECT_QUERY>;"
```

#### MySQL/MariaDB

```bash
mysql --execute="select version();"
mysql --execute="select database(), user();"
mysql --execute="show tables;"
mysql --execute="show indexes from <table>;"
mysql --execute="explain <SELECT_QUERY>;"
```

#### SQLite

```bash
sqlite3 <database.sqlite> ".tables"
sqlite3 <database.sqlite> ".schema <table>"
sqlite3 <database.sqlite> "EXPLAIN QUERY PLAN <SELECT_QUERY>;"
sqlite3 <database.sqlite> "select name, type from sqlite_master order by type, name limit 100;"
```

#### migration review

```bash
git diff -- db/migrations migrations prisma schema.sql
git diff -- '*.sql'
```

### guarded

```sql
BEGIN;
-- proposed non-production change
-- verify affected rows
ROLLBACK;
```

Guarded transaction rehearsal is only for local/sandbox databases when policy permits. Production writes remain high risk and non-automatic.

### approval_or_policy_required

```sql
INSERT INTO <table> (...) VALUES (...);
UPDATE <table> SET ... WHERE ...;
DELETE FROM <table> WHERE ...;
ALTER TABLE <table> ...;
CREATE INDEX CONCURRENTLY <index> ON <table> (...);
```

```bash
pg_dump "$DATABASE_URL" --format=custom --file=<backup.dump>
mysqldump <database> > <backup.sql>
sqlite3 <database.sqlite> ".backup <backup.sqlite>"
```

### blocked

```sql
DROP DATABASE <database>;
DROP SCHEMA <schema> CASCADE;
DROP TABLE <table>;
TRUNCATE <table>;
DELETE FROM <table>;
UPDATE <table> SET <column>=<value>;
```

## 7. Failure recovery

### connection refused

Inspect host/port, service status if VM-local, DNS, network policy, and connection string without printing secrets. Do not modify firewall or database service automatically.

### permission denied

Report missing privilege and query attempted. Do not escalate role or grant permissions automatically.

### migration failed

Stop writes. Inspect migration name, error line, transaction state, backup status, and rollback availability. Draft recovery plan only.

### lock timeout

PostgreSQL:

```sql
select pid, state, wait_event_type, wait_event, query from pg_stat_activity where wait_event is not null limit 20;
```

MySQL:

```sql
show processlist;
```

Do not kill sessions automatically.

### long-running query

Inspect query plan and active sessions. Prefer aggregates and limits. Do not terminate queries automatically unless VM-local policy explicitly permits.

### missing backup

Classify write/migration as high or critical. Do not proceed with destructive or schema change operations.

### unknown production database

Default to read-only metadata inspection. Block writes, dumps of customer data, and destructive actions.

## 8. Stop / block conditions

Stop when action is production write, unknown environment write, destructive SQL, raw PII output, bulk export, restore, migration without verified backup, privilege escalation, or session termination.

## 9. Output contract

Return:

- summary;
- database type and environment;
- evidence inspected;
- commands/tools used;
- query/migration classification;
- data sensitivity notes;
- backup/rollback status;
- risk classification;
- actions taken;
- blocked actions;
- recommended next steps.

## 10. Eval requirements

Add evals for metadata inspection, read-only SELECT with LIMIT, migration failure, lock timeout, missing backup, DROP/TRUNCATE blocking, MCP database preference, CLI fallback, and correct estimated_risk classification.
