---
name: debian13-service-discovery
version: "9.0"
skill_format: operational_contract_v1
category: devops/debian
selection_profile: narrow
summary: Discover Debian 13 package-provided services and unit names before changing or creating systemd units.
default_mode: read_only
default_risk: low
requires_tools:
  preferred:
    - mcp:filesystem:read_file
  fallback:
    - shell
    - apt
    - dpkg
    - systemctl
policy_refs:
  - policy_rules/shell.yaml
  - policy_rules/package_managers.yaml
triggers:
  include:
    - debian 13 service discovery
    - package provided systemd unit
    - systemctl list-unit-files
    - php-fpm unit name
    - mariadb service unit name
    - nginx package service
    - service unit not found after apt install
  exclude:
    - generic system question
    - url fetch
    - http request only
    - unrelated package install
negative_triggers:
  - system
  - service
  - unit
  - http
  - url
  - and
activation_examples:
  - "After installing php-fpm on Debian 13, find the real service name before enabling it."
  - "Do not create a custom unit until dpkg/systemctl prove the package did not ship one."
output_template: debian13_service_discovery_report
---

# Debian 13 Service Discovery

## 1. Use when

Use this skill when the task needs to map a Debian package to the systemd unit or socket it provides, especially on Debian 13 or Debian-like systems where package names and service names are versioned.

Use it before enabling, starting, editing, replacing, or manually creating a unit for packaged software such as `nginx`, `mariadb`, `php-fpm`, `redis`, `postgresql`, `fail2ban`, `cron`, or language runtime services installed through `apt`.

## 2. Do not use when

Do not use for generic Linux troubleshooting, generic package installation, arbitrary HTTP/URL tasks, or custom application units that are clearly not package-provided.

Do not trigger from generic words like `system`, `service`, `unit`, `url`, `http`, or `and` alone.

## 3. Operating mode

Default mode is read-only discovery. Do not create a manual unit until package ownership and systemd unit inventory have been checked.

For autonomous VM-local work, service discovery is low risk. Starting/restarting a discovered service is medium only if the environment is VM-local/non-production and runtime policy permits it. Unknown or production service changes are high risk.

## 4. Risk mapping

### low
- list unit files;
- inspect package files;
- map package name to unit name;
- inspect package metadata;
- inspect service status without changing state.

### medium
- enable/start/restart a VM-local package service after discovery and config validation;
- reload daemon after adding a VM-local custom unit only when package did not ship one.

### high
- enable/restart service in unknown or production environment;
- edit package-provided unit directly;
- replace package-provided service with custom unit;
- remove package files or purge packages.

### critical
- disable audit/security services without explicit policy;
- delete system unit directories;
- mask core services in production;
- overwrite packaged units in `/lib/systemd/system` or `/usr/lib/systemd/system`.

## 5. Preferred tool order

1. Prefer MCP file tools for reading known files if the runtime exposes them.
2. Use shell discovery commands for VM-local Debian inspection.
3. Use `apt`, `dpkg`, and `systemctl` read-only commands before any write action.
4. Never create a manual unit merely because `systemctl status <guessed-name>` failed.

## 6. Command templates

### read_only: baseline OS and systemd

```bash
cat /etc/os-release
systemctl --version
systemctl list-unit-files --type=service --type=socket --no-pager
systemctl list-units --type=service --type=socket --all --no-pager
```

### read_only: package to unit mapping

```bash
apt-cache policy <package>
dpkg -L <package> | grep -E '/(systemd|init\.d)/|\.service$|\.socket$|\.timer$'
dpkg-query -L <package> | grep -E '\.(service|socket|timer)$'
dpkg-query -S '/lib/systemd/system/*' '/usr/lib/systemd/system/*' 2>/dev/null | grep '<package>'
```

### read_only: discover versioned PHP-FPM units

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl list-units '*php*fpm*' --all --no-pager
dpkg -l | grep -E '^ii\s+php[0-9.]+-fpm\b|^ii\s+php-fpm\b'
dpkg-query -L 'php*-fpm' 2>/dev/null | grep -E '\.(service|socket)$'
```

### read_only: discover MariaDB/MySQL units

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
systemctl list-units '*mariadb*' '*mysql*' --all --no-pager
dpkg -l | grep -E '^ii\s+(mariadb|mysql)'
dpkg-query -L mariadb-server 2>/dev/null | grep -E '\.(service|socket)$'
```

### read_only: inspect discovered unit

```bash
systemctl status <unit> --no-pager
systemctl cat <unit> --no-pager
systemctl show <unit> -p FragmentPath -p UnitFileState -p ActiveState -p SubState -p ExecMainStatus --no-pager
```

### guarded: VM-local service operation after discovery

```bash
systemctl start <discovered-unit>
systemctl reload <discovered-unit>
systemctl restart <discovered-unit>
```

Only use guarded commands when the environment is VM-local/non-production, the unit has been discovered from package inventory, and runtime policy permits service changes.

### blocked: package-provided unit replacement

```bash
cat > /etc/systemd/system/<package>.service
rm -f /lib/systemd/system/<unit>
systemctl mask <unit>
systemctl disable <unit>
```

Do not do these automatically when the package already provides a unit.

## 7. Failure recovery

### If `systemctl status <service>` says `Unit not found`

1. Do not create a manual unit.
2. Run:

```bash
systemctl list-unit-files '*<service>*' --no-pager
systemctl list-units '*<service>*' --all --no-pager
dpkg -l | grep -i '<service>'
dpkg-query -L <package> 2>/dev/null | grep -E '\.(service|socket|timer)$'
```

3. If the package exists and provides a differently named/versioned unit, use the discovered unit name.
4. If no package-owned unit exists, report that a custom unit may be needed and classify authoring as medium/high depending on environment.

### If `dpkg-query -L <package>` says package not installed

1. Verify package name:

```bash
apt-cache search '^<package>$'
apt-cache policy <package>
```

2. Do not install automatically unless package installation is within the autonomy envelope.
3. Return a package-not-installed finding.

### If service is installed but inactive

1. Inspect status and logs:

```bash
systemctl status <unit> --no-pager
journalctl -u <unit> -n 80 --no-pager
```

2. If the environment is unknown/production, do not start automatically.
3. If VM-local and policy permits, start once, verify status, then stop further changes.

## 8. Stop / block conditions

Stop before writes if:

- package ownership is unknown;
- discovered unit is production/unknown environment;
- manual unit would duplicate a package-provided unit;
- action would edit `/lib/systemd/system` or `/usr/lib/systemd/system`;
- action would mask/disable/delete packaged services.

## 9. Output contract

```markdown
## Debian 13 service discovery report

### Summary

### Environment
- OS:
- systemd version:

### Package inspected
- Package:
- Installed:
- Version:

### Unit discovery
- Discovered units:
- Unit source paths:
- Active state:

### Commands/tools used
- ...

### Risk classification
- estimated_risk:
- risk drivers:

### Actions taken
- ...

### Blocked actions
- ...

### Recommendation
- ...
```

## 10. Eval requirements

Create evals for:

- `php-fpm.service not found` resolves through `systemctl list-unit-files '*php*fpm*'`;
- MariaDB package maps to `mariadb.service`, not PostgreSQL tooling;
- package-provided nginx unit blocks custom unit creation;
- unknown production restart is high/blocked;
- VM-local service start after discovery is medium and verified.
