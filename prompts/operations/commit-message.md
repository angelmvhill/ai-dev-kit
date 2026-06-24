<!--
id: operations/commit-message
version: 0.1.0
purpose: Generate a conventional commit message tied to a plan/phase
inputs:
  - plan_id
  - phase_number
outputs:
  - commit message string (no STATE change)
-->

## Task
Produce a commit message in this shape:

```
<type>(<scope>): <subject>

Plan: {{PLAN_ID}} / Phase {{PHASE_NUMBER}}
- <change 1>
- <change 2>

Refs: <issue links if any>
```

- **Types**: feat, fix, refactor, test, docs, chore, exp (for experiments).
- **Subject**: imperative mood, under 72 characters.

## Constraints
- This is a generator utility: it does not modify files or advance STATE.
- Use the exact plan id and phase number provided. Do not invent scope or refs.
