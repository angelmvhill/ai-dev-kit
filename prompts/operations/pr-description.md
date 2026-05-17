---
id: operations/pr-description
version: 0.1.0
purpose: Generate a PR description tied to plan/phase
inputs: [plan, phase, diff, review]
outputs: [PR description markdown]
next_stage: (no change)
---

## Task

Produce a PR description:

```
## Summary
<one paragraph>

## Plan reference
- Plan: `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md`
- Phase: {{PHASE_NUMBER}} of {{TOTAL_PHASES}}

## Acceptance criteria
- [x] <criterion 1>
- [x] <criterion 2>

## Validation
<command output or pointer>

## Review summary
- Findings: <n blocking, n recommended, n addressed, n deferred>
- Deferred → FOLLOWUPS: <list>
```
