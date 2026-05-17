<!--
id: review/verify
version: 0.1.0
purpose: Confirm that each MUST-FIX finding from the code review is resolved
inputs:
  - plan_id
  - phase_number
  - review_path
outputs:
  - .ai/reviews/<plan-id>-phase-<n>.verify.md
  - STATE.md status advance on PASS
-->

{{> _partials/preamble-orient }}

## Task
Re-review only the deltas since `review/code-review`. Confirm that each MUST-FIX is resolved, accepted SHOULD-FIXes are resolved or properly deferred, and no new regressions were introduced.

## User must provide
- **plan_id**, **phase_number**, **review_path**.

## AI must do
1. Read the original code review and the address ledger.
2. Run `git diff` since the address commit started.
3. For each MUST-FIX, check:
   - The change exists in the diff.
   - It actually resolves the finding (not just renames or comments).
   - No new behavior was introduced beyond what was needed.
4. For each accepted SHOULD-FIX, check the same.
5. Run the phase's verification commands. Confirm zero new failures.
6. Cross-check `.ai/FOLLOWUPS.md` for deferred items — each must reference the original finding.

## Output format
Write to `.ai/reviews/<plan-id>-phase-<phase_number>.verify.md`:
```markdown
# Verify: <plan-id> phase <n>
Date: <yyyy-mm-dd>

## Resolution table
| Finding | Severity | Resolved? | Evidence |
|---|---|---|---|

## Verification commands
- <cmd>: PASS/FAIL
- ...

## Verdict
PASS | UNRESOLVED — loop back to review-address.
```

If PASS, advance STATE.md `status` to `PHASE_VERIFIED` and set phase status to `done` in the plan front matter.

## Constraints
- Be strict. "Looks resolved" is not a verdict. Cite diff lines.
- Never advance status on UNRESOLVED.
- Do not modify code. This is a check, not a fix.

{{> _partials/postamble-wrap }}
