---
id: execution/feature-add
version: 0.1.0
purpose: Tier-feature — lightweight single-phase plan + execute
inputs: [BRIEF (lightweight), PROJECT.md]
outputs: [single-phase plan + implementation]
next_stage: CODE_REVIEW
---

{{> _partials/orient }}
{{> _partials/conventions-reminder }}

## Task

Implement a small feature with a single-phase plan.

Steps:
1. Read the brief.
2. Create `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md` with `tier: feature`, `total_phases: 1`. Skip plan-review/redteam unless human invokes them.
3. Present `files_allowed` and acceptance criteria to the human. Wait for confirmation BEFORE implementing.
4. Once confirmed, human sets `status: approved`.
5. Implement on `phase/{{PLAN_ID}}-1-{{SLUG}}`.
6. Validate.

{{> _partials/exit }}
