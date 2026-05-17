# Workflow

This kit implements a prompt-driven state machine for AI-assisted development. Every workflow stage is triggered by exactly one prompt template. Each prompt loads context, performs a stage's work, and advances state via STATE.md.

## State machine

```
CHARTER → DISCOVERY → PLAN → PLAN_REVIEW → PLAN_REDTEAM → PLAN_REVISE
    → EXECUTE → CODE_REVIEW → REVIEW_ADDRESS → VERIFY → INTEGRATE
    → (next phase: EXECUTE) or DONE
```

Side stage callable at any point: SESSION_WRAP.

## Stage → prompt map

| Stage          | Trigger prompt                              |
|----------------|---------------------------------------------|
| CHARTER        | prompts/planning/charter.md                 |
| DISCOVERY      | prompts/discovery/understand-codebase.md    |
| PLAN           | prompts/planning/plan-create.md             |
| PLAN_REVIEW    | prompts/planning/plan-review.md             |
| PLAN_REDTEAM   | prompts/planning/plan-redteam.md            |
| PLAN_REVISE    | prompts/planning/plan-revise.md             |
| EXECUTE        | prompts/execution/phase-execute.md          |
| CODE_REVIEW    | prompts/review/code-review.md               |
| REVIEW_ADDRESS | prompts/review/review-address.md            |
| VERIFY         | prompts/review/verify.md                    |
| INTEGRATE      | prompts/operations/integrate.md             |
| SESSION_WRAP   | prompts/meta/session-wrap.md                |

## Tier variants

- **patch**: skip PLAN through PLAN_REVISE. Use prompts/execution/small-change.md.
- **feature**: lightweight single-phase plan via prompts/execution/feature-add.md. Skip redteam unless invoked.
- **component / project**: full workflow.

## Artifact ownership per stage

| Stage          | Reads                                         | Writes                                  |
|----------------|-----------------------------------------------|-----------------------------------------|
| CHARTER        | BRIEF or freeform problem                     | PROJECT.md                              |
| DISCOVERY      | codebase, PROJECT.md                          | JOURNAL.md                              |
| PLAN           | brief, PROJECT.md, plans/, FOLLOWUPS.md       | plans/NNN-*.md (draft)                  |
| PLAN_REVIEW    | draft plan, schemas                           | plans/NNN-*.review.md                   |
| PLAN_REDTEAM   | draft plan, review                            | plans/NNN-*.redteam.md                  |
| PLAN_REVISE    | draft, review, redteam                        | plans/NNN-*.md (in-review)              |
| EXECUTE        | approved plan, current phase                  | code, STATE.md, JOURNAL.md              |
| CODE_REVIEW    | plan phase, git diff                          | plans/NNN-*.review.md (code section)    |
| REVIEW_ADDRESS | review findings                               | code, FOLLOWUPS.md, DECISIONS.md        |
| VERIFY         | findings, new diff                            | review file (resolved markers)          |
| INTEGRATE      | branch state                                  | merge, tag, STATE.md, plans/INDEX.md    |
| SESSION_WRAP   | session activity                              | STATE.md, JOURNAL.md                    |

## Status gates (human-only)

- Plan moves from `in-review` → `approved` ONLY by human action.
- EXECUTE cannot start unless plan `status: approved`.
- INTEGRATE cannot complete unless VERIFY shows all must-fix resolved.

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
│   └── plans/
│       ├── INDEX.md         # generated
│       ├── 001-<slug>.brief.md
│       ├── 001-<slug>.md
│       ├── 001-<slug>.review.md
│       └── 001-<slug>.redteam.md
```

Prompt resolution: `.ai/overrides/<path>` first, then `.ai/kit/<path>`.
