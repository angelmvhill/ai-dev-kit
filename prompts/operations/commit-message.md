---
id: operations/commit-message
version: 0.1.0
purpose: Generate a conventional commit message
inputs: [diff, plan id, phase]
outputs: [commit message string]
next_stage: (no change)
---

## Task

Produce a commit message in this shape:

```
<type>(<scope>): <subject>

Plan: {{PLAN_ID}} / Phase {{PHASE_NUMBER}}
- <change 1>
- <change 2>

Refs: <issue links if any>
```

Types: feat, fix, refactor, test, docs, chore, exp (for experiments).
Subject: imperative, <72 chars.
