# Wiki: Schema

The agent-maintained knowledge layer for the workspace. Agent-first, human-readable second. The wiki is a compiled, kept-current artifact, not re-derived per query. Compiling once IS the caching strategy.

## Scope

- The wiki holds **reference knowledge and synthesis**. Durable procedures live in skills; operational status lives in the live tracker; session-level decisions live in `.agents/session-notes/`. Never duplicate those here.
- Define your own focus areas and promote domains into the wiki deliberately. A wiki that ingests everything becomes expensive to maintain and cheap to distrust.
- Boundary: document operational mechanics and verified facts. Never private strategy or personal context. The wiki may be read by any agent; write accordingly.

## Layers

1. **Raw sources**: `wiki/sources/<domain>/`. Immutable. Extracted web pages, research output, clipped articles, verbatim quotes. Every file carries a `source:` frontmatter link. Never edited after ingest; corrections go in wiki pages, not sources.
2. **Wiki pages**: `wiki/entities/` (things: products, tools, people, orgs) and `wiki/concepts/` (ideas: architectures, methods, verified findings). Agent-owned. Kept current on every ingest.
3. **This schema**: governance. Co-evolves with the human.

## Special files

- **`index.md`**: the ONLY always-loaded wiki file. Catalog of every page: link, one-line summary, domain tag. Updated in the same pass as any page write. If index and pages disagree, fix index immediately.
- **`log.md`**: append-only, chronological. Entry format: `## [YYYY-MM-DD] <op> | <subject>` (ops: ingest, query, lint, create). Parseable with `grep "^## \["`.
- **`ledger.md`**: the single contradiction/verification layer. Doc-vs-doc conflicts, open verdicts, and verification narratives live here, not in entity pages. Entity and concept pages carry at most a one-line status-flag pointer to the ledger.

## Operations

### Ingest
1. Extract the source to `wiki/sources/<domain>/` (with source link) if not already present. Never re-fetch what is already extracted.
2. Write or update a source summary page if the source is substantial.
3. Update affected entity and concept pages. Flag contradictions with existing claims rather than silently overwriting.
4. Update `index.md` and append to `log.md` in the same pass.

### Query
Search `index.md` first, then drill into pages. Answers citing wiki pages carry file paths. A valuable synthesis (comparison, analysis) is filed back as a new page and logged. Explorations compound.

### Lint (periodic)
Check for: stale claims superseded by newer sources, contradictions between pages, orphans with no inbound links, index drift, missing cross-references. Log the pass.

## Page conventions

- **Pages are the shortest accurate version of the knowledge.** A compiled page may never exceed the raw docs it replaces. Depth (contradiction detail, verification narratives, history) lives in `ledger.md` and `log.md`, not in entity or concept pages.
- **Current state goes first in an entity page; history is labeled before it can be read.** If a page must retain superseded design, compress it into a short labeled historical paragraph below the current-state section.
- Filename: lowercase-hyphen (`agent-memory.md`). One topic per page.
- Frontmatter: `domain`, `type` (entity|concept|source-summary), `updated`, `sources` (list of relative source paths or URLs).
- Cross-reference with relative markdown links. Keep pages short. Depth via links, not walls of text.

## Cost rules

- Compiling once IS the caching strategy: a source is read and digested into pages exactly once.
- The index lists sources by name only. Grep is the retrieval path; never one-line summaries in the index.
- Retrieval is index + grep. Add hybrid search (BM25 + embeddings) only when the wiki outgrows it, not before.
- Measure the win. A benchmark that shows wiki orientation costing more than raw docs means the pages are too fat: slim them.
