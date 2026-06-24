<!--
id: execution/phase-execute
version: 0.1.0
purpose: Implement exactly one phase of an approved dev plan
inputs:
  - plan_id
  - phase_number
outputs:
  - code changes on phase/<n>-<slug> branch (or current branch per project convention)
  - phase test results
  - updated .ai/STATE.md, .ai/JOURNAL.md, .ai/FOLLOWUPS.md
-->

{{> _partials/preamble-orient }}

## Task
Implement Phase **{{PHASE_NUMBER}}** of plan **{{PLAN_ID}}**. Nothing else.

## User must provide
- **plan_id**: e.g., `003-factor-ingest`.
- **phase_number**: integer.
- (Implicit) the plan must be `status: approved` in its front matter. If not, stop.

## Scope lock
Only modify files explicitly listed in Phase {{PHASE_NUMBER}}'s file list. If a file is shared with later phases, implement **only** the behavior assigned to Phase {{PHASE_NUMBER}}. Do not pull later-phase work forward. Do not opportunistically refactor.

Forbidden without explicit user approval:
- `.env`, root `data/`, generated artifacts, unrelated files
- Any file not named in this phase's scope lock
- New dependencies not specified in the plan

## AI must do
1. **Read before writing any code**, in order:
   - `.ai/plans/{{PLAN_ID}}.plan.md` (entire plan, for context)
   - The Phase {{PHASE_NUMBER}} section in particular
   - The repo's conventions file (`AGENTS.md` / `CLAUDE.md` / `.cursor/rules/*`)
   - The codebase map referenced in the plan
2. State in 2-4 sentences what you understand the phase to be, what files you will touch, and what tests you will write. Wait if the user has set up a confirmation gate; otherwise proceed.
3. Implement the phase. Match repo conventions:
   - Typed dataclasses, `slots=True` (frozen when pure data).
   - UTC-aware timestamps unless the plan documents a local-time boundary.
   - No raw provider/exchange dicts past the normalization boundary.
   - Fail loudly on invalid config / unknown runtime conditions.
   - No new concurrency unless the phase explicitly requires it.
4. Write the tests assigned by the phase. Tests are deliverables. **Do not weaken assertions to fit the implementation.** If a test fails because the implementation is wrong, fix the implementation. If a test fails because the spec is wrong, stop and surface the spec issue.
5. Use the project's exact Python invocation (`py -3.11`, `python3.11`, `uv run`, etc.) as specified in the codebase map / conventions file. Do not assume `python`.
6. Run `git diff --stat` and `git diff --name-only` before committing. Confirm only phase-scoped files were modified. If any unexpected file changed, revert only your own change and explain why it happened.
7. Run the phase-specific test/verification commands exactly as listed in the plan. If the plan specifies a results file (e.g., `tests/<...>/phase_<n>_results.md`), produce it as a markdown table with each acceptance criterion and pass/fail evidence.
8. If a test fails, determine whether it was caused by this phase. Do not stash/reset/revert unrelated user work without approval. Use only safe read-only Git commands to isolate cause. Report pre-existing failures clearly and separately from new ones.
9. Verify **every** acceptance criterion from Phase {{PHASE_NUMBER}}. Include pass/fail evidence inline in the final response and in the results file if the plan calls for one.
10. Create the phase commit **only after all required phase checks pass**, using the exact commit message specified in the phase. Do not amend or squash unless the plan says to.
11. Advance STATE: `status: PHASE_IMPLEMENTED`, `current_phase: {{PHASE_NUMBER}}`, `next_action: review/code-review`, `last_prompt: execution/phase-execute`, `last_updated` (today).
12. Stop. Do **not** proceed to the next phase.

## Output format
Final message must contain, in order:
1. **What I changed** — file list with NEW/MODIFY tags.
2. **Acceptance criteria** — table with `criterion | pass/fail | evidence`.
3. **Deviations from the plan** — any, with reason. If none, say "none."
4. **Pre-existing failures** — any test failures unrelated to this phase, with reproducer.
5. **Commit** — hash + message.
6. **Next step** — exactly `review/code-review` for this phase.

## Constraints
- Correctness and operational safety over convenience.
- No scope creep, no opportunistic refactors.
- No fake success for unimplemented workflows. If something isn't implemented, the test must fail or be marked `xfail` with a referenced FOLLOWUPS entry.
- Deviations from the plan must be highlighted in the final output with reason. Do not absorb them silently.
- Any new issue you discover that is **not** required by this phase: append to `.ai/FOLLOWUPS.md`. Do not silently fix it.

{{> _partials/postamble-wrap }}
