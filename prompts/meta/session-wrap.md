---
id: meta/session-wrap
version: 0.1.0
purpose: Force a clean handoff before clearing context
inputs: [current session state]
outputs: [updated STATE.md, JOURNAL.md entry]
next_stage: (no change)
---

{{> _partials/orient }}

## Task

Wrap this session for handoff.

Steps:
1. Summarize what was done in 3-7 bullets.
2. State the current stage and what the next prompt should be.
3. Update `.ai/STATE.md`.
4. Append a journal entry per the schema.
5. List blockers explicitly. If any decision was deferred, name what's needed to unblock.

This is the only safe way to end a session. Always run before clearing context.
