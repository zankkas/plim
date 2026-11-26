# Run Results

One line per run, newest first.

- 2026-11-25: wiki 5/5 passed — reasoning pass against cases.json before first commit. Cases: new source, existing page, no page, oversized page, index drift. Each judged against the SKILL.md steps by inspection of the text, not by execution; there is no runtime for this skill. Low confidence on case 4 (page-too-fat): the skill states the rule but gives no size test, so an agent must judge "longer than the raw" itself. Acceptable for a prose skill; the doctor covers the structural half.
