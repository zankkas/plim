# Plim

*Governance for agent workspaces.*

Plim is a small kit of files that gives an AI agent written rules, memory, and
one source of truth for status — so no session starts by inventing its own
habits. It was extracted from a workspace that has run daily across several
projects. The artifacts are generic: copy them, fill the placeholders, adapt
them to your agent and your projects.

## The problem

An agent with no governance layer fails in the same six ways:

- It reconstructs current status from memory and gets it wrong.
- It copies status into static files, which then contradict the live source.
- It creates a new document instead of updating the existing one.
- It forgets decisions between sessions because nothing recorded them.
- It loads every procedure into context instead of the relevant ones.
- It applies its own judgment where the workspace named an authority.

None of these are model problems. They are missing-structure problems.

## Start

Paste this link into your agent:

**https://github.com/zankkas/plim/blob/main/SETUP.md** ([same file here](SETUP.md))

It clones the kit, runs the setup interview, and finishes by running the
doctor. Nothing else to read first.

Or do it yourself: clone the repo, open your agent in that folder, and say
**"plim, setup workspace"**. Either way, the doctor decides whether the result
is sound:

```console
$ python3 scripts/doctor.py
  skills: clean
  budget: clean
  evals: clean
  links: clean
  mirrors: clean

no drift found.
```

Until it prints `no drift found`, do not trust the workspace.

## What you get

| Piece | What it is |
|---|---|
| `AGENTS.md` | the gateway a fresh clone boots into; onboarding replaces it with your adapter |
| `templates/` | SOUL, PROFILE, compass and boot adapter, with placeholders |
| `skills/` | six procedures: onboard, capture-as-you-go, close-session, wiki, run-evals, workspace-hygiene |
| `directives/` | five always-on rules: agent-execution-directive, no-documentation-garbage, skill-awareness-directive, spec-location-directive, environment-plumbing-directive |
| `scripts/doctor.py` | the check above |
| `tests/` | contract tests for the kit's own promises |

## Why believe it

The claims are checkable, and that is the whole design:

- **The doctor checks six things** — skill shape, description budget, eval
  cases, relative links, status mirrors, and the wiki (index entries resolve,
  every page carries its frontmatter) — and exits non-zero on drift. It does not
  check ADRs, session notes, or your judgment. It checks the layer it was
  written for.
- **Evals gate every skill.** A skill edit without a recorded eval pass does not
  ship (ADR-0003).
- **`tests/` checks the kit's own contracts**: ADR format, wiki frontmatter, one
  H1 per template, every relative link resolves, every skill and ADR reachable
  from this file.

## The one rule

Live status and written knowledge never merge. The tracker (issues, board,
whatever live system you use) owns what is active now. The files own
orientation, knowledge, and decisions. When the tracker is unreachable, report
state as **unverified** — never reconstruct it from memory or a local copy. A
static copy of status becomes a second, lying authority within days.

A conversation is not the record either. A decision that exists only in a chat
thread is lost, because the next session cannot read it.

See `patterns/two-truths-split.md` and ADR-0001.

## A session

1. **Boot.** The agent reads the adapter, identity, profile, and compass, then
   fetches live status once and reuses it.
2. **Work.** It loads the one relevant skill instead of every procedure.
3. **Capture.** A decision is written down when it happens, not reconstructed
   at the end.
4. **Close.** It audits what capture recorded and leaves one handoff.

## What it is not

- Not a framework you install and forget. It decays without hygiene; run the
  workspace-hygiene skill weekly.
- Not a task manager. Status lives in your tracker.
- Not a memory system. Session notes record decisions, not conversation.
- Not a runner. It states the five contracts an autonomous loop has to honour —
  see [docs/running-it-autonomously.md](docs/running-it-autonomously.md) — and
  ships none of the engine.
- Not a product. It is a set of files that earn their keep by being read.

## The manual

The reasoning is one click away, starting at [docs/index.md](docs/index.md).

- **ADRs:** [ADR-0001](decisions/ADR-0001-live-status-and-static-knowledge-never-merge.md)
  live status and static knowledge never merge · [ADR-0002](decisions/ADR-0002-capture-at-the-moment-of-decision.md)
  capture at the moment of decision · [ADR-0003](decisions/ADR-0003-evals-are-the-regression-gate.md)
  evals are the regression gate · [ADR-0004](decisions/ADR-0004-gateway-is-shipped-and-onboarding-consumes-it.md)
  the gateway is shipped, and onboarding consumes it.
- **Patterns:** session-notes-protocol · two-truths-split · skill-anatomy ·
  github-as-the-workspace · multi-intelligence-review · agent-definition-stack ·
  the-clone-ritual.

## License

MIT. See `LICENSE`.
