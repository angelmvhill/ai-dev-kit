# Kit Conventions

These apply to every AI session that uses this kit. A project's `.ai/CONVENTIONS.md` may extend or override these.

## Branching
- One branch per phase: `phase/<plan-id>-<phase-num>-<slug>`.
- Main is always green. No direct commits to main except at integrate (`prompts/operations/integrate.md`).

## Commits
- Conventional commits with plan/phase reference (see prompts/operations/commit-message.md).
- Commits happen at integrate (`prompts/operations/integrate.md`), not during phase execution (`prompts/execution/phase-execute.md`).

## File scope
- Never modify files outside a phase's `files_allowed` ∪ plan's `modules_touched`. If a change requires it, halt and document under Scope-questions in the review file.

## Asking vs assuming
- If a slot value, file path, or acceptance criterion is ambiguous, ASK the human. Do not invent.
- If a judgment call must be made, state the call and your reasoning explicitly before acting.

## State updates
- Every session ends with STATE.md and JOURNAL.md updated. No exceptions.
- DECISIONS.md gets an entry for every non-trivial choice.

## Conflict resolution
- Project's `.ai/CONVENTIONS.md` overrides this file when they conflict.
- A prompt under `.ai/overrides/` overrides the same-path prompt under `.ai/kit/`.
