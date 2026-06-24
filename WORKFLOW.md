# Workflow

This kit implements a prompt-driven state machine for AI-assisted development. Every workflow stage is triggered by exactly one prompt template. Each prompt loads context, performs a stage's work, and advances the cursor via `STATE.md`.

`STATE.md`'s `status` field is the single source of truth for workflow position. Each status names the **milestone just completed**; the router maps it to the next prompt to run. These are the only legal `status` values.

## State machine

```
INIT → CHARTER → DISCOVERY → PLAN_DRAFT → PLAN_REVIEWED → PLAN_REDTEAMED → PLAN_IN_REVIEW
    → PLAN_APPROVED → PHASE_IMPLEMENTED → PHASE_REVIEWED → PHASE_ADDRESSED → PHASE_VERIFIED → INTEGRATED
    → (more phases: PLAN_APPROVED) or DONE
```

Side stage callable at any point: `SESSION_WRAP`.

## Status → trigger prompt map

| STATE status      | Set by                                   | Next prompt to run                          | Notes                                            |
|-------------------|------------------------------------------|---------------------------------------------|--------------------------------------------------|
| INIT              | prompts/meta/init-project.md             | prompts/planning/charter.md                 | One-time per project                             |
| CHARTER           | prompts/planning/charter.md              | prompts/discovery/understand-codebase.md    | Or planning/brainstorm; trivial/small work uses a tier variant (small-change/feature-add), which needs no discovery |
| DISCOVERY         | prompts/discovery/understand-codebase.md | prompts/planning/plan-create.md             | Required before PLAN_DRAFT                        |
| PLAN_DRAFT        | prompts/planning/plan-create.md          | prompts/planning/plan-review.md             |                                                  |
| PLAN_REVIEWED     | prompts/planning/plan-review.md          | prompts/planning/plan-redteam.md            | Run on a different LLM if possible               |
| PLAN_REDTEAMED    | prompts/planning/plan-redteam.md         | prompts/planning/plan-revise.md             |                                                  |
| PLAN_IN_REVIEW    | prompts/planning/plan-revise.md          | human gate → PLAN_APPROVED                  | Optionally planning/plan-cross-analyze first     |
| PLAN_APPROVED     | human (flips plan `status: approved`)    | prompts/execution/phase-execute.md          | One phase per invocation                         |
| PHASE_IMPLEMENTED | prompts/execution/phase-execute.md       | prompts/review/code-review.md               | Optionally review/quant-validation in parallel   |
| PHASE_REVIEWED    | prompts/review/code-review.md            | prompts/review/review-address.md            |                                                  |
| PHASE_ADDRESSED   | prompts/review/review-address.md         | prompts/review/verify.md                    |                                                  |
| PHASE_VERIFIED    | prompts/review/verify.md                 | prompts/operations/integrate.md             | Loop back to review-address if unresolved        |
| INTEGRATED        | prompts/operations/integrate.md          | next phase (PLAN_APPROVED) or DONE          |                                                  |
| DONE              | prompts/operations/integrate.md          | pick next brief (new CHARTER cycle)         | Plan complete                                    |
| SESSION_WRAP      | prompts/meta/session-wrap.md             | resume per STATE `next_action`              | Callable any time; run before clearing context   |

## Off-workflow prompts

| When                                | Prompt                              |
|-------------------------------------|-------------------------------------|
| Don't know which status you're in   | prompts/meta/route.md               |
| Explore the solution space pre-plan | prompts/planning/brainstorm.md      |
| Merge another engineer's revisions  | prompts/planning/plan-cross-analyze.md |

## Tier variants

- **patch**: skip PLAN_DRAFT through PLAN_IN_REVIEW. Use prompts/execution/small-change.md.
- **feature**: lightweight single-phase plan via prompts/execution/feature-add.md. Skip redteam unless invoked.
- **component / project**: full workflow.

## Artifact ownership per status

| Status            | Reads                                         | Writes                                       |
|-------------------|-----------------------------------------------|----------------------------------------------|
| CHARTER           | BRIEF or freeform problem                     | PROJECT.md                                   |
| DISCOVERY         | codebase, PROJECT.md                           | notes/codebase-map-<date>.md, JOURNAL.md     |
| PLAN_DRAFT        | brief, PROJECT.md, plans/, FOLLOWUPS.md       | plans/NNN-<slug>.plan.md (draft)             |
| PLAN_REVIEWED     | draft plan, schemas                           | reviews/NNN-<slug>.review.md                 |
| PLAN_REDTEAMED    | draft plan, review                            | reviews/NNN-<slug>.redteam.md                |
| PLAN_IN_REVIEW    | draft, review, redteam                        | plans/NNN-<slug>.plan.md (in-review)         |
| PHASE_IMPLEMENTED | approved plan, current phase                  | code, STATE.md, JOURNAL.md, FOLLOWUPS.md     |
| PHASE_REVIEWED    | plan phase, git diff                          | reviews/NNN-<slug>-phase-<n>.code-review.md  |
| PHASE_ADDRESSED   | review findings                               | code, FOLLOWUPS.md, DECISIONS.md             |
| PHASE_VERIFIED    | findings, new diff                            | reviews/NNN-<slug>-phase-<n>.verify.md       |
| INTEGRATED        | branch state                                  | merge, tag, STATE.md, plans/INDEX.md         |
| SESSION_WRAP      | session activity                              | STATE.md, JOURNAL.md                         |

## Status gates (human-only)

- Plan moves from `in-review` → `approved` ONLY by human action. When the human approves, they flip the plan front matter to `status: approved` **and** set `STATE.status: PLAN_APPROVED` (no prompt makes this transition for the first phase; for later phases `integrate` sets `PLAN_APPROVED`).
- phase-execute cannot start unless plan `status: approved`.
- integrate cannot complete unless verify shows all must-fix resolved (STATE `PHASE_VERIFIED`).

## Project layout this kit assumes

```
project/
├── .ai/
│   ├── kit/                 # this repo, submoduled or symlinked
│   ├── overrides/           # project-specific prompt overrides
│   ├── PROJECT.md
│   ├── STATE.md
│   ├── JOURNAL.md
│   ├── DECISIONS.md
│   ├── FOLLOWUPS.md
│   ├── CONVENTIONS.md       # extends kit/CONVENTIONS.md
│   ├── notes/
│   │   └── codebase-map-<date>.md
│   ├── briefs/
│   │   └── NNN-<slug>.brief.md
│   ├── plans/
│   │   ├── INDEX.md         # generated
│   │   └── NNN-<slug>.plan.md
│   └── reviews/
│       ├── NNN-<slug>.review.md
│       ├── NNN-<slug>.redteam.md
│       └── NNN-<slug>-phase-<n>.code-review.md
```

Prompt resolution: `.ai/overrides/<path>` first, then `.ai/kit/<path>`.
