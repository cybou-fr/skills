# Metadata Canonicalization v6.8.1

v6.8.1 removes live stale metadata references left over from older prototype-oriented packs.

## Fixed

```text
cybou.yaml rewritten as skills-only corpus manifest
package.yaml rewritten with only existing live files
runtime/ removed from top-level repository
runtime/decision_enums.yaml migrated to integration/decision_enums.yaml
runtime/runtime_objects.yaml migrated to integration/object_mapping.yaml
AGENTS.md updated from old v3 wording to v6.8.1 skills-corpus wording
legacy legacy-removed-runtime-prototype/reference_prototype references purged from live metadata
new validator added for missing metadata references
```
