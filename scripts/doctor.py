#!/usr/bin/env python3
"""doctor — check a Plim workspace for the drift it exists to prevent.

The kit's thesis is that an agent workspace drifts in predictable ways. This
script makes that claim checkable instead of aspirational. Run it at boot, or
whenever a status claim matters.

Checks
  1. skills     every skill is a directory with a SKILL.md, nothing loose or nested
  2. budget     skill descriptions fit the per-session context budget
  3. evals      every skill ships eval cases that parse and have cases
  4. links      relative links in README and skills point at files that exist
  5. mirrors    no file claims to be a status tracker (status belongs in the live system)
  6. wiki       the index resolves and every page carries its frontmatter, so
                "check the wiki" is a gate and not a habit

Exit 0 = clean. Exit 1 = drift found, do not report state as fact.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DESCRIPTION_BUDGET = 260  # bytes, injected into every session
WIKI_KEYS = ("domain", "type", "updated", "sources")
WIKI_EXEMPT = {"index", "log", "SCHEMA", "STARTER"}
MIRROR_NAMES = re.compile(r"(status|tracker|backlog|dashboard)", re.IGNORECASE)
LINK = re.compile(r"\[[^\]]+\]\(([^)#]+)\)")


def _skill_description(text: str) -> str | None:
    """Read a YAML description, folded or inline, without needing a YAML parser."""
    match = re.search(r"^description:[ \t]*(.*)$", text, re.MULTILINE)
    if not match:
        return None
    first = match.group(1).strip()
    if first in (">", "|", ">-", "|-", ""):
        collected: list[str] = []
        for line in text[match.end():].splitlines():
            if line.strip() and not line.startswith((" ", "\t")):
                break
            collected.append(line.strip())
        return " ".join(part for part in collected if part)
    if first[0] in "\"'":
        return first.strip(first[0])
    return first


def check_skills(root: Path) -> list[str]:
    skills = root / "skills"
    if not skills.is_dir():
        return ["skills/ is missing"]
    findings = []
    for entry in sorted(skills.iterdir()):
        if entry.is_file():
            findings.append(f"skills/{entry.name} is loose; only directories belong here")
            continue
        if not (entry / "SKILL.md").is_file():
            nested = [p.name for p in entry.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()]
            if nested:
                findings.append(f"skills/{entry.name}/ holds nested skills ({', '.join(nested)})")
            else:
                findings.append(f"skills/{entry.name}/ has no SKILL.md")
    return findings


def check_budget(root: Path) -> list[str]:
    findings = []
    for skill in sorted((root / "skills").glob("*/SKILL.md")):
        size = len((_skill_description(skill.read_text()) or "").encode())
        if size == 0:
            findings.append(f"{skill.parent.name}: no description (the loader cannot select it)")
        elif size > DESCRIPTION_BUDGET:
            findings.append(
                f"{skill.parent.name}: description is {size}B (budget {DESCRIPTION_BUDGET}) — it is injected into every session"
            )
    return findings


def check_evals(root: Path) -> list[str]:
    findings = []
    for skill in sorted((root / "skills").glob("*/SKILL.md")):
        cases = skill.parent / "evals" / "cases.json"
        if not cases.is_file():
            findings.append(f"{skill.parent.name}: no evals/cases.json — ADR-0003 requires one")
            continue
        try:
            data = json.loads(cases.read_text())
        except json.JSONDecodeError as exc:
            findings.append(f"{skill.parent.name}: cases.json does not parse ({exc.msg})")
            continue
        count = len(data.get("cases", data)) if isinstance(data, (dict, list)) else 0
        if not count:
            findings.append(f"{skill.parent.name}: cases.json holds no cases")
    return findings


def check_links(root: Path) -> list[str]:
    findings = []
    targets = [root / "README.md", *sorted((root / "skills").glob("*/SKILL.md"))]
    for doc in targets:
        if not doc.is_file():
            continue
        for raw in LINK.findall(doc.read_text()):
            if raw.startswith(("http://", "https://", "mailto:")):
                continue
            if not (doc.parent / raw).resolve().exists():
                findings.append(f"{doc.relative_to(root)}: link target missing: {raw}")
    return findings


def check_mirrors(root: Path) -> list[str]:
    findings = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if rel.parts and rel.parts[0] in {".git", "decisions", "patterns"}:
            continue
        if MIRROR_NAMES.search(path.name) and path.name != "README.md":
            findings.append(f"{rel}: looks like a status mirror; status belongs in the live system")
    return findings


def check_wiki(root: Path) -> list[str]:
    """The wiki is the reference layer: if it exists, it must be navigable and honest.

    A wiki nobody can trust is worse than no wiki, because the agent reads it as
    truth. This is the check that keeps "ask the wiki first" from being a habit.
    """
    wiki = root / "wiki"
    if not wiki.is_dir():
        return []
    findings = []
    index = wiki / "index.md"
    if index.is_file():
        for raw in LINK.findall(index.read_text()):
            if raw.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw.split("#")[0]
            if target and not (index.parent / target).exists():
                findings.append(f"wiki/index.md links {raw}, which does not exist")
    for page in sorted(wiki.rglob("*.md")):
        rel = page.relative_to(wiki)
        if rel.parts[0] == "templates" or page.stem in WIKI_EXEMPT:
            continue
        text = page.read_text()
        block = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not block:
            findings.append(f"wiki/{rel}: no frontmatter (the page cannot be filed or aged)")
            continue
        missing = [key for key in WIKI_KEYS if not re.search(rf"^{key}\s*:", block.group(1), re.M)]
        if missing:
            findings.append(f"wiki/{rel}: frontmatter missing {', '.join(missing)}")
    return findings


CHECKS = (
    ("skills", check_skills),
    ("budget", check_budget),
    ("evals", check_evals),
    ("links", check_links),
    ("mirrors", check_mirrors),
    ("wiki", check_wiki),
)


def run(root: Path) -> int:
    print(f"plim doctor — {root}")
    failures = 0
    for name, check in CHECKS:
        findings = check(root)
        if findings:
            failures += len(findings)
            print(f"  {name}: {len(findings)} finding(s)")
            for finding in findings:
                print(f"    - {finding}")
        else:
            print(f"  {name}: clean")
    print()
    if failures:
        print(f"{failures} finding(s). Fix before reporting state as fact.")
        return 1
    print("no drift found.")
    return 0


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    return run(root)


if __name__ == "__main__":
    sys.exit(main())
