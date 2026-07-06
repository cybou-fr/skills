---
name: nginx-php-fpm-wordpress
description: Configure WordPress behind nginx with discovered PHP-FPM sockets and XML-RPC denial.
description_fr: Configurer WordPress derrière nginx avec découverte des sockets PHP-FPM et blocage XML-RPC.
summary: "Configure WordPress behind nginx with discovered PHP-FPM sockets and XML-RPC denial. / Configurer WordPress derrière nginx avec découverte des sockets PHP-FPM et blocage XML-RPC."
summary_fr: Configurer WordPress derrière nginx avec découverte des sockets PHP-FPM et blocage XML-RPC.
category: devops
default_risk: medium
default_mode: guarded
skill_format: operational_contract_v1
version: "10.1"
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - mcp:filesystem:write_file
  fallback:
    - shell
triggers:
  - nginx php fpm wordpress
  - wordpress nginx config
  - php fpm socket discovery
  - block wordpress xmlrpc
  - nginx test before reload
  - xmlrpc php deny
  - nginx php fpm wordpress
  - configuration nginx wordpress
  - découverte socket php fpm
  - bloquer xmlrpc wordpress
  - nginx test avant rechargement
  - refuser xmlrpc php
---

# Nginx PHP-FPM WordPress

## 1. Use when

Use this skill when configuring WordPress with nginx and PHP-FPM on Debian. The agent must discover the real PHP-FPM unit/socket before writing nginx config.

## 2. Operating mode

Default mode: guarded. Discovery is low risk. Writing nginx config and reload is medium in a VM and high in production.

## 3. Risk mapping

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

## 4. Preferred tool order

1. Use `debian13-service-discovery` for PHP-FPM unit discovery.
2. Use `mcp:filesystem:read_file` for existing nginx and pool configs.
3. Use `mcp:filesystem:write_file` or `write_file` for config authoring.
4. Use shell for `nginx -t` and reload verification.

## 5. Discovery commands

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

## 6. Config authoring pattern

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

## 7. Reload & PHP-FPM Configuration Sequence

```bash
# Discovery and update php.ini FPM upload limits
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

## 8. Verify-before-finish

A mutating task is not complete until the PHP-FPM socket was discovered, config was authored through `write_file`, `nginx -t` passed, nginx was reloaded, and local HTTP/XML-RPC verification commands ran.

## 9. Stop / block conditions

Do not reload nginx unless `nginx -t` succeeds. Do not use an assumed PHP-FPM socket. A socket is valid only after discovery via `find`, pool config, or systemd status.

## 10. Required output format

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
