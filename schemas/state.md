# STATE schema

Filename: `.ai/STATE.md`. The workflow cursor. Read this first in every session.

```markdown
---
status: <stage name from WORKFLOW.md, e.g. EXECUTE>
active_plan: <plan_id or null>
current_phase: <int or null>
last_updated: YYYY-MM-DD
last_session: <one-line description>
next_action: <one sentence>
blockers: []
---

## Recent activity
- <date>: <what happened>

## Open questions
- <if any>
```
