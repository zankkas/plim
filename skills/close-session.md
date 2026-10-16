---
name: close-session
description: >
  Close a work session without creating a second source of truth. Use when the
  user says done, close the session, end here, or asks for a handoff. Capture
  decisions, reconcile the linked tracker item, verify the working tree, and
  report the next move at planning altitude.
---

# Session Close

**Why:** A close should preserve the reasoning and next move without turning the session into another status system or silently performing consequential Git actions.

## Steps

### 1. Identify the canonical work item

- Find the issue or pull request handled in this session, in the tracker named by the compass.
- Read its current state from the live tracker when access is available.
- If no work item exists, do not create one merely to close the session. Record that the work has no canonical work-item link.

### 2. Capture the durable decision

Prepend one concise entry to `.agents/session-notes/{domain}.md`. Include only:

- decision or completed work
- rejected alternative, when important
- unresolved risk or blocker
- one concrete next action
- links to the issue, PR, spec, or artifact

Update `.agents/PROFILE.md` only when the session revealed a durable pattern about the human. Do not add temporary project state or a chronological diary to the profile.

### 3. Reconcile the canonical work item

When a linked issue exists:

- Update `Next action`, `Blocker`, and `Last verified` when the evidence is clear.
- Update `Status` only when the transition is objective and already authorized by the work. Ending a chat does not mean the issue is done.
- Keep implementation evidence in branches, commits, PRs, and linked files.
- Use an item comment for handoff detail only when the next agent needs context that does not belong in the item body.

If the tracker is unavailable, report current work state as unverified. Do not copy state into local snapshots or caches.

### 4. Verify before reporting

Run only the checks relevant to the work:

- `git status --short` and branch status
- targeted tests or validation if changes were made
- issue or PR state when an external state claim is being reported

Do not clean, reset, commit, push, merge, deploy, close issues, or delete files automatically.

### 5. Produce the close report

Use this structure:

```text
Decision
Product or user implication
Risk or unverified state
Next action
```

Mention uncommitted files and unfinished work. Keep technical detail behind the planning-altitude boundary unless it changes the decision or creates material risk.

## Explicit non-goals

This skill does not:

- write to any workspace-memory system automatically
- create a temporary handoff file by default
- run end-of-day narrative synthesis
- commit or push without an explicit user request

## Completion criterion

The session is closed only when the decision is recorded, the canonical work item is reconciled or explicitly marked unverified, unfinished work has one next action, and the report has been delivered at planning altitude.
