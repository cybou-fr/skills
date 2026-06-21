#!/usr/bin/env python3
from pathlib import Path
import yaml, sys
ROOT=Path.cwd()
paths=list(ROOT.glob('**/evals/v10_1/bilingual_external_devops_selection.yaml'))
if not paths:
    print('missing v10.1 bilingual executable evals'); sys.exit(1)
data=yaml.safe_load(paths[0].read_text(encoding='utf-8'))
errors=[]
for e in data.get('evals',[]):
    for key in ['id','lang','task','expected_skills','must_include','must_not_include','expected_risk']:
        if key not in e: errors.append(f"{e.get('id','<unknown>')}: missing {key}")
    if e.get('lang') not in ['en','fr']: errors.append(f"{e.get('id')}: invalid lang")
langs={e.get('lang') for e in data.get('evals',[])}
if not {'en','fr'} <= langs: errors.append('evals must include both EN and FR')
if len(data.get('evals',[])) < 10: errors.append('expected at least 10 evals')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: v10.1 bilingual executable evals validated')
