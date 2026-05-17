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

## Step by Step Guide

Per project (one-time setup)
1. Attach the kit (submodule/symlink) and initialize .ai/ with PROJECT.md, STATE.md, JOURNAL.md, FOLLOWUPS.md.

Starting a new piece of work
1. Decide tier — trivial → small-change, small feature → feature-add, otherwise full plan flow.
2. Write the brief — copy templates/brief.template.md to NNN-<slug>.brief.md and fill it. (Manual, ~5–10 min.)
3. Create the plan — via prompt (plan-create). Reads brief + FOLLOWUPS.md, outputs draft plan.
4. Review the plan — via prompt (plan-review) in a fresh session. Outputs review file.
5. Red-team the plan — via prompt (plan-redteam), ideally on a different LLM. Outputs redteam file.
6. Revise the plan — via prompt (plan-revise). Consolidates review + redteam, sets status: in-review.

Per phase (loop until plan complete)
1. Execute phase — via prompt (phase-execute).
2. Code review — via prompt (code-review); add quant-validation if quant work.
3. Address findings — via prompt (review-address). Deferred items append to FOLLOWUPS.md.
4. Verify — via prompt (verify). If unresolved, loop back to step 3. If clean, phase flips to done.
5. Integrate — via prompt (integrate). Commit/merge.

Anytime
- Lost on which prompt to run — via prompt (meta/route). Reads STATE.md, returns the correct next prompt.
- Before clearing context, always — via prompt (session-wrap). Only safe stopping point; updates STATE.md + JOURNAL.md.

Kit evolution
- If you edit a prompt inside a project, stop. Port the edit back to the kit repo, bump version, log in CHANGELOG.md. Projects pick it up on next pin bump.