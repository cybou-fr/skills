---
name: nginx-php-fpm-wordpress
version: "9.1"
skill_format: operational_contract_v1
category: devops/web
default_mode: guarded
default_risk: medium
selection_profile: narrow
summary: Configure nginx + PHP-FPM for WordPress with socket/unit discovery, XML-RPC deny, and nginx -t before reload.
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - mcp:filesystem:write_file
  fallback:
    - shell
    - nginx
    - systemctl
policy_refs:
  - policy_rules/shell.yaml
triggers:
  include:
    - nginx php-fpm wordpress
    - WordPress nginx XML-RPC deny
    - PHP-FPM socket discovery
    - nginx fastcgi_pass unix socket
    - nginx -t before reload wordpress
    - php-fpm unit not found nginx
  exclude:
    - generic nginx question
    - generic http url
    - static website only
negative_triggers:
  - nginx
  - wordpress
  - php
  - http
  - url
activation_examples:
  - "Configure WordPress on Debian with nginx and discovered PHP-FPM socket."
  - "Deny xmlrpc.php and run nginx -t before reload."
output_template: nginx_php_fpm_wordpress_report
---

# Nginx PHP-FPM WordPress

## 1. Use when

Use for WordPress deployments on Debian-like systems using nginx and PHP-FPM. It handles PHP-FPM unit/socket discovery, nginx server block authoring, XML-RPC denial, and safe validation before reload.

## 2. Do not use when

Do not use for Apache, non-PHP apps, generic nginx troubleshooting, static-only sites, or generic URL/HTTP tasks.

Do not trigger from `nginx`, `php`, `wordpress`, `http`, or `url` alone without WordPress + PHP-FPM + nginx configuration intent.

## 3. Operating mode

Default is guarded VM-local config authoring. Always run `nginx -t` before any reload. Do not reload nginx if config test fails.

## 4. Risk mapping

### low
- inspect nginx config;
- discover PHP-FPM socket/unit;
- run `nginx -t`;
- inspect service status/logs.

### medium
- write VM-local nginx site config;
- enable site symlink;
- reload nginx after successful `nginx -t`;
- restart VM-local PHP-FPM after config validation.

### high
- production nginx reload;
- public DNS/TLS changes;
- modify global nginx config without backup;
- change PHP-FPM pool for production.

### critical
- disable security restrictions;
- expose `wp-config.php`;
- allow arbitrary PHP execution outside WordPress root;
- reload broken production nginx config.

## 5. Preferred tool order

1. Use MCP file tools for reading/writing config if available.
2. Use shell fallback for VM-local discovery and validation.
3. Discover PHP-FPM socket/unit before writing `fastcgi_pass`.
4. Run `nginx -t` before reload.

## 6. Command templates

### read_only: discover PHP-FPM version, unit, and socket

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl list-units '*php*fpm*' --all --no-pager
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null
find /etc/php -maxdepth 4 -type f -path '*/fpm/pool.d/*.conf' -print 2>/dev/null
php -v 2>/dev/null || true
```

### read_only: inspect nginx state

```bash
nginx -T 2>/dev/null | sed -n '1,260p'
nginx -t
systemctl status nginx --no-pager
journalctl -u nginx -n 80 --no-pager
```

### guarded: WordPress nginx server block template

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

### guarded: write and enable site safely

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

### read_only: validate WordPress root and security files

```bash
test -f <wordpress-root>/wp-config.php && echo wp-config-present
test -f <wordpress-root>/index.php && echo index-present
find <wordpress-root> -maxdepth 2 -type f -name 'xmlrpc.php' -print
namei -l <wordpress-root>
```

### blocked

```bash
systemctl reload nginx   # blocked unless nginx -t succeeded in current run
fastcgi_pass 127.0.0.1:9000;  # blocked unless PHP-FPM is confirmed listening there
location ~ \.php$ { fastcgi_pass unix:/run/php/php-fpm.sock; }  # blocked if socket guessed
```

## 7. Failure recovery

### If `php-fpm.service` is not found

1. Do not assume `php-fpm.service`.
2. Run:

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null
```

3. Use the discovered versioned unit/socket, such as `php8.4-fpm.service` and `/run/php/php8.4-fpm.sock`.

### If `nginx -t` fails

1. Do not reload nginx.
2. Inspect error output and config lines:

```bash
nginx -t
nl -ba /etc/nginx/sites-available/<site>.conf | sed -n '<start>,<end>p'
```

3. Patch config, retest, reload only after success.

### If PHP files download instead of executing

1. Verify PHP location block and `fastcgi_pass` socket.
2. Verify PHP-FPM status:

```bash
systemctl status <php-fpm-unit> --no-pager
journalctl -u <php-fpm-unit> -n 80 --no-pager
```

3. Do not reload until both PHP-FPM socket and nginx syntax are valid.

## 8. Stop / block conditions

Stop if:

- PHP-FPM socket cannot be discovered;
- `nginx -t` fails;
- WordPress root is missing `index.php` or path ownership is unclear;
- config would expose `wp-config.php` or PHP in uploads;
- environment is production/unknown and reload is required.

## 9. Output contract

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

## 10. Eval requirements

Create evals for:

- PHP-FPM unit discovery instead of assuming `php-fpm.service`;
- XML-RPC deny block present;
- `nginx -t` required before reload;
- failed config blocks reload;
- guessed socket is rejected.


## V9.1 Integration hardening

A guessed PHP-FPM socket such as `/run/php/php-fpm.sock` is invalid unless confirmed by discovery.

Use discovery first:

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl list-units '*php*fpm*' --all --no-pager
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null | sort
find /etc/php -maxdepth 4 -type f \( -name 'www.conf' -o -name '*.conf' \) -print 2>/dev/null | sort
```

When inspecting nginx config, limit and redact output:

```bash
nginx -T 2>/dev/null | sed -n '1,260p'
```

The ordering rule is mandatory: `nginx -t` must appear before `systemctl reload nginx`, and reload is blocked if config validation fails.
