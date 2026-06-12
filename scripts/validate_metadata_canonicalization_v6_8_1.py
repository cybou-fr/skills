#!/usr/bin/env python3
from pathlib import Path
import yaml,json
ROOT=Path(__file__).resolve().parents[1]
def load_yaml(path):
    with open(path,encoding='utf-8') as f: return yaml.safe_load(f) or {}
def exists(p): return (ROOT/p).exists()
def main():
    errors=[]; warnings=[]
    forbidden_dirs=['runtime','runtime_prototype','reference_prototype','patches','rust_scaffold','cybou-core','cybou_core','tests','normalizer_tests','approval_tests','audit_tests','sandbox_tests','detection_tests','cloud_secops_tests','identity_secrets_tests','forensics_tests']
    for d in forbidden_dirs:
        if (ROOT/d).exists(): errors.append(f'forbidden/deprecated top-level directory present: {d}')
    rust_files=[str(p.relative_to(ROOT)) for p in ROOT.rglob('*.rs')]
    if rust_files: errors.append(f'forbidden Rust files present: {rust_files}')
    cybou=load_yaml(ROOT/'cybou.yaml')
    if cybou.get('repository_role')!='skills_corpus_only': errors.append('cybou.yaml repository_role must be skills_corpus_only')
    if cybou.get('contains_runtime_code') is not False: errors.append('cybou.yaml contains_runtime_code must be false')
    for e in cybou.get('canonical_entrypoints',[]):
        if not exists(e): errors.append(f'cybou.yaml canonical_entrypoint missing: {e}')
    for d in cybou.get('canonical_directories',[]):
        if not exists(d): errors.append(f'cybou.yaml canonical_directory missing: {d}')
    package=load_yaml(ROOT/'package.yaml')
    if package.get('repository_role')!='skills_corpus_only': errors.append('package.yaml repository_role must be skills_corpus_only')
    if package.get('contains_runtime_code') is not False: errors.append('package.yaml contains_runtime_code must be false')
    for rel in package.get('cybou_extensions',[]):
        if not exists(rel): errors.append(f'package.yaml cybou_extensions missing: {rel}')
    allowed={'CHANGELOG.md','VALIDATION_REPORT.md','scripts/validate_metadata_canonicalization_v6_8_1.py','docs/HYGIENE_PATCH_V6_1.md','docs/V6_2_LOADER_CONTRACT_CHANGELOG.md','docs/V6_3_IMMUNITY_COMPATIBILITY_CHANGELOG.md','docs/V6_4_SKILL_VETTING_SUPPLY_CHAIN_CHANGELOG.md','docs/V6_5_EVAL_RUNNER_ADVERSARIAL_CHANGELOG.md','docs/V6_6_RELEASE_SIGNING_PROVENANCE_CHANGELOG.md','docs/V6_7_COMMAND_NORMALIZATION_POLICY_HARDENING_CHANGELOG.md','docs/V6_8_SKILLS_CORPUS_FINALIZATION_CHANGELOG.md','docs/V6_8_1_METADATA_CANONICALIZATION_CHANGELOG.md','docs/METADATA_CANONICALIZATION_V6_8_1.md','docs/PUBLIC_REPOSITORY_CLEANUP_V6_8.md'}
    forbidden_terms=['runtime_prototype/','reference_prototype/','docs/RUST_IMMUNITY_CONTRACT_SKETCH.rs','scripts/run_behavior_tests.py','scripts/normalize_command.py','scripts/evaluate_policy.py','scripts/route_task.py','scripts/simulate_tool_call.py','normalizer_tests/','approval_tests/','audit_tests/','sandbox_tests/','detection_tests/','cloud_secops_tests/','identity_secrets_tests/','forensics_tests/']
    text_exts={'.md','.yaml','.yml','.json','.toml','.py','.txt','.placeholder'}; stale=[]
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.suffix not in text_exts: continue
        rel=str(p.relative_to(ROOT))
        if rel in allowed: continue
        txt=p.read_text(encoding='utf-8',errors='ignore')
        for term in forbidden_terms:
            if term in txt: stale.append({'file':rel,'term':term})
    if stale: errors.append({'stale_live_references':stale[:50],'count':len(stale)})
    registry=load_yaml(ROOT/'registry.yaml')
    runtime_ids=[s.get('id') for s in registry.get('skills',[]) if str(s.get('id','')).startswith('runtime-')]
    if runtime_ids: errors.append(f'runtime-* skill ids remain: {runtime_ids[:20]}')
    for skill in registry.get('skills',[]):
        sid=skill.get('id'); path=skill.get('path')
        if not sid or not path: errors.append(f'malformed registry skill: {skill}'); continue
        fp=ROOT/path
        if not fp.exists(): errors.append(f'missing skill path for {sid}: {path}'); continue
        text=fp.read_text(encoding='utf-8')
        if not text.startswith('---'): errors.append(f'{sid}: missing frontmatter'); continue
        meta=yaml.safe_load(text.split('---',2)[1]) or {}
        if meta.get('name')!=sid: errors.append(f'{sid}: frontmatter name mismatch {meta.get("name")}')
    result={'status':'pass' if not errors else 'fail','errors':errors,'warnings':warnings,'canonical_entrypoints':len(cybou.get('canonical_entrypoints',[])),'package_extensions':len(package.get('cybou_extensions',[])),'skills':len(registry.get('skills',[])),'rust_files':len(rust_files)}
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
