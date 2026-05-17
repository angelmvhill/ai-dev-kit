<!--
id: meta/session-wrap
version: 0.1.0
purpose: Safely end a session — flush state, summarize, hand off to next context
inputs:
  - none (reads STATE/JOURNAL/diff)
outputs:
  - updated STATE.md
  - JOURNAL entry
  - session summary block
-->

## Task
Wrap the current session so the next session can pick up cleanly.

## AI must do
1. Read `.ai/STATE.md` and the latest `.ai/JOURNAL.md` entries (last 5).
2. Run `git status` and `git diff --stat` to see uncommitted changes.
3. Update `STATE.md` to reflect the true current position. Do not lie about status — if a phase is half-done, say so explicitly in the `## Recent activity` section. Fields to update: `status`, `active_plan`, `current_phase`, `last_updated`, `last_session`, `last_prompt`, `next_action`, `blockers`.
4. Append a multi-line JOURNAL entry: timestamp, what was done, what is in-progress, what is blocked, what to do next.
5. Identify the exact prompt the next session should run to resume — write it to STATE's `next_action`.

## Output format
A single "Session summary" block the user can paste at the start of the next session:
```
Last session: <yyyy-mm-dd hh:mm>
Status: <status>
Active plan: <plan-id>
Current phase: <n> — <status>
Uncommitted changes: <yes/no, summary>
Next prompt: <path>
Blockers: <list or "none">
Open questions for user: <bulleted, or "none">
```

## Constraints
- Never auto-commit during session-wrap. Surface uncommitted work to the user.
- Never advance `status` past actual progress.
- If git working tree is dirty in a way that doesn't match STATE, flag it loudly.
