#!/usr/bin/env python3
"""Contract tests for the kit.

These check that the documented rules in wiki/SCHEMA.md, the ADR format and the
patterns are actually honoured by the files shipped. Stdlib only, no network.

Run: python3 -m unittest discover -s tests -v
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FRONTMATTER_KEYS = ("domain", "type", "updated", "sources")
ADR_SECTIONS = ("status", "context", "decision", "consequences")


def read(p):
    return p.read_text(encoding="utf-8", errors="replace")


def md_files(*dirs):
    out = []
    for d in dirs:
        base = ROOT / d
        if base.exists():
            out.extend(sorted(base.rglob("*.md")))
    return out


class WikiTemplateContract(unittest.TestCase):
    """wiki/SCHEMA.md: pages carry frontmatter with domain, type, updated, sources."""

    def test_page_templates_declare_required_frontmatter(self):
        offenders = []
        for p in md_files("wiki/templates"):
            text = read(p)
            m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
            if not m:
                offenders.append(f"{p.relative_to(ROOT)}: no frontmatter block")
                continue
            body = m.group(1)
            missing = [k for k in FRONTMATTER_KEYS if not re.search(rf"^{k}\s*:", body, re.M)]
            if missing:
                offenders.append(f"{p.relative_to(ROOT)}: missing {', '.join(missing)}")
        self.assertEqual(offenders, [], "template frontmatter contract violated: " + "; ".join(offenders))


class AdrContract(unittest.TestCase):
    def test_adrs_have_required_sections(self):
        files = md_files("decisions")
        self.assertTrue(files, "no ADRs found")
        for p in files:
            text = read(p).lower()
            for section in ADR_SECTIONS:
                self.assertIn(section, text, f"{p.relative_to(ROOT)} lacks '{section}'")


class DirectiveContract(unittest.TestCase):
    def test_every_directive_is_referenced(self):
        corpus = "\n".join(read(p) for p in md_files(".") if "directives" not in str(p.relative_to(ROOT)))
        for p in md_files("directives"):
            self.assertIn(p.stem, corpus, f"directive {p.name} is never referenced")


class IndexContract(unittest.TestCase):
    """README.md is the entry point: every ADR and pattern must be reachable from it."""

    def test_every_adr_and_pattern_is_referenced_in_readme(self):
        readme = read(ROOT / "README.md")
        for p in md_files("decisions", "patterns"):
            self.assertIn(p.stem, readme, f"{p.relative_to(ROOT)} is never referenced in README.md")


class LinkContract(unittest.TestCase):
    def test_relative_links_resolve(self):
        broken = []
        for p in md_files("."):
            for target in re.findall(r"\]\((?!https?:|mailto:|#)([^)]+)\)", read(p)):
                t = (p.parent / target.split("#")[0]).resolve()
                if not t.exists():
                    broken.append(f"{p.relative_to(ROOT)} -> {target}")
        self.assertEqual(broken, [], "broken links: " + "; ".join(broken))


class HeadingContract(unittest.TestCase):
    def test_templates_have_one_h1(self):
        for p in md_files("templates", "wiki/templates"):
            h1 = [l for l in read(p).splitlines() if l.startswith("# ")]
            self.assertEqual(len(h1), 1, f"{p.relative_to(ROOT)} has {len(h1)} H1 headings")


if __name__ == "__main__":
    unittest.main()
