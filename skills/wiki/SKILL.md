---
name: wiki
description: >
  Maintain the reference wiki: ingest a source into pages, answer from the index,
  and lint for rot. Use when a durable fact appears, when a reference question is
  asked, or on the hygiene cadence.
---

# Wiki

**Why:** the wiki is the workspace's cheapest truth. A source is read and digested once; after that the answer comes from the index and a page, not from re-reading the world. It stays cheap only while pages are short, filed, and current.

## Ingest: a source becomes pages

1. **Look before reading.** Check `wiki/index.md` for a page that already covers it. If one exists, update it; never add a twin.
2. **Keep the raw source** under `wiki/sources/<domain>/`, with its link. Raw is immutable; pages cite it.
3. **Write or update the page.** Current state first, history below and labelled. The page must be shorter than the raw it replaces; depth stays in the source and the log.
4. **File it.** One line in `index.md` (a name and what it holds, not a summary) and one entry in `log.md` (what changed, why).
5. **Run the doctor.** `scripts/doctor.py` must stay clean: every index entry resolves, every page carries its frontmatter.

## Query: a reference question

1. Read `index.md`, pick the page, read the page.
2. Answer with the page path. If the page is missing or stale, say so and ingest — never answer a reference question from memory.
3. A synthesis worth keeping is written back as a page and logged.

## Lint: the periodic pass

Stale claims, contradictions between pages, orphans, index drift, missing cross-references. Log the pass. The doctor covers structure every session; this covers judgment.

## What this is not

- Not a second status tracker. Status lives in the tracker.
- Not a transcript. Decisions belong in session notes; the wiki holds reference knowledge.
- Not a place to decorate. Do not seed pages from imagination; an empty wiki that grows from real sources stays true.

## Completion criterion

The source is digested exactly once: a page exists, the index and log name it, and the doctor is clean.
