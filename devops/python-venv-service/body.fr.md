# Service Python avec venv


> Corps FR structurellement équivalent à SKILL.md. Les commandes, chemins, noms d’outils et labels de risque restent inchangés.

## 1. Quand utiliser

Use this skill for Debian Python applications, especially FastAPI/uvicorn services, where system Python is externally managed by PEP 668 and dependencies must be installed into a virtual environment.

## 2. Mode opératoire

Default mode: guarded. Creating a VM-local venv and service plan is medium risk. Production service changes are high risk.

## 3. Cartographie du risque

### low
- inspect Python version and existing venv;
- inspect requirements and service files.

### medium
- create a VM-local virtual environment;
- install dependencies from trusted requirements in the venv;
- author a service file through `write_file` in an isolated VM.

### high
- modify production service units;
- install untrusted dependencies;
- expose a network service externally.

### critical
- use `--break-system-packages`;
- overwrite system Python packages.

## 4. Ordre préféré des outils

1. Use `mcp:filesystem:read_file` for requirements and existing units.
2. Use `mcp:filesystem:write_file` or `write_file` for any service file content.
3. Use shell for venv creation and service verification.
4. If dependencies are untrusted or newly changed, load `package-manager-safety` before install.

## 5. Modèles de commandes

```bash
python3 --version
python3 -m venv --help | head -20
cd <app-dir>
python3 -m venv .venv
.venv/bin/python -m pip --version
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

```bash
cd <app-dir>
.venv/bin/python -m uvicorn <module>:<app> --host 127.0.0.1 --port <port>
```

Preferred service authoring uses a file tool, not shell file redirection:

```text
write_file(path="/etc/systemd/system/<service>.service", mode="0644", content="<systemd unit content>")
```

Systemd unit pattern:

```ini
[Unit]
Description=<service description>
After=network.target

[Service]
User=<service-user>
Group=<service-group>
WorkingDirectory=<app-dir>
Environment="PATH=<app-dir>/.venv/bin"
ExecStart=<app-dir>/.venv/bin/python -m uvicorn <module>:<app> --host 127.0.0.1 --port <port>
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
systemd-analyze verify /etc/systemd/system/<service>.service
systemctl daemon-reload
systemctl enable --now <service>.service
systemctl status <service>.service --no-pager
curl -fsS http://127.0.0.1:<port>/ || true
```

## 6. Blocked patterns

Do not use system pip, sudo pip, or `--break-system-packages`. Do not run `ExecStart=uvicorn ...` without the venv interpreter path.

## 7. Vérifier avant de terminer

A mutating task is not complete until the service file verifies, the daemon reload succeeds, the service is active, and a local HTTP or process check has run.

## 8. Format de sortie requis

```markdown
## Python venv service report

### Summary

### Environment

### Venv path

### Service file path

### Commands/tools used

### Verification

### Blocked actions

### Risk classification

### Next step
```
