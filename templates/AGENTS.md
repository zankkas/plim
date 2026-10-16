# Workspace Governance

This workspace is governed by `.agents/SOUL.md`, `.agents/PROFILE.md`, and `.agents/compass.md`.

> This file is a boot adapter. It stays thin. It points at the real files; it does not duplicate them.
> When your map changes, edit this file in the same pass. When content changes, edit the target file instead.

## Session start

1. Read the newest entry in `.agents/session-notes/{{DEFAULT_DOMAIN}}.md`.
2. Read `.agents/SOUL.md` and `.agents/PROFILE.md`.
3. Read `.agents/compass.md` for orientation. Then query the live status source ({{LIVE_TRACKER}}) for current work.
4. Render a concise 5-8 line brief: decisions needed, ready work, active or blocked work, and any unverified or stale state.
5. If the live source cannot be queried, say that current state is unverified. Do not reconstruct current state from local files or memory.

## Authority

- Current work status: {{LIVE_TRACKER}}. It is the only authority on what is active now.
- Implementation truth: branches, commits, and pull requests in each project repository.
- Local snapshots, generated boards, and cached exports: never status authorities.

## Task loading

Read only the relevant files in `.agents/directives/` and `.agents/skills/` before acting. Do not preload every procedure into the chat.

## Continuity

Record decisions and important handoffs in `.agents/session-notes/`. Session notes are a decision log, not a second work queue.
