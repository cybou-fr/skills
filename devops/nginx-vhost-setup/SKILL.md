---
name: nginx-vhost-setup
description: Configure Nginx virtual hosts, symlinks, default server clashing, port mapping, and verification on Debian/Ubuntu guests.
description_fr: Configurer les hôtes virtuels Nginx, les liens symboliques, les conflits de serveur par défaut, le mappage de ports et la vérification sur Debian/Ubuntu.
category: devops
triggers: nginx, vhost, virtualhost, site, sites-enabled, sites-available, port, proxy
risk: medium
---

# Nginx Virtual Hosts Setup

## 1. Use when

Use this skill when configuring Nginx virtual hosts (server blocks), setting up proxies, managing multiple websites, mapping ports, or verifying web server configurations.

## 2. Default site conflict prevention

Before configuring a new `default_server` block or a custom site, check if the default Nginx configuration is enabled:
- Check `/etc/nginx/sites-enabled/default`
- If it exists and clashes with your new block, disable it by removing the symlink:
  ```bash
  rm -f /etc/nginx/sites-enabled/default
  ```

## 3. Directory structure & Symlinking

Always place virtual host configurations in `sites-available/` and create a symbolic link to `sites-enabled/`:
- Write the configuration file: `/etc/nginx/sites-available/<site_name>`
- Create the symlink:
  ```bash
  ln -sfn /etc/nginx/sites-available/<site_name> /etc/nginx/sites-enabled/<site_name>
  ```
- Do not edit `/etc/nginx/nginx.conf` directly unless explicitly required.

## 4. Multi-site Port Allocation

If multiple applications or sites are installed on the same VM, configure them with unique listening ports (e.g. 80, 8080, 8090) instead of binding them all to port 80 with `server_name _`:
- Ensure different sites use different ports in their `listen` directives:
  ```nginx
  server {
      listen 8080;
      server_name _;
      ...
  }
  ```

## 5. Verification before Reload

Never reload or restart Nginx without testing the configuration:
- Test configuration syntax:
  ```bash
  nginx -t
  ```
- If the test passes, reload the service:
  ```bash
  systemctl reload nginx
  ```
- Verify that the port is listening:
  ```bash
  ss -tlnp
  ```
