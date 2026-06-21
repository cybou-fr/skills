#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
SKILLS=['debian13-service-discovery','python-venv-service','nginx-php-fpm-wordpress','mariadb-wordpress-admin','safe-file-authoring']
errors=[]
regp=Path('registry.yaml')
graphp=Path('skill_graph.yaml')
if not regp.exists() or not graphp.exists():
    # allow overlay-only mode by checking active entries files
    regp=Path('registry.v10.bilingual_external_devops_active_entries.yaml')
    graphp=Path('skill_graph.v10.bilingual_external_devops_active_entries.yaml')
reg=yaml.safe_load(regp.read_text())
graph=yaml.safe_load(graphp.read_text())
reg_items={x.get('id'):x for x in reg.get('skills',[])} if isinstance(reg.get('skills'),list) else {}
graph_items=graph.get('skills',{})
for sid in SKILLS:
    r=reg_items.get(sid)
    if not r: errors.append(f'{sid}: missing from registry'); continue
    if not r.get('summary_fr'): errors.append(f'{sid}: registry missing summary_fr')
    if not r.get('i18n',{}).get('fr',{}).get('summary'): errors.append(f'{sid}: registry missing i18n.fr.summary')
    triggers=r.get('triggers',[])
    if len(triggers)<8: errors.append(f'{sid}: registry triggers too short for bilingual selection')
    g=graph_items.get(sid)
    if not g: errors.append(f'{sid}: missing from skill_graph'); continue
    if 'fr' not in g.get('language_support',{}).get('co_primary',[]): errors.append(f'{sid}: skill_graph missing FR language support')
if errors:
    print('\n'.join(errors), file=sys.stderr); raise SystemExit(1)
print('OK: v10 active registry/skill_graph bilingual integration validated')
