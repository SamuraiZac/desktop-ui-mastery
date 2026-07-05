---
name: desktop-ui-mastery
description: Design world-class desktop application interfaces by synthesizing principles from 30 masters of design history (Rams, Kare, Ive, Tufte, Victor, Kay, Raskin, Norman, Vignelli, Eames, Hara, and more) and the defining studios and products (Apple macOS, Fantasy, N26, Linear, Raycast, Things, Arc). Use this skill whenever the user wants to design, build, redesign, critique, review, deslop, or imagine a desktop app UI, an Electron or Tauri app, an app shell, a dashboard, a panel layout, a command palette, a settings screen, a data table, or any native-feeling desktop interface, even if they do not say "desktop" explicitly. Also use it when the user asks for UI that feels like Apple, Linear, or Stripe quality, asks why their UI looks generic or AI-generated, asks for a design system or tokens for an app, or asks to imagine the future of an interface. Do NOT use it to produce pixel copies of existing products.
---

# Desktop UI Mastery

Design desktop application interfaces at the level of the best work in the field by stealing reasoning (never pixels) from 30 masters. A reasoning library plus working machinery: exemplar anatomies, a token derivation engine, a slop linter, and a synthesis method that forces original output.

## Prime directive

Every output must pass this test: **a design director could name the influences from the reasoning, but could not name a single screen it was copied from.** Copy decisions, constraints, and taste. Never copy the artifact.

## Modes

Detect which mode the request is, and follow its procedure:

- **Generate** (design/build something new): full workflow below.
- **Critique** (review/judge existing UI): run `scripts/lint_slop.py` on the files, then read `references/critique-and-deslop.md` and run the six-step critique.
- **Deslop** (fix generic or AI-looking UI): run the linter, then the deslop procedure in `references/critique-and-deslop.md`; optionally continue into Generate for direction.
- **Envision** (imagine the future of X): weight the Paradigm tier, follow the futures section of `references/synthesis.md`.

## Generate workflow

1. **Frame before visuals.** What is the app for, who uses it daily, what is the one action performed 100x a day, what is the emotional register? The 100x action defines the interface.
2. **Check for design memory.** If the project contains a `DESIGN-POV.md`, read it and treat its decisions as binding unless the user overrides. If it does not exist and this is a real project, create one from `templates/DESIGN-POV.md` at the end of the session. This keeps every future session consistent.
3. **Select 2-3 lenses using the matrix below,** deliberately mismatched: one foundational or paradigm voice plus one modern craft voice minimum. Read those designer files. Tension between lenses produces originality; agreement produces pastiche.
4. **Always read `references/desktop-craft.md`** (the non-negotiable mechanics) and, for Electron/Tauri targets, `references/web-desktop.md`.
5. **Read the nearest exemplar** in `exemplars/` (shell, table, palette, or settings). Adopt its anatomy and behavioral contracts; its skin is off-limits. The exemplar README explains the anatomy-vs-skin split.
6. **Derive the token system**, do not pick one: run `scripts/derive_tokens.py --hue H --temperature T --density D --register R` with values argued from the brief, or derive equivalent tokens by hand following its structure. Record the invocation in DESIGN-POV.md.
7. **Write the point of view** (3-5 sentences: what this interface believes, which conventions it honors, the one it breaks and why, where its budgets are spent), consulting `references/synthesis.md` for the recombination method. Then generate.
8. **Verify against reality, not intention.** Run `scripts/lint_slop.py` on the output: zero severe findings, and every remaining warning either fixed or justified in the point of view. **Lint-clean is the floor, not the finish**: the linter cannot see hierarchy, rhythm, or control craft, and a lint-clean design can still be a joyless grey wireframe. After the lint, run the craft pass in `references/critique-and-deslop.md` against the rendered output. If the environment can render (browser, screenshot tool), look at the actual output and run the eight-point checklist in `desktop-craft.md` section 8 against what is seen, including a keyboard-only walkthrough and a realistic-load check. Then run the synthesis distance checks (attribution, substitution, novelty ledger), revise once, and deliver with the point of view attached. Also apply `references/accessibility.md`'s final pass.

## Lens selection matrix

Pick from the relevant row, then add one voice from a different tier for tension:

