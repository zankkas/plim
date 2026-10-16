# Workspace Map

<!--
PRINCIPLES BAKED INTO THIS FILE (do not delete the comments, they are the lesson):

1. The compass is orientation, never status. It maps the workspace and names the
   authorities. It must never hold a status table, a work queue, or a "current
   projects" list. The moment it does, it becomes a second, stale authority.

2. Two-truths split: the live tracker is the only authority on current status.
   This file names that tracker and points at it. It does not mirror it.

3. Strategy (why and where) stays separate from operational status (what is
   active now). Specs describe requirements and design; they do not establish
   priority by themselves.

4. A new knowledge layer gets wired into this file the day it ships. A store
   no session reads at boot is dead inventory.
-->

This is a static orientation guide, not a work tracker. It must not duplicate current project status.

## Current work and source of truth

**{{LIVE_TRACKER}}** is the canonical view of current work. Issues hold scope, state, discussion, and next actions. Use the live source at session start; do not rely on local snapshots, generated boards, or copied status tables.

## Workspace identity

{{WORKSPACE_NAME}} is a multi-project build environment. Specs and session history live here; implementation repositories live in their own repositories.

## Navigation

| Path | Purpose |
|------|---------|
| `.agents/SOUL.md` | Assistant identity, boundaries, and continuity protocol |
| `.agents/PROFILE.md` | Stable user context and preferences |
| `.agents/session-notes/{domain}.md` | Decision history, newest entries first |
| `.agents/directives/` | Workspace-wide behavioral rules |
| `.agents/skills/` | Workspace-specific procedures; read the relevant file before use |
| `{{SPECS_DIR}}/{project}/` | Active design and implementation specs |
| `{{STRATEGY_DIR}}/` | Stateless project direction, not progress tracking |
| `wiki/` | Agent-maintained reference knowledge; `wiki/index.md` is the always-loaded catalog |

<!-- Adapt this table to your own workspace. Delete rows you do not have. Add rows for your own layers. -->

## Operating conventions

- The live tracker is the only source of current status. Keep issue state distinct from project status.
- Keep strategy (why and where) separate from operational status (what is active now).
- Record durable decisions in `.agents/session-notes/{domain}.md` at natural milestones, newest first.
- For reference questions, query `wiki/` starting from `wiki/index.md` before re-reading raw documents.
- Route specialist judgment through your judgment layer if one exists (see SOUL §7). Vision and priority questions go to the human directly.
- Do not expose `.agents/` private context or private paths in public-facing output.

## Session orientation

Read `.agents/PROFILE.md` for stable user context, consult this map for navigation, then query the live tracker for current work. Read session notes and specs on demand, not preloaded.

**Dependency-order the lead question.** Before asking "what do we work on?", check which open decisions gate which open work. Present decisions in dependency order, gates first. Never present a flat menu of options when some are gated by others.
