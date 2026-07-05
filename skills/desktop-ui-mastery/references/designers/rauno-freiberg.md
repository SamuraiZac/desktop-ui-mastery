# Rauno Freiberg - Invisible Interaction Details

Staff design engineer at Vercel, previously at The Browser Company designing and building the Arc browser; author of the essay "Invisible Details of Interaction Design", the craft catalog at rauno.me, the open Web Interface Guidelines, and the interaction manual Devouring Details. Freiberg's territory is the last 10% of feel: the hover states, focus rings, selection behaviors, and micro-timings that users never consciously notice but that entirely determine whether software feels crafted or cheap. This file is the checklist voice of the skill.

## Core principles, translated to desktop UI

1. **Interfaces are physical systems.** Metaphors of weight, momentum, and continuity make software comprehensible: things come from somewhere and go somewhere; nothing teleports. Every appearance and disappearance should answer "from where?" and "to where?", even with a 120ms fade-and-shift.
2. **The details are not polish, they are the design.** A product with correct structure but dead interactions reads as a prototype. Budget the interaction pass as a first-class phase, with its own review.
3. **Feedback within 100ms, always.** Every press, drag, and keystroke produces immediate acknowledgment: a pressed state, an optimistic update, a cursor change. Silence after input is the strongest cheapness signal that exists.
4. **States are the design surface.** Default, hover, active, focus-visible, selected, disabled, loading, error, empty, overflowing. A component is not designed until all its states are; most cloned-looking UI copied only the default state.
5. **Respect the platform's reflexes.** Text selectability where users expect it (and not on labels/buttons), correct cursors, right-click doing something useful, standard shortcuts unhijacked, scroll behavior native. Fighting reflexes burns trust invisibly.

## Signature moves to steal (the checklist)

- **Focus-visible done properly.** A high-contrast 2px ring, offset from the element, appearing for keyboard navigation. Never `outline: none` without replacement. Tab through the entire app as a test.
- **Hover reveals, never layout shifts.** Row actions appear on hover via opacity, reserved space, or overlay; the row must not change height or push content.
- **Hit targets larger than visuals.** Small icons get invisible padded hit areas (min ~32px effective on desktop, more for frequent targets). Fitts's law is a law.
- **Interruptible, redirectable motion.** Animations driven by springs or cancellable transitions so a second click mid-animation retargets instead of queueing. Queued animation feels like lag.
- **Optical over mathematical alignment.** Nudge icons next to text baselines, compensate glyph side-bearings, center triangles by their visual mass. Trust the eye over the number.
- **Keyboard-and-pointer parity for selection.** Lists support shift-click ranges, cmd-click toggles, arrow-key movement, type-ahead jump. This quartet is what separates desktop software from a webpage.
- **Scroll position and selection persistence.** Navigating away and back restores exactly where the user was. Losing scroll state tells users their attention is disposable.

## Never copy

- His published component recipes wholesale (they are widely recognized in the craft community; direct lifts are identifiable).
- Detail obsession before structure. Freiberg's layer is the final 10%; applying it to a wrong information architecture is lacquering a bad chair.

## Interrogation questions

Tab through every screen: is focus always visible and logical? Does anything appear or vanish with no spatial explanation? Do all lists support range selection and type-ahead? What acknowledges each input within 100ms?
