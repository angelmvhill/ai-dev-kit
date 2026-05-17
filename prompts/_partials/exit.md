Before ending this session:

1. Update `.ai/STATE.md`:
   - `status` → next stage if exit criteria for current stage are met; otherwise leave unchanged and document the blocker
   - `active_plan`, `current_phase`, `last_updated`, `last_session`, `next_action`
   - `blockers` if any
2. Append a dated entry to `.ai/JOURNAL.md` following `.ai/kit/schemas/journal.md` (Did / Learned / Decided / Next).
3. If a non-trivial decision was made, append to `.ai/DECISIONS.md`.
4. If you produced an artifact governed by a schema, verify it conforms before exit.
5. Do not commit, push, or merge unless this stage explicitly requires it (see WORKFLOW.md artifact ownership).
