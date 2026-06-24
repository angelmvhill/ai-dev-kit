<!--
id: _partials/postamble-wrap
version: 0.1.0
purpose: Standard wrap-up block included at the end of every prompt
-->

## Wrap-up (always)

Before ending your turn:
1. Update `.ai/STATE.md` **per this prompt's own STATE instruction**: set `status` to exactly the value named in this prompt's steps (advancing the cursor per the map in `WORKFLOW.md`), and set `active_plan`, `current_phase`, `next_action`. Always refresh `last_prompt` and `last_updated`.
   - If this prompt advances `status` only conditionally (e.g., `verify` on PASS), honor that condition — never advance on a failing/unresolved outcome.
   - Off-workflow prompts that have no milestone (`planning/brainstorm`, `planning/plan-cross-analyze`, `review/quant-validation`) leave `status` unchanged and update only `last_prompt`, `last_updated`, and (if relevant) `next_action`.
2. Prepend a new entry at the top of `.ai/JOURNAL.md` following `schemas/journal.md` (the structured `## <timestamp> — <stage> — <plan_id>` block with Did / Learned / Decided / Next).
3. If you deferred any work, append it to `.ai/FOLLOWUPS.md` with: source plan/phase, description, severity, why deferred.
4. If you made a non-trivial decision, append it to `.ai/DECISIONS.md` per `schemas/decisions.md`.
5. End with a "Next step" line naming the exact prompt the user should run next.