| Brief type | Primary lenses | Tension partner |
|---|---|---|
| Dashboard / analytics / financial data | Tufte, Vignelli | Kowalski or Fantasy (one signature viz) |
| Dense operational tool / admin | Saarinen, Tufte, Raskin | Hara (where can it breathe) |
| Creative tool / canvas / editor | Kay, Matas, Cooper | Rams (deletion pass) |
| Notes / knowledge / thinking tool | Ryo Lu, Wiggins, Hara | Norman (model clarity) |
| Money / regulated / high-stakes | N26, Taylor, Norman | Ording (physics for trust moments) |
| Utility / launcher / companion app | Raycast lens (desktop-natives), Coursey, Chaudhri | Kare (the one warm glyph) |
| Onboarding / first-run / marketing-adjacent | Fantasy, Eames, Rand | Kowalski (motion discipline) |
| AI-native features | Singer, Ryo Lu, Victor | Raskin (mode safety) |
| Iconography / visual identity | Kare, Rand, Vignelli | - |
| Type system / tokens | Andersson, Carter, Vignelli | - |
| Motion / interaction feel | Kowalski, Ording, Castilho, Brichter | Raskin (habituation) |
| Future concepts | Victor, Kay, Yuan, Cooper, Wiggins | Apple HIG (the ladder back) |
| Any brief, final pass | Freiberg (details), Norman (gulfs), Ive (inevitability) | - |

## The library

### Designers (`references/designers/`)

**Form and foundations:** `dieter-rams` (reduction) · `paul-rand` (form and content, wit) · `massimo-vignelli` (semantic discipline, grid) · `charles-ray-eames` (details, the good host) · `kenya-hara` (emptiness as capacity) · `naoto-fukasawa` (without thought, affordance) · `matthew-carter` (design for the worst rendering case) · `susan-kare` (meaning at small sizes) · `edward-tufte` (data density) · `jony-ive` (inevitability, material honesty)

**Paradigm and humane computing:** `alan-kay` (user illusion, medium) · `jef-raskin` (modes, habituation, attention) · `don-norman` (affordances, mappings, errors) · `muriel-cooper` (information landscapes) · `bret-victor` (direct manipulation, liveness) · `jason-yuan` (intention-organized futures)

**Interaction inventors:** `bas-ording` (interface physics) · `mike-matas` (content as the interface) · `loren-brichter` (inventing the default) · `imran-chaudhri` (attention as material)

**Modern craft and futures:** `karri-saarinen` (opinionated software, speed) · `rasmus-andersson` (systems typography) · `rauno-freiberg` (invisible details) · `emil-kowalski` (motion restraint) · `paco-coursey` (the command layer) · `mariana-castilho` (tactility) · `benji-taylor` (warm precision, trust) · `jordan-singer` (tools that design) · `ryo-lu` (blocks, AI in the document) · `adam-wiggins` (local-first, malleable software)

### Studios and products (`references/studios/`)

`apple-macos` (platform conventions, when to break them) · `fantasy` (cinematic vision, 95/5) · `n26` (trust through clarity) · `desktop-natives` (Linear, Raycast, Things, Arc)

### Method and machinery

- `references/desktop-craft.md` - mandatory mechanics, read every time
- `references/web-desktop.md` - Electron/Tauri: titlebars, per-OS divergence, killing browser reflexes
- `references/accessibility.md` - the hard checklist and final pass
- `references/synthesis.md` - steal-like-an-artist method and distance checks
- `references/critique-and-deslop.md` - review modes and the slop list
- `exemplars/` - four annotated working anatomies (shell, table, palette, settings) with the anatomy-vs-skin proof
- `templates/DESIGN-POV.md` - the design memory file created per project
- `scripts/derive_tokens.py` - full OKLCH token system derived from hue, temperature, density, register
- `scripts/lint_slop.py` - deterministic detection of generated-UI tells; zero severe findings before delivery

## Anti-patterns (reject and revise if any are true)

- **The stretched website:** centered column, marketing whitespace, mobile metrics at desktop scale.
- **The carbon copy:** any screen recognizable as a specific product's screen. Linear's exact sidebar, Family's exact sheets, Notion's exact blocks, or these exemplars' skins.
- **Trend soup:** styles chosen from a menu (glassmorphism, bento, gradient mesh) instead of derived from a stated principle.
- **Mouse-only thinking:** no keyboard path to the primary action.
- **Empty-state-only design:** unvalidated at 400 rows, long strings, zero data, and error states.
- **Decoration without information:** pixels carrying no data, structure, or affordance.
- **Motion as garnish:** animation that explains no spatial or causal relationship.
- **Single-source gravity:** output drifting to the most familiar reference (usually Linear) regardless of chosen lenses.

## Output standards

- Interface typeface at desktop sizes with tabular figures in all numeric contexts (see `rasmus-andersson.md`, `matthew-carter.md`).
- Semantic tokens with light and dark from day one (derive_tokens.py structure); accent spent on a handful of elements per screen.
- Real, plausible content everywhere; lorem ipsum and John Doe are banned and linted.
- The written point of view ships with every design; `DESIGN-POV.md` is created or updated when decisions change.
