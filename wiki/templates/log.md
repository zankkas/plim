# {{DOMAIN}} Wiki — Log

Append-only. Newest entries first. One entry per wiki operation.

Format:

```markdown
## [{{YYYY-MM-DD}}] {{op}} | {{subject}}
- {{what changed, and the why when it is not obvious}}
- {{state after: page count or notable deltas}}
```

Operations: `create` (new page or scaffold), `ingest` (source material compiled into pages), `lint` (verify, prune, slim), `decision` (a recorded choice about the wiki itself), `retire` (page removed or merged, with tombstone note).

The log is the wiki's session note. A page change without a log entry is a lost decision.
