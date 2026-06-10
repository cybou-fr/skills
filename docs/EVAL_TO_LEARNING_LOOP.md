# Eval to Learning Loop

v6 exposes the v5 test corpus under `evals/`.

Mapping:

```text
successful safe eval -> SkillLibrary candidate
failed path -> Lesson / Reflexion candidate
unsafe behavior -> immunity regression
cross-task success -> knowledge graph synthesis
```

A successful eval is not automatically trusted; it is a candidate and must pass vetting.
