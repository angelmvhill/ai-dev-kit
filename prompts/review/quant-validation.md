<!--
id: review/quant-validation
version: 0.1.0
purpose: Quant-specific validation of a phase, run in parallel with code-review
inputs:
  - plan_id
  - phase_number
  - review_path
outputs:
  - quant-validation findings appended to the phase code-review file
-->

{{> _partials/preamble-orient }}
{{> _partials/quant-guardrails }}

## Task
Validate the Phase **{{PHASE_NUMBER}}** implementation of plan **{{PLAN_ID}}** for quant correctness specifically. Style and architecture are out of scope here — `code-review` owns those.

## User must provide
- **plan_id**, **phase_number**.
- **review_path**: the phase code-review file to append to (`.ai/reviews/<plan-id>-phase-<n>.code-review.md`).

## AI must do
1. Read the plan's phase section, the diff, and any experiment outputs the phase produced.
2. Check:
   - **Lookahead** — every feature/signal/label uses as-of-t information only.
   - **Leakage** — train/test/validation splits disjoint in time and identity.
   - **Sample selection** — universe construction documented; no survivorship bias.
   - **Reproducibility** — seeds set; data version referenced; configs captured.
   - **Statistical hygiene** — effect sizes alongside p-values; multiple-testing burden disclosed.
   - **Backtest realism** — costs, slippage, capacity, borrow/short constraints where applicable.
   - **Production / research separation** — production code free of research-only artifacts.
3. Classify each finding MUST-FIX / SHOULD-FIX / NIT, consistent with `code-review`.

## Output format
Append a `## Quant validation` section to `review_path` with `review_type: quant-validation`, listing findings with severity and file:line evidence. Do not modify code.

## Constraints
- Cite file:line for every finding. A clean validation is a valid outcome.
- Do not duplicate pure style/architecture findings already owned by `code-review`.
- Do not apply fixes. `review/review-address` does that.
- Do **not** advance `STATE.status` — this runs in parallel with `code-review`, which owns the `PHASE_REVIEWED` milestone. Update only `last_prompt` and `last_updated`.

{{> _partials/postamble-wrap }}
