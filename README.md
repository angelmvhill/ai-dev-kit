# ai-dev-kit

Versioned prompt and workflow toolkit for AI-assisted development (quant-friendly). There is no SDK or package to install — the kit is Markdown prompts, schemas, and templates, plus a few optional helper scripts under `scripts/`.

## What this is

A git repo of prompt templates, schemas, and a state-machine workflow definition. Projects reference it as a submodule (or symlink). Templates are read-only inside projects; the kit is the single source of truth.

## Quick start in a new project

**Recommended — bootstrap script (cross-platform):**

```bash
cd <your-project>
python path/to/ai-dev-kit/scripts/init_project.py \
  --project-root . \
  --project-name my-project
```

PowerShell:

```powershell
cd <your-project>
python C:\ai-dev-kit\scripts\init_project.py `
  --project-root (Get-Location) `
  --project-name my-project
```

The script attaches `.ai/kit` as a git submodule (pinned to `v0.2.0`), scaffolds `.ai/` from templates, and writes `.cursor/rules/ai-dev-kit-workflow.mdc`.

**Local kit override (dev machines):**

```powershell
$env:AI_DEV_KIT_LOCAL = "C:\ai-dev-kit"
python C:\ai-dev-kit\scripts\init_project.py --project-root . --project-name my-project
```

**Cursor global skill:** install `~/.cursor/skills/init-ai-dev-kit/` and ask the agent to "init ai-dev-kit" in any workspace.

**Manual (bash):**

```bash
cd <your-project>
git submodule add https://github.com/angelmvhill/ai-dev-kit.git .ai/kit
cd .ai/kit && git checkout v0.2.0 && cd ../..
mkdir -p .ai/overrides .ai/notes .ai/briefs .ai/plans .ai/reviews
cp .ai/kit/templates/project.template.md  .ai/PROJECT.md
cp .ai/kit/templates/state.template.md    .ai/STATE.md
cp .ai/kit/templates/followups.template.md .ai/FOLLOWUPS.md
touch .ai/JOURNAL.md .ai/DECISIONS.md .ai/CONVENTIONS.md
```

(Or run `prompts/meta/init-project.md`, which scaffolds the same layout for you.)

Fill in PROJECT.md, then run `planning/charter` (or skip to `planning/plan-create` if the charter is trivial).

## Anatomy

- `WORKFLOW.md` — canonical state machine; every prompt references it
- `CONVENTIONS.md` — house rules every session inherits
- `schemas/` — front-matter and section contracts for project artifacts
- `prompts/` — stage trigger prompts and shared partials
- `templates/` — blank project artifacts to copy into a new project
- `scripts/` — bootstrap (`init_project.py`) and mechanical checks (deviation, overlap, plans index)

## Workflow at a glance

INIT → CHARTER → DISCOVERY → PLAN_DRAFT → PLAN_REVIEWED → PLAN_REDTEAMED → PLAN_IN_REVIEW → PLAN_APPROVED → PHASE_IMPLEMENTED → PHASE_REVIEWED → PHASE_ADDRESSED → PHASE_VERIFIED → INTEGRATED → (next phase or DONE)

These are the `STATE.md` `status` values; each names the milestone just completed. See `WORKFLOW.md` for the status → prompt map.

## Versioning

Semver tags. Bump rules:
- patch: typo/clarification, no behavior change
- minor: new template, new slot (backward compatible)
- major: removed/renamed slot or schema change

Every change goes in `CHANGELOG.md` with a one-line rationale.

## Step by Step Guide

Per project (one-time setup)
1. Attach the kit (submodule/symlink) and initialize .ai/ — either run `prompts/meta/init-project.md` or follow the Quick start above. This creates PROJECT.md, STATE.md, JOURNAL.md, FOLLOWUPS.md, DECISIONS.md, CONVENTIONS.md, and the overrides/ notes/ briefs/ plans/ reviews/ directories.

Starting a new piece of work
1. Decide tier — trivial → small-change, small feature → feature-add, otherwise full plan flow.
2. Write the brief — copy templates/brief.template.md to .ai/briefs/NNN-<slug>.brief.md and fill it. (Manual, ~5–10 min.)
3. Map the codebase — via prompt (understand-codebase). Required for the full plan flow; outputs the codebase map that plan-create consumes.
4. Create the plan — via prompt (plan-create). Reads brief + codebase map + FOLLOWUPS.md, outputs draft plan.
5. Review the plan — via prompt (plan-review) in a fresh session. Outputs review file.
6. Red-team the plan — via prompt (plan-redteam), ideally on a different LLM. Outputs redteam file.
7. Revise the plan — via prompt (plan-revise). Consolidates review + redteam, sets status: in-review. Then the human approves (sets STATE.status: PLAN_APPROVED).

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