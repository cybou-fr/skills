# Écriture sûre de fichiers


> Corps FR structurellement équivalent à SKILL.md. Les commandes, chemins, noms d’outils et labels de risque restent inchangés.

## 1. Quand utiliser

Use this skill whenever an agent must create or replace a config file, service unit, source file, script, nginx site, SQL client config, or any other multi-line file.

## 2. Mode opératoire

Default mode: guarded. The preferred operation is a host-governed file write followed by concrete validation.

## 3. Cartographie du risque

### low
- inspect an existing file;
- validate generated content without writing.

### medium
- write a VM-local file with `write_file` or `mcp:filesystem:write_file`;
- validate and reload a VM-local service after syntax check.

### high
- write production config;
- write secret-bearing files.

### critical
- overwrite security controls or system-critical files without rollback.

## 4. Ordre préféré des outils

1. Use `mcp:filesystem:write_file` or `write_file` for content creation.
2. Use `mcp:filesystem:read_file` to inspect the written file.
3. Use domain validators such as `systemd-analyze verify`, `nginx -t`, JSON parser, or application-specific syntax checks.
4. If no safe file-write tool exists, stop and emit a blocked action instead of using shell redirection.

## 5. Contrat write_file

```text
write_file(path="<target-path>", mode="0644", content="<complete literal content>")
```

For secret-bearing files:

```text
write_file(path="<target-path>", mode="0600", content="<complete literal content>")
```

## 6. Commandes de validation

```bash
test -f <target-path>
stat -c '%a %U %G %n' <target-path>
sed -n '1,220p' <target-path>
```

```bash
systemd-analyze verify <target-path>
nginx -t
python3 -m json.tool <target-path>
python3 -m py_compile <target-path>
php -l <target-path>
```

## 7. Modèles bloqués

Do not create multi-line files with shell redirection, shell string interpolation, or ad-hoc command output. If a file-writing tool is unavailable, stop and report that safe authoring is blocked.

## 8. Vérifier avant de terminer

A file-authoring task is not complete until the file exists, permissions are checked, content is inspected, and the domain-specific validator has run.

## 9. Format de sortie requis

```markdown
## Safe file authoring report

### Summary

### File path

### Tool used

### Validation

### Permissions

### Blocked shell-write patterns

### Risk classification

### Next step
```
