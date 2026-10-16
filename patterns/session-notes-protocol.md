# The Session-Notes Protocol

Session notes are the agent's long-term memory for decisions. One file per domain. Prepend-only. Newest entry at the top.

## The shape

Each file starts with a header block that scopes it:

```markdown
# {{DOMAIN}}: Session Notes
> What this file covers, in one or two lines.
> Chronological, prepend-only. Newest entries go at the top.
```

Each session prepends exactly one entry below the header:

```markdown
## {{DATE}}: {{SESSION_THEME}}

### What was decided (and why)
- {{DECISION}}

### Open threads for next session
- {{NEXT_ACTION or open question}}
```

## What belongs in a note

- The decision or completed work, stated at outcome altitude
- The rejected alternative, when the rejection matters later
- Unresolved risks and blockers
- One concrete next action
- Links to the issue, spec, PR, or artifact that carries the detail

## What does not belong

- A second work queue. Next actions live in the tracker; the note names them, it does not own them.
- Current status tables. The live tracker is the status authority.
- Conversation transcripts or narrative diaries.
- Durable patterns about the human. Those go in PROFILE.md observations.

## Why prepend-only

The newest entry is the first thing a fresh session reads at boot. Prepending makes recency free: no search, no timestamps to parse. The older an entry, the deeper it sinks. If an entry needs constant revisiting, it is not a note, it is a document, and it belongs in the wiki or a spec.

## Enforcement

The close-session skill owns the write. One entry per session, written when the decision happens or at close, never batched later when the reasoning has faded.
