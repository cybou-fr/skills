# Nginx Php Fpm Wordpress — corps français

> Version française step-for-step du contrat opérationnel. Les commandes, chemins, noms d'outils, tags de risque et clés de sortie restent identiques à `SKILL.md`.

## 1. Quand utiliser

Utiliser ce skill pour les tâches décrites par `SKILL.md` lorsque la demande opérateur est en français ou mixte EN/FR. Le comportement attendu est identique au corps anglais.

Résumé FR: Configurer nginx + PHP-FPM pour WordPress avec découverte socket/unité, blocage XML-RPC et nginx -t avant rechargement.

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
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl list-units '*php*fpm*' --all --no-pager
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null
find /etc/php -maxdepth 4 -type f -path '*/fpm/pool.d/*.conf' -print 2>/dev/null
php -v 2>/dev/null || true
```

```bash
nginx -T 2>/dev/null | sed -n '1,260p'
nginx -t
systemctl status nginx --no-pager
journalctl -u nginx -n 80 --no-pager
```

```nginx
server {
    listen 80;
    server_name <domain>;
    root <wordpress-root>;
    index index.php index.html;

    access_log /var/log/nginx/<site>.access.log;
    error_log /var/log/nginx/<site>.error.log;

    client_max_body_size 64m;

    location = /favicon.ico { log_not_found off; access_log off; }
    location = /robots.txt { allow all; log_not_found off; access_log off; }

    location = /xmlrpc.php {
        deny all;
        access_log off;
        log_not_found off;
    }

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:<php-fpm-socket>;
    }

    location ~* /(?:uploads|files)/.*\.php$ {
        deny all;
    }

    location ~ /\.ht {
        deny all;
    }
}
```

```bash
install -d -m 0755 /etc/nginx/sites-available /etc/nginx/sites-enabled
tee /etc/nginx/sites-available/<site>.conf >/dev/null <<'EOF'
<server-block>
EOF
ln -sfn /etc/nginx/sites-available/<site>.conf /etc/nginx/sites-enabled/<site>.conf
nginx -t
systemctl reload nginx
systemctl status nginx --no-pager
```

```bash
test -f <wordpress-root>/wp-config.php && echo wp-config-present
test -f <wordpress-root>/index.php && echo index-present
find <wordpress-root> -maxdepth 2 -type f -name 'xmlrpc.php' -print
namei -l <wordpress-root>
```

```bash
systemctl reload nginx   # blocked unless nginx -t succeeded in current run
fastcgi_pass 127.0.0.1:9000;  # blocked unless PHP-FPM is confirmed listening there
location ~ \.php$ { fastcgi_pass unix:/run/php/php-fpm.sock; }  # blocked if socket guessed
```

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null
```

```bash
nginx -t
nl -ba /etc/nginx/sites-available/<site>.conf | sed -n '<start>,<end>p'
```

```bash
systemctl status <php-fpm-unit> --no-pager
journalctl -u <php-fpm-unit> -n 80 --no-pager
```

```markdown
## Nginx PHP-FPM WordPress report

### Summary

### Environment
- nginx version:
- PHP-FPM unit:
- PHP-FPM socket:

### WordPress site
- Site name/domain:
- Root:
- XML-RPC policy:

### Config changes
- File:
- Enabled symlink:
- nginx -t result:

### Commands/tools used

### Risk classification
- estimated_risk:
- risk drivers:

### Actions taken

### Blocked actions

### Recommendation
```

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl list-units '*php*fpm*' --all --no-pager
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null | sort
find /etc/php -maxdepth 4 -type f \( -name 'www.conf' -o -name '*.conf' \) -print 2>/dev/null | sort
```

```bash
nginx -T 2>/dev/null | sed -n '1,260p'
```

## 7. Récupération d'échec

Suivre les mêmes chemins de récupération que dans `SKILL.md`: symptôme → inspection → classification → action sûre → condition d'arrêt → sortie. Si l'environnement est inconnu ou production, ne pas exécuter d'action write/restart destructive automatiquement.

## 8. Conditions d'arrêt / blocage

S'arrêter si la demande sort de l'enveloppe d'autonomie VM-local, si un secret serait exposé, si l'action est destructive, ou si le skill étroit n'est pas réellement pertinent pour la tâche.

## 9. Format de sortie requis

Utiliser le même `output_template` que `SKILL.md`. Les titres peuvent être en français, mais les clés parsables comme `estimated_risk`, `actions_taken`, `blocked_actions`, `commands_used` doivent rester stables si elles sont consommées par downstream tooling.

## 10. Exigences d'évaluation

Les evals doivent exister en paire EN/FR et vérifier `selected_relevant_skill`, les commandes attendues, les commandes interdites, le niveau de risque et l'absence de sélection par mots génériques.
