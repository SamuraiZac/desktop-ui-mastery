# Trigger eval

Measures whether the skill's frontmatter description makes Claude Code invoke the
skill when it should — and stay quiet when it shouldn't. `queries.json` holds 20
realistic prompts: 10 that must trigger (including disguised ones — a file-pointed
component review, a keyboard-only warehouse tool, a "be brutal" critique) and 10
near-misses that must not (API design, PRDs, landing pages, iOS work, pixel-copy
requests).

```bash
python3 run_trigger_eval.py            # defaults: 3 runs/query, 8 workers, sonnet
```

Each run plants a probe command carrying the description into a throwaway project
directory and checks the `claude -p` event stream for whether the probe fires.
Exit code 0 means every query landed on the right side at majority vote.

Two shadowing traps to know about (both produce a false ~0% recall):

1. **Uninstall or disable the desktop-ui-mastery plugin before running.** An
   installed copy appears alongside the probe in every child session; the model
   invokes the real skill and the probe scores as a miss.
2. Probes must not share a project directory across concurrent workers — N
   identical probes in one `.claude/commands/` means each session picks one at
   random and recall collapses to ~1/N. The script isolates each run for this
   reason; keep that if you modify it.

The v1.1.1 description scored 94% train / 88% holdout accuracy with 100%
precision (zero false triggers) on this set, up from 78% / 83% for v1.1.0.
