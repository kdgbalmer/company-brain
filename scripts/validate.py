#!/usr/bin/env python3
"""Check that the Company Brain repo is structurally sound.

For maintainers. Run: python3 scripts/validate.py
Prints OK and exits 0, or prints one line per problem and exits 1.
Standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List

SKILLS = [
    "setup",
    "hq",
    "marketing",
    "sales",
    "delivery",
    "offers",
    "finance",
    "operations",
    "team",
    "builder",
]

WORKFLOW_HEADINGS = [
    "Purpose",
    "Use when",
    "Load first",
    "Steps",
    "Check before handing over",
    "Save to",
    "Needs a yes",
]

SETUP = ".claude/skills/setup"
REQUIRED_FILES = (
    [f"{SETUP}/templates/business/{n}.md" for n in
     ["profile", "offers", "customers", "voice", "brand", "goals", "tools", "rules"]]
    + [f"{SETUP}/templates/department/{n}.md" for n in ["context", "role"]]
    + [f"{SETUP}/templates/memory/decisions.md"]
    + [f"{SETUP}/business-types/{n}.md" for n in
       ["coach", "consultant", "agency-freelancer", "local-service"]]
    + [f"{SETUP}/connectors/{n}.md" for n in
       ["gmail", "google-calendar", "google-drive", "notion", "canva", "stripe", "any-other-tool"]]
)

PRIVATE_FOLDERS = ["business", "departments", "outputs", "memory"]
GITIGNORE_LINES = [f"/{f}/" for f in PRIVATE_FOLDERS] + ["/.env"]

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def rel(root: Path, p: Path) -> str:
    return p.relative_to(root).as_posix()


def frontmatter(text: str) -> dict:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    out = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def check_skills(root: Path) -> List[str]:
    probs = []
    skills_dir = root / ".claude/skills"
    found = sorted(p.name for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.is_dir() else []
    for s in SKILLS:
        if s not in found:
            probs.append(f"missing skill: .claude/skills/{s}")
    for s in found:
        if s not in SKILLS:
            probs.append(f"unexpected skill: .claude/skills/{s}")
            continue
        f = skills_dir / s / "SKILL.md"
        if not f.is_file():
            probs.append(f"missing file: .claude/skills/{s}/SKILL.md")
            continue
        fm = frontmatter(f.read_text())
        if fm.get("name") != s:
            probs.append(f".claude/skills/{s}/SKILL.md: name must be '{s}'")
        d = fm.get("description", "")
        if not 1 <= len(d) <= 500:
            probs.append(f".claude/skills/{s}/SKILL.md: description must be 1-500 chars (is {len(d)})")
    return probs


def check_workflows(root: Path) -> List[str]:
    probs = []
    files = []
    for base in [root / ".claude/skills", root / "examples"]:
        if base.is_dir():
            files += [p for p in base.rglob("*.md") if p.parent.name == "workflows"]
    for f in sorted(files):
        heads = [m.group(1).strip() for m in re.finditer(r"^## (.+)$", f.read_text(), re.M)]
        present = [h for h in heads if h in WORKFLOW_HEADINGS]
        if present != WORKFLOW_HEADINGS:
            missing = [h for h in WORKFLOW_HEADINGS if h not in heads]
            why = f"missing {missing}" if missing else "headings out of order"
            probs.append(f"{rel(root, f)}: workflow shape wrong ({why})")
    return probs


def check_links(root: Path) -> List[str]:
    probs = []
    files = [root / "README.md", root / "CLAUDE.md"]
    for base in [root / ".claude", root / "examples"]:
        if base.is_dir():
            files += list(base.rglob("*.md"))
    for f in files:
        if not f.is_file():
            continue
        text = re.sub(r"```.*?```", "", f.read_text(), flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for target in LINK_RE.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if not path:
                continue
            if not (f.parent / path).exists():
                probs.append(f"{rel(root, f)}: dead link -> {target}")
    return probs


def check_required(root: Path) -> List[str]:
    probs = []
    for r in REQUIRED_FILES:
        if not (root / r).is_file():
            probs.append(f"missing file: {r}")
    prof = root / SETUP / "templates/business/profile.md"
    if prof.is_file() and "setup_stage:" not in prof.read_text():
        probs.append(f"{SETUP}/templates/business/profile.md: needs a setup_stage: field")
    conn = root / SETUP / "connectors"
    if conn.is_dir():
        for f in sorted(conn.glob("*.md")):
            if "## If it doesn't work" not in f.read_text():
                probs.append(f"{rel(root, f)}: needs an '## If it doesn't work' section")
    return probs


def check_privacy(root: Path) -> List[str]:
    probs = []
    gi = root / ".gitignore"
    lines = gi.read_text().splitlines() if gi.is_file() else []
    for want in GITIGNORE_LINES:
        if want not in lines:
            probs.append(f".gitignore: must contain '{want}'")
    for folder in PRIVATE_FOLDERS:
        if (root / folder).exists():
            probs.append(f"{folder}/ must not ship at the repo root (onboarding creates it)")
    return probs


def check_repo(root: Path) -> List[str]:
    root = Path(root)
    return (
        check_skills(root)
        + check_workflows(root)
        + check_links(root)
        + check_required(root)
        + check_privacy(root)
    )


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    probs = check_repo(root)
    if probs:
        print("\n".join(probs))
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
