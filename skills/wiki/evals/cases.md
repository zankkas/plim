# Wiki Skill Evals

1. **Scenario:** a durable fact arrives from a source the wiki does not cover.
   - Expected: raw source saved under `wiki/sources/<domain>/`, one page written or updated, one index line and one log entry, doctor still clean.
   - Forbidden: re-reading the source next session, or a page longer than the raw it replaces.

2. **Scenario:** the source is already covered by an existing page.
   - Expected: the existing page is updated in place, and the log records what changed.
   - Forbidden: a second page on the same topic, or two pages left to disagree.

3. **Scenario:** a reference question has no page and no obvious source.
   - Expected: say the wiki does not hold it, then offer to ingest the source or ask for it.
   - Forbidden: answering from memory as if the wiki had said it.

4. **Scenario:** a page has grown longer than the source it summarises.
   - Expected: slim it to the shortest accurate version; move depth into sources and the log.
   - Forbidden: treating the page as the new source of record.

5. **Scenario:** the index names a page that no longer exists.
   - Expected: the doctor reports the entry, and the entry is fixed or the page restored.
   - Forbidden: leaving the index as an approximation.
