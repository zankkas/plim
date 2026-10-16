# Wiki: Starter

The wiki is the reference layer: the shortest accurate version of what the workspace durably knows. The schema defines the rules. This file gets you from zero to a living wiki in one pass.

## Bootstrap, in order

1. **Create `wiki/index.md`** from `templates/index.md`. Start with an empty catalog: one line per page, what it holds, nothing more. The index is always loaded at boot for reference questions, so it stays a list, never a summary.
2. **Create `wiki/log.md`** from `templates/log.md`. Append-only. One entry per wiki operation, newest first. The log is the wiki's own session note: what changed, when, and why.
3. **Write your first page** when the first durable fact appears. Do not seed pages from imagination. A wiki that starts empty and grows from real ingests stays true; a wiki that starts decorated starts lying.
4. **Wire it into boot.** The boot adapter and the SOUL file gain one line: for reference questions, read `wiki/index.md` first, then the page. Never re-fetch what the wiki already holds.
5. **Schedule the lint.** The schema's lint operation runs on a pass cadence: verify pages still match reality, prune what rotted, tombstone what graduated elsewhere.

## What makes it work

The value does not come from the schema. It comes from three habits:

- **Pages are the shortest accurate version.** Depth lives in sources and the ledger, not in the page. A page longer than what it replaced is a failure.
- **The log is append-only and honest.** Every operation recorded, including the failed ones.
- **The wiki is maintained in the same pass that changes things.** A page write without a log entry is a lost decision.

## What it is not

It is not a dump of every document. Sources stay where they live; the wiki holds the compiled truth and points at the source for the full version. It is not a status system either: the live tracker owns status, the wiki owns what is durably true.
