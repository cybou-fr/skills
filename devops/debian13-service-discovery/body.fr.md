# Découverte des services Debian 13


> Corps FR structurellement équivalent à SKILL.md. Les commandes, chemins, noms d’outils et labels de risque restent inchangés.

## 1. Quand utiliser

Use this skill when a Debian 13 task needs to discover which systemd unit, socket, timer, or service name is provided by an installed package. This is especially important for versioned services such as PHP-FPM, MariaDB/MySQL, Redis, PostgreSQL, nginx, and other packages that already ship units.

## 2. Mode opératoire

Default mode: read-only discovery. Do not author a manual unit until package-provided service discovery is complete.

## 3. Cartographie du risque

### low
- list package-provided units;
- inspect installed packages;
- inspect unit files and package file lists.

### medium
- enable or start a known package-provided service in a VM-local environment after discovery.

### high
- enabling services in production or unknown environments.

### critical
- replacing a package-provided unit with a manual unit.

## 4. Ordre préféré des outils

1. Use MCP file/package inventory tools if available.
2. Use read-only shell discovery commands.
3. If a file must be authored later, hand off to `safe-file-authoring` and use `mcp:filesystem:write_file` or `write_file`.

## 5. Commandes de lecture seule

```bash
systemctl list-unit-files --type=service --type=socket --type=timer --no-pager
systemctl list-units --type=service --type=socket --type=timer --all --no-pager
dpkg -l | awk '/^ii/ {print $2}' | sort
```

```bash
dpkg-query -L <package> | grep -E '\.(service|socket|timer)$'
systemctl cat <unit> --no-pager
systemctl status <unit> --no-pager
```

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
dpkg -l | awk '/^ii[[:space:]]+php[0-9.]+-fpm|^ii[[:space:]]+php-fpm/ {print $2}' | xargs -r dpkg-query -L | grep -E '\.(service|socket)$'
find /run /var/run -type s -name 'php*-fpm*.sock' 2>/dev/null
```

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' '*postgresql*' '*redis*' '*nginx*' --no-pager
dpkg -l | awk '/^ii[[:space:]]+(mariadb|mysql|postgresql|redis|nginx)/ {print $2}'
```

## 6. Conditions d’arrêt / blocage

Stop if the next step is to create a unit for a package that already ships a unit. First report the discovered package-provided unit and propose using that unit.

## 7. Vérifier avant de terminer

If a package service is enabled or started by a later guarded step, finish only after a concrete check:

```bash
systemctl is-enabled <unit> --no-pager
systemctl is-active <unit> --no-pager
systemctl status <unit> --no-pager
```

## 8. Format de sortie requis

```markdown
## Debian service discovery report

### Summary

### Environment

### Commands/tools used

### Package-provided units found

### Selected unit

### Blocked manual authoring

### Risk classification

### Next step
```
