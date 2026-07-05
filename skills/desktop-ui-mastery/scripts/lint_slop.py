#!/usr/bin/env python3
"""lint_slop.py - Detect the tells of generated/templated desktop UI in HTML/CSS/JSX/TSX.

Enforcement companion to references/critique-and-deslop.md. Heuristic by design:
it flags for review, it does not prove correctness. Warnings never block; only
severe violations affect the exit code.

Usage:
  python3 lint_slop.py <file-or-directory> [...]
  python3 lint_slop.py --strict <path>     # warnings also affect exit code

Exit codes: 0 clean (or warnings only), 1 severe violations found.
"""
import re
import sys
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".jsx", ".tsx", ".vue", ".svelte"}

SEVERE = "SEVERE"
WARN = "WARN"

CHECKS = [
    # (level, name, regex, message)
    (SEVERE, "placeholder-content",
     re.compile(r"lorem ipsum|john doe|jane doe|\bacme corp\b", re.I),
     "Placeholder content found. Real, plausible content is required (see SKILL.md output standards)."),
    (SEVERE, "focus-suppressed",
     re.compile(r"outline\s*:\s*none|outline\s*:\s*0(?![\w.])", re.I),
     "outline:none detected. Never suppress focus without a :focus-visible replacement (Freiberg)."),
    (SEVERE, "body-size-in-tool-ui",
     re.compile(r"(?:\bbody|\bhtml|:root)\s*(?:,[^{]*)?{[^}]*font-size\s*:\s*(1[6-9]|2\d)px", re.I | re.S),
     "Base font size >=16px. Desktop tool UI runs 11-15px; 16px+ is website scale (desktop-craft.md #5). Fine for marketing pages, wrong for app chrome."),
    (WARN, "border-plus-shadow",
     re.compile(r"(?:border\s*:[^;{}]*;[^{}]*box-shadow\s*:)|(?:box-shadow\s*:[^;{}]*;[^{}]*border\s*:)", re.I | re.S),
     "border and box-shadow in the same rule. Pick one separation method: tone, then border, then shadow (desktop-craft.md #5). True floating layers (dialogs, menus) may justify both; say so in the point of view."),
    (WARN, "gradient-accent",
     re.compile(r"linear-gradient\([^)]*(?:#?8b5cf6|#?a855f7|#?6366f1|purple|violet)", re.I),
     "Purple/violet gradient: the statistical center of generated UI. Justify from a stated principle or remove."),
    (WARN, "animation-duration-long",
     re.compile(r"(?:transition|animation)[^;{}]*?(?:[4-9]\d\d|\d{4,})ms", re.I),
     "Transition/animation >=400ms. Utility motion lives at 120-200ms; exits ~2/3 of entrances (Kowalski)."),
    (WARN, "ease-in-entrance",
     re.compile(r"transition[^;{}]*ease-in\b(?!-out)", re.I),
     "ease-in on a transition reads as hesitation. Use ease-out for entrances (Kowalski)."),
    (WARN, "pill-farm",
     re.compile(r"border-radius\s*:\s*(?:999+px|9999px|50rem|100vmax)", re.I),
     "Full-pill radius. Fine occasionally; audit for badge/pill overuse (slop list, visual tells)."),
]

TABULAR_HINT = re.compile(r"font-variant-numeric\s*:\s*tabular-nums|font-feature-settings\s*:[^;]*tnum", re.I)
TABLE_HINT = re.compile(r"<table\b|role=[\"']grid[\"']|class=[\"'][^\"']*(?:data-table|data-grid)", re.I)
FOCUS_VISIBLE = re.compile(r":focus-visible", re.I)
INTERACTIVE = re.compile(r"<button|<a\s|<input|<select|tabindex", re.I)
HOVER = re.compile(r":hover", re.I)
HEX = re.compile(r"#[0-9a-fA-F]{3,8}\b")
ROOT_BLOCK = re.compile(r":root\s*{[^}]*}|\[data-theme[^\]]*\]\s*{[^}]*}", re.S)
REDUCED_MOTION = re.compile(r"prefers-reduced-motion", re.I)
HAS_MOTION = re.compile(r"@keyframes|transition\s*:", re.I)


COMMENT = re.compile(r"/\*.*?\*/|<!--.*?-->", re.S)


def lint_text(text: str, path: Path):
    text = COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)  # preserve line numbers
    findings = []
    for level, name, rx, msg in CHECKS:
        for m in rx.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            findings.append((level, name, line, msg))
            break  # one report per check per file keeps output readable

    # File-level (presence/absence) checks
    if TABLE_HINT.search(text) and not TABULAR_HINT.search(text):
        findings.append((WARN, "no-tabular-figures", 0,
                         "Table/grid present without tabular-nums. Numeric columns need aligned digits (Andersson, Carter)."))
    if INTERACTIVE.search(text):
        if not FOCUS_VISIBLE.search(text):
            findings.append((SEVERE, "no-focus-visible", 0,
                             "Interactive elements without any :focus-visible styling. Keyboard focus must be visible (desktop-craft.md #2)."))
        if not HOVER.search(text):
            findings.append((WARN, "no-hover-states", 0,
                             "Interactive elements without any :hover styling. Dead hover is a top generated-UI tell."))
    if HAS_MOTION.search(text) and not REDUCED_MOTION.search(text):
        findings.append((WARN, "no-reduced-motion", 0,
                         "Motion present without a prefers-reduced-motion path (Kowalski, accessibility.md)."))

    # Hardcoded hexes outside token blocks
    token_zone = "".join(m.group(0) for m in ROOT_BLOCK.finditer(text))
    all_hexes = set(HEX.findall(text))
    token_hexes = set(HEX.findall(token_zone))
    stray = all_hexes - token_hexes
    if len(stray) > 6:
        findings.append((WARN, "stray-hexes", 0,
                         f"{len(stray)} hex colors outside :root/theme token blocks. Colors belong to semantic tokens (SKILL.md output standards)."))
    return findings


def collect(paths):
    files = []
    for p in map(Path, paths):
        if p.is_dir():
            files += [f for f in p.rglob("*") if f.suffix.lower() in EXTS]
        elif p.suffix.lower() in EXTS:
            files.append(p)
    return files


def main(argv):
    strict = "--strict" in argv
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 0
    files = collect(paths)
    if not files:
        print("lint_slop: no HTML/CSS/JSX/TSX/Vue/Svelte files found.")
        return 0
    severe_total = warn_total = 0
    for f in files:
        try:
            findings = lint_text(f.read_text(errors="ignore"), f)
        except OSError as e:
            print(f"  ?  {f}: unreadable ({e})")
            continue
        for level, name, line, msg in findings:
            loc = f"{f}:{line}" if line else str(f)
            print(f"  {level:6} [{name}] {loc}\n         {msg}")
            if level == SEVERE:
                severe_total += 1
            else:
                warn_total += 1
    print(f"\nlint_slop: {len(files)} file(s), {severe_total} severe, {warn_total} warnings.")
    if severe_total or (strict and warn_total):
        print("Fix severe items, or justify each in the design's point of view before delivering.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
