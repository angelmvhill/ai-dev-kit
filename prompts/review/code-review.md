---
id: review/code-review
version: 0.1.0
purpose: Review a phase implementation against the plan
inputs: [plan, phase, git diff]
outputs: [.ai/plans/NNN-<slug>.review.md with review_type: code]
next_stage: REVIEW_ADDRESS
---

{{> _partials/orient }}
{{> _partials/quant-guardrails }}

## Task

Review the implementation of Phase {{PHASE_NUMBER}} of `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md`.

Inputs:
- Plan and phase definition
- Git diff: `git diff $(git merge-base HEAD main)...HEAD`

MANDATORY first step — deviation check:
1. Run `python .ai/kit/scripts/deviation-check.py {{PLAN_ID}} {{PHASE_NUMBER}}`.
2. Every flagged file is an `Out-of-scope addition` finding.

Then assess against the code-review schema sections:
- **In-scope, passed** — for each acceptance criterion: how was it verified?
- **In-scope, failed** — criteria not met, with evidence.
- **Out-of-scope additions** — from deviation check.
- **Missing deliverables** — criteria not addressed at all.
- **Quality findings** — file:line, severity, issue, suggested fix.

Apply quant guardrails. Flag any lookahead, leakage, or sample-selection issues regardless of phase scope.

Append output to `.ai/plans/{{PLAN_ID}}-{{SLUG}}.review.md` with `review_type: code`. Set `verdict`.

Do not modify code. Review only.

{{> _partials/exit }}
