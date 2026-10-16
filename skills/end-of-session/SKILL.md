---
name: end-of-session
description: >
  End a session the right way: two exits, one light audit. Use when the user
  says done, close the session, end here, or asks for a handoff. Decisions
  were captured as they happened; the exit verifies, it does not reconstruct.
---

# End of Session

**Why:** Sessions are ephemeral. Decisions and next moves must outlive them. Because capture happens continuously during the session, the exit stays light: it audits what is already written instead of rebuilding it from memory.

## During the session: capture as you go

Decisions, ideas, limitations, and verified knowledge are recorded the moment they happen, by the capture-as-you-go skill. A few lines, no ceremony. That continuous loop is what makes this exit cheap, and it is the honest record: every decision is the decision made. A later one supersedes it. It does not erase it.

The DONE audit below catches anything capture missed. Nothing else.

## First: pick the exit

- **DONE**: the work reached its end. Reconcile and audit.
- **HANDOFF**: work continues in another session or agent. Crystallize and bridge.

One question settles it: will anyone act on this work before you see it again? Yes means handoff. No means done.

## Mode: DONE

1. **Audit the note.** Read today's entry. If continuous capture missed a decision, add it now, from what is still in context. Do not reconstruct what is already gone; anything missed that is no longer in context gets flagged, by name, for the next hygiene pass.
2. **Classify in passing, under two minutes.** For each decision made today ask: would a fresh agent need this to act correctly? If yes and graduating it takes under two minutes, do it now: a wiki page, an ADR in the owning spec's `design.md`, or a flag for the next hygiene pass. Never research at exit time.
3. **Identify the canonical work item** in the tracker named by the compass. If none exists, record that in the session note. Do not create one to justify the close.
4. **Reconcile the tracker.** Update next action and blockers. Change status only when the work objectively did so. Ending a chat does not close an issue. If the tracker cannot be reached, mark the work item unverified in the close report; never copy or reconstruct its state.
5. **Verify before reporting.** Run only the relevant checks: working tree, targeted tests, live tracker state when claiming external state.
6. **Report at planning altitude:** decision, implication, risk, next action. Mention uncommitted files.

## Mode: HANDOFF

1. **Crystallize.** Update the truth files the next agent will read: spec requirements and design, task files showing the true next step. Keep status in the live tracker, where it belongs.
2. **Clean the path.** Archive or delete notes that would mislead the next agent. Fix outdated claims in the project README.
3. **Write the bridge.** Start from variant A, the standard form, in [references/bridge-prompts.md](references/bridge-prompts.md): the goal, the files to read, the ritual to observe, the immediate next step. If your workspace runs a persona or judgment layer, move up to variant B and embed the decision patterns the next session needs. Skip cleanly if none exists.
4. **Record.** Same note as DONE, marked as a handoff.

## The lightness rule

The exit takes minutes. Deep pruning and wiki distillation belong to scheduled hygiene passes, never to the exit. A heavy close gets skipped, and a skipped close loses everything.

## Explicit non-goals

- No automatic writes to any workspace-memory system.
- No end-of-day narrative synthesis.
- No commits, pushes, merges, or deploys without an explicit user request.
- No research or deep pruning at exit time.

## Completion criterion

DONE: note audited, work item reconciled or marked unverified, report delivered. HANDOFF: truth files current, bridge written, record kept.
