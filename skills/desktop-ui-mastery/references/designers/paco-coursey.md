# Paco Coursey - The Command Layer

Design engineer at Linear; previously at Vercel, where he built the design system, website, and dashboard; creator of cmdk, the open-source command-menu primitive behind countless Cmd+K implementations. Coursey's territory is the command layer as a designed object: search-first interaction, API design as interface design, and the discipline of building primitives others compose.

## Core principles, translated to desktop UI

1. **The command menu is the app's index.** A well-built Cmd+K surface exposes every verb and noun through one fast, fuzzy, keyboard-native field: navigation, actions, settings, and search unified. It converts feature sprawl into a flat, learnable namespace, and its contents are an honest audit of the product's vocabulary.
2. **Composable primitives beat finished components.** cmdk ships behavior (filtering, keyboard handling, accessibility) unstyled, letting every product keep its own skin. Design-system translation: encode interaction contracts at the primitive level and let visual identity vary above it; behavior is where consistency matters most.
3. **API design is interface design.** The props and slots a component exposes shape every UI built with it, exactly as controls shape user behavior. Name things for the mental model, make the default usage correct, make misuse hard.
4. **Speed and keyboard purity are the spec.** Instant filtering as you type, arrow-key traversal, Enter to commit, Escape to dismiss, no pointer required, no perceptible latency. A command layer that lags or drops keystrokes is worse than none; it teaches distrust of the fastest path.
5. **Craft in public.** Polished open-source primitives and detailed personal-site experiments as a career method: the work itself, inspectable, is the portfolio and the argument.

## Signature moves to steal

- **Nested command pages.** Selecting a command can open a scoped sub-menu (assign to..., move to...) within the same surface, keeping multi-step actions keyboard-native.
- **Verb-noun duality.** The palette accepts both directions: find the object then act, or pick the action then choose its target.
- **Loading-state honesty in search.** Async results appear under a stable instant local section, never reordering what the user is about to select.

## Never copy

- Command menus as a checkbox feature: a palette exposing 20% of the app's actions with inconsistent naming actively damages trust in the pattern.
- His minimal monochrome personal aesthetic as a product skin; it is a personal signature, widely imitated already.

## Interrogation questions

Is every action in the product reachable and correctly named in the command layer? Do the primitives enforce interaction contracts while leaving skin free? Can a result list change under the user's committed selection?
