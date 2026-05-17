---
id: execution/small-change
version: 0.1.0
purpose: Tier-patch — small contained change, no dev plan
inputs: [human description]
outputs: [code change, JOURNAL entry]
next_stage: CODE_REVIEW (lightweight) or INTEGRATE
---

{{> _partials/orient }}
{{> _partials/conventions-reminder }}

## Task

Make a small contained change:
{{CHANGE_DESCRIPTION}}

Rules:
1. State the file list before making changes.
2. If the change requires >50 lines or >2 files: STOP. Recommend escalating to feature-add or a full plan.
3. Run relevant tests.
4. No new dependencies, no refactors not strictly required.

{{> _partials/exit }}
