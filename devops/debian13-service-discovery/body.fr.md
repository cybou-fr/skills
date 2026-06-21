# Debian13 Service Discovery — corps français

> Version française step-for-step du contrat opérationnel. Les commandes, chemins, noms d'outils, tags de risque et clés de sortie restent identiques à `SKILL.md`.

## 1. Quand utiliser

Utiliser ce skill pour les tâches décrites par `SKILL.md` lorsque la demande opérateur est en français ou mixte EN/FR. Le comportement attendu est identique au corps anglais.

Résumé FR: Découvrir les services et noms d'unités fournis par les paquets Debian 13 avant de modifier ou créer des unités systemd.

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
systemctl --version
systemctl list-unit-files --type=service --type=socket --no-pager
systemctl list-units --type=service --type=socket --all --no-pager
```

```bash
apt-cache policy <package>
dpkg -L <package> | grep -E '/(systemd|init\.d)/|\.service$|\.socket$|\.timer$'
dpkg-query -L <package> | grep -E '\.(service|socket|timer)$'
dpkg-query -S '/lib/systemd/system/*' '/usr/lib/systemd/system/*' 2>/dev/null | grep '<package>'
```

```bash
systemctl list-unit-files '*php*fpm*' --no-pager
systemctl list-units '*php*fpm*' --all --no-pager
dpkg -l | grep -E '^ii\s+php[0-9.]+-fpm\b|^ii\s+php-fpm\b'
dpkg -l | awk '/^ii\s+php([0-9.]+)?-fpm/ {print $2}' | xargs -r dpkg-query -L | grep -E '\.(service|socket|timer)$'
```

```bash
systemctl list-unit-files '*mariadb*' '*mysql*' --no-pager
systemctl list-units '*mariadb*' '*mysql*' --all --no-pager
dpkg -l | grep -E '^ii\s+(mariadb|mysql)'
dpkg-query -L mariadb-server 2>/dev/null | grep -E '\.(service|socket)$'
```

```bash
systemctl status <unit> --no-pager
systemctl cat <unit> --no-pager
systemctl show <unit> -p FragmentPath -p UnitFileState -p ActiveState -p SubState -p ExecMainStatus --no-pager
```

```bash
systemctl start <discovered-unit>
systemctl reload <discovered-unit>
systemctl restart <discovered-unit>
```

```bash
cat > /etc/systemd/system/<package>.service
rm -f /lib/systemd/system/<unit>
systemctl mask <unit>
systemctl disable <unit>
```

```bash
systemctl list-unit-files '*<service>*' --no-pager
systemctl list-units '*<service>*' --all --no-pager
dpkg -l | grep -i '<service>'
dpkg-query -L <package> 2>/dev/null | grep -E '\.(service|socket|timer)$'
```

```bash
apt-cache search '^<package>$'
apt-cache policy <package>
```

```bash
systemctl status <unit> --no-pager
journalctl -u <unit> -n 80 --no-pager
```

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

```bash
dpkg -l | awk '/^ii\s+php([0-9.]+)?-fpm/ {print $2}' | xargs -r dpkg-query -L | grep -E '\.(service|socket|timer)$'
dpkg -l | awk '/^ii\s+(mariadb|mysql)-/ {print $2}' | xargs -r dpkg-query -L | grep -E '\.(service|socket|timer)$'
```

## 7. Récupération d'échec

Suivre les mêmes chemins de récupération que dans `SKILL.md`: symptôme → inspection → classification → action sûre → condition d'arrêt → sortie. Si l'environnement est inconnu ou production, ne pas exécuter d'action write/restart destructive automatiquement.

## 8. Conditions d'arrêt / blocage

S'arrêter si la demande sort de l'enveloppe d'autonomie VM-local, si un secret serait exposé, si l'action est destructive, ou si le skill étroit n'est pas réellement pertinent pour la tâche.

## 9. Format de sortie requis

Utiliser le même `output_template` que `SKILL.md`. Les titres peuvent être en français, mais les clés parsables comme `estimated_risk`, `actions_taken`, `blocked_actions`, `commands_used` doivent rester stables si elles sont consommées par downstream tooling.

## 10. Exigences d'évaluation

Les evals doivent exister en paire EN/FR et vérifier `selected_relevant_skill`, les commandes attendues, les commandes interdites, le niveau de risque et l'absence de sélection par mots génériques.
