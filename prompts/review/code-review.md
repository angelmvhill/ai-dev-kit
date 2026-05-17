<!--
id: review/code-review
version: 0.1.0
purpose: Review the code changes produced by phase-execute against the plan and repo conventions
inputs:
  - plan_id
  - phase_number
outputs:
  - .ai/reviews/<plan-id>-phase-<n>.code-review.md
-->

{{> _partials/preamble-orient }}

## Task
Review the code changes from Phase **{{PHASE_NUMBER}}** of plan **{{PLAN_ID}}**. Produce a findings list with severity levels. Do not modify code.

## User must provide
- **plan_id**, **phase_number**.

## AI must do
1. Read the plan's phase section, the codebase map, and conventions file.
2. Run:
   - `git diff <merge-base>..HEAD --stat`
   - `git diff <merge-base>..HEAD` (or per file if too large)
3. For each modified file, evaluate against:
   - **Scope**: was anything modified outside the phase's scope lock?
   - **Plan adherence**: does the change implement what the phase specified?
   - **Conventions**: dataclass usage, slots/frozen, UTC timestamps, no raw provider dicts past normalization, no silent failure.
   - **Ownership**: state owners not doing I/O; normalizers as single raw boundary; orchestration in engine/task layers.
   - **Invariants**: do the changes preserve invariants stated in the plan?
   - **Tests**: tests assigned by the phase exist, cover happy path / boundary / malformed / ordering / idempotency, and assertions are not weakened.
   - **Error handling**: failure paths raise / log / reject / mark-stale per the plan, not silently continue.
   - **Quant guardrails** (if applicable): no lookahead, no leakage, time boundaries explicit.
4. Classify each finding:
   - **MUST-FIX** — blocks acceptance.
   - **SHOULD-FIX** — worth fixing this phase if cheap, else defer to FOLLOWUPS.
   - **NIT** — style, naming, comment. Optional.
5. Note any **deviations from the plan** that the executor flagged or that you discovered.

## Output format
Write to `.ai/reviews/<plan-id>-phase-<phase_number>.code-review.md`:
```markdown
# Code review: <plan-id> phase <n>
Date: <yyyy-mm-dd>

## Scope check
- Files modified: <list>
- Files in scope-lock: <list>
- Out-of-scope changes: <list or "none">

## Findings
### MUST-FIX
1. **<file>:<line>** — <issue>. Evidence: <quote/cite>.
### SHOULD-FIX
1. ...
### NIT
1. ...

## Deviations
- <list or "none">

## Verdict
PASS | NEEDS-ADDRESS
```

## Constraints
- Cite file:line for every finding. No vague "consider improving X."
- Do not write or apply fixes. The next prompt (`review/review-address`) does that.
- A clean review is a valid outcome. Do not invent findings to look thorough.

{{> _partials/postamble-wrap }}
