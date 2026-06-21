#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT = Path.cwd()
entries_path = ROOT / 'registry.v10.bilingual_external_devops_active_entries.yaml'
graph_path = ROOT / 'skill_graph.v10.bilingual_external_devops_active_entries.yaml'
registry_path = ROOT / 'registry.yaml'
skill_graph_path = ROOT / 'skill_graph.yaml'
if not entries_path.exists() or not graph_path.exists():
    raise SystemExit('v10 active entries files are missing; apply overlay first')
entries = yaml.safe_load(entries_path.read_text())['skills']
reg = yaml.safe_load(registry_path.read_text()) if registry_path.exists() else {'version':'10.0','skills':[]}
reg.setdefault('skills', [])
by_id = {s.get('id') or s.get('name'): i for i, s in enumerate(reg['skills'])}
for e in entries:
    item = dict(e)
    if item['id'] in by_id:
        old = reg['skills'][by_id[item['id']]]
        old.update(item)
    else:
        reg['skills'].append(item)
reg['version'] = '10.0'
reg['bilingual'] = {'co_primary_languages':['en','fr'], 'trigger_mode':'merged_en_fr', 'summary_mode':'bilingual_summary_plus_summary_fr'}
registry_path.write_text(yaml.safe_dump(reg, sort_keys=False, allow_unicode=True, width=140))

graph_entries = yaml.safe_load(graph_path.read_text())['skills']
graph = yaml.safe_load(skill_graph_path.read_text()) if skill_graph_path.exists() else {'version':'10.0','skills':{}}
graph.setdefault('skills', {})
for sid, node in graph_entries.items():
    graph['skills'][sid] = node
graph['version'] = '10.0'
graph['bilingual'] = {'co_primary_languages':['en','fr'], 'selection':'merged bilingual triggers'}
skill_graph_path.write_text(yaml.safe_dump(graph, sort_keys=False, allow_unicode=True, width=140))
print('OK: active registry.yaml and skill_graph.yaml updated with v10 bilingual external DevOps skills')
