# Exemplars - Anatomy, Not Looks

Four annotated, working reference implementations of the surfaces desktop apps most often get wrong. Every principle-bearing line cites its source file in the references library.

**These are anatomies to learn from, never skins to ship.** The proof is built into `app-shell.html`: a POV switcher renders three entirely different designs (instrument, paper, ledger) from the same markup by swapping tokens only. Anatomy is fixed; skin is derived. Derive yours with `scripts/derive_tokens.py` and record the choice in `DESIGN-POV.md`.

| File | Teaches |
|---|---|
| `app-shell.html` | Shell anatomy (top bar, sidebar, content, status bar), the accent budget, hover reveals without layout shift, honest sync state, and the anatomy-vs-skin proof |
| `data-table.html` | Density band, tabular figures, no vertical rules, sparklines, sticky header, the full desktop selection model (click, shift-range, ctrl-toggle, ctrl+a, arrows, space) with a visible bulk state |
| `command-palette.html` | The Cmd+K contract: instant fuzzy filter, full keyboard traversal, sections, shortcuts taught in place, origin-aware 150ms entrance with a faster exit |
| `settings-surface.html` | Settings without card soup: one row anatomy repeated with total consistency, sections by type and space, live application, consequence-scaled danger zone |

All four pass `scripts/lint_slop.py` with zero severe findings. The two remaining warnings are deliberately left in and justified in comments, modeling the correct response to a lint warning: name it and defend it in writing, or fix it. Never silently ignore it.

How to use during generation: read the exemplar closest to the surface being designed, adopt its anatomy and behavioral contracts, then derive an original skin from the brief's point of view. If the output could be mistaken for the exemplar's skin, the derivation step was skipped.
