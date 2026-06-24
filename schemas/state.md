# STATE schema

Filename: `.ai/STATE.md`. The workflow cursor. Read this first in every session.

```markdown
---
status: <canonical status from WORKFLOW.md: INIT|CHARTER|DISCOVERY|PLAN_DRAFT|PLAN_REVIEWED|PLAN_REDTEAMED|PLAN_IN_REVIEW|PLAN_APPROVED|PHASE_IMPLEMENTED|PHASE_REVIEWED|PHASE_ADDRESSED|PHASE_VERIFIED|INTEGRATED|DONE>
active_plan: <plan_id or null>
current_phase: <int or null>
last_updated: YYYY-MM-DD
last_session: <one-line description>
last_prompt: <prompt id that last advanced state, or null>
next_action: <one sentence>
blockers: []
kit_version: <pinned kit version, e.g. 0.2.0>
---

## Recent activity
- <date>: <what happened>

## Open questions
- <if any>
```

`status` names the milestone just completed; `WORKFLOW.md` maps it to the next prompt to run.
