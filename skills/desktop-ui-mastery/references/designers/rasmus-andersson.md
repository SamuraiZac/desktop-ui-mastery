# Rasmus Andersson - Systems Typography

Designer-engineer: created Inter, the open-source interface typeface used across much of modern software; early designer at Spotify (led its early product design language), Dropbox, Figma; founder of Playbit. Andersson represents the discipline where typography, engineering, and design systems are one practice. For desktop UI, where text is 90% of the interface, his lens is decisive.

## Core principles, translated to desktop UI

1. **The interface is typography.** Buttons, tables, menus, labels: nearly everything on a desktop screen is set text. Before choosing colors or illustrations, get the type system right and most of the design is done. A great UI with mediocre type does not exist.
2. **Design for the rendering reality.** Inter exists because text on screens at 11-14px behaves differently from print: it needs a tall x-height, open apertures, loose default spacing, and disambiguated glyphs (Il1, 0O). Choose and configure typefaces for the actual sizes and rasterization of the target platform, and test on a non-retina display, because your users have them.
3. **Features are functional, not decorative.** Use OpenType deliberately: tabular numbers (tnum) in every table, timer, and price so digits align; slashed zero where 0/O confusion costs money; case-sensitive forms in all-caps labels; contextual alternates off where precision matters. These settings are design decisions.
4. **Tools shape output; build the tool.** Andersson builds his own instruments (typefaces, software, languages) when existing ones impose the wrong constraints. Translation: encode the type system as tokens and components so the good decision is the default and drift is impossible.
5. **Open and systematic beats precious.** Inter is open source and versioned like software. Treat the design language the same way: documented, versioned, contributable, with rationale attached to every token.

## Signature moves to steal

- **A compact, purposeful scale.** Desktop apps need few sizes used consistently: roughly 11px (dense meta), 12px (secondary), 13px (body/default UI), 15px (section), 20px (page title). Steal the discipline of a small scale with assigned roles, not these exact values.
- **Weight and tone before size.** Create hierarchy inside a single size using weight (regular vs medium) and color tone (primary vs muted) first; change size only between levels of structure. This keeps dense screens calm.
- **Optical sizing awareness.** Larger display text wants tighter letter-spacing and can afford lighter weight; small UI text wants slightly looser spacing and sturdier weight. Apply tracking as a function of size.
- **Line-height by context.** Tight (1.2-1.3) for headings and single-line UI labels, comfortable (1.5) for reading paragraphs. One global line-height is always wrong somewhere.

## Never copy

- Inter-by-default without thought. Inter is excellent, but it is also the visual signature of a thousand identical products. Consider platform-native stacks (SF Pro, Segoe) for native feel, or a deliberately chosen alternative when differentiation matters. If you use Inter, use its features (tnum, ss01) rather than just its name.
- Spotify's brand era he worked on. That is identity design owned by a company, not a transferable principle.

## Interrogation questions

Is every table using tabular figures? How many type sizes exist, and does each have one job? Was the type tested at real UI sizes on a standard-DPI screen? Which OpenType features are doing functional work?
