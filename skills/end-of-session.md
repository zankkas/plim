---
name: end-of-session
description: >
  End a session the right way: two exits, one light ritual. Use when the user
  says done, close the session, end here, or asks for a handoff. DONE closes
  the work. HANDOFF moves unfinished work to a fresh session or agent.
---

# End of Session

**Why:** Sessions are ephemeral. Decisions and next moves must outlive them, and the exit ritual must never become heavier than the work it protects.

## First: pick the exit

- **DONE**: the work reached its end. Reconcile and record.
- **HANDOFF**: work continues in another session or agent. Crystallize and bridge.

One question settles it: will anyone act on this work before you see it again? Yes means handoff. No means done.

## Mode: DONE

1. **Identify the canonical work item** in the tracker named by the compass. If none exists, record that. Do not create one to justify the close.
2. **Record the decision.** Prepend one entry to the session-notes file: the decision, the rejected alternative when it matters, the risk, one next action, links.
3. **Classify in passing, under two minutes.** For each decision made today ask: would a fresh agent need this to act correctly? If yes and graduating it takes under two minutes, do it now: a wiki page, an ADR in the spec, or a flag for the next hygiene pass. Never research at exit time.
4. **Reconcile the tracker.** Update next action and blockers. Change status only when the work objectively did so. Ending a chat does not close an issue.
5. **Verify before reporting.** Run only the relevant checks: working tree, targeted tests, live tracker state when claiming external state.
6. **Report at planning altitude:** decision, implication, risk, next action. Mention uncommitted files.

## Mode: HANDOFF

1. **Crystallize.** Update the truth files the next agent will read: spec requirements and design, task files showing the true next step. Keep status in the live tracker, where it belongs.
2. **Clean the path.** Archive or delete notes that would mislead the next agent. Fix outdated claims in the project README.
3. **Write the bridge.** A paste-ready prompt for the next session: the goal, the files to read, the ritual to observe, the immediate next step. If your workspace runs a persona or judgment layer, embed the decision patterns the next session needs. Skip cleanly if none exists.
4. **Record.** Same one-entry note as DONE, marked as a handoff.

## The lightness rule

The exit takes minutes. Deep pruning and wiki distillation belong to scheduled hygiene passes, never to the exit. A heavy close gets skipped, and a skipped close loses everything.

## Explicit non-goals

- No automatic writes to any workspace-memory system.
- No end-of-day narrative synthesis.
- No commits, pushes, merges, or deploys without an explicit user request.
- No research or deep pruning at exit time.

## Completion criterion

DONE: decision recorded, work item reconciled or marked unverified, report delivered. HANDOFF: truth files current, bridge written, record kept.
