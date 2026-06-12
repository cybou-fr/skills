# Semantic Skill Corpus Review

v6.9 adds a semantic review layer for the Cybou skills corpus.

Structural validators prove that the corpus is well-formed. Semantic review asks whether the skills are coherent, non-duplicative, correctly categorized and risk-calibrated.

## Artifacts

```text
semantic_review/semantic_review_manifest.yaml
semantic_review/skill_quality_report.yaml
semantic_review/taxonomy_review.yaml
semantic_review/duplicate_candidates.yaml
semantic_review/risk_recalibration_candidates.yaml
semantic_review/trigger_normalization_review.yaml
semantic_review/output_template_consistency.yaml
```

## Important rule

```text
semantic candidate != automatic rewrite
risk suggestion != automatic risk change
duplicate candidate != confirmed duplicate
```
