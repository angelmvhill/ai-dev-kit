---
id: review/verify
version: 0.1.0
purpose: Confirm review findings are resolved
inputs: [review file, new diff]
outputs: [review file with resolved markers; STATE advanced on pass]
next_stage: INTEGRATE
---

{{> _partials/orient }}

## Task

Verify each must-fix and should-fix finding in `.ai/plans/{{PLAN_ID}}-{{SLUG}}.review.md` is resolved in the current diff.

For each finding:
- Confirm the cited issue is fixed; cite the line or commit.
- If a finding cannot be confirmed resolved: mark `unresolved` with reason.

Re-run deviation check: `python .ai/kit/scripts/deviation-check.py {{PLAN_ID}} {{PHASE_NUMBER}}`. Confirm the address pass did not itself introduce out-of-scope changes.

Outcome:
- All must-fix resolved AND no new deviations → set phase `status: done` in plan. Advance STATE to INTEGRATE.
- Otherwise → loop back to REVIEW_ADDRESS with explicit list of unresolved.

{{> _partials/exit }}
