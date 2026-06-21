# Python Venv Service — corps français

> Version française step-for-step du contrat opérationnel. Les commandes, chemins, noms d'outils, tags de risque et clés de sortie restent identiques à `SKILL.md`.

## 1. Quand utiliser

Utiliser ce skill pour les tâches décrites par `SKILL.md` lorsque la demande opérateur est en français ou mixte EN/FR. Le comportement attendu est identique au corps anglais.

Résumé FR: Créer des services Python venv compatibles Debian avec PEP 668, FastAPI/Uvicorn sous systemd et venv/bin/python.

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

```bash
pwd
find . -maxdepth 2 -type f \( -name 'requirements*.txt' -o -name 'pyproject.toml' -o -name 'main.py' -o -name 'app.py' \) -print
sed -n '1,220p' requirements.txt 2>/dev/null || true
sed -n '1,220p' pyproject.toml 2>/dev/null || true
```

```bash
cd <app-dir>
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip wheel
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip show fastapi uvicorn 2>/dev/null || true
```

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

```bash
ss -tulpn | grep -E ':(<port>)\b' || true
curl -fsS http://127.0.0.1:<port>/health || curl -fsS http://127.0.0.1:<port>/ || true
```

```bash
pip install <package>
sudo pip install <package>
python3 -m pip install --break-system-packages <package>
ExecStart=/usr/bin/python3 -m uvicorn <module>:<app>
ExecStart=uvicorn <module>:<app>
```

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip wheel
```

```bash
python3 -m venv --help 2>&1 || true
apt-cache policy python3-venv
```

```bash
systemctl status <app-name>.service --no-pager
journalctl -u <app-name>.service -n 120 --no-pager
systemctl cat <app-name>.service --no-pager
```

```bash
ss -tulpn | grep -E ':(<port>)\b'
```

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

```bash
cd <app-dir>
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip wheel
.venv/bin/python -m pip install -r requirements.txt
```

```ini
WorkingDirectory=<app-dir>
Environment="PATH=<app-dir>/.venv/bin"
ExecStart=<app-dir>/.venv/bin/python -m uvicorn <module>:<app> --host 127.0.0.1 --port <port>
```

## 7. Récupération d'échec

Suivre les mêmes chemins de récupération que dans `SKILL.md`: symptôme → inspection → classification → action sûre → condition d'arrêt → sortie. Si l'environnement est inconnu ou production, ne pas exécuter d'action write/restart destructive automatiquement.

## 8. Conditions d'arrêt / blocage

S'arrêter si la demande sort de l'enveloppe d'autonomie VM-local, si un secret serait exposé, si l'action est destructive, ou si le skill étroit n'est pas réellement pertinent pour la tâche.

## 9. Format de sortie requis

Utiliser le même `output_template` que `SKILL.md`. Les titres peuvent être en français, mais les clés parsables comme `estimated_risk`, `actions_taken`, `blocked_actions`, `commands_used` doivent rester stables si elles sont consommées par downstream tooling.

## 10. Exigences d'évaluation

Les evals doivent exister en paire EN/FR et vérifier `selected_relevant_skill`, les commandes attendues, les commandes interdites, le niveau de risque et l'absence de sélection par mots génériques.
