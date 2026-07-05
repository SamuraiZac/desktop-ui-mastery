# Don Norman - Affordances, Mappings, and Blameless Errors

Cognitive scientist, author of The Design of Everyday Things, coiner of the term user experience during his Apple years. Norman supplied the vocabulary the whole field thinks in: affordances and signifiers, natural mapping, feedback, conceptual models, the gulfs of execution and evaluation, slips versus mistakes. This file is the skill's psychological floor.

## Core principles, translated to desktop UI

1. **Affordance needs a signifier.** An affordance is what an element can do; a signifier is the perceptible evidence of it. Flat design's chronic failure is affordance without signifier: clickable things indistinguishable from labels. Every interactive element needs a visible or immediate-on-hover signal of its interactivity; every draggable region a hint of grip.
2. **Natural mapping.** Controls arranged to mirror their effects (the stove-knob problem). Panel toggles positioned on the side of the panel they control; ordering controls that match the visual order they affect; sliders oriented along the dimension they change.
3. **Close both gulfs.** Gulf of execution: can users figure out what action achieves their intention? Gulf of evaluation: after acting, can they tell what happened? Every feature is tested against both questions; most UX debt is one gulf left open.
4. **The conceptual model is the real deliverable.** Users build a mental story of how the system works from the interface alone, and predict behavior from that story. Design the model first (what are the objects, what persists, what syncs when), then make every surface consistent with it. Surprises mean the interface taught the wrong model.
5. **Errors are design failures, and slips differ from mistakes.** Slips (right intention, wrong action) are prevented by spacing, size, and undo. Mistakes (wrong intention from a wrong model) are prevented by clearer models and feedback. Error messages take system blame, state what happened, and offer the path forward.
6. **Emotion is functional.** Visceral, behavioral, reflective levels: attractive things work better because positive affect broadens thinking. Craft and beauty are usability features, not vanity, which is the bridge between Norman and the Ive/Saarinen lineage.

## Signature moves to steal

- **The signifier pass.** Screenshot the UI, mark everything interactive; show it to someone cold and ask them to mark what they believe is interactive. Diff the two.
- **Constraint-based error prevention.** Make wrong actions impossible or inert (disabled with a stated reason) rather than caught and scolded after.
- **Knowledge in the world.** Options visible or one keystroke away beat options memorized; menus, palettes, and tooltips over recall.

## Never copy

- Signifier maximalism: beveling and outlining everything returns to clutter. The signifier budget goes where confusion is measured, not everywhere.
- Norman's occasional anti-aesthetic pragmatism as license for ugliness; his own emotional-design work overrules it.

## Interrogation questions

What here is interactive but does not look it? What mental model does a first session teach, and is it the true one? For the last user error, was it a slip or a mistake, and what design change would have prevented it?
