---
id: planning/plan-review
version: 0.1.0
purpose: Structural review of a draft dev plan
inputs: [draft plan, brief, kit schemas]
outputs: [.ai/plans/NNN-<slug>.review.md with review_type: plan]
next_stage: PLAN_REDTEAM
---

{{> _partials/orient }}

## Task

Review `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md` against the brief and the schema. Produce `.ai/plans/{{PLAN_ID}}-{{SLUG}}.review.md` per `.ai/kit/schemas/review.md` with `review_type: plan`.

Check:
1. **Brief coverage** — every acceptance criterion in the brief is addressed by a phase.
2. **Schema conformance** — front matter complete, required sections present.
3. **Phase quality** — each phase has files_allowed, testable acceptance, validation.
4. **Scope clarity** — out_of_scope explicit; phase boundaries don't bleed.
5. **Dependencies** — depends_on and modules_touched honest; overlaps surfaced.
6. **Quant guardrails** — lookahead, leakage, sample selection addressed where relevant.
7. **Decomposition** — no hand-waved phases.

Emit findings in standard review shape. Set `verdict`.

Do not modify the plan. Review only.

{{> _partials/exit }}
