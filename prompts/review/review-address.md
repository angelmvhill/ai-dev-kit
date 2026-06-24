<!--
id: review/review-address
version: 0.1.0
purpose: Address MUST-FIX and accepted SHOULD-FIX findings from code review
inputs:
  - plan_id
  - phase_number
  - review_path
outputs:
  - code changes addressing findings
  - .ai/FOLLOWUPS.md updates for deferred items
-->

{{> _partials/preamble-orient }}

## Task
Address findings from a code review of Phase **{{PHASE_NUMBER}}** of plan **{{PLAN_ID}}**.

## User must provide
- **plan_id**, **phase_number**, **review_path**.

## Rules of address
1. Only files referenced in the review findings may be modified.
2. No new code beyond what the findings require.
3. Any **new issue discovered** while addressing a finding is **appended to the review file as a new finding**, not silently fixed.
4. Deferred items (SHOULD-FIX you are not fixing now, plus anything classified as defer) append to `.ai/FOLLOWUPS.md` with: source plan/phase, finding ref, severity, reason for deferral.
5. Tests are deliverables. Update or add tests to cover any behavior change. Do not weaken existing assertions.

## AI must do
1. Read the review file, the plan's phase section, and conventions.
2. For each finding, decide one of:
   - **FIX** — apply the change.
   - **DEFER** — append to FOLLOWUPS with reason.
   - **DISPUTE** — disagree with the finding. Write a one-paragraph rebuttal and stop on that finding; the user resolves.
3. Apply FIXes. Confirm scope via `git diff --name-only` — only review-referenced files should be touched.
4. Run the phase's verification commands. All previously passing tests must still pass.
5. Update the results file (if the plan specifies one) with the new evidence.
6. Advance STATE: `status: PHASE_ADDRESSED`, `next_action: review/verify`, `last_prompt: review/review-address`, `last_updated` (today). (This is the STATE workflow cursor; do not flip the *plan's* phase status — `verify` does that.) **Exception:** if any finding is left in DISPUTE awaiting the user, do not advance — leave `status: PHASE_REVIEWED` and set `next_action` to the user decision needed.

## Output format
1. **Address ledger** — table: `finding | FIX/DEFER/DISPUTE | summary`.
2. **Code changes** — file list with what changed per file.
3. **FOLLOWUPS additions** — bullet list.
4. **Disputes** — paragraphs.
5. **New findings discovered** — appended to review file; list them here too.
6. **Verification** — pass/fail of phase checks.
7. **Next step** — `review/verify`.

## Constraints
- No drift. If you want to refactor something not flagged, append to FOLLOWUPS instead.
- Never silently change behavior outside the findings.
- Do not flip phase status. `verify` does that.

{{> _partials/postamble-wrap }}
