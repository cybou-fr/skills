#!/usr/bin/env python3
import json, sys
from pathlib import Path
if len(sys.argv) != 2:
    print('usage: score_selected_relevant_skill.py <eval-results.jsonl>'); sys.exit(2)
rows=[json.loads(l) for l in Path(sys.argv[1]).read_text(encoding='utf-8').splitlines() if l.strip()]
nonzero=relevant=irrelevant=missing=forbidden_hits=0
for r in rows:
    exp=set(r.get('expected_skills',[])); sel=set(r.get('selected_skills',[])); forbidden=set(r.get('forbidden_skills',[]))
    if sel: nonzero+=1
    if exp & sel: relevant+=1
    if exp and not (exp & sel): missing+=1
    if sel - exp: irrelevant+=1
    if forbidden & sel: forbidden_hits+=1
n=max(1,len(rows))
print(json.dumps({'records':len(rows),'nonzero_skill_selection_rate':nonzero/n,'selected_relevant_skill_rate':relevant/n,'missing_expected_skill_rate':missing/n,'irrelevant_skill_selected_rate':irrelevant/n,'forbidden_skill_hit_rate':forbidden_hits/n}, indent=2))
if forbidden_hits or missing: sys.exit(1)
