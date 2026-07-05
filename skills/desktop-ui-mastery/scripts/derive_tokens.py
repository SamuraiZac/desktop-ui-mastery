#!/usr/bin/env python3
"""derive_tokens.py - Derive a complete desktop UI token system from a point of view.

Not a palette picker. You state the design's intent (hue, temperature, density,
register) and a full semantic token system is derived: OKLCH tonal ramps for
light and dark, semantic surface/text/border roles, one disciplined accent,
status colors, a compact desktop type scale, spacing, radii, and motion tokens.

Usage:
  python3 derive_tokens.py --hue 255 --temperature cool --density compact --register instrument
  python3 derive_tokens.py --hue 30 --temperature warm --density regular --register companion -o tokens.css

  --hue          0-360. The accent hue. Pick from the subject's world, not from habit.
  --temperature  warm | neutral | cool     (tints the neutral ramp)
  --density      compact | regular         (spacing + type scale)
  --register     instrument | companion    (contrast character + radii + motion)

Output is plain CSS custom properties: framework-agnostic, ready for
:root and [data-theme="dark"]. OKLCH keeps perceptual steps even, so greys
stay neutral and ramps stay consistent across hues (the Saarinen/LCH method).
"""
import argparse
import sys

TEMP_HUE = {"warm": 75.0, "neutral": 255.0, "cool": 240.0}
TEMP_CHROMA = {"warm": 0.008, "neutral": 0.0, "cool": 0.006}


def okl(l, c, h):
    return f"oklch({l:.3f} {c:.4f} {h:.1f})"


def neutral_ramp(temp, dark=False):
    """12-step neutral ramp, step 1 = app background, step 12 = highest-contrast text."""
    h = TEMP_HUE[temp]
    c = TEMP_CHROMA[temp]
    if not dark:
        lights = [0.985, 0.972, 0.955, 0.932, 0.90, 0.86, 0.76, 0.64, 0.52, 0.42, 0.30, 0.16]
    else:
        lights = [0.165, 0.19, 0.215, 0.245, 0.28, 0.33, 0.42, 0.52, 0.62, 0.72, 0.84, 0.955]
    return [okl(l, c, h) for l in lights]


def accent_set(hue, dark=False):
    if not dark:
        return {
            "accent": okl(0.55, 0.17, hue),
            "accent-hover": okl(0.50, 0.18, hue),
            "accent-subtle": okl(0.95, 0.03, hue),
            "accent-text": okl(0.99, 0.005, hue),
        }
    return {
        "accent": okl(0.68, 0.15, hue),
        "accent-hover": okl(0.74, 0.15, hue),
        "accent-subtle": okl(0.26, 0.05, hue),
        "accent-text": okl(0.14, 0.02, hue),
    }


def status_set(dark=False):
    l, c = (0.55, 0.15) if not dark else (0.70, 0.14)
    return {"success": okl(l, c, 150), "warning": okl(l + 0.12, c, 85), "danger": okl(l, c + 0.03, 25)}


DENSITY = {
    "compact": {
        "type": [("2xs", 10.5), ("xs", 11), ("sm", 12), ("base", 13), ("md", 15), ("lg", 18), ("xl", 22)],
        "space": [2, 4, 6, 8, 12, 16, 24, 32],
        "row": 30, "control": 26,
    },
    "regular": {
        "type": [("2xs", 11), ("xs", 12), ("sm", 13), ("base", 14), ("md", 16), ("lg", 20), ("xl", 24)],
        "space": [4, 6, 8, 12, 16, 20, 28, 40],
        "row": 36, "control": 30,
    },
}

REGISTER = {
    # radii tuned per register; motion: utility duration / entrance / exit
    "instrument": {"radius": [3, 5, 8], "motion": (140, "cubic-bezier(0.2, 0, 0, 1)", 100)},
    "companion": {"radius": [6, 10, 14], "motion": (180, "cubic-bezier(0.2, 0.8, 0.2, 1)", 120)},
}


