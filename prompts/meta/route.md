---
id: meta/route
version: 0.1.0
purpose: Help the human pick the right prompt for the current situation
inputs: [human intent]
outputs: [recommended prompt + slot values]
next_stage: (depends)
---

## Task

The human will describe what they want to do. Recommend the correct kit prompt.

Routing:
1. Read `.ai/STATE.md` for current stage.
2. Read the intent: "{{INTENT}}".
3. Match against the state machine in `.ai/kit/WORKFLOW.md`.
4. Recommend ONE prompt; list the slot values the human must provide.

If the intent skips required stages (e.g., executing without an approved plan), call it out before recommending.

If the intent sounds like a small change, recommend `execution/small-change.md` and verify it qualifies.
