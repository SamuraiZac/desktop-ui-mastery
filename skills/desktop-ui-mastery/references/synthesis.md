# Synthesis - How to Steal Like an Artist

The method that turns the reference library into original work. "Steal like an artist" (Austin Kleon's formulation of a truth every master has stated) means: take the thinking, transform it through your problem, and produce something the source would not have made. Copying one master produces a clone. Copying the surface produces a costume. This file is the procedure for doing neither.

## The core rule: steal decisions, not artifacts

Every reference in this library is decomposed into principles, moves, and reasoning precisely so you never need to look at (or reproduce) a specific screen. If you find yourself specifying "a sidebar like Linear's," stop, and instead answer the question Linear answered: how does this product's navigation stay dense, calm, and keyboard-traversable? Your answer, derived from your domain, will differ, and that difference is the design.

## The procedure

### 1. Extract the problem's own character

Before choosing influences, write down: the domain's native data shapes (records? streams? documents? graphs?), the 100x-daily action, the emotional register (calm instrument? confident cockpit? warm companion?), and the one thing this product believes that competitors do not. Original design comes from the problem more than from the references; the references are lenses, not sources.

### 2. Choose 2-3 masters with deliberate tension

Pairs that already agree (Rams + Ive, Saarinen + Freiberg) produce competent pastiche. Pairs that argue produce ideas:

- **Tufte + Kowalski:** maximum data density with a strict motion budget; the animated sparkline that earns its 150ms.
- **Victor + N26:** live scrubbable consequences applied to money, where graphical integrity is an ethical constraint. What does "drag to preview the outcome" mean when the outcome is a fee?
- **Kare + Saarinen:** warmth and single-glyph clarity inside a dark keyboard-first instrument; where exactly does the one smile live?
- **Yuan + Apple HIG:** intention-organized computing that still honors Cmd+Z and the window system; the radical idea made adoptable.
- **Rams + Fantasy:** as little design as possible, plus one engineered signature moment; the argument between 100% instrument and 95/5.
- **Raskin + Coursey:** monotony (one good way) versus the everything-everywhere command layer; how many paths to an action does this product believe in?
- **Hara + Tufte:** emptiness as capacity versus maximum data density; usually resolved by zone, and deciding the zones is the design.
- **Norman + Matas:** every affordance signified versus chrome-free direct manipulation; how does an invisible interface stay learnable?
- **Kay/Wiggins + Saarinen:** malleable, user-shaped software versus opinionated, decided software; which parts of this tool belong to the user?
- **Fukasawa + Victor:** borrowed reflexes users already have versus invented live interactions nobody has seen; innovation spent only where behavior is broken.

Name the tension explicitly, then design the resolution. The resolution is where original work lives.

### 3. Write the point of view (before any pixels)

Three to five sentences: what this interface believes, which conventions it honors, which single convention it breaks and why, where its motion/color/personality budgets are spent. If two different products could share this paragraph, it is not yet a point of view.

### 4. Transform through constraints

Run the borrowed principles through the specifics: this data, this platform, this user's day, this density requirement. A principle that survives contact with real constraints comes out looking unlike its source. If the output still resembles the source, the constraints were not applied hard enough; add real data and re-derive.

### 5. The distance check

Before delivering, run three tests:

- **Attribution test:** a design director should be able to guess the influences from the reasoning ("Tufte density, Things-like motion") but not point to a copied screen. If any single view maps to a nameable product's view, redesign that view.
- **Substitution test:** swap in a competitor's logo. If the design still fits them, it lacks a point of view; return to step 3.
- **Novelty ledger:** list what in this design exists nowhere in the reference library. There must be at least one entry: a pattern, a representation, a resolution of the chosen tension. If the ledger is empty, the synthesis produced only recombination, not invention; push the tension further.

### 6. Imagining futures (when the brief asks for it)

For future-of-UI work, weight Victor and Yuan, then discipline the speculation:

1. Define the primitives and their grammar (what are the atoms, how do they compose) before any visual.
2. Break exactly one paradigm assumption (apps, windows, files, forms, cursors) and keep the rest conventional; total novelty is unlearnable (see Arc's cautionary lesson in `studios/desktop-natives.md`).
3. Ship the fiction with an honest ladder back to the present: what version of this could be built this year. A future with no ladder is a mood board.

## Failure modes to catch in self-review

- **Single-source gravity:** the output drifted toward the strongest reference (usually Linear). Re-read the neglected master and re-balance.
- **Tension abandoned:** the stated tension got resolved by ignoring one side. The resolution must visibly contain both.
- **Style transfer:** principles were cited but the surface was copied anyway. Delete the surface, keep the reasoning, redraw.
- **Frankensteining:** one screen per influence, stitched. Synthesis happens within every screen, not across the screen list.
