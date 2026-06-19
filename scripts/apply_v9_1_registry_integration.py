#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from datetime import datetime
import sys
try:
    import yaml
except Exception as exc:
    raise SystemExit("PyYAML required: python3 -m pip install pyyaml") from exc
ROOT=Path.cwd(); REG=ROOT/'registry.yaml'; GRAPH=ROOT/'skill_graph.yaml'
REG_PATCH=ROOT/'registry.v9.1.external_devops_active_entries.yaml'; GRAPH_PATCH=ROOT/'skill_graph.v9.1.external_devops_active_entries.yaml'
BANNED={"and","or","the","a","an","system","service","unit","url","http","https","file","write","config","database","sql","user","admin","python","nginx","php","wordpress"}
def load(p):
    if not p.exists(): raise SystemExit(f"missing {p}")
    return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
def backup(p):
    if p.exists(): p.with_suffix(p.suffix+'.bak-v9.1-'+datetime.utcnow().strftime('%Y%m%d%H%M%S')).write_text(p.read_text(encoding='utf-8'),encoding='utf-8')
def main():
    reg=load(REG); patch=load(REG_PATCH); skills=reg.setdefault('skills',[])
    if not isinstance(skills,list): raise SystemExit('registry.yaml skills must be a list')
    reg['version']='9.1'
    pol=reg.setdefault('skill_selection_policy',{})
    pol['primary_metric']='selected_relevant_skill'; pol['prefer_narrow_skills']=True; pol['banned_tokens_are_exact_single_token_only']=True; pol['banned_single_token_triggers']=sorted(BANNED)
    by={s.get('id'):i for i,s in enumerate(skills) if isinstance(s,dict) and s.get('id')}
    for e in patch.get('skills',[]):
        sid=e['id']; bad=[t for t in e.get('triggers',[]) if isinstance(t,str) and t.lower().strip() in BANNED]
        if bad: raise SystemExit(f'{sid}: banned single-token trigger {bad}')
        if sid in by: skills[by[sid]]=e
        else: skills.append(e)
    backup(REG); REG.write_text(yaml.safe_dump(reg,sort_keys=False,allow_unicode=True),encoding='utf-8')
    graph=load(GRAPH); gp=load(GRAPH_PATCH); graph['version']='9.1'; gskills=graph.setdefault('skills',{})
    if not isinstance(gskills,dict): raise SystemExit('skill_graph.yaml skills must be a mapping')
    for sid,e in gp.get('skills',{}).items(): gskills[sid]=e
    backup(GRAPH); GRAPH.write_text(yaml.safe_dump(graph,sort_keys=False,allow_unicode=True),encoding='utf-8')
    print('OK: active registry.yaml and skill_graph.yaml updated with v9.1 external DevOps skills')
if __name__=='__main__': main()
