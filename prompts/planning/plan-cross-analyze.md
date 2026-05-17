<!--
id: planning/plan-cross-analyze
version: 0.1.0
purpose: Compare another engineer's plan revisions against your own and merge novel/additive ideas
inputs:
  - own_plan_path
  - other_plan_path
  - other_engineer_context (optional, free-text — e.g., "had codebase access")
outputs:
  - .ai/reviews/<plan-id>.cross-analysis.md
  - updated own_plan (optional, if user approves merge)
-->

{{> _partials/preamble-orient }}

## Task
Another engineer (different LLM or different session) revised the same plan. Compare their version against yours. Classify every difference, then produce an updated plan that merges the novel and additive ideas while rejecting the unnecessary and repetitive ones.

## User must provide
- **own_plan_path**: your current revised plan.
- **other_plan_path**: the other engineer's plan.
- **other_engineer_context** (optional but useful): anything that affects how to weight their suggestions (e.g., "had codebase access," "ran static analysis," "used different model").

## AI must do
1. Read both plans, the brief, and the codebase map.
2. Diff the two plans **semantically**, not textually. Group differences by phase and by category (architecture, contract, invariant, test, scope-lock, ordering, risk).
3. For each difference, classify as exactly one of:
   - **UNNECESSARY** — adds churn without clear value.
   - **REPETITIVE** — same idea as something already in your plan, possibly worded differently.
   - **ADDITIVE** — compatible with your plan and strengthens it (e.g., extra test case, missed invariant).
   - **NOVEL** — a genuinely new idea or correction your plan missed (e.g., a constraint, a hidden dependency, a different module boundary).
   - **CONFLICTING** — directly contradicts your plan. Surface and require user decision.
4. If `other_engineer_context` suggests the other engineer had stronger ground truth (codebase access, static analysis, runtime data), weight NOVEL and CONFLICTING items toward acceptance. Be honest about uncertainty.
5. Produce the cross-analysis report **before** modifying anything.
6. Ask the user to approve the merge set (default: all NOVEL + ADDITIVE).
7. On approval, produce the updated plan with a new changelog entry citing this cross-analysis.

## Output format
Write to `.ai/reviews/<plan-id>.cross-analysis.md`:
```markdown
# Cross-analysis: <plan-id>
Date: <yyyy-mm-dd>
Other engineer context: <free-text>

## Classification table
| # | Phase | Category | Their suggestion | Classification | Reason |
|---|---|---|---|---|---|

## Conflicts requiring user decision
1. ...

## Proposed merge set
- ADDITIVE: <list>
- NOVEL: <list>
- (UNNECESSARY/REPETITIVE excluded)

## Recommended action
<one paragraph>
```

## Constraints
- Do not auto-merge. Always present the classification first.
- Be honest if their plan is better in places — the goal is the strongest plan, not yours winning.
- If you cannot tell whether something is NOVEL or CONFLICTING because it depends on facts you can't verify, mark it as CONFLICTING and ask.
- Lost-detail check applies: nothing from either prior version vanishes silently after merge.

{{> _partials/postamble-wrap }}
