# Accessibility - The Hard Checklist

Accessibility principles appear throughout the library (Norman's signifiers, Freiberg's focus discipline, Carter's worst-case rendering, Raskin's humane laws). This file consolidates them into one enforceable pass. It is not optional polish: for desktop tools people use eight hours a day, accessibility failures are daily injuries, and most of these items make the product better for every user.

## Perception

- **Contrast, verified not eyeballed:** 4.5:1 minimum for text, 3:1 for large text (18px+/14px bold+) and for essential UI shapes (control boundaries, focus rings, icons that carry meaning), in BOTH themes. Dark themes fail this more often than light ones; muted-text-on-tonal-surface is the usual casualty.
- **Color never carries meaning alone.** Status conveyed by color gets a second channel: icon shape, label, position, or weight. Test with a grayscale filter; if statuses become indistinguishable, add the channel.
- **Respect OS text scaling.** Layouts survive 125-200% scaling: no clipped labels, no overlapping controls. Use rem-based or scalable sizing for text containers even in dense UI.
- **prefers-reduced-motion honored globally:** movement replaced with opacity-only or instant transitions. One media query in the token layer (see derive_tokens.py output) covers the product if all motion uses the tokens.
- **prefers-contrast: more** gets a genuine response where supported: stronger borders, darker muted text.

## Operation

- **Complete keyboard path** (desktop-craft.md #2 is the spec): every action reachable, logical tab order, focus visible always (2px offset ring at 3:1 contrast against its background), focus trapped in dialogs and returned to the trigger on close, no keyboard traps anywhere.
- **Hit targets:** 24px minimum effective size for pointer targets in dense desktop UI, larger for frequent actions; invisible padding may provide it (freiberg).
- **Timing under user control:** no content that disappears on a timer without pause/hover-hold (toasts pause on hover); no forced timeouts on reading or input.
- **Shortcuts do not trap:** single-character shortcuts only when focus is outside text inputs; all shortcuts remappable or at least documented; no OS/AT shortcut collisions.

## Understanding

- **Every control is named:** visible label, or aria-label where the design is icon-only. Icon-only buttons without accessible names are the most common desktop-app failure.
- **State is exposed, not just drawn:** aria-pressed on toggles, aria-selected on rows and tabs, aria-current on navigation, aria-expanded on disclosures, aria-sort on table headers. If the exemplars pattern is followed, this comes free.
- **Errors identify, explain, and point forward** in text adjacent to the field, announced via a live region, never by color alone (norman: blameless, actionable).
- **Live regions for what changes without user action:** sync status, background completions, bulk-selection counts (aria-live="polite"; assertive only for urgent safety).

## Structure for assistive tech

- Semantic roots: real button/table/nav/dialog elements before ARIA imitations; ARIA only to fill genuine gaps (combobox, listbox, grid patterns per the ARIA Authoring Practices).
- Headings form a real outline; landmarks (main, nav, complementary) partition the shell; the app's regions are traversable by landmark navigation.
- Custom components implement the full expected keyboard pattern for their role (a listbox arrows and type-aheads; a menu wraps and Escapes; a grid arrows in two dimensions), not just click handlers with a role attribute.

## The pass (run before delivering)

1. Unplug the mouse: complete a real task start to finish.
2. Tab the whole surface: focus always visible, order sensible, no traps.
3. Grayscale filter on: statuses still distinguishable.
4. Contrast-check the five most-used text/background pairs in both themes.
5. Screen-reader spot check (VoiceOver/NVDA): shell landmarks, one table, one dialog, one toggle; names and states announced.
6. Reduced-motion on: nothing still moves; nothing depends on animation to be understood.
7. OS text scaling at 150%: nothing clips or overlaps.
