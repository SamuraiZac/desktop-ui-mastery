# Jef Raskin - The Humane Interface

Initiator of the Macintosh project at Apple (1979), designer of the Canon Cat, author of The Humane Interface (2000). Raskin is the field's most rigorous theorist of modes, habits, and attention: an interface is humane if it is responsive to human needs and considerate of human frailties. Where others give taste, Raskin gives laws.

## Core principles, translated to desktop UI

1. **Modes cause errors, by law.** A mode exists when the same user action produces different results depending on hidden system state. Habituation (the automation of repeated actions) is unstoppable, so users will fire the habitual gesture in the wrong mode; the error is the designer's fault. Hunt modes: toggle states without persistent visible indication, focus-dependent shortcuts, editing vs viewing states that look identical.
2. **Quasimodes are the humane alternative.** A mode maintained by continuous physical action (holding Shift, holding a key to peek) cannot be forgotten because the body is doing it. Prefer spring-loaded, hold-to-activate states over sticky toggles for anything transient.
3. **The user's attention is singular and precious.** Humans have one locus of attention. Anything that yanks it (badges, modal interruptions, layout shifts) has spent the scarcest resource in the system. Interruptions must queue politely at the periphery.
4. **Monotony is a virtue.** One good way to do a thing beats three; multiple redundant methods multiply what must be learned and split habits. (Direct tension with the everything-everywhere command surfaces of modern apps; resolving this tension is a design decision worth making consciously.)
5. **Measure the interface.** Raskin applied GOMS and Fitts's law to count keystrokes and predict task time. The daily loop deserves an actual count: how many actions from intention to done, and what could remove one?
6. **Never destroy the user's work; never make users feel stupid.** His two commandments. Autosave, universal undo, and blame-free error copy are moral requirements.

## Signature moves to steal

- **The mode audit.** Enumerate every hidden state that changes what an action does; give each a persistent visible indicator, convert it to a quasimode, or delete it.
- **Hold-to-preview.** Hold a key to peek at another state (original vs edited, before vs after), release to return. Habit-proof by construction.
- **The keystroke ledger.** Count actions for the five most frequent tasks; treat each removed step as a shipped feature.

## Never copy

- The Canon Cat's text-only, leap-key interaction model wholesale; it lost to the GUI for reasons. Raskin's laws transfer; his specific hardware answers mostly do not.

## Interrogation questions

Where does the same gesture do different things depending on invisible state? What currently steals the locus of attention, and could it queue instead? Can any user action destroy work irrecoverably?
