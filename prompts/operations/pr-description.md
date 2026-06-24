<!--
id: operations/pr-description
version: 0.1.0
purpose: Generate a PR description tied to a plan/phase
inputs:
  - plan_id
  - phase_number
outputs:
  - PR description markdown (no STATE change)
-->

## Task
Produce a PR description:

```
## Summary
<one paragraph>

## Plan reference
- Plan: `.ai/plans/{{PLAN_ID}}.plan.md`
- Phase: {{PHASE_NUMBER}} of {{TOTAL_PHASES}}

## Acceptance criteria
- [x] <criterion 1>
- [x] <criterion 2>

## Validation
<command output or pointer to results file>

## Review summary
- Findings: <n blocking, n recommended, n addressed, n deferred>
- Deferred → FOLLOWUPS: <list>
```

## Constraints
- This is a generator utility: it does not modify files or advance STATE.
- Acceptance criteria and review counts must come from the phase's review and results files, not be invented.
