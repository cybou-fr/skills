#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT = Path.cwd()
overlay = ROOT / 'registry.v10.1.bilingual_external_devops_active_entries.yaml'
if not overlay.exists(): overlay = ROOT / 'repo-overlay' / 'registry.v10.1.bilingual_external_devops_active_entries.yaml'
entries = yaml.safe_load(overlay.read_text(encoding='utf-8'))['skills']
registry = ROOT / 'registry.yaml'
if registry.exists():
    data = yaml.safe_load(registry.read_text(encoding='utf-8')) or {}
else:
    data = {'version':'10.1','skills':[]}
skills = data.setdefault('skills', [])
by_id = {s.get('id'): i for i,s in enumerate(skills) if isinstance(s,dict)}
for e in entries:
    if e['id'] in by_id: skills[by_id[e['id']]] = e
    else: skills.append(e)
data['version'] = '10.1'
registry.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding='utf-8')

graph_overlay = ROOT / 'skill_graph.v10.1.bilingual_external_devops_active_entries.yaml'
if not graph_overlay.exists(): graph_overlay = ROOT / 'repo-overlay' / 'skill_graph.v10.1.bilingual_external_devops_active_entries.yaml'
graph_file = ROOT / 'skill_graph.yaml'
graph_entries = yaml.safe_load(graph_overlay.read_text(encoding='utf-8'))['nodes']
if graph_file.exists():
    g = yaml.safe_load(graph_file.read_text(encoding='utf-8')) or {}
else:
    g = {'version':'10.1','nodes':{}}
nodes = g.setdefault('nodes', {})
for k,v in graph_entries.items(): nodes[k] = v
g['version'] = '10.1'
graph_file.write_text(yaml.safe_dump(g, sort_keys=False, allow_unicode=True), encoding='utf-8')
print('OK: v10.1 registry.yaml and skill_graph.yaml integrated')
