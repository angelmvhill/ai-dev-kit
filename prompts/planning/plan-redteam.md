---
id: planning/plan-redteam
version: 0.1.0
purpose: Adversarial review, ideally from a different model than plan-review
inputs: [draft plan, plan-review findings]
outputs: [.ai/plans/NNN-<slug>.redteam.md]
next_stage: PLAN_REVISE
---

{{> _partials/orient }}

## Task

Adversarially review `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md` and the existing review at `.ai/plans/{{PLAN_ID}}-{{SLUG}}.review.md`. Produce `.ai/plans/{{PLAN_ID}}-{{SLUG}}.redteam.md` with `review_type: plan-redteam`.

Adversarial lenses:
1. **Hidden assumptions** — what is the plan assuming that isn't stated?
2. **Failure modes** — what breaks this if the world differs slightly?
3. **Latent scope creep** — which phases will balloon when implemented?
4. **Research validity** — can the experiment actually answer the question? Lookahead? Leakage? Multiple testing?
5. **Under-specified acceptance** — which criteria are not actually testable?
6. **Cross-plan conflict** — interactions with active plans missed by the first review.
7. **Reversibility** — what does this plan make hard to undo?

Note things the prior review missed. Duplicates with prior review are fine — they elevate severity.

{{> _partials/exit }}
