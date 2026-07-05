# Bret Victor - Direct Manipulation and Live Representations

Interface researcher, former Apple Human Interface Inventor, author of the talks and essays Inventing on Principle, Learnable Programming, Up and Down the Ladder of Abstraction, Magic Ink, and A Brief Rant on the Future of Interaction Design. Now Dynamicland. Victor is this skill's primary engine for "imagining the future": he provides principled reasons why most current UI is a historical accident, and concrete alternatives.

## Core principles, translated to desktop UI

1. **Creators need an immediate connection to what they create.** Any delay between action and consequence (edit, then compile, then look; type into a form, then submit, then see) severs understanding. The future of desktop tools is live: the result updates while the parameter changes. If your design has an Apply button, ask hard why the change cannot simply be live with undo.
2. **Show the data, show the comparisons, show the process over time.** A number you can only see one value of is nearly blind. Every adjustable value should reveal its neighborhood: scrub it, see the outcome sweep. This is the ladder of abstraction: let users move between the concrete single case and the abstract space of all cases.
3. **Most software is information software, and information software is graphic design, not conversation.** From Magic Ink: users mostly want to learn something and decide, not to operate widgets. Cut interaction (clicks, forms, navigation) wherever better information graphics can answer the question at a glance. Interaction is a cost, not a feature.
4. **Context inference over interrogation.** Great information software infers what the user wants from environment and history instead of asking. The train-schedule app should already show the next train home. Desktop translation: use time of day, recent activity, and current selection to pre-answer, and let the user correct rather than specify from scratch.
5. **Reject "pictures under glass" as an endpoint.** Victor's rant: hands and bodies are capable of far more than tapping flat rectangles. Even within a desktop, prefer manipulating the thing itself (drag the deadline on the timeline, resize the allocation bar) over manipulating a form about the thing.

## Signature moves to steal

- **Scrubbable values.** Any number in the UI can be dragged to change, with everything downstream updating live. The single cheapest way to make a tool feel ten years ahead.
- **Preview-on-hover of consequences.** Hovering a destructive or transformative action shows what would happen (ghost state, diff) before commitment. Undo becomes redundant confidence rather than the safety net.
- **Multiple simultaneous representations.** The same object shown as visual, as data, and as timeline, all live-linked; edit any one, all update. Kills the mode-switching tax.
- **Explain state by showing history.** Instead of a mysterious current state, show the trajectory: how this number got here, what changed it. Time is data.

## Never copy

- Demo-ware maximalism. Victor's prototypes make every pixel live because they are arguments. Shipping tools need a hierarchy of liveness: the 100x-a-day loop gets full liveness; rare configuration can stay conventional.
- Dynamicland's physical-space program as a skin. Projected-paper aesthetics on a screen misses his point entirely.

## Interrogation questions

Where is the gap between action and consequence, and can it be closed to zero? Which form in this design could become direct manipulation of the artifact? What question is the user really asking, and could a graphic answer it before they interact at all?
