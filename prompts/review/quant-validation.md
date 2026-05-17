---
id: review/quant-validation
version: 0.1.0
purpose: Quant-specific validation, parallel to code review
inputs: [plan, phase, diff, experiment outputs]
outputs: [review file entries with review_type: quant-validation]
next_stage: REVIEW_ADDRESS
---

{{> _partials/orient }}
{{> _partials/quant-guardrails }}

## Task

Validate this implementation for quant correctness specifically. Style and architecture out of scope here.

Check:
1. **Lookahead** — every feature/signal/label uses as-of-t information only.
2. **Leakage** — train/test/validation splits disjoint in time and identity.
3. **Sample selection** — universe construction documented; no survivorship bias.
4. **Reproducibility** — seeds set; data version referenced; configs captured.
5. **Statistical hygiene** — effect sizes alongside p-values; multiple-testing burden disclosed.
6. **Backtest realism** — costs, slippage, capacity, borrow/short constraints if applicable.
7. **Production-research separation** — production code free of research-only artifacts.

Append findings to the same review file as code-review with `review_type: quant-validation`.

{{> _partials/exit }}
