# Followups

Deferred items. Read by `plan-create` when scaffolding new plans. Appended by `review-address`, `phase-execute`, `plan-revise` whenever an issue is identified but not fixed this round.

## Entry schema

Each entry uses this structure:

```
### YYYY-MM-DD — <one-line summary>
- source: <plan-id>/phase-<n> or <prompt-id>
- severity: must-fix | should-fix | nit
- description: <what the issue is and why it was deferred>
- proposed action: fold-into-next-plan | open-issue | discard
- status: open | adopted-into-<plan-id> | discarded
```

## Open

(none yet)

## Closed

(none yet)
