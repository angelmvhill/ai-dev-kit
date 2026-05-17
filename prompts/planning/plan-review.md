<!--
id: planning/plan-review
version: 0.1.0
purpose: Review a draft dev plan for completeness, correctness, and executability
inputs:
  - plan_path
outputs:
  - .ai/reviews/<plan-id>.review.md
-->

{{> _partials/preamble-orient }}

## Task
Review a draft dev plan. Decide whether it will produce **production-level code** if executed as written. If yes, approve. If no, output concrete revisions as a structured, token-aware change list.

## User must provide
- **plan_path**: path to the plan to review.

## AI must do
1. Read the plan, the brief it references, the codebase map, and `PROJECT.md`.
2. Evaluate against the rubric below. For each criterion, mark **PASS**, **WEAK**, or **FAIL** with one-sentence evidence.

### Rubric
- **Scope clarity**: Goals, Out of Scope, and Acceptance Criteria are explicit and verifiable.
- **Architectural fit**: respects existing module boundaries and ownership rules from the codebase map.
- **File-level concreteness**: every phase names real files (NEW/MODIFY) and the exact responsibility per file.
- **Contracts**: data models / APIs specified with field types and semantics. No hand-waving.
- **Invariants**: failure behavior explicit (raise / log / mark-stale / reject) per phase.
- **Tests as deliverables**: happy path, boundary, malformed input, ordering/idempotency, regression.
- **Scope lock**: each phase has a file list it may touch.
- **Determinism**: no "refactor as needed," no implicit assumptions about runtime.
- **Quant guardrails** (if quant project): no lookahead, no leakage, timezone handling explicit, timestamps UTC-aware unless boundary is documented.
- **Phase ordering**: dependencies between phases are explicit and acyclic.
- **Risks & rollback**: identified and credible.

3. Then produce one of two outputs:
   - **Approve**: if every criterion is PASS, write "APPROVED — plan is production-ready" plus a 3-bullet summary of why.
   - **Revise**: if any WEAK or FAIL, output a structured, **token-aware revision prompt** the user can hand back to the planning agent. Format as numbered list, grouped by phase, with each item phrased as a concrete instruction ("Phase 3, file `engine.py`: specify which task owns timer state").
4. Briefly explain each proposed change in **1 sentence**.
5. Confirm no key details or architecture components from the brief or prior revisions have been lost. List any that are missing.

## Output format
Write to `.ai/reviews/<plan-id>.review.md`:
```markdown
# Review: <plan-id> v<plan-version>
Reviewer: <model name>
Date: <yyyy-mm-dd>

## Rubric
| Criterion | Result | Evidence |
|---|---|---|
| ... | PASS/WEAK/FAIL | ... |

## Decision
APPROVED | NEEDS REVISION

## Revisions (if any)
1. ...
2. ...

## Per-change rationale
1. ...

## Lost-detail check
Missing from prior version: <list or "none">
```

## Constraints
- Be concrete, not stylistic. "Phase 4 doesn't specify what triggers retry" is useful. "Phase 4 could be clearer" is not.
- Token-aware: revision items in imperative voice, no preamble, no flattery.
- Do not rewrite the plan yourself — output the change list. Revision is the planner's job (next prompt).

{{> _partials/postamble-wrap }}
