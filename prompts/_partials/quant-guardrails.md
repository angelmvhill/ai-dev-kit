<!--
id: _partials/quant-guardrails
version: 0.1.0
purpose: Quant-specific guardrails for work touching data, signals, models, or backtests
-->

## Quant guardrails

Apply these when the work touches data, signals, models, or backtests:

- **No lookahead**: features at time t may only use information available at or before t.
- **No leakage**: train/test/validation splits are temporally or logically disjoint. Cross-validation respects time order.
- **Sample selection**: document any universe filtering. Survivorship bias is a defect.
- **Reproducibility**: any randomness uses a seed recorded in the experiment config. Data versions referenced explicitly.
- **Statistical claims**: effect sizes alongside p-values. Disclose multiple-testing burden.
- **Production vs research separation**: production code must not depend on research-only artifacts (notebooks, dev data dumps).

If any of these are at risk, raise it explicitly before proceeding.
