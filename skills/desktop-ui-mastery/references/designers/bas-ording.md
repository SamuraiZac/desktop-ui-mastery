# Bas Ording - Interface Physics

Apple UI designer (1998-2013) whose prototypes defined how software feels in motion: inertial scrolling and the rubber-band bounce (the detail that reportedly convinced Jobs the iPhone was possible), the Dock's genie effect and magnification, Expose, pinch behaviors. Ording's craft is giving pixels believable physics so the interface becomes a place with laws rather than a slideshow of states.

## Core principles, translated to desktop UI

1. **Momentum and friction make virtual objects real.** Content that moves with inertia and decelerates naturally is understood by the body, not just the eye. Scrolling, panning, and dragging should carry velocity; abrupt full-stops read as broken.
2. **Boundaries push back.** The rubber-band bounce communicates the edge of content by resistance instead of a wall or an error. Translate: overscroll hints, panels that resist past their minimum then settle, values that spring back when dragged out of range. Limits explained by physics need no copy.
3. **Playful prototypes find the answer.** Ording built dozens of toy-like interactive prototypes; the ones that made people smile and immediately understand shipped. Feel decisions are discovered by building, never by discussing.
4. **Physics must be consistent to be believed.** One gravity per product: consistent friction curves, consistent spring stiffness, consistent notions of mass by element size. Mixed physics reads as cheap even to users who cannot say why.
5. **Delight through comprehension.** The genie effect is charming, but its job is spatial: it shows exactly where the window went. Every physical flourish must double as an explanation.

## Signature moves to steal

- **Velocity-aware interactions.** Flick-to-dismiss with follow-through; throwing a panel closed; scroll distance proportional to gesture energy.
- **Resistance as affordance.** Increasing drag resistance near invalid territory, teaching limits through the hand.
- **The smile test.** Prototype the interaction; if testers understand it instantly and smile, ship; if they only smile, cut.

## Never copy

- Bounce and elasticity pasted onto desktop UI wholesale; mouse-wheel and trackpad contexts have different physics expectations than touch. Derive constants for the input device actually in hand.

## Interrogation questions

Does moving content carry momentum? How does the user learn each boundary: by wall, by error, or by resistance? Is there exactly one physics in this product?
