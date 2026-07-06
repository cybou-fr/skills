# Nginx PHP-FPM WordPress


> Corps FR structurellement équivalent à SKILL.md. Les commandes, chemins, noms d’outils et labels de risque restent inchangés.

## 1. Quand utiliser

Use this skill when configuring WordPress with nginx and PHP-FPM on Debian. The agent must discover the real PHP-FPM unit/socket before writing nginx config.

## 2. Mode opératoire

Default mode: guarded. Discovery is low risk. Writing nginx config and reload is medium in a VM and high in production.

## 3. Cartographie du risque

### low
- inspect nginx config and PHP-FPM units;
- discover sockets and pool config.

### medium
- author VM-local nginx server block through `write_file`;
- reload nginx after `nginx -t` passes.

### high
- change production TLS, vhost, or PHP handling.

### critical
- reload broken config;
- guess a PHP-FPM socket without discovery.

## 4. Ordre préféré des outils

1. Use `debian13-service-discovery` for PHP-FPM unit discovery.
2. Use `mcp:filesystem:read_file` for existing nginx and pool configs.
3. Use `mcp:filesystem:write_file` or `write_file` for config authoring.
4. Use shell for `nginx -t` and reload verification.

## 5. Commandes de découverte

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl status 'php*-fpm.service' --no-pager || true
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null
find /etc/php -path '*/fpm/pool.d/*.conf' -type f -print 2>/dev/null
```

```bash
nginx -t
nginx -T 2>/dev/null | sed -n '1,260p'
```

## 6. Modèle d’écriture de configuration

Preferred authoring uses a file tool:

```text
write_file(path="/etc/nginx/sites-available/<site>", mode="0644", content="<nginx server block content>")
```

Required nginx content properties:

```nginx
server {
    listen 80;
    server_name <domain>;
    root <wordpress-root>;
    index index.php index.html;

    client_max_body_size 64M;

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
        fastcgi_pass unix:<discovered-php-fpm-socket>;
    }
}
```

## 7. Séquence de rechargement & Configuration de PHP-FPM

```bash
# Découverte et mise à jour des limites d'upload de php.ini FPM
PHP_INI=$(find /etc/php/ -path '*/fpm/php.ini' | head -n 1)
if [ -n "$PHP_INI" ]; then
    sed -i 's/upload_max_filesize =.*/upload_max_filesize = 64M/' "$PHP_INI"
    sed -i 's/post_max_size =.*/post_max_size = 64M/' "$PHP_INI"
    systemctl restart php*-fpm
fi

ln -sfn /etc/nginx/sites-available/<site> /etc/nginx/sites-enabled/<site>
nginx -t
systemctl reload nginx
systemctl status nginx --no-pager
curl -I http://127.0.0.1/ || true
curl -I http://127.0.0.1/xmlrpc.php || true
```

## 8. Vérifier avant de terminer

Une tâche mutante n’est pas terminée tant que la socket PHP-FPM a été découverte, la configuration a été écrite via `write_file`, `nginx -t` a réussi, nginx a été rechargé et les vérifications HTTP/XML-RPC locales ont été exécutées.

## 9. Conditions d’arrêt / blocage

Do not reload nginx unless `nginx -t` succeeds. Do not use an assumed PHP-FPM socket. A socket is valid only after discovery via `find`, pool config, or systemd status.

## 10. Format de sortie requis

```markdown
## Nginx PHP-FPM WordPress report

### Summary

### Discovered PHP-FPM unit/socket

### Config path

### Commands/tools used

### Nginx test result

### XML-RPC control

### Verification

### Blocked actions

### Risk classification
```
