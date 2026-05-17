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
2. Map `status` → next prompt using the canonical workflow:
   - `CHARTER` → write a brief, then `planning/brainstorm` (if exploratory) or `planning/plan-create`.
   - `PLAN_DRAFT` → `planning/plan-review`.
   - `PLAN_REVIEWED` → `planning/plan-redteam` (different LLM if possible).
   - `PLAN_REDTEAMED` → `planning/plan-revise`.
   - `PLAN_IN_REVIEW` → human gate (user flips `status: approved`).
   - `PLAN_APPROVED` → `execution/phase-execute` for next pending phase.
   - `PHASE_IMPLEMENTED` → `review/code-review`.
   - `PHASE_REVIEWED` → `review/review-address`.
   - `PHASE_ADDRESSED` → `review/verify`.
   - `PHASE_VERIFIED` → `operations/integrate`.
   - `INTEGRATED` → next phase or `PLAN_APPROVED` if more phases remain, else back to `CHARTER`.
3. If `user_intent` conflicts with `status`, surface the conflict and ask which path to take.

## Output format
- One-line current state summary.
- Recommended next prompt (path).
- 1-sentence reasoning.
- If conflict: the question to resolve.

## Constraints
- Do not execute the recommended prompt. Just recommend.
- Do not modify any files.
