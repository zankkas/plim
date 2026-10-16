# The Two-Truths Split

An agent workspace holds two kinds of truth. They must never merge.

1. **Live truth.** The tracker (issues, project board, whatever live system you use) is the only authority on current status: what is active, blocked, done, or next.
2. **Static truth.** Local files hold orientation (the compass), knowledge (the wiki), and decisions (session notes). They describe the shape of the world, not its current state.

## The rule

Never mirror live status into static files. Three corollaries:

- When the live tracker is unreachable, report state as **unverified**. Never reconstruct it from memory, local snapshots, or caches.
- Legacy artifacts (old boards, exported JSON, generated dashboards) stay clearly marked as migration artifacts. They are never presented as current state.
- A note may name a next action. It may not own one. If a next action lives only in a static file, it is a missing tracker item.

## Why it matters

A static copy of status becomes a second authority within days. Two authorities that disagree produce worse behavior than one stale authority: the agent picks whichever it read last, and neither the human nor the agent can tell which truth is live. The drift is invisible until it costs a decision.

The split also protects the static files. The compass stays small and stable because it never carries status. Small and stable is what makes it safe to load at every boot.

## Enforcement

- The boot adapter names the live tracker as the sole status authority.
- The compass states the rule in its own text ("not a work tracker").
- The workspace-hygiene skill checks for authority drift and duplicate registries.
- The close-session skill reconciles the live tracker directly instead of copying state into local files.
