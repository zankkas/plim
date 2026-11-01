# Plim

*Governance for agent workspaces.*

**Plim** is a kit of working artifacts that keep an agent team from inventing its own habits every session.

An agent workspace needs governance the way a team needs a charter and rituals. Agents are capable and stateless. Every session starts blank. Without written rules, each session invents its own habits, builds duplicate trackers, and drifts. This kit is what stops that drift.

It was extracted from a live agent workspace that has run daily across multiple projects. Nothing here was designed in the abstract. The artifacts are generic. Copy them, fill the placeholders, and adapt them to your own agent and projects.

Three things make it more than a set of templates. The rules carry their reasons, in ADRs. The procedures carry eval cases, so a rule that stops working is caught rather than assumed. And live status never merges with written knowledge, so the kit cannot quietly become a stale tracker of itself.

## The problem it solves

An agent with no governance layer fails in predictable ways:

- It reconstructs current status from memory and gets it wrong.
- It copies status into static files, which then contradict the live source of truth.
- It creates a new document instead of updating the existing one.
- It forgets decisions between sessions because nothing records them.
- It loads every procedure into context instead of the relevant ones.
- It applies its own engineering judgment where the workspace has a designated authority.

None of these are model problems. They are missing-structure problems.

## The layers

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

The agent reads identity, profile, and the compass at boot. It reads directives and skills only when relevant. It writes continuity and wiki during and after work.

The directives that ship with the kit:

- [Agent execution](directives/agent-execution-directive.md): how an agent executes work, from receiving a task to delivering results.
- [No documentation garbage](directives/no-documentation-garbage.md): what not to write down.
- [Skill awareness](directives/skill-awareness-directive.md): when to reach for a skill instead of improvising.
- [Spec location](directives/spec-location-directive.md): where specifications live and how to find them.
- [Environment plumbing](directives/environment-plumbing-directive.md): how to fix the files jobs read, wire backends and credentials, and verify the primary instead of the fallback.

The decisions that ship with the kit (ADRs, the reasoning behind the rules):

- [Live status and static knowledge never merge](decisions/ADR-0001-live-status-and-static-knowledge-never-merge.md): the live tracker owns status, static files own knowledge, and the two never merge.
- [Capture at the moment of decision](decisions/ADR-0002-capture-at-the-moment-of-decision.md): decisions are recorded when they happen; the close audits rather than reconstructs.
- [Evals are the regression gate](decisions/ADR-0003-evals-are-the-regression-gate.md): every skill ships evals, and they run whenever the skill changes.

The skills that ship with the kit:

- [Capture as you go](skills/capture-as-you-go/SKILL.md): record decisions, ideas, knowledge, and limitations the moment they happen.
- [End of session](skills/end-of-session/SKILL.md): end a session with two exits and one light audit.
- [Run evals](skills/run-evals/SKILL.md): run a skill's eval cases and report the verdict per case.
- [Workspace hygiene](skills/workspace-hygiene/SKILL.md): audit the governance layer for drift, duplicate skills, stale adapters, and broken references.
- [Onboard](skills/onboard/SKILL.md): on a first session, ask a few plain questions and fill the template placeholders.

## The two truths

Two kinds of truth live in the workspace, and they must never merge:

1. **The live tracker holds current status.** Issues, boards, or whatever live system you use. It is the only authority on what is active now.
2. **The static files hold orientation and knowledge.** The compass maps the workspace. The wiki holds verified facts. Session notes record decisions.

The rule: never mirror live status into static files. When the live system is unreachable, report state as unverified. Never reconstruct it from memory or local caches. A static copy of status becomes a second, lying authority within days. See [patterns/two-truths-split.md](patterns/two-truths-split.md).

## The division of labor

The kit exists for a symbiosis, not for delegation. In biology, the precise word for a symbiosis where both sides gain is mutualism, and that is the design target: the human brings what no model can copy (context, taste, and the judgment of what matters); the agent brings what humans exhaust on (recall, consistency, and stamina for the grunt work). A third layer can sit between them: a judgment layer for specialist decisions the human should not make alone. Route those through it and act on its grounded recommendation. Skip cleanly if you run none.

The split only works when it is written down. Both sides need to know what they own. The SOUL template carries the decision routing. When the split stays implicit, the agent drifts into judgment that belongs to the human, or the human gets buried in execution the agent should absorb.

## The boot protocol (two hops)

Boot is a thin adapter, not a data dump.

1. **First hop:** the agent reads the adapter file (`AGENTS.md` at the repo root, or your runtime's equivalent). It points at the identity, profile, and compass files and at the live status source.
2. **Second hop:** the agent reads those files, then renders a short brief: decisions needed, ready work, blocked work, unverified state.

The adapter stays tiny. It changes only when the map changes. All real content lives one hop away, in files the agent can also read mid-session. Keep the adapter and its targets identical across every client that boots into the workspace.

## What holds the agent mid-session

Boot files stay in context for the whole session. Skill descriptions stay resident too: one line each, saying what the procedure is for and when to load it. The full procedure loads only when relevant. That is the hint layer: a permanent index of small pointers, not a permanent pile of full text.

When the runtime supports hard guardrails, they sit underneath the hints: approve-or-deny rules that no prompt can bypass. Hints shape judgment. Guardrails bound action.

## Quickstart

1. Copy `templates/` into your workspace as `.agents/`.
2. Fill the placeholders: agent name, human name, file paths, live tracker.
3. Point the boot adapter (`AGENTS.md` or your runtime's equivalent) at the files.
4. Create the session-notes file with its header block. See [patterns/session-notes-protocol.md](patterns/session-notes-protocol.md).
5. Adopt the end-of-session skill first. It is the ritual that keeps the rest honest.
6. Add directives and the wiki only when you feel the problem they solve.

## The patterns

Read them when the problem they solve shows up in your workspace:

- [Session-notes protocol](patterns/session-notes-protocol.md): the decision log, its graduation rule, and capture as you go.
- [The two-truths split](patterns/two-truths-split.md): live status versus static knowledge.
- [Skill anatomy](patterns/skill-anatomy.md): how to build skills that stay loadable, with references and evals.
- [GitHub as the workspace](patterns/github-as-the-workspace.md): using the repo as knowledge layer and governance layer, not just code hosting.
- [Multi-intelligence review](patterns/multi-intelligence-review.md): checkpoint sweeps and parallel panels of other intelligences, to close gaps the primary conversation cannot see.
- [The agent definition stack](patterns/agent-definition-stack.md): how the kit instantiates agents, from character to schedule.

## What this is not

- It is not a framework you install and forget. It decays without hygiene rituals. Run the workspace-hygiene skill weekly.
- It is not a task manager. Status lives in your tracker, not here.
- It is not a memory system. Session notes record decisions, not conversation history.
- It is not a product. It is a set of files that earn their keep by being read and maintained.

## License

MIT. See [LICENSE](LICENSE).
