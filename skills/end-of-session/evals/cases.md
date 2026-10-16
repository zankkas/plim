# End-of-Session Evals

Run when the skill changes, or when a live session surfaces behavior these cases did not anticipate. Each case: scenario, expected behavior, forbidden behavior.

## DONE mode

1. **Scenario:** user says "done" after a session with three decisions, one already captured mid-session in the note.
   - Expected: audit the note, add nothing fabricated, classify under two minutes, reconcile the tracker item, report at planning altitude.
   - Forbidden: rewriting captured decisions, researching wiki pages at exit, committing or pushing.

2. **Scenario:** session had no linked issue.
   - Expected: record "no canonical work item" in the note; do not create an issue to justify the close.
   - Forbidden: opening a tracker item during the close.

3. **Scenario:** live tracker unreachable.
   - Expected: report work state as unverified in the close report.
   - Forbidden: copying tracker state into local files or reconstructing it from memory.

4. **Scenario:** the session's decisions include an architectural change.
   - Expected: flag or graduate it to an ADR in the spec's design.md if under two minutes.
   - Forbidden: writing a full ADR with research at exit time.

## HANDOFF mode

5. **Scenario:** user asks for a handoff with work incomplete.
   - Expected: crystallize truth files, write the bridge prompt from the reference template, mark the note as a handoff.
   - Forbidden: closing the tracker item, writing status into the compass, ending without a paste-ready bridge.

6. **Scenario:** workspace has no persona layer.
   - Expected: variant A bridge without persona embedding.
   - Forbidden: inventing decision patterns or stalling the handoff over the missing layer.

## The lightness rule

7. **Scenario:** the close would take more than a few minutes because capture was skipped all session.
   - Expected: audit writes only what is still in context, flag the rest for the next hygiene pass, deliver the report.
   - Forbidden: a long exit ritual, reconstructing forgotten reasoning from transcripts.
