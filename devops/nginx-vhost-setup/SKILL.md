---
name: nginx-vhost-setup
description: Configure Nginx virtual hosts, symlinks, default server clashing, port mapping, and verification on Debian/Ubuntu guests.
description_fr: Configurer les hôtes virtuels Nginx, les liens symboliques, les conflits de serveur par défaut, le mappage de ports et la vérification sur des hôtes Debian/Ubuntu.
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
  - nginx vhost setup
  - nginx virtualhost
  - nginx sites-enabled
  - nginx sites-available
  - nginx port mapping
  - nginx proxy pass
  - nginx server block
  - configuration hôte virtuel nginx
  - nginx multi-site
  - nginx port conflit
  - nginx default server conflit
---

# Nginx Virtual Hosts Setup

## 1. Use when

Use this skill when configuring Nginx virtual hosts (server blocks), setting up reverse proxies, managing multiple websites on the same host, mapping ports, disabling the default site, or verifying web server configuration.

## 2. Operating mode

Default mode: guarded. Inspecting configuration is low risk. Writing a new virtual host and reloading nginx in a VM is medium risk. Changes to production TLS or publicly reachable services are high risk.

## 3. Risk mapping

### low
- inspect current nginx configuration (`nginx -T`, `ls sites-enabled`);
- test configuration syntax without changing it (`nginx -t`).

### medium
- write a VM-local virtual host via `write_file` and reload nginx after `nginx -t` passes;
- disable the default site symlink.

### high
- configure TLS termination, change firewall/port rules, proxy to an external host.

### critical
- reload nginx with a broken config;
- delete or overwrite the main `nginx.conf` without backup.

## 4. Preferred tool order

1. Use `mcp:filesystem:read_file` to inspect existing configs and `sites-enabled` contents.
2. Use `mcp:filesystem:write_file` or `write_file` for config authoring.
3. Use shell for `nginx -t`, `systemctl reload nginx`, and `ss -tlnp` verification.

## 5. Default site conflict prevention

Before configuring a new `default_server` block or a custom site that listens on port 80, check for the conflicting default:

```bash
ls -la /etc/nginx/sites-enabled/
nginx -T 2>/dev/null | grep -E 'server_name|listen|default_server'
```

If the default site is enabled and clashes with the new block, disable it:

```bash
rm -f /etc/nginx/sites-enabled/default
nginx -t
```

## 6. Directory structure & symlinking

Always place virtual host configurations in `sites-available/` then symlink to `sites-enabled/`:

```text
write_file(path="/etc/nginx/sites-available/<site_name>", mode="0644", content="<server block>")
```

```bash
ln -sfn /etc/nginx/sites-available/<site_name> /etc/nginx/sites-enabled/<site_name>
```

Do **not** edit `/etc/nginx/nginx.conf` directly unless explicitly required by the task.

## 7. Multi-site port allocation

If multiple applications are installed on the same VM, assign each a unique listening port to prevent `server_name _` collisions:

```nginx
server {
    listen 80;
    server_name _;
    # site 1
}

server {
    listen 8080;
    server_name _;
    # site 2
}

server {
    listen 8090;
    server_name _;
    # site 3
}
```

Rule: never bind two different sites with `server_name _;` to the same port.

## 8. Reverse proxy block template

```nginx
server {
    listen <port>;
    server_name <domain_or_underscore>;

    location / {
        proxy_pass http://127.0.0.1:<backend_port>;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
    }
}
```

## 9. Reload sequence

```bash
nginx -t
systemctl reload nginx
systemctl status nginx --no-pager
ss -tlnp | grep nginx
curl -I http://127.0.0.1:<port> || true
```

## 10. Verify-before-finish

A virtual host task is not complete until:
- the config file exists in `sites-available/`;
- the symlink exists in `sites-enabled/`;
- `nginx -t` passed;
- nginx was reloaded;
- the port is confirmed listening with `ss -tlnp`.

## 11. Stop / block conditions

- Do not reload nginx unless `nginx -t` succeeds.
- Do not create a `server_name _;` block on a port already used by another enabled site.
- Do not edit `nginx.conf` directly unless the task explicitly requires it.

## 12. Required output format

```markdown
## Nginx virtual host report

### Summary

### Site name

### Config path

### Port

### Symlink

### Default site conflict resolved

### Nginx test result

### Port listening (ss -tlnp)

### Verification curl

### Blocked actions

### Risk classification
```
