---
name: mariadb-wordpress-admin
version: "9.0"
skill_format: operational_contract_v1
category: devops/database
default_mode: guarded
default_risk: medium
selection_profile: narrow
summary: Administer MariaDB for WordPress using mysql/mariadb CLI, socket auth basics, DB/user/grants, and no PostgreSQL drift.
requires_tools:
  preferred:
    - mcp:filesystem:read_file
  fallback:
    - shell
    - mysql
    - mariadb
policy_refs:
  - policy_rules/shell.yaml
triggers:
  include:
    - MariaDB WordPress database user grants
    - mysql -e create database wordpress
    - mariadb socket auth Debian
    - create WordPress DB user grants
    - avoid PostgreSQL for WordPress MariaDB
  exclude:
    - PostgreSQL migration
    - generic database question
    - sqlite only
negative_triggers:
  - database
  - sql
  - user
  - admin
activation_examples:
  - "Create MariaDB database and user for WordPress using mysql -e."
  - "Fix drift where agent tries psql for MariaDB WordPress."
output_template: mariadb_wordpress_admin_report
---

# MariaDB WordPress Admin

## 1. Use when

Use for MariaDB/MySQL administration required by WordPress installation: create database, create user, grant privileges, check socket authentication, verify service status, and update WordPress DB credentials safely.

## 2. Do not use when

Do not use for PostgreSQL, generic SQL tuning, analytics queries, or non-WordPress schema work.

Do not trigger from `database`, `sql`, `user`, or `admin` alone.

## 3. Operating mode

Default is guarded VM-local DB administration. Use `mysql`/`mariadb`, not `psql`. Prefer `mysql -e`/`mariadb -e` commands with explicit SQL. Do not echo real passwords into logs. Use placeholders in reports.

## 4. Risk mapping

### low
- inspect MariaDB service status;
- inspect current databases/users metadata;
- test socket-auth login;
- read WordPress config with secrets redacted.

### medium
- create VM-local WordPress database;
- create VM-local DB user;
- grant least-privilege access to WordPress DB;
- flush privileges;
- verify login with redacted command display.

### high
- alter production database/user;
- dump database containing customer data;
- reset root password;
- expose credentials in output;
- broad grants outside target DB.

### critical
- drop/truncate database;
- grant `ALL PRIVILEGES ON *.*` to app user;
- disable authentication/security;
- delete database files.

## 5. Preferred tool order

1. Use MCP file read for config inspection if available.
2. Use shell MariaDB CLI for VM-local commands.
3. Use `mysql` or `mariadb`; never drift to PostgreSQL tooling.
4. Redact passwords in logs and final output.

## 6. Command templates

### read_only: discover service and CLI

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
systemctl status mariadb --no-pager || systemctl status mysql --no-pager
command -v mariadb || command -v mysql
mariadb --version 2>/dev/null || mysql --version 2>/dev/null
```

### read_only: socket auth and metadata

```bash
sudo mysql -e "SELECT USER(), CURRENT_USER(), VERSION();" 2>/dev/null || sudo mariadb -e "SELECT USER(), CURRENT_USER(), VERSION();"
sudo mysql -e "SHOW DATABASES;" 2>/dev/null || sudo mariadb -e "SHOW DATABASES;"
sudo mysql -e "SELECT User, Host, plugin FROM mysql.user;" 2>/dev/null || sudo mariadb -e "SELECT User, Host, plugin FROM mysql.user;"
```

### guarded: create WordPress DB and least-privilege user

```bash
sudo mysql -e "CREATE DATABASE IF NOT EXISTS \`<wp_db>\` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
sudo mysql -e "CREATE USER IF NOT EXISTS '<wp_user>'@'localhost' IDENTIFIED BY '<strong-password>';"
sudo mysql -e "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON \`<wp_db>\`.* TO '<wp_user>'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"
```

Use `mariadb -e` equivalents if `mysql` is unavailable.

### read_only: verify app user login without exposing password in report

```bash
MYSQL_PWD='<strong-password>' mysql -u '<wp_user>' -h localhost -e "SHOW DATABASES; SELECT DATABASE();" '<wp_db>'
```

Do not print the real password in final output.

### read_only: inspect WordPress DB config with redaction

```bash
grep -nE "DB_NAME|DB_USER|DB_PASSWORD|DB_HOST" <wordpress-root>/wp-config.php | sed -E "s/(DB_PASSWORD'.*, *')[^']+/'DB_PASSWORD', '***REDACTED***/"
```

### blocked

```bash
psql -c "..."
sudo -u postgres psql
DROP DATABASE <wp_db>;
GRANT ALL PRIVILEGES ON *.* TO '<wp_user>'@'localhost';
UPDATE mysql.user SET authentication_string=...
```

## 7. Failure recovery

### If MariaDB login fails for root

1. Try Debian socket auth:

```bash
sudo mysql -e "SELECT CURRENT_USER();" || sudo mariadb -e "SELECT CURRENT_USER();"
```

2. If socket auth fails, inspect service logs:

```bash
systemctl status mariadb --no-pager || systemctl status mysql --no-pager
journalctl -u mariadb -n 80 --no-pager || journalctl -u mysql -n 80 --no-pager
```

3. Do not reset root credentials automatically.

### If agent context drifts to PostgreSQL

1. Stop PostgreSQL commands.
2. Reconfirm service:

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
```

3. Use `mysql`/`mariadb` commands only.

### If grant fails due to syntax/version

1. Inspect version:

```bash
sudo mysql -e "SELECT VERSION();"
```

2. Split `CREATE USER` and `GRANT` commands.
3. Verify with `SHOW GRANTS`:

```bash
sudo mysql -e "SHOW GRANTS FOR '<wp_user>'@'localhost';"
```

## 8. Stop / block conditions

Stop if:

- environment is production/unknown and write is requested;
- root/socket auth cannot be established;
- requested grants exceed target WordPress DB;
- command would expose DB password;
- destructive SQL is requested.

## 9. Output contract

```markdown
## MariaDB WordPress admin report

### Summary

### Environment
- Service:
- CLI:
- Version:
- Auth mode observed:

### WordPress DB plan
- Database:
- User:
- Host:
- Grants:

### Commands/tools used
- secrets redacted

### Verification
- DB exists:
- User exists:
- Grants verified:

### Risk classification
- estimated_risk:
- risk drivers:

### Actions taken

### Blocked actions

### Recommendation
```

## 10. Eval requirements

Create evals for:

- WordPress MariaDB task rejects PostgreSQL drift;
- socket auth uses `sudo mysql -e`;
- creates DB/user/grants with least privilege;
- blocks `GRANT ALL ON *.*`;
- redacts password in output.
