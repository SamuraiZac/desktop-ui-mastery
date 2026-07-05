# Karri Saarinen - Opinionated Software and Craft as Strategy

Co-founder and CEO of Linear; previously principal designer at Airbnb (design systems) and Coinbase. Saarinen is the clearest living argument that in mature markets, craft and opinion are the differentiator: Linear entered the most crowded category in software (issue tracking) and won mindshare on quality of feel and strength of point of view.

## Core principles, translated to desktop UI

1. **Opinionated beats configurable.** Linear ships one good workflow instead of a settings page of workflows. Decide how the tool believes work should be done, and build that path to perfection. Every preference you add is a decision you refused to make and a permanent tax on every future feature.
2. **Speed is a design feature, and the spec is measurable.** Interactions should complete in under 100ms perceived. Achieve it with optimistic UI (apply locally, sync later), local-first data, preloading, and skeleton-free instant rendering. A fast mediocre interface feels better than a slow beautiful one; a fast beautiful one is unbeatable.
3. **Craft is a company habit, not a polish phase.** "Quality of the product is the accumulation of hundreds of small decisions." Sweat the defaults: default column widths, default ordering, first-run state. Users live in your defaults.
4. **Design the system, then the screens.** From his Airbnb DLS work: tokens, primitives, and composition rules first, so a small team ships large surface area coherently. Screens designed one-off drift immediately.
5. **Keyboard is a first-class citizen, not an accelerator layer.** Every action reachable by keyboard; the command menu (Cmd+K) as the universal verb surface; single-key shortcuts for the daily loop. Power users are made, not found: the UI teaches shortcuts contextually.

## Signature moves to steal

- **The dark, quiet instrument aesthetic.** Near-black surfaces stepped by subtle tone (not borders), one restrained accent, small crisp type, generous line-height, everything slightly desaturated using perceptual color (LCH/OKLCH) so greys feel neutral at every step. Steal the tonal-stepping method and perceptual ramps, not the exact palette.
- **Optimistic everything.** No spinners for local actions. The change appears instantly; conflicts reconcile in the background; failures surface as gentle corrections.
- **Contextual menus that mirror the command menu.** Right-click, Cmd+K, and toolbar expose the same verb set with the same names and shortcuts, so learning transfers.
- **Density with air.** Linear's lists show a lot per screen yet feel calm: one-line rows, meta-data in muted tone, hover-revealed actions. Steal the pattern of progressive disclosure on hover.

## Never copy

- The literal Linear look (its exact sidebar structure, its purple, its row anatomy). It is the most cloned aesthetic in software right now, and shipping it marks the product as a follower. Use the reasoning to reach a different visual conclusion.
- Opinionation in domains you do not understand. Linear earned its opinions from deep domain conviction. Strong opinions plus shallow domain knowledge produces arrogant software.

## Interrogation questions

What does this product believe about how the work should be done? Which settings can be deleted by making a decision? Is the primary loop under 100ms perceived? Can a user do a full day of work without the mouse?
