---
id: planning/charter
version: 0.1.0
purpose: Turn a brief or problem statement into a PROJECT.md charter
inputs: [BRIEF or freeform problem statement]
outputs: [.ai/PROJECT.md]
next_stage: DISCOVERY
---

{{> _partials/orient }}

## Task

Produce `.ai/PROJECT.md` following the schema in `.ai/kit/schemas/project.md`.

Input: {{INPUT}}

Steps:
1. Extract problem, goal/hypothesis, success criteria, scope, out-of-scope, references.
2. For research projects, frame the goal as a hypothesis with falsifiability conditions.
3. If anything in the input is ambiguous, ASK the human before writing. Do not invent.
4. Write `.ai/PROJECT.md` conforming to the schema.

{{> _partials/exit }}
