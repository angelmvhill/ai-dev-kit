<!--
id: operations/integrate
version: 0.1.0
purpose: Merge a verified phase into the main branch and advance the plan
inputs:
  - plan_id
  - phase_number
outputs:
  - merge commit (or PR draft) on main branch
  - STATE.md and plan front matter updated
-->

{{> _partials/preamble-orient }}

## Task
Integrate Phase **{{PHASE_NUMBER}}** of plan **{{PLAN_ID}}** into the main branch.

## Preconditions (verify before doing anything)
- Phase status is `done` in plan front matter.
- STATE.md status is `PHASE_VERIFIED`.
- No uncommitted changes outside the phase branch.

If any precondition fails, stop and report.

## AI must do
1. Confirm the user's integration convention from the conventions file: direct merge, PR-only, rebase-then-merge, etc. If unclear, ask.
2. For direct merge: fast-forward or merge commit per repo convention.
3. For PR-only: draft the PR description using the phase plan section and acceptance criteria results.
4. After integration:
   - Mark the phase as `integrated` in the plan front matter.
   - If more phases remain: set STATE `status` back to `PLAN_APPROVED`, `active_phase` to next pending.
   - If no phases remain: set STATE `status` to `CHARTER` (ready for next piece of work) and append a plan-complete entry to JOURNAL.

## Output format
- Merge/PR result with hash or PR URL.
- Updated STATE block.
- Next step: next phase number, or "plan complete — pick next brief."

## Constraints
- Never integrate without PHASE_VERIFIED.
- Never force-push without explicit user approval.
- Do not bundle multiple phases into one integration unless the plan explicitly says to.

{{> _partials/postamble-wrap }}
