# quant-ai-kit

Versioned prompt and workflow toolkit for AI-assisted quant development. Markdown-only. No SDK, no package.

## What this is

A git repo of prompt templates, schemas, and a state-machine workflow definition. Projects reference it as a submodule (or symlink). Templates are read-only inside projects; the kit is the single source of truth.

## Quick start in a new project

```bash
cd <your-project>
git submodule add <kit-url> .ai/kit
cd .ai/kit && git checkout v0.1.0 && cd ../..
mkdir -p .ai/plans .ai/overrides
cp .ai/kit/templates/project.template.md  .ai/PROJECT.md
cp .ai/kit/templates/state.template.md    .ai/STATE.md
cp .ai/kit/templates/followups.template.md .ai/FOLLOWUPS.md
touch .ai/JOURNAL.md .ai/DECISIONS.md .ai/CONVENTIONS.md
```

Fill in PROJECT.md, then trigger CHARTER (or start at PLAN if charter is trivial).

## Anatomy

- `WORKFLOW.md` — canonical state machine; every prompt references it
- `CONVENTIONS.md` — house rules every session inherits
- `schemas/` — front-matter and section contracts for project artifacts
- `prompts/` — stage trigger prompts and shared partials
- `templates/` — blank project artifacts to copy into a new project
- `scripts/` — mechanical checks (deviation, overlap, plans index)

## Workflow at a glance

CHARTER → DISCOVERY → PLAN → PLAN_REVIEW → PLAN_REDTEAM → PLAN_REVISE → EXECUTE → CODE_REVIEW → REVIEW_ADDRESS → VERIFY → INTEGRATE

See `WORKFLOW.md`.

## Versioning

Semver tags. Bump rules:
- patch: typo/clarification, no behavior change
- minor: new template, new slot (backward compatible)
- major: removed/renamed slot or schema change

Every change goes in `CHANGELOG.md` with a one-line rationale.
