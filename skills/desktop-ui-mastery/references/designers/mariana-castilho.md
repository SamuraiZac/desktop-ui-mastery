# Mariana Castilho - Tactility on Screen

Design engineer, creator of UI Labs (uilabs.dev), an open catalog of hand-built micro-interactions studied across the industry. Castilho's contribution is a working vocabulary of screen tactility: how hover, press, drag, and settle can make flat interfaces feel touchable, and how these details are designed in code, at 1:1 fidelity, as the primary medium.

## Core principles, translated to desktop UI

1. **Micro-interactions are the texture of software.** Between the macro layout and the visual style sits a third layer: how each element responds to approach, press, and release. This layer is what hands remember; two identical-looking products with different micro-layers feel entirely different.
2. **Design the response curve, not the state pair.** A press is not off-then-on; it is an envelope: how fast it responds, how far it travels, how it settles. Specify the curve (scale, translate, shadow over time) for the interactive primitives once, and reuse it everywhere for a coherent tactile identity.
3. **Build to judge.** Micro-interactions cannot be evaluated in static tools; her entire catalog exists as running code because timing lives at 60-120fps. The prototype is the spec.
4. **Small scope, total depth.** Each UI Labs piece perfects one interaction in isolation. Method to steal: extract the product's five most-touched primitives (button, row, toggle, input, drag handle) and craft each as a standalone study before integrating.
5. **Delight within utility budgets.** Her work is playful but exposure-aware: strong personality on low-frequency moments, restraint on the hot path, aligning with Kowalski's frequency rule from the craft side.

## Signature moves to steal

- **The press envelope.** Interactive elements compress subtly on press (scale 0.97-0.98, 80-120ms) and release with a soft spring, giving mouse clicks a tactile read.
- **Magnetic and proximity effects, dosed.** Elements that acknowledge cursor approach (subtle lift, icon tilt) on a few signature controls only.
- **Drag with weight.** Dragged items lift (shadow, slight scale), tilt faintly with velocity, and settle with a spring on drop, making reordering legible and satisfying.

## Never copy

- Her published studies verbatim; they are widely recognized within the craft community and function as her signed work.
- Catalog-completeness in one product. A product uses a handful of tactile signatures consistently; using twenty is noise.

## Interrogation questions

What do the five most-touched primitives feel like on press, and was that designed or defaulted? Is there one response-curve identity across the product? Which interactions were judged as running code rather than mockups?
