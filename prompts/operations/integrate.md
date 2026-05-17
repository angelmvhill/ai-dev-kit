---
id: operations/integrate
version: 0.1.0
purpose: Merge a completed phase branch
inputs: [verified phase branch]
outputs: [merged main, tag, updated STATE.md, regenerated INDEX]
next_stage: EXECUTE (next phase) or DONE
---

{{> _partials/orient }}

## Task

Integrate the completed phase.

Pre-check:
- Phase `status: done` in plan.
- All must-fix findings resolved.
- Validation passes on the branch.

Steps:
1. Commit any uncommitted changes using the commit-message convention (see prompts/operations/commit-message.md).
2. Merge to main per project convention (PR or direct).
3. Tag if appropriate: `plan-{{PLAN_ID}}-phase-{{PHASE_NUMBER}}`.
4. Update plan front matter: `updated`, `current_phase` advanced, plan `status: done` if all phases complete.
5. Update STATE.md: status → EXECUTE for next phase, or DONE if plan complete.
6. Regenerate `.ai/plans/INDEX.md`: `python .ai/kit/scripts/plans-index.py`.

{{> _partials/exit }}