def emit(args):
    d = DENSITY[args.density]
    r = REGISTER[args.register]
    lines = [
        "/* Derived by derive_tokens.py (desktop-ui-mastery)",
        f"   hue={args.hue} temperature={args.temperature} density={args.density} register={args.register}",
        "   Semantic roles only in components; raw ramp steps stay in this file. */",
        "", ":root {",
    ]

    def block(dark):
        ramp = neutral_ramp(args.temperature, dark)
        acc = accent_set(args.hue, dark)
        st = status_set(dark)
        out = [f"  --neutral-{i + 1}: {v};" for i, v in enumerate(ramp)]
        out += [
            "", "  /* Surfaces: separate regions by tone before borders, borders before shadows */",
            "  --bg-app: var(--neutral-1);",
            "  --bg-surface: var(--neutral-2);",
            "  --bg-raised: var(--neutral-3);",
            "  --bg-hover: var(--neutral-4);",
            "  --bg-active: var(--neutral-5);",
            "", "  /* Text: three tiers is enough */",
            "  --text-primary: var(--neutral-12);",
            "  --text-secondary: var(--neutral-10);",
            "  --text-muted: var(--neutral-8);",
            "", "  /* Borders */",
            "  --border-subtle: var(--neutral-4);",
            "  --border-strong: var(--neutral-6);",
            "", "  /* Accent: budget is a handful of elements per screen */",
        ]
        out += [f"  --{k}: {v};" for k, v in acc.items()]
        out += ["", "  /* Status */"] + [f"  --{k}: {v};" for k, v in st.items()]
        return out

    lines += block(dark=False)
    lines += [
        "", "  /* Type scale: each size has one job (see rasmus-andersson.md) */",
    ]
    lines += [f"  --text-{name}: {px}px;" for name, px in d["type"]]
    lines += [
        "  --font-ui: 'Inter', 'SF Pro Text', 'Segoe UI Variable', system-ui, sans-serif;",
        "  --font-mono: 'Berkeley Mono', 'JetBrains Mono', ui-monospace, monospace;",
        "  --leading-ui: 1.25;",
        "  --leading-prose: 1.5;",
        "", "  /* Spacing and metrics */",
    ]
    lines += [f"  --space-{i + 1}: {v}px;" for i, v in enumerate(d["space"])]
    lines += [
        f"  --row-height: {d['row']}px;",
        f"  --control-height: {d['control']}px;",
        "", "  /* Radii: nested inner = outer minus inset (see jony-ive.md) */",
    ]
    lines += [f"  --radius-{n}: {v}px;" for n, v in zip(("sm", "md", "lg"), r["radius"])]
    dur, ease, exit_dur = r["motion"]
    lines += [
        "", "  /* Motion: utility transitions; exits faster than entrances (see emil-kowalski.md) */",
        f"  --motion-utility: {dur}ms;",
        f"  --motion-exit: {exit_dur}ms;",
        f"  --motion-ease: {ease};",
        "}", "", '[data-theme="dark"] {',
    ]
    lines += block(dark=True)
    lines += [
        "}", "",
        "@media (prefers-reduced-motion: reduce) {",
        "  :root { --motion-utility: 0ms; --motion-exit: 0ms; }",
        "}", "",
        "/* Numeric columns everywhere: */",
        "/* .tnum { font-variant-numeric: tabular-nums; } */",
    ]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--hue", type=float, required=True)
    p.add_argument("--temperature", choices=list(TEMP_HUE), default="neutral")
    p.add_argument("--density", choices=list(DENSITY), default="compact")
    p.add_argument("--register", choices=list(REGISTER), default="instrument")
    p.add_argument("-o", "--out", default=None)
    args = p.parse_args()
    css = emit(args)
    if args.out:
        with open(args.out, "w") as f:
            f.write(css)
        print(f"Wrote {args.out}")
    else:
        sys.stdout.write(css)


if __name__ == "__main__":
    main()
