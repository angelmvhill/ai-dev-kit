---
id: review/review-address
version: 0.1.0
purpose: Address findings from review on the same phase branch
inputs: [review file, code]
outputs: [code changes, updated review file, FOLLOWUPS/DECISIONS updates]
next_stage: VERIFY
---

{{> _partials/orient }}
{{> _partials/conventions-reminder }}

## Task

Address review findings on the current phase branch.

Categorization (do this first, before any code change):
- **must-fix** — Blocking findings. Address now.
- **should-fix** — Recommended. Address if <30 min each, else defer.
- **nit** — Optional. Address only if trivially fast.
- **defer** — Move to `.ai/FOLLOWUPS.md` with reference to this plan/phase.
- **reject** — Append rationale to `.ai/DECISIONS.md`; mark in review file.

Rules while addressing:
1. Touch ONLY files referenced in the findings. Strict deviation-prevention for the address pass.
2. No refactoring, no new code beyond what findings require.
3. Any NEW issue discovered while addressing is appended to the review file as a new finding — do not silently fix.

For each finding addressed, mark it `[x]` in the review file with a one-line note on the fix.

{{> _partials/exit }}
