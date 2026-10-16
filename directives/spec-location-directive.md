# Spec Location Directive

**Status**: ACTIVE
**Purpose**: Standardize where specs are created

---

## The Rule

**All specs go in `_spec/{project}/{status}/{feature-name}/`**: never in the strategy folder or `.agents/`.

- `_spec/` → executable specs (requirements.md, design.md, tasks.md)
- `_strategy/{project}-STRATEGY.md` → strategic vision only
- `_strategy/` → research and strategic analysis only

## Structure

```
_spec/{project}/{status}/{feature-name}/
├── requirements.md
├── design.md
└── tasks.md
```

For projects that need orchestration-level detail, add a `blueprints/` subfolder holding the scrutinized, detail-rich task blueprints. Not every project earns blueprints. Projects that need consolidation and stability do.

<!-- The principle: specs are executable work inputs, strategy is direction.
     They live in different places so the agent never treats a strategy note
     as something to implement, or a spec as something to debate. -->
