#!/usr/bin/env python3
from pathlib import Path
import yaml, json
ROOT=Path(__file__).resolve().parents[1]
def load_yaml(p):
    with open(p,encoding='utf-8') as f: return yaml.safe_load(f) or {}
def main():
    errors=[]; warnings=[]
    required=['semantic_review/semantic_review_manifest.yaml','semantic_review/skill_quality_report.yaml','semantic_review/taxonomy_review.yaml','semantic_review/duplicate_candidates.yaml','semantic_review/risk_recalibration_candidates.yaml','semantic_review/trigger_normalization_review.yaml','semantic_review/output_template_consistency.yaml','schemas/semantic_review_manifest.schema.json','schemas/semantic_review_report.schema.json','docs/SEMANTIC_SKILL_CORPUS_REVIEW.md','docs/SKILL_TAXONOMY_REVIEW.md','docs/RISK_RECALIBRATION_GUIDE.md']
    for rel in required:
        if not (ROOT/rel).exists(): errors.append(f'missing v6.9 semantic review artifact: {rel}')
    if errors:
        print(json.dumps({'status':'fail','errors':errors,'warnings':warnings},indent=2,ensure_ascii=False)); return 1
    registry=load_yaml(ROOT/'registry.yaml'); manifest=load_yaml(ROOT/'semantic_review/semantic_review_manifest.yaml'); quality=load_yaml(ROOT/'semantic_review/skill_quality_report.yaml'); taxonomy=load_yaml(ROOT/'semantic_review/taxonomy_review.yaml'); duplicates=load_yaml(ROOT/'semantic_review/duplicate_candidates.yaml'); risk=load_yaml(ROOT/'semantic_review/risk_recalibration_candidates.yaml')
    count=len(registry.get('skills',[]))
    if manifest.get('scope',{}).get('skills_reviewed') != count: errors.append('semantic_review_manifest skills_reviewed does not match registry skill count')
    if quality.get('skills_reviewed') != count: errors.append('skill_quality_report skills_reviewed does not match registry skill count')
    expected={'core','devops','secops','productivity'}
    unknown=[c for c in taxonomy.get('category_counts',{}).keys() if c not in expected]
    if unknown: errors.append(f'unknown categories in taxonomy review: {unknown}')
    for item in duplicates.get('candidates',[]):
        if not item.get('skill_a') or not item.get('skill_b'): errors.append(f'malformed duplicate candidate: {item}')
    for item in risk.get('candidates',[]):
        if not item.get('skill_id') or not item.get('suggested_risk'): errors.append(f'malformed risk recalibration candidate: {item}')
    result={'status':'pass' if not errors else 'fail','errors':errors,'warnings':warnings,'skills_reviewed':count,'duplicate_candidates':len(duplicates.get('candidates',[])),'risk_recalibration_candidates':len(risk.get('candidates',[])),'category_findings':len(taxonomy.get('findings',[]))}
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
