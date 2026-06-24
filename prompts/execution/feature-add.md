<!--
id: execution/feature-add
version: 0.1.0
purpose: Tier-feature — a lightweight single-phase plan plus its execution
inputs:
  - brief_path
outputs:
  - .ai/plans/<NNN>-<slug>.plan.md (single phase)
  - code change on phase/<plan-id>-1-<slug>
  - advanced STATE.md status
-->

{{> _partials/preamble-orient }}
{{> _partials/conventions-reminder }}

## Task
Implement a small feature via a single-phase plan. Skip `plan-review` and `plan-redteam` unless the human explicitly invokes them.

## User must provide
- **brief_path**: path to the (lightweight) brief.

## AI must do
1. Read the brief, `PROJECT.md`, and the codebase map if one exists.
2. Create `.ai/plans/<NNN>-<slug>.plan.md` matching `templates/dev-plan.template.md` with `tier: feature`, `total_phases: 1`, `status: draft`.
3. Present `files_allowed` and the acceptance criteria for Phase 1 to the human. **Wait for confirmation before implementing.**
4. The human sets `status: approved` in the plan front matter (status gate is human-only).
5. Implement Phase 1 on branch `phase/<plan-id>-1-<slug>`, matching repo conventions (typed dataclasses with `slots=True`, UTC-aware timestamps, fail loudly, no raw provider/exchange dicts past normalization, no unrequested concurrency).
6. Write the Phase 1 tests as deliverables. Do not weaken assertions to fit the implementation.
7. Run the phase verification commands using the project's exact Python invocation. Verify every acceptance criterion with pass/fail evidence.
8. Advance STATE: `status: PHASE_IMPLEMENTED`, `active_plan: <NNN-slug>`, `current_phase: 1`, `next_action: review/code-review`, `last_prompt: execution/feature-add`, `last_updated` (today).

## Output format
1. **Plan** — path to the created single-phase plan.
2. **What I changed** — file list with NEW/MODIFY tags (after approval + implementation).
3. **Acceptance criteria** — table: `criterion | pass/fail | evidence`.
4. **Next step** — `review/code-review`.

## Constraints
- Do not implement before the human flips `status: approved`.
- Stay inside Phase 1's `files_allowed`. Anything else goes to `.ai/FOLLOWUPS.md`.
- If the work clearly needs more than one phase, STOP and recommend the full plan flow.

{{> _partials/postamble-wrap }}
