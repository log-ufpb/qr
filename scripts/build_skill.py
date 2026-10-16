#!/usr/bin/env python3
"""Generate the log-qr skill references from the mdBooks.

The mdBooks are the source of truth. This script copies every chapter listed
in each book's SUMMARY.md into skills/log-qr/references/, strips what only
matters for the rendered site (images, separators, mdBook math escapes), and
rewrites the topic table in skills/log-qr/SKILL.md.

Usage:
    python3 scripts/build_skill.py          # regenerate
    python3 scripts/build_skill.py --check  # fail if the skill is out of date
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ["qr-book", "qr-dev", "qr-algorithms", "qr-modelling"]
SKILL = ROOT / "skills" / "log-qr"
REFS = SKILL / "references"
BEGIN = "<!-- BEGIN GENERATED: run scripts/build_skill.py -->"
END = "<!-- END GENERATED -->"
NOISE = {"Summary", "References"}


def parse_summary(book):
    """Yield (section, title, path) for each chapter, skipping prefix chapters."""
    src = ROOT / book / "src"
    heads = []
    parents = {}
    for line in (src / "SUMMARY.md").read_text().splitlines():
        if m := re.match(r"(#+)\s+(.+)", line):
            if m[2] != "Summary":
                heads = heads[: len(m[1]) - 1] + [m[2].strip()]
            continue
        m = re.match(r"(\s*)- \[(.+?)\]\((.*?)\)", line)
        if not m or not heads:
            continue
        depth = len(m[1]) // 2
        parents[depth] = m[2]
        if m[3]:
            title = " / ".join([parents[d] for d in range(depth)] + [m[2]])
            yield " / ".join(heads), title, src / m[3]


def ref_name(book, path):
    rel = path.relative_to(ROOT / book / "src").with_suffix("")
    parts = [p.lower().replace("+", "p").replace("_", "-") for p in rel.parts]
    if len(parts) > 1 and parts[-1].startswith(parts[-2]):
        parts.pop(-2)
    return "-".join(parts) + ".md"


def clean(text):
    text = re.sub(r"<img\b[^>]*>\s*", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)\s*", "", text)
    text = re.sub(r"^\s*(\*\*\*|---)\s*$", "", text, flags=re.M)
    text = re.sub(r"\\\\\((.+?)\\\\\)", r"$\1$", text)
    text = re.sub(r"\\\\\[(.+?)\\\\\]", r"$$\1$$", text, flags=re.S)
    text = re.sub(r"[ \t]+$", "", text, flags=re.M)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def build():
    files, rows = {}, []
    for book in BOOKS:
        for section, title, path in parse_summary(book):
            body = clean(path.read_text())
            if not body.strip():
                continue
            name = ref_name(book, path)
            assert name not in files, f"duplicate reference name {name}"
            files[name] = body
            heads = re.findall(r"^##\s+(.+?)\s*$", body, flags=re.M)
            heads = [h for h in heads if h not in NOISE]
            covers = ", ".join(heads[:8]) or "-"
            rows.append(f"| {section} | {title} | `references/{name}` | {covers} |")
    table = "\n".join(
        ["| Section | Topic | File | Covers |", "|---|---|---|---|", *rows]
    )
    return files, table


def main():
    check = "--check" in sys.argv
    files, table = build()
    skill_md = (SKILL / "SKILL.md").read_text()
    head, rest = skill_md.split(BEGIN)
    _, tail = rest.split(END)
    new_skill_md = f"{head}{BEGIN}\n{table}\n{END}{tail}"

    current = {p.name: p.read_text() for p in REFS.glob("*.md")} if REFS.exists() else {}
    stale = current != files or skill_md != new_skill_md
    if check:
        if stale:
            sys.exit("skills/log-qr is out of date: run python3 scripts/build_skill.py")
        return

    REFS.mkdir(parents=True, exist_ok=True)
    for name in current.keys() - files.keys():
        (REFS / name).unlink()
    for name, body in files.items():
        (REFS / name).write_text(body)
    (SKILL / "SKILL.md").write_text(new_skill_md)
    print(f"Wrote {len(files)} references to {REFS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
