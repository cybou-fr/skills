# Safe File Authoring — corps français

> Version française step-for-step du contrat opérationnel. Les commandes, chemins, noms d'outils, tags de risque et clés de sortie restent identiques à `SKILL.md`.

## 1. Quand utiliser

Utiliser ce skill pour les tâches décrites par `SKILL.md` lorsque la demande opérateur est en français ou mixte EN/FR. Le comportement attendu est identique au corps anglais.

Résumé FR: Écrire des fichiers en sécurité avec MCP write_file si disponible, sinon install -d + tee et heredoc cité en shell fallback.

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
test -e <target> && ls -l <target> || true
test -f <target> && sed -n '1,220p' <target> || true
namei -l <target-dir>
```

```bash
install -d -m 0755 <target-dir>
if test -f <target>; then cp -a <target> <target>.bak.$(date +%Y%m%d%H%M%S); fi
```

```bash
tee <target> >/dev/null <<'EOF'
<literal-content>
EOF
```

```bash
install -d -m 0755 <target-dir>
tmp=$(mktemp <target-dir>/.<basename>.tmp.XXXXXX)
cat > "$tmp" <<'EOF'
<literal-content>
EOF
chmod 0644 "$tmp"
mv "$tmp" <target>
```

```bash
sed -n '1,260p' <target>
systemd-analyze verify <target>          # for systemd units
nginx -t                                # for nginx config
python3 -m json.tool <target>            # for JSON
python3 - <<'PY'
import sys, yaml
for p in sys.argv[1:]: yaml.safe_load(open(p))
PY <target>                              # for YAML if PyYAML exists
```

```bash
cat > <target> <<EOF        # unquoted heredoc for complex config
printf "<complex-content>" > <target>
sed -i '...' <critical-file>
chmod -R 777 <path>
chown -R <user>:<group> <path>
```

```bash
test -f <target> && sed -n '1,260p' <target> || true
```

```bash
namei -l <target>
ls -ld <target-dir>
```

```markdown
## Safe file authoring report

### Summary

### Target
- Path:
- Existing file:
- Backup:

### Authoring method
- Tool/pattern:
- Parent directory created:
- Permissions:

### Validation
- Validator:
- Result:

### Risk classification
- estimated_risk:
- risk drivers:

### Actions taken

### Blocked actions

### Recommendation
```

```text
write_file(path="<target>", content="<literal-content>", mode="0644")
```

```bash
python3 - <<'PY'
try:
    import yaml
    with open('<target>', 'r', encoding='utf-8') as f:
        yaml.safe_load(f)
    print('YAML OK')
except ModuleNotFoundError:
    print('YAML validation skipped: PyYAML unavailable')
except Exception as e:
    raise SystemExit(f'YAML invalid: {e}')
PY
```

## 7. Récupération d'échec

Suivre les mêmes chemins de récupération que dans `SKILL.md`: symptôme → inspection → classification → action sûre → condition d'arrêt → sortie. Si l'environnement est inconnu ou production, ne pas exécuter d'action write/restart destructive automatiquement.

## 8. Conditions d'arrêt / blocage

S'arrêter si la demande sort de l'enveloppe d'autonomie VM-local, si un secret serait exposé, si l'action est destructive, ou si le skill étroit n'est pas réellement pertinent pour la tâche.

## 9. Format de sortie requis

Utiliser le même `output_template` que `SKILL.md`. Les titres peuvent être en français, mais les clés parsables comme `estimated_risk`, `actions_taken`, `blocked_actions`, `commands_used` doivent rester stables si elles sont consommées par downstream tooling.

## 10. Exigences d'évaluation

Les evals doivent exister en paire EN/FR et vérifier `selected_relevant_skill`, les commandes attendues, les commandes interdites, le niveau de risque et l'absence de sélection par mots génériques.
