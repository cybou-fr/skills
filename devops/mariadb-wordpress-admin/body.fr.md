# Administration MariaDB WordPress


> Corps FR structurellement équivalent à SKILL.md. Les commandes, chemins, noms d’outils et labels de risque restent inchangés.

## 1. Quand utiliser

Use this skill to create or inspect a WordPress database, user, and grants on MariaDB/MySQL. Do not drift to PostgreSQL tools for WordPress tasks.

## 2. Mode opératoire

Default mode: guarded. Metadata inspection is low risk. Creating a database/user/grants in a VM is medium risk. Production DB writes are high risk.

## 3. Cartographie du risque

### low
- inspect MariaDB status and current users/databases;
- verify socket authentication.

### medium
- create a VM-local WordPress database/user/grants;
- verify grants and connectivity.

### high
- production database/user changes;
- credential handling.

### critical
- drop database/user;
- use broad global grants.

## 4. Ordre préféré des outils

1. Use secret-safe host tools for credential storage if available.
2. Use MariaDB/MySQL CLI with bounded `-e` commands.
3. Never use PostgreSQL tools for WordPress MariaDB administration.

## 5. Commandes de découverte

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
systemctl status mariadb --no-pager || systemctl status mysql --no-pager || true
mysql --version || mariadb --version
```

```bash
mysql -e "SELECT CURRENT_USER();" 2>/dev/null || sudo mysql -e "SELECT CURRENT_USER();" 2>/dev/null || mariadb -e "SELECT CURRENT_USER();" 2>/dev/null || sudo mariadb -e "SELECT CURRENT_USER();"
mysql -NBe "SELECT COUNT(*) FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='<wp_db>';"
```

## 6. Créer base/utilisateur/droits

Use explicit checks before creation. Do not use PostgreSQL syntax.

```bash
mysql -e "CREATE DATABASE \`<wp_db>\` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -e "CREATE USER '<wp_user>'@'localhost' IDENTIFIED BY '<strong-password>';"
mysql -e "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON \`<wp_db>\`.* TO '<wp_user>'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"
```

For connectivity verification, prefer a temporary client defaults file created through `write_file` and removed immediately. Do not print its content.

```text
write_file(path="<tmp-client-cnf>", mode="0600", content="[client]\nuser=<wp_user>\npassword=<strong-password>\nhost=localhost\ndatabase=<wp_db>\n")
```

```bash
mysql --defaults-extra-file=<tmp-client-cnf> -e "SELECT DATABASE(), CURRENT_USER();"
rm -f <tmp-client-cnf>
```

## 7. Modèles bloqués

Do not use `psql`, `sudo -u postgres psql`, broad global grants, or destructive database commands for a WordPress MariaDB task.

## 8. Vérifier avant de terminer

Finish only after checking database existence, user grants, and a successful connection as the WordPress user.

```bash
mysql -NBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='<wp_db>';"
mysql -e "SHOW GRANTS FOR '<wp_user>'@'localhost';"
```

## 9. Format de sortie requis

```markdown
## MariaDB WordPress admin report

### Summary

### Database/user

### Commands/tools used

### Grants

### Verification

### Blocked PostgreSQL drift

### Risk classification
```
