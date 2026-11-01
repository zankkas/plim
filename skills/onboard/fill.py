#!/usr/bin/env python3
"""Fill a cloned workspace from onboarding answers.

The person does not copy templates or edit placeholders. This script does
the write, and it refuses to invent anything the answers did not say.

Stdlib only. No network.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

KIT = Path(__file__).resolve().parents[2]

REQUIRED = (
    "human_name",
    "workspace_name",
    "live_tracker",
    "default_domain",
    "background",
)
PAIR_FIELDS = (
    ("trait_name", "trait_consequence"),
    ("pitfall_name", "pitfall_prompt"),
)
TEXT_FIELDS = (
    "working_style",
    "working_model",
    "voice_rules",
    "specs_dir",
    "strategy_dir",
)
DOMAIN_RE = re.compile(r"^[a-z][a-z0-9-]{0,31}$")
PATH_RE = re.compile(r"^[A-Za-z0-9_./-]{1,80}$")
GATEWAY_MARKER = "<!-- plim:gateway"
EXAMPLE_RE = re.compile(r"<!-- Example \(delete\):.*?-->\n?", re.S)

TRAIT_LINE = "- **{{TRAIT}}**: {{how it shows up and what the agent should do about it}}\n"
PITFALL_LINE = '- **{{PITFALL}}**: needs the question: "{{counter-move prompt}}"\n'
STYLE_LINE = "- {{WORKING_STYLE}}\n"
MODEL_LINE = "- {{WORKING_MODEL}}\n"
VOICE_LINE = "- {{VOICE_RULES}}\n"
OBSERVATION_BLOCK = (
    "### {{DATE}}: {{SESSION_THEME}}\n"
    "\n"
    "- **{{PATTERN}}**: {{evidence: what happened, what it implies for how to work with them}}\n"
)


class FillError(Exception):
    def __init__(self, code: int, message: str) -> None:
        self.code = code
        super().__init__(message)


def read_template(name: str) -> str:
    return (KIT / "templates" / name).read_text(encoding="utf-8")


def reject_braces(value: str, label: str) -> str:
    if "{{" in value or "}}" in value:
        raise FillError(2, f"{label} contains a placeholder")
    return value


def optional_text(data: dict, key: str) -> str:
    value = data.get(key) or ""
    if not isinstance(value, str):
        raise FillError(2, f"{key} must be a string")
    value = value.strip()
    return reject_braces(value, key) if value else ""


def optional_path(value: str, label: str) -> str:
    if not value:
        return ""
    if not PATH_RE.fullmatch(value) or ".." in value.split("/"):
        raise FillError(2, f"{label} is not a safe relative path")
    return value


def load_answers(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise FillError(2, f"could not read answers: {exc}") from exc
    if not isinstance(data, dict):
        raise FillError(2, "answers must be a JSON object")

    answers: dict[str, str] = {}
    missing = []
    for key in REQUIRED:
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            missing.append(key)
            continue
        answers[key] = reject_braces(value.strip(), key)
    if missing:
        raise FillError(2, "missing required answers: " + ", ".join(missing))
    if not DOMAIN_RE.fullmatch(answers["default_domain"]):
        raise FillError(
            2,
            "default_domain must be a short lowercase word, such as work",
        )

    for left, right in PAIR_FIELDS:
        lv = optional_text(data, left)
        rv = optional_text(data, right)
        if bool(lv) != bool(rv):
            raise FillError(2, f"{left} and {right} must both be set or both be empty")
        answers[left] = lv
        answers[right] = rv

    for key in TEXT_FIELDS:
        answers[key] = optional_text(data, key)
    answers["specs_dir"] = optional_path(answers["specs_dir"], "specs_dir")
    answers["strategy_dir"] = optional_path(answers["strategy_dir"], "strategy_dir")
    return answers


def already_onboarded(dest: Path) -> bool:
    soul = dest / ".agents" / "SOUL.md"
    return soul.is_file() and "{{" not in soul.read_text(encoding="utf-8")


def tidy(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(---\n)\n+(---\n)", r"\1", text)
    return text.strip() + "\n"


def swap_line(text: str, old: str, new: str) -> str:
    if old not in text:
        raise FillError(1, "a template line the filler expects is gone")
    return text.replace(old, new, 1)


def drop_token_rows(text: str, token: str) -> str:
    needle = "{{" + token + "}}"
    return "".join(line for line in text.splitlines(keepends=True) if needle not in line)


def point_at_shipped_layout(text: str) -> str:
    return text.replace(".agents/directives/", "directives/").replace(
        ".agents/skills/", "skills/"
    )


def render_soul(answers: dict, when: str) -> str:
    text = read_template("SOUL.template.md")
    text = text.replace("{{HUMAN_NAME}}", answers["human_name"])
    text = text.replace("{{DATE}}", when)
    text = text.replace("{{REASON}}", "Workspace onboarded")
    return finish("SOUL.md", text)


def render_profile(answers: dict) -> str:
    text = EXAMPLE_RE.sub("", read_template("PROFILE.template.md"))
    text = text.replace("{{HUMAN_NAME}}", answers["human_name"])
    text = text.replace("{{BACKGROUND}}", answers["background"])
    if answers["trait_name"]:
        bullet = f"- **{answers['trait_name']}**: {answers['trait_consequence']}\n"
        text = swap_line(text, TRAIT_LINE, bullet)
    else:
        text = swap_line(text, TRAIT_LINE, "")
    if answers["pitfall_name"]:
        bullet = (
            f"- **{answers['pitfall_name']}**: needs the question: "
            f"\"{answers['pitfall_prompt']}\"\n"
        )
        text = swap_line(text, PITFALL_LINE, bullet)
    else:
        text = swap_line(text, PITFALL_LINE, "")
    style = f"- {answers['working_style']}\n" if answers["working_style"] else ""
    model = f"- {answers['working_model']}\n" if answers["working_model"] else ""
    text = swap_line(text, STYLE_LINE, style)
    text = swap_line(text, MODEL_LINE, model)
    if answers["voice_rules"]:
        text = swap_line(text, VOICE_LINE, f"- {answers['voice_rules']}\n")
    else:
        start = text.find("\n## Voice (for public output)\n")
        end = text.find("\n---\n", start)
        if start < 0 or end < 0:
            raise FillError(1, "the voice section is not where the filler expects")
        text = text[:start] + text[end:]
    if OBSERVATION_BLOCK not in text:
        raise FillError(1, "the observation placeholder is not where the filler expects")
    text = text.replace(OBSERVATION_BLOCK, "", 1)
    return finish("PROFILE.md", text)


def render_compass(answers: dict) -> str:
    text = read_template("compass.template.md")
    text = text.replace("{{LIVE_TRACKER}}", answers["live_tracker"])
    text = text.replace("{{WORKSPACE_NAME}}", answers["workspace_name"])
    if answers["specs_dir"]:
        text = text.replace("{{SPECS_DIR}}", answers["specs_dir"])
    else:
        text = drop_token_rows(text, "SPECS_DIR")
    if answers["strategy_dir"]:
        text = text.replace("{{STRATEGY_DIR}}", answers["strategy_dir"])
    else:
        text = drop_token_rows(text, "STRATEGY_DIR")
    return finish("compass.md", point_at_shipped_layout(text))


def render_adapter(answers: dict) -> str:
    text = read_template("AGENTS.md")
    text = text.replace("{{DEFAULT_DOMAIN}}", answers["default_domain"])
    text = text.replace("{{LIVE_TRACKER}}", answers["live_tracker"])
    return finish("AGENTS.md", point_at_shipped_layout(text))


def render_note(answers: dict, when: str) -> str:
    domain = answers["default_domain"]
    text = (
        f"# {domain}: Session Notes\n"
        f"> Decision log for {answers['workspace_name']}. Newest entry at the top.\n"
        "\n"
        f"## {when}: Onboarding\n"
        "\n"
        "### What was decided (and why)\n"
        "- Workspace files were filled from the person's answers. "
        f"Current work lives at: {answers['live_tracker']}\n"
        "\n"
        "### Open threads for next session\n"
        "- Start the work.\n"
    )
    return finish(f"{domain}.md", text)


def finish(label: str, text: str) -> str:
    text = tidy(text)
    if "{{" in text or "}}" in text:
        raise FillError(1, f"{label} still contains a placeholder")
    return text


def write_under(dest: Path, relative: str, text: str) -> None:
    path = (dest / relative).resolve()
    if not path.is_relative_to(dest.resolve()):
        raise FillError(2, "refusing to write outside the destination")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"wrote {relative}")


def gateway_conflict(dest: Path) -> bool:
    """True when a root AGENTS.md exists but is not the shipped gateway —
    written by a human, so the filler must not clobber it."""
    adapter = dest / "AGENTS.md"
    return adapter.is_file() and GATEWAY_MARKER not in adapter.read_text(encoding="utf-8")


def fill(dest: Path, answers: dict, when: str, force: bool) -> None:
    if already_onboarded(dest) and not force:
        raise FillError(
            3,
            "this workspace is already onboarded; pass --force only to start over",
        )
    if gateway_conflict(dest) and not force:
        raise FillError(
            2,
            "AGENTS.md exists and is not the shipped gateway (no plim:gateway marker); "
            "move it aside by hand, then run again",
        )
    files = {
        "AGENTS.md": render_adapter(answers),
        ".agents/SOUL.md": render_soul(answers, when),
        ".agents/PROFILE.md": render_profile(answers),
        ".agents/compass.md": render_compass(answers),
        f".agents/session-notes/{answers['default_domain']}.md": render_note(answers, when),
    }
    for relative, text in files.items():
        write_under(dest, relative, text)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fill a cloned Symbiotic Workspace from onboarding answers.",
        epilog=(
            "Answer fields. Required: human_name, workspace_name, live_tracker, "
            "default_domain, background. Optional pairs: trait_name + trait_consequence, "
            "pitfall_name + pitfall_prompt. Optional text: working_style, working_model, "
            "voice_rules, specs_dir, strategy_dir. Omit an optional field to leave it empty. "
            "Do not invent values."
        ),
    )
    parser.add_argument("--dest", required=True, help="Workspace root to write into")
    parser.add_argument("--answers", required=True, help="JSON file of onboarding answers")
    parser.add_argument("--date", default=date.today().isoformat(), help="ISO date for the note")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite a workspace that is already onboarded",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        print("date must be YYYY-MM-DD", file=sys.stderr)
        return 2
    try:
        fill(Path(args.dest), load_answers(Path(args.answers)), args.date, args.force)
    except FillError as exc:
        print(exc, file=sys.stderr)
        return exc.code
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
