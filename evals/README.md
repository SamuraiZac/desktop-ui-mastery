# Evals

## Results: five briefs, two tiers of finish

Five of the fourteen briefs in `briefs.json` were run end to end against baselines representing the documented statistical center of AI-generated UI. All ten HTML files are in `baseline/` and `with-skill/`.

**Two briefs were taken to full visual polish** (dash-fleet and finance-treasury); their screenshots and labeled comparisons are in `gallery/` and at the top of the main README. **Three stop at mechanics-verified drafts** (settings-sync, admin-claims, utility-clip): correct anatomy, keyboard paths, states, tokens, and lint-clean, but not brought to the craft bar, and therefore not shown as gallery images.

That gap exists on purpose, because the first full run of this eval produced it by accident and the lesson was worth keeping: **the initial with-skill outputs passed the linter and were still joyless grey wireframes** (uniform 12px text, unstyled native selects, signature elements that failed the squint test). Lint-clean is the floor, not the finish. That failure is now encoded in the skill as the craft pass in `references/critique-and-deslop.md`, and the two polished briefs are what the workflow produces when that pass is actually run against the rendered output.

| Brief | Baseline lint | With-skill lint | Finish |
|---|---|---|---|
| dash-fleet | severe findings | 0 severe, 0 warnings | Full craft pass |
| finance-treasury | severe findings | 0 severe, 0 warnings | Full craft pass |
| settings-sync | severe findings | 0 severe | Mechanics-verified draft |
| admin-claims | severe findings | 0 severe | Mechanics-verified draft |
| utility-clip | severe findings | 1 justified warning | Mechanics-verified draft |
| **Totals** | **13 severe, 17 warnings** | **0 severe, 1 justified warning** | |

Each with-skill file carries its point of view, lens pair, token derivation, and novelty-ledger entry as a header comment. No two share a palette, structure method, or temperature, and none reproduces the exemplars' skins.

## Methodology, honestly

These runs were produced and judged by the same model family the skill targets, in one environment, with baselines written to represent default generation rather than sampled from a fresh skill-free session. They are a demonstration with receipts, not an independent benchmark. The lint numbers are deterministic and reproducible; the visual judgment is yours to make from the gallery and the raw HTML. For independent numbers, run the full set in your own Claude Code with and without the skill and blind-compare against the grading assertions in `briefs.json`. If your results disagree, open an issue with outputs attached.

## Running the full set

1. In a scratch project WITHOUT the skill, run each brief; save to `evals/baseline/<id>/`.
2. Install the skill and repeat into `evals/with-skill/<id>/`.
3. `python3 skills/desktop-ui-mastery/scripts/lint_slop.py` over both sets; record counts.
4. Blind-compare shuffled pairs against the grading list, INCLUDING the craft pass from `references/critique-and-deslop.md` on rendered output.
5. Screenshot winners into `evals/gallery/` and link them from the README.
