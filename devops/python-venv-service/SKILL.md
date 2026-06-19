---
name: python-venv-service
version: "9.0"
skill_format: operational_contract_v1
category: devops/python
default_mode: guarded
default_risk: medium
selection_profile: narrow
summary: Build Debian-safe Python venv services using PEP 668, FastAPI/Uvicorn systemd patterns, and venv/bin/python.
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - mcp:filesystem:write_file
  fallback:
    - shell
    - python3
    - systemctl
policy_refs:
  - policy_rules/shell.yaml
  - policy_rules/package_managers.yaml
triggers:
  include:
    - Debian PEP 668 Python service
    - FastAPI uvicorn systemd venv
    - externally-managed-environment pip
    - venv/bin/python systemd ExecStart
    - python3 -m venv service
    - uvicorn.service with virtualenv
  exclude:
    - generic Python script question
    - generic service question
    - unrelated package manager safety
negative_triggers:
  - python
  - service
  - system
  - api
  - http
activation_examples:
  - "Deploy a FastAPI app on Debian 13 using venv and systemd without system pip."
  - "PEP 668 blocks pip install; create venv and use venv/bin/python."
output_template: python_venv_service_report
---

# Python Venv Service

## 1. Use when

Use for Debian-based Python service deployment where PEP 668 may block system `pip`, especially FastAPI/Uvicorn apps managed by systemd.

This skill is for VM-local service authoring, venv creation, dependency installation into the venv, unit authoring, and verification.

## 2. Do not use when

Do not use for generic Python coding, library explanation, non-service scripts, Kubernetes deployments, or package review without systemd/venv concerns.

Do not trigger from `python`, `service`, `api`, or `http` alone.

## 3. Operating mode

Default is guarded VM-local authoring. It may write files inside an explicitly provided app directory and create `/etc/systemd/system/<name>.service` only when runtime policy allows VM-local service setup.

Do not install into system Python. Do not use `sudo pip install`. Do not pass `--break-system-packages` unless a human explicitly chooses that outside the autonomous path.

## 4. Risk mapping

### low
- inspect OS, Python, pip, venv state;
- read app files and requirements;
- validate unit file syntax with `systemd-analyze verify`.

### medium
- create venv in app directory;
- install dependencies into venv;
- author VM-local systemd unit;
- start/restart VM-local app service once and verify.

### high
- modify production service;
- install OS packages;
- bind to privileged ports;
- write service running as root without need;
- use network-exposed host without firewall context.

### critical
- use `pip install --break-system-packages` automatically;
- overwrite unrelated system units;
- run untrusted application code as root;
- expose secrets in unit environment.

## 5. Preferred tool order

1. Use MCP file read/write tools for project files and unit file authoring if available.
2. Use shell fallback for VM-local commands.
3. Use `python3 -m venv` and `<venv>/bin/python -m pip`, never system pip.
4. Validate before starting/reloading.

## 6. Command templates

### read_only: environment and PEP 668 detection

```bash
cat /etc/os-release
python3 --version
python3 -m pip --version 2>&1 || true
python3 - <<'PY'
import sysconfig, pathlib
p = pathlib.Path(sysconfig.get_paths().get('stdlib','')) / 'EXTERNALLY-MANAGED'
print(p)
print('externally_managed=', p.exists())
PY
```

### read_only: inspect application

```bash
pwd
find . -maxdepth 2 -type f \( -name 'requirements*.txt' -o -name 'pyproject.toml' -o -name 'main.py' -o -name 'app.py' \) -print
sed -n '1,220p' requirements.txt 2>/dev/null || true
sed -n '1,220p' pyproject.toml 2>/dev/null || true
```

### guarded: create venv and install dependencies into venv

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip wheel
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip show fastapi uvicorn 2>/dev/null || true
```

### guarded: minimal FastAPI/Uvicorn systemd unit pattern

```ini
[Unit]
Description=<app-name> FastAPI service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=<service-user>
Group=<service-group>
WorkingDirectory=<app-dir>
Environment="PATH=<app-dir>/.venv/bin"
ExecStart=<app-dir>/.venv/bin/python -m uvicorn <module>:<app> --host 127.0.0.1 --port <port>
Restart=on-failure
RestartSec=5
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=full
ProtectHome=true

[Install]
WantedBy=multi-user.target
```

### guarded: write unit safely with shell fallback

```bash
install -d -m 0755 /etc/systemd/system
tee /etc/systemd/system/<app-name>.service >/dev/null <<'EOF'
<unit-content>
EOF
systemd-analyze verify /etc/systemd/system/<app-name>.service
systemctl daemon-reload
systemctl enable <app-name>.service
systemctl start <app-name>.service
systemctl status <app-name>.service --no-pager
journalctl -u <app-name>.service -n 80 --no-pager
```

### read_only: local HTTP health check

```bash
ss -tulpn | grep -E ':(<port>)\b' || true
curl -fsS http://127.0.0.1:<port>/health || curl -fsS http://127.0.0.1:<port>/ || true
```

### blocked

```bash
pip install <package>
sudo pip install <package>
python3 -m pip install --break-system-packages <package>
ExecStart=/usr/bin/python3 -m uvicorn <module>:<app>
ExecStart=uvicorn <module>:<app>
```

## 7. Failure recovery

### If pip fails with externally-managed-environment

1. Do not retry with `--break-system-packages`.
2. Create a venv:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip wheel
```

3. Install into the venv only.
4. Use `.venv/bin/python` in `ExecStart`.

### If `python3 -m venv` is unavailable

1. Inspect package availability:

```bash
python3 -m venv --help 2>&1 || true
apt-cache policy python3-venv
```

2. OS package installation is high/medium depending on environment and runtime policy. Do not auto-install in unknown/production environment.

### If systemd service fails to start

1. Inspect:

```bash
systemctl status <app-name>.service --no-pager
journalctl -u <app-name>.service -n 120 --no-pager
systemctl cat <app-name>.service --no-pager
```

2. Check common errors: wrong WorkingDirectory, wrong module path, missing venv dependency, port in use.
3. For port conflict:

```bash
ss -tulpn | grep -E ':(<port>)\b'
```

4. Patch only VM-local unit/app path issues, verify, then restart once.

## 8. Stop / block conditions

Stop if:

- only system pip is available and venv cannot be created;
- the app source is untrusted and would execute during inspection;
- service would run as root unnecessarily;
- credentials are requested in unit file;
- environment is production/unknown and write/restart is needed.

## 9. Output contract

```markdown
## Python venv service report

### Summary

### Environment
- OS:
- Python:
- PEP 668 externally managed:

### Application
- Directory:
- Module/app:
- Port:
- Service user:

### Venv/dependencies
- Venv path:
- Dependency source:
- Commands/tools used:

### Systemd unit
- Unit path:
- ExecStart:
- Verification result:

### Risk classification
- estimated_risk:
- risk drivers:

### Actions taken

### Blocked actions

### Recommendation
```

## 10. Eval requirements

Create evals for:

- PEP 668 error leads to venv path, not `--break-system-packages`;
- FastAPI service uses `.venv/bin/python -m uvicorn`;
- service failure checks journal and port conflict;
- app binds to loopback behind nginx by default;
- production/unknown restart is blocked.
