# Desktop Natives - Linear, Raycast, Things, Arc

The current masters of shipped desktop software. Where the designer files give voices and the Apple file gives conventions, this file gives living proof: four products that define what "great desktop app" means right now, each for a different reason. Study the reasoning; the looks are all heavily imitated and therefore off-limits as surfaces.

## Linear - the instrument

(Deep dive in `designers/karri-saarinen.md`; summary here for comparison.)
Teaches: opinionated workflow over configuration, sub-100ms optimistic interactions, keyboard-first with Cmd+K as the verb surface, tonal dark density. Its meta-lesson: in a commodity category, feel is the moat.

## Raycast - the invisible app

A launcher/command platform that replaced the app-window paradigm with a summonable palette. Teaches:

1. **Zero-UI resting state.** The best interface for a 50x-a-day tool may be no persistent interface at all: a hotkey, a field, results, gone. Ask of any utility feature whether it should be a screen or a summonable command.
2. **Everything is a list with actions.** One master interaction pattern (filterable list, Enter for primary action, Cmd+K for the action menu on any item) scales to thousands of extensions without new UI concepts. Steal the economy: one pattern, infinitely reused, beats fifty bespoke screens.
3. **Latency as identity.** Raycast's entire brand is that it appears instantly. For utilities, performance is not a feature of the design; it is the design.
4. **A platform needs a design system with teeth.** Third-party extensions look native because the component kit is constrained. When designing extensible surfaces, constrain harder than feels polite.

## Things (Cultured Code) - the quiet craft object

The most refined personal task manager on Apple platforms; famously slow-moving, famously polished. Teaches:

1. **Whitespace as structure in a light UI.** Things achieves hierarchy almost without lines or boxes: type, spacing, and indentation carry the whole structure. The light-mode counterpart to Linear's tonal dark method.
2. **Motion as physical explanation.** Its transitions (a task opening in place into an editing card, lists sliding as real sheets) are the reference standard for origin-aware, sub-300ms, meaning-carrying animation. Kowalski's principles, shipped a decade early.
3. **Restraint as a feature policy.** Every addition is weighed against the calm of the whole. The product says no constantly and is loved for it. Design corollary: a coherent small product beats an incoherent large one.
4. **Ceremony for capture, zero ceremony for everything else.** The magic-plus button and quick-entry hotkey make adding a task instant from anywhere; organizing can wait. Identify your product's capture moment and make it frictionless above all else.

## Arc (The Browser Company) - the brave experiment

A radical rethink of the browser: sidebar tabs, spaces, ephemeral tab hygiene, personality-forward design. Teaches, including by its failures:

1. **Interrogate inherited chrome.** Arc asked why tabs must be a top strip and why they must live forever, and found better answers (vertical spatial organization, auto-archiving). Every legacy element of your category deserves the same interrogation.
2. **Opinionated defaults with escape hatches.** Auto-archiving tabs shipped as default-on with a setting; radical behavior became adoptable because it was reversible.
3. **Personality is memorable and polarizing.** Arc's voice, easter eggs, and visual identity created devotion competitors could not, and also alienated users who wanted a tool, not a companion. Dose personality by audience: consumer tools can flirt; professional instruments should mostly stand back.
4. **The cautionary lesson.** Arc's complexity ceiling (too many novel concepts stacked) eventually led its maker to restart simpler. Novelty budget is real: users absorb roughly one radical rethink per product. Spend it on the highest-leverage break and keep everything else conventional.

## Cross-cutting synthesis

All four converge on: one master interaction pattern, keyboard as first-class, sub-perceptual latency, motion only where it explains, and a single deliberate break from convention. They diverge on tone (instrument vs companion) and surface (dark tonal vs light spatial). The divergence is the design space this skill should explore; the convergence is the floor it should never go below.
