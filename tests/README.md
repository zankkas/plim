# Contract tests

Checks that the kit's own rules are honoured by the files it ships.

```
python3 -m unittest discover -s tests -v
```

Five contracts: wiki page templates carry the frontmatter `wiki/SCHEMA.md` requires; ADRs carry Status / Context / Decision / Consequences; every directive is referenced somewhere; relative markdown links resolve; every template has exactly one H1.

Stdlib only. No network. Fast enough to run on every commit.
