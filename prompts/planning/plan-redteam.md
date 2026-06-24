<!--
id: planning/plan-redteam
version: 0.1.0
purpose: Adversarial review of a draft plan, ideally on a different model than plan-review
inputs:
  - plan_path
  - review_path
outputs:
  - .ai/reviews/<plan-id>.redteam.md
  - advanced STATE.md status (PLAN_REDTEAMED)
-->

{{> _partials/preamble-orient }}

## Task
Adversarially review the draft plan and the existing review. Run on a different LLM than `plan-review` if possible. Produce a redteam file with `review_type: plan-redteam` matching `schemas/review.md`.

## User must provide
- **plan_path**: path to the draft plan (`.ai/plans/<plan-id>.plan.md`).
- **review_path**: path to the existing review (`.ai/reviews/<plan-id>.review.md`).

## AI must do
1. Read the plan, the existing review, the brief, the codebase map, and `PROJECT.md`.
2. Attack the plan through these adversarial lenses:
   - **Hidden assumptions** — what does the plan assume that it never states?
   - **Failure modes** — what breaks if the world differs slightly from the happy path?
   - **Latent scope creep** — which phases will balloon when actually implemented?
   - **Research validity** (if quant/research work) — can the experiment actually answer the question? Lookahead, leakage, multiple testing?
   - **Under-specified acceptance** — which acceptance criteria are not genuinely testable?
   - **Cross-plan conflict** — interactions with other active plans the first review missed.
   - **Reversibility** — what does this plan make hard to undo?
3. Note findings the prior review missed. Duplicating a prior-review finding is fine — agreement elevates its severity.
4. Write the redteam file. Do not modify the plan itself.
5. Advance STATE: `status: PLAN_REDTEAMED`, `next_action: planning/plan-revise`, `last_prompt: planning/plan-redteam`, `last_updated` (today).

## Output format
Write to `.ai/reviews/<plan-id>.redteam.md` following `schemas/review.md` with `review_type: plan-redteam` (Blocking / Recommended / Nits / Questions for human / Approved as-is).

## Constraints
- Be concrete and cite the phase or section. No vague "could be stronger."
- Do not rewrite the plan. Revision is `plan-revise`'s job.
- Token-aware: imperative findings, no flattery.

{{> _partials/postamble-wrap }}
