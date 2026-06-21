# Mariadb Wordpress Admin — corps français

> Version française step-for-step du contrat opérationnel. Les commandes, chemins, noms d'outils, tags de risque et clés de sortie restent identiques à `SKILL.md`.

## 1. Quand utiliser

Utiliser ce skill pour les tâches décrites par `SKILL.md` lorsque la demande opérateur est en français ou mixte EN/FR. Le comportement attendu est identique au corps anglais.

Résumé FR: Administrer MariaDB pour WordPress avec CLI mysql/mariadb, authentification socket, base/utilisateur/droits et sans dérive PostgreSQL.

## 2. Quand ne pas utiliser

Ne pas utiliser pour des demandes génériques qui ne contiennent pas l'intention étroite du skill. Les mots génériques français comme `service`, `système`, `fichier`, `configuration`, `http` ou `url` ne doivent jamais suffire seuls à sélectionner ce skill.

## 3. Mode opératoire

Respecter le même `default_mode`, le même périmètre d'autonomie VM-local et les mêmes conditions d'arrêt que dans `SKILL.md`. Ne pas traduire ni modifier les commandes exécutables.

## 4. Cartographie du risque

### low
- inspection en lecture seule;
- découverte ou validation sans changement d'état;
- rapporter les résultats avec secrets masqués.

### medium
- changement VM-local réversible et validé;
- écriture de configuration dans un périmètre autorisé;
- démarrage/rechargement local seulement si la politique runtime l'autorise.

### high
- modification de production ou d'environnement inconnu;
- action touchant secrets, droits, base de données ou service exposé;
- changement sans rollback clair.

### critical
- suppression irréversible;
- désactivation de contrôles sécurité/audit;
- action destructive ou globale hors périmètre.

## 5. Ordre de préférence des outils

1. Préférer les outils MCP/host-governed déclarés dans le frontmatter quand ils existent.
2. Utiliser le shell seulement pour l'inspection/exécution VM-local autorisée.
3. Ne jamais utiliser le shell pour contourner la politique runtime, les contrôles secrets ou les limites d'approbation.

## 6. Modèles de commandes

Les blocs de commandes ci-dessous sont repris sans traduction depuis `SKILL.md` afin de garder le contrat strictement identique.

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
systemctl status mariadb --no-pager || systemctl status mysql --no-pager
command -v mariadb || command -v mysql
mariadb --version 2>/dev/null || mysql --version 2>/dev/null
```

```bash
sudo mysql -e "SELECT USER(), CURRENT_USER(), VERSION();" 2>/dev/null || sudo mariadb -e "SELECT USER(), CURRENT_USER(), VERSION();"
sudo mysql -e "SHOW DATABASES;" 2>/dev/null || sudo mariadb -e "SHOW DATABASES;"
sudo mysql -e "SELECT User, Host, plugin FROM mysql.user;" 2>/dev/null || sudo mariadb -e "SELECT User, Host, plugin FROM mysql.user;"
```

```bash
sudo mysql -e "CREATE DATABASE IF NOT EXISTS \`<wp_db>\` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
sudo mysql -e "CREATE USER IF NOT EXISTS '<wp_user>'@'localhost' IDENTIFIED BY '<strong-password>';"
sudo mysql -e "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES ON \`<wp_db>\`.* TO '<wp_user>'@'localhost';"
sudo mysql -e "FLUSH PRIVILEGES;"
```

```bash
tmp_cnf=$(mktemp)
chmod 0600 "$tmp_cnf"
cat > "$tmp_cnf" <<'EOF'
[client]
user=<wp_user>
password=<strong-password>
host=localhost
database=<wp_db>
EOF
mysql --defaults-extra-file="$tmp_cnf" -e "SELECT DATABASE(), CURRENT_USER(); SHOW TABLES;"
rm -f "$tmp_cnf"
```

```bash
grep -nE "DB_NAME|DB_USER|DB_PASSWORD|DB_HOST" <wordpress-root>/wp-config.php | sed -E "s/(DB_PASSWORD'.*, *')[^']+/'DB_PASSWORD', '***REDACTED***/"
```

```bash
psql -c "..."
sudo -u postgres psql
DROP DATABASE <wp_db>;
GRANT ALL PRIVILEGES ON *.* TO '<wp_user>'@'localhost';
UPDATE mysql.user SET authentication_string=...
```

```bash
sudo mysql -e "SELECT CURRENT_USER();" || sudo mariadb -e "SELECT CURRENT_USER();"
```

```bash
systemctl status mariadb --no-pager || systemctl status mysql --no-pager
journalctl -u mariadb -n 80 --no-pager || journalctl -u mysql -n 80 --no-pager
```

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
```

```bash
sudo mysql -e "SELECT VERSION();"
```

```bash
sudo mysql -e "SHOW GRANTS FOR '<wp_user>'@'localhost';"
```

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

```bash
mysql -e "SELECT CURRENT_USER(), VERSION();" 2>/dev/null || \
sudo mysql -e "SELECT CURRENT_USER(), VERSION();" 2>/dev/null || \
mariadb -e "SELECT CURRENT_USER(), VERSION();" 2>/dev/null || \
sudo mariadb -e "SELECT CURRENT_USER(), VERSION();"
```

## 7. Récupération d'échec

Suivre les mêmes chemins de récupération que dans `SKILL.md`: symptôme → inspection → classification → action sûre → condition d'arrêt → sortie. Si l'environnement est inconnu ou production, ne pas exécuter d'action write/restart destructive automatiquement.

## 8. Conditions d'arrêt / blocage

S'arrêter si la demande sort de l'enveloppe d'autonomie VM-local, si un secret serait exposé, si l'action est destructive, ou si le skill étroit n'est pas réellement pertinent pour la tâche.

## 9. Format de sortie requis

Utiliser le même `output_template` que `SKILL.md`. Les titres peuvent être en français, mais les clés parsables comme `estimated_risk`, `actions_taken`, `blocked_actions`, `commands_used` doivent rester stables si elles sont consommées par downstream tooling.

## 10. Exigences d'évaluation

Les evals doivent exister en paire EN/FR et vérifier `selected_relevant_skill`, les commandes attendues, les commandes interdites, le niveau de risque et l'absence de sélection par mots génériques.
