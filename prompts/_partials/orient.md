You are operating inside an AI-assisted development workflow defined in `.ai/kit/WORKFLOW.md`. Follow it strictly.

Before doing anything else:
1. Read `.ai/STATE.md`. Confirm the current `status` matches the stage this prompt is for. If not, STOP and surface the mismatch to the human.
2. Read `.ai/PROJECT.md` for project context.
3. Read `.ai/CONVENTIONS.md` (which extends `.ai/kit/CONVENTIONS.md`). If they conflict, the project file wins.
4. Read the relevant schema(s) from `.ai/kit/schemas/` for any artifact you will produce or modify.
5. If a plan is referenced, read `.ai/plans/<active>` in full.
6. Do not perform work outside this stage's scope per WORKFLOW.md. If you find yourself needing to, STOP and document why in the appropriate review or FOLLOWUPS file.
