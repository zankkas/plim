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

## Graduation: when a note becomes something else

Not every decision stays a note. At close, each decision gets one question: **would a fresh agent need this to act correctly?**

- **Yes, and it is a durable fact or procedure** → graduate to the wiki. The wiki is the reference layer; notes are the provenance layer.
- **Yes, and it changes how the system is built** → graduate to an ADR in the owning spec's `design.md`.
- **Yes, but only for the next session** → it stays in the note as the next action.
- **No, it only explains what happened** → it stays in the note and eventually sinks.

Graduation happens at close only when it takes under two minutes. Everything else gets flagged for the periodic wiki ingest, which is where notes get pruned: once an entry's content lives in the wiki or a spec, the note keeps a one-line tombstone or loses the entry entirely. The notes stay short because the wiki holds the weight.

## Capture as you go

The close is an audit, not a writer. When a decision lands mid-session, record it immediately: a few prepended lines, no ceremony. The reasoning is freshest at the moment of decision, capture costs seconds then, and the exit ritual stays light because the work is already done. Waiting for close means reconstructing from a fading context, which is where fidelity dies.

Continuous capture also keeps the honest record: every decision is the decision made. A later decision supersedes it. It does not erase it.

## Enforcement

Continuous capture during the session; the close-session skill audits what was captured, classifies for graduation, and reconciles the tracker. One entry per session, written when the decision happens, never batched later when the reasoning has faded.
