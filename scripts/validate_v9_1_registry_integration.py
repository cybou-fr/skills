#!/usr/bin/env python3
from pathlib import Path
try:
    import yaml
except Exception:
    yaml=None
ROOT=Path.cwd()
SKILLS={
 'debian13-service-discovery':'devops/debian13-service-discovery/SKILL.md',
 'python-venv-service':'devops/python-venv-service/SKILL.md',
 'nginx-php-fpm-wordpress':'devops/nginx-php-fpm-wordpress/SKILL.md',
 'mariadb-wordpress-admin':'devops/mariadb-wordpress-admin/SKILL.md',
 'safe-file-authoring':'devops/safe-file-authoring/SKILL.md'}
BANNED={"and","or","the","a","an","system","service","unit","url","http","https","file","write","config","database","sql","user","admin","python","nginx","php","wordpress"}
def main():
    errors=[]
    for sid,p in SKILLS.items():
        if not (ROOT/p).exists(): errors.append(f'missing skill file {p}')
    if yaml:
        reg=yaml.safe_load((ROOT/'registry.yaml').read_text(encoding='utf-8')) or {}; graph=yaml.safe_load((ROOT/'skill_graph.yaml').read_text(encoding='utf-8')) or {}
        by={s.get('id'):s for s in reg.get('skills',[]) if isinstance(s,dict)}
        for sid,p in SKILLS.items():
            e=by.get(sid)
            if not e: errors.append(f'registry missing {sid}'); continue
            if e.get('path')!=p: errors.append(f'registry path mismatch for {sid}')
            if e.get('selection_profile')!='narrow': errors.append(f'{sid} selection_profile not narrow')
            for t in e.get('triggers',[]) or []:
                if isinstance(t,str) and t.lower().strip() in BANNED: errors.append(f'{sid} banned trigger {t}')
            ge=(graph.get('skills') or {}).get(sid)
            if not ge: errors.append(f'skill_graph missing {sid}')
            elif ge.get('path')!=p: errors.append(f'skill_graph path mismatch for {sid}')
    else:
        rt=(ROOT/'registry.yaml').read_text(encoding='utf-8'); gt=(ROOT/'skill_graph.yaml').read_text(encoding='utf-8')
        for sid,p in SKILLS.items():
            if f'id: {sid}' not in rt or f'path: {p}' not in rt: errors.append(f'registry text missing {sid}')
            if f'  {sid}:' not in gt: errors.append(f'skill_graph text missing {sid}')
    tmpl='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in ROOT.glob('**/output_templates*.yaml') if p.is_file())
    for name in ['debian13_service_discovery_report','python_venv_service_report','nginx_php_fpm_wordpress_report','mariadb_wordpress_admin_report','safe_file_authoring_report']:
        if name not in tmpl: errors.append(f'missing output template {name}')
    if errors:
        print('FAIL:'); [print('-',e) for e in errors]; raise SystemExit(1)
    print('OK: v9.1 active registry/skill_graph integration validated')
if __name__=='__main__': main()
