<!--
id: execution/small-change
version: 0.1.0
purpose: Tier-patch — a small, contained change with no dev plan
inputs:
  - change_description
outputs:
  - code change on a branch per project convention
  - advanced STATE.md status (PHASE_IMPLEMENTED)
  - JOURNAL entry
-->

{{> _partials/preamble-orient }}
{{> _partials/conventions-reminder }}

## Task
Make a small, contained change (tier `patch`): no plan, no phases. The change is:

{{CHANGE_DESCRIPTION}}

## Rules
1. State the exact file list before making any change.
2. If the change requires more than ~50 lines or touches more than 2 files: STOP and recommend escalating to `execution/feature-add` or the full plan flow.
3. No new dependencies. No refactors that are not strictly required by the change.
4. Tests are deliverables. Add or update tests for the behavior change; do not weaken assertions.
5. Run the project's relevant tests using its exact invocation (per the codebase map / conventions file). Do not assume `python`.
6. On success, advance STATE: `status: PHASE_IMPLEMENTED`, `next_action: review/code-review`, `last_prompt: execution/small-change`, `last_updated` (today).

## Output format
1. **What I changed** — file list with NEW/MODIFY tags.
2. **Verification** — commands run and pass/fail.
3. **Next step** — `review/code-review` (lightweight) or, for a trivial fix the convention allows, `operations/integrate`.

## Constraints
- No scope creep. Anything you notice but do not fix goes to `.ai/FOLLOWUPS.md`.
- Commits happen at integrate per `CONVENTIONS.md`, not here, unless the project convention says otherwise.

{{> _partials/postamble-wrap }}
