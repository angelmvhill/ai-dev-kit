---
id: execution/phase-execute
version: 0.1.0
purpose: Execute one phase of an approved plan
inputs: [approved plan, current phase number]
outputs: [code on phase branch, updated STATE/JOURNAL]
next_stage: CODE_REVIEW
---

{{> _partials/orient }}
{{> _partials/conventions-reminder }}
{{> _partials/quant-guardrails }}

## Task

Execute Phase {{PHASE_NUMBER}} of `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md`.

Pre-flight contract (verify ALL before writing code):
1. Plan `status: approved`. If not, ABORT.
2. Phase status is `pending` or `active`. If `done`, ABORT.
3. The phase scope is `files_allowed` ∪ plan `modules_touched`. You may not modify any file outside this set.
4. Restate the phase's acceptance criteria and validation command in your own words. If unclear, ASK.

If at any point you believe a file outside scope must change: STOP. Document why in `.ai/plans/{{PLAN_ID}}-{{SLUG}}.review.md` under a "Scope-questions" section. End the session.

Steps:
1. Create or check out branch `phase/{{PLAN_ID}}-{{PHASE_NUMBER}}-{{SLUG}}`.
2. Implement changes, file by file, within scope.
3. Run the validation command. Capture output.
4. Update plan: set phase `status: done` if all acceptance criteria pass; otherwise leave `active` and document gaps.
5. Do NOT commit. Code review runs on the working tree diff. Commits happen at INTEGRATE.

{{> _partials/exit }}
