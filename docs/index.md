# The manual

The README is the front page. This is the reasoning behind the kit, for the
reader who wants to know why a rule exists before following it.

| Page | Question it answers |
|---|---|
| [Architecture](architecture.md) | What are the layers, and what does the agent load when? |
| [Boot protocol](boot-protocol.md) | How does an agent get from a clone to a working session? |
| [Design](design.md) | Who decides what — human, agent, judgment layer? |
| [Decisions](../decisions/) | Why was each rule chosen? Four ADRs. |
| [Patterns](../patterns/) | How do the recurring procedures work in practice? |
| [Wiki schema](../wiki/SCHEMA.md) | What does durable reference knowledge look like? |

## Decisions

- [ADR-0001](../decisions/ADR-0001-live-status-and-static-knowledge-never-merge.md) — live status and static knowledge never merge.
- [ADR-0002](../decisions/ADR-0002-capture-at-the-moment-of-decision.md) — capture at the moment of decision; the close audits.
- [ADR-0003](../decisions/ADR-0003-evals-are-the-regression-gate.md) — evals are the regression gate for skills.
- [ADR-0004](../decisions/ADR-0004-gateway-is-shipped-and-onboarding-consumes-it.md) — the gateway is shipped, and onboarding consumes it.

## Patterns

- [Session-notes protocol](../patterns/session-notes-protocol.md): the decision log, its graduation rule, and capture as you go.
- [The two-truths split](../patterns/two-truths-split.md): live status versus static knowledge.
- [Skill anatomy](../patterns/skill-anatomy.md): how to build skills that stay loadable, with references and evals.
- [GitHub as the workspace](../patterns/github-as-the-workspace.md): using the repo as knowledge layer and governance layer, not just code hosting.
- [Multi-intelligence review](../patterns/multi-intelligence-review.md): checkpoint sweeps and parallel panels, to close gaps the primary conversation cannot see.
- [The agent definition stack](../patterns/agent-definition-stack.md): how the kit instantiates agents, from character to schedule.
- [The clone ritual](../patterns/the-clone-ritual.md): gateway, pointer, and trigger phrase — how any repo becomes clone-it-and-tell-your-agent.

## Directives

The hard rules an agent keeps on hand. Each one is also a file in
[`directives/`](../directives/).

- [Agent execution](../directives/agent-execution-directive.md): how an agent executes work, from receiving a task to delivering results.
- [No documentation garbage](../directives/no-documentation-garbage.md): what not to write down.
- [Skill awareness](../directives/skill-awareness-directive.md): when to reach for a skill instead of improvising.
- [Spec location](../directives/spec-location-directive.md): where specifications live and how to find them.
- [Environment plumbing](../directives/environment-plumbing-directive.md): how to fix the files jobs read, wire backends and credentials, and verify the primary instead of the fallback.
