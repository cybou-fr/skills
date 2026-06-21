---
name: safe-file-authoring
version: '10.0'
skill_format: operational_contract_v1
category: devops/filesystem
default_mode: guarded
default_risk: medium
selection_profile: narrow
summary: Safely author files using MCP write_file when available, or robust install -d + tee / quoted heredoc shell fallback.
  / Écrire des fichiers en sécurité avec MCP write_file si disponible, sinon install -d + tee et heredoc cité en shell fallback.
requires_tools:
  preferred:
  - mcp:filesystem:write_file
  - mcp:filesystem:read_file
  fallback:
  - shell
policy_refs:
- policy_rules/shell.yaml
triggers:
  include:
  - safe write file heredoc
  - quoted heredoc tee file authoring
  - install -d tee system config
  - write_file fallback shell
  - avoid unterminated heredoc
  - robust file creation systemd nginx config
  - écrire fichier en sécurité
  - création fichier robuste
  - heredoc cité
  - tee avec heredoc
  - éviter cat heredoc non cité
  - créer répertoire install -d
  - écrire configuration sans casser guillemets
  - write_file préféré
  - fallback tee heredoc
  - éviter heredoc interrompu
  - fichier config nginx avec variables
  - écrire unité systemd avec tee
  exclude:
  - generic file question
  - read file only
  - code formatting only
negative_triggers:
- file
- write
- config
- shell
activation_examples:
- Create a systemd unit without heredoc quoting bugs.
- Use write_file if available, otherwise install -d plus tee with quoted EOF.
- Créer une unité systemd sans bogue de guillemets heredoc.
- Utiliser write_file si disponible, sinon install -d et tee avec EOF cité.
output_template: safe_file_authoring_report
summary_fr: Écrire des fichiers en sécurité avec MCP write_file si disponible, sinon install -d + tee et heredoc cité en shell
  fallback.
i18n:
  fr:
    summary: Écrire des fichiers en sécurité avec MCP write_file si disponible, sinon install -d + tee et heredoc cité en
      shell fallback.
    body: body.fr.md
---


# Safe File Authoring

## 1. Use when

Use when an agent must create or replace text files such as systemd units, nginx configs, env files, scripts, or application config inside an allowed VM/local workspace.

Prefer `write_file`/MCP file authoring tools when available. Use shell fallback only with robust quoting patterns.

## 2. Do not use when

Do not use for generic file reading, code explanation, or writing secrets into logs. Do not trigger from `file`, `write`, `config`, or `shell` alone.

## 3. Operating mode

Default is guarded authoring. File writes are allowed only within explicitly permitted paths and autonomy envelope. Always create parent directories deliberately and verify file content after write.

## 4. Risk mapping

### low
- inspect target path;
- read existing file;
- generate patch/diff without writing;
- validate syntax after writing in sandbox.

### medium
- write VM-local config file with backup;
- create parent directory with safe mode;
- write systemd/nginx config in isolated VM then validate.

### high
- overwrite production config;
- write executable scripts in privileged path;
- write files containing secrets;
- change ownership/permissions broadly.

### critical
- overwrite `/etc/sudoers`, SSH authorized keys, PAM configs, or security policy files without explicit policy;
- recursive chmod/chown;
- destructive truncation of unknown files;
- write secrets to world-readable paths.

## 5. Preferred tool order

1. Use `mcp:filesystem:write_file` if available.
2. Use `mcp:filesystem:read_file` to verify existing state.
3. Use shell fallback with `install -d` and `tee` plus single-quoted heredoc delimiter.
4. Do not use fragile unquoted heredocs for content containing `$`, backticks, quotes, or shell substitutions.

## 6. Command templates

### read_only: inspect target

```bash
test -e <target> && ls -l <target> || true
test -f <target> && sed -n '1,220p' <target> || true
namei -l <target-dir>
```

### guarded: create parent and backup existing file

```bash
install -d -m 0755 <target-dir>
if test -f <target>; then cp -a <target> <target>.bak.$(date +%Y%m%d%H%M%S); fi
```

### guarded: robust quoted heredoc with tee

```bash
tee <target> >/dev/null <<'EOF'
<literal-content>
EOF
```

The delimiter must be single-quoted as `<<'EOF'` when content contains `$`, backticks, quotes, regexes, nginx variables, systemd environment lines, YAML, JSON, or shell snippets.

### guarded: atomic temp file pattern

```bash
install -d -m 0755 <target-dir>
tmp=$(mktemp <target-dir>/.<basename>.tmp.XXXXXX)
cat > "$tmp" <<'EOF'
<literal-content>
EOF
chmod 0644 "$tmp"
mv "$tmp" <target>
```

Use this pattern when partial writes would be harmful.

### read_only: verify and validate by file type

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

### blocked

```bash
cat > <target> <<EOF        # unquoted heredoc for complex config
printf "<complex-content>" > <target>
sed -i '...' <critical-file>
chmod -R 777 <path>
chown -R <user>:<group> <path>
```

## 7. Failure recovery

### If heredoc fails or quote is unterminated

1. Stop appending more shell lines.
2. Inspect target and shell script context:

```bash
test -f <target> && sed -n '1,260p' <target> || true
```

3. Rewrite using `write_file` if available or quoted heredoc/atomic temp pattern.
4. Validate syntax before using the file.

### If permission denied

1. Inspect path ownership:

```bash
namei -l <target>
ls -ld <target-dir>
```

2. Do not escalate blindly.
3. If VM-local privileged config is in scope, use the runtime-approved privileged write path.

### If validation fails

1. Do not reload/restart dependent service.
2. Show validation error and relevant file lines.
3. Patch the file, revalidate, then continue only after success.

## 8. Stop / block conditions

Stop if:

- target path is outside allowed workspace/autonomy envelope;
- content includes secrets that would be logged or world-readable;
- write would overwrite critical auth/security files;
- validation fails;
- only available pattern is an unsafe/unquoted heredoc for complex content.

## 9. Output contract

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

## 10. Eval requirements

Create evals for:

- prefers `write_file` when available;
- uses `install -d` + quoted heredoc fallback;
- blocks unquoted heredoc for nginx/systemd content;
- validation failure blocks reload/restart;
- permission denied does not escalate blindly.


## V9.1 Integration hardening

### preferred_tool: explicit write_file contract

When available, prefer the host-governed file writer rather than shell heredocs:

```text
write_file(path="<target>", content="<literal-content>", mode="0644")
```

Then verify with read-back and a syntax-specific validator.

### read_only: YAML validation fallback

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
