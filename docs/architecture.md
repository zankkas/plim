# Architecture: the layers

An agent workspace has ten layers, each answering one question. Two of them are
read at boot; the rest are read when relevant.

| Layer | File | Question it answers |
|---|---|---|
| Identity | `SOUL.md` | Who is the agent? What voice, boundaries, and values? |
| Human profile | `PROFILE.md` | Who is it working with? Strengths, pitfalls, working style? |
| Navigation | `compass.md` | Where is everything, and what is authoritative? |
| Continuity | `session-notes/` | What was decided, and why? |
| Directives | `directives/` | What hard rules always apply? |
| Decisions | `decisions/` | Why was this chosen? What reasoning must survive? |
| Skills | `skills/` | How is a specific procedure run? |
| Reference | `wiki/` | What is durably true? |
| Verification | `scripts/doctor.py` | Is the workspace still doing what it says? |
| Gateway | `AGENTS.md` | What does an agent see when it opens the clone? |

The agent reads identity, profile, and the compass at boot. It reads directives
and skills only when relevant. It writes continuity and wiki during and after
work.

## What holds the agent mid-session

Boot files stay in context for the whole session. Skill descriptions stay
resident too: one line each, saying what the procedure is for and when to load
it. The full procedure loads only when relevant. That is the hint layer: a
permanent index of small pointers, not a permanent pile of full text.

When the runtime supports hard guardrails, they sit underneath the hints:
approve-or-deny rules that no prompt can bypass. Hints shape judgment.
Guardrails bound action.
