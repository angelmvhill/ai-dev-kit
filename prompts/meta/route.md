<!--
id: meta/route
version: 0.1.0
purpose: Inspect STATE.md and recommend the next prompt to run
inputs:
  - user_intent (free-text, optional)
outputs:
  - prompt recommendation + reasoning
-->

## Task
Read `.ai/STATE.md` and tell the user which prompt they should run next.

## User must provide
- **user_intent** (optional): plain-English description of what they want to do. If absent, infer from STATE.

## AI must do
1. Read `.ai/STATE.md`, `.ai/FOLLOWUPS.md`, and the active plan if one exists.
2. Map `status` → next prompt using the canonical workflow in `WORKFLOW.md`:
   - `INIT` → `planning/charter`.
   - `CHARTER` → `discovery/understand-codebase` (or `planning/brainstorm` if exploratory). For trivial/patch work use `execution/small-change`, and for a small feature use `execution/feature-add` — these tier variants skip discovery and the full plan flow.
   - `DISCOVERY` → write a brief, then `planning/plan-create`.
   - `PLAN_DRAFT` → `planning/plan-review`.
   - `PLAN_REVIEWED` → `planning/plan-redteam` (different LLM if possible).
   - `PLAN_REDTEAMED` → `planning/plan-revise`.
   - `PLAN_IN_REVIEW` → human gate (user flips plan `status: approved` and sets `STATE.status: PLAN_APPROVED`); optionally `planning/plan-cross-analyze` first.
   - `PLAN_APPROVED` → `execution/phase-execute` for next pending phase.
   - `PHASE_IMPLEMENTED` → `review/code-review` (optionally `review/quant-validation` in parallel for quant work).
   - `PHASE_REVIEWED` → `review/review-address`.
   - `PHASE_ADDRESSED` → `review/verify`.
   - `PHASE_VERIFIED` → `operations/integrate`.
   - `INTEGRATED` → `execution/phase-execute` if more phases remain (status returns to `PLAN_APPROVED`), else `DONE`.
   - `DONE` → pick the next brief (new `CHARTER` cycle).
3. For tier variants, recommend `execution/small-change` (patch) or `execution/feature-add` (feature) when the intent qualifies.
4. If `user_intent` conflicts with `status`, surface the conflict and ask which path to take.

## Output format
- One-line current state summary.
- Recommended next prompt (path).
- 1-sentence reasoning.
- If conflict: the question to resolve.

## Constraints
- Do not execute the recommended prompt. Just recommend.
- Do not modify any files.
