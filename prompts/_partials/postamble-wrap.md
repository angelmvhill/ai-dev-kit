<!--
id: _partials/postamble-wrap
version: 0.1.0
purpose: Standard wrap-up block included at the end of every prompt
-->

## Wrap-up (always)

Before ending your turn:
1. Update `.ai/STATE.md`: advance `status`, set `active_plan`, `active_phase`, `last_prompt`, `last_updated`.
2. Append a one-line entry to `.ai/JOURNAL.md`: `YYYY-MM-DD HH:MM | <prompt-id> | <outcome>`.
3. If you deferred any work, append it to `.ai/FOLLOWUPS.md` with: source plan/phase, description, severity, why deferred.
4. End with a "Next step" line naming the exact prompt the user should run next.
