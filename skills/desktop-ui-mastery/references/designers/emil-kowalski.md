# Emil Kowalski - Motion Restraint

Design engineer (Linear, previously Vercel); creator of Sonner (the toast library), Vaul (drawer), and the course Animations on the Web. Kowalski is the field's clearest current articulation of taste in interface motion: when to animate, when not to, and why most animation in software should be deleted. He is the counterweight that keeps this skill's futurism from becoming a motion-graphics reel.

## Core principles, translated to desktop UI

1. **Animation must earn its existence.** Valid reasons: explaining a spatial relationship (where the panel came from), preserving continuity of an object across states, providing feedback, or adding deliberate character in a low-frequency moment. "It looks nice" is not a reason. Default is no animation; motion is opt-in per case.
2. **Frequency determines budget.** An interaction performed 100 times a day gets 0-120ms of motion or none at all; an onboarding moment seen once can afford 400ms of personality. Animating the hot path is how delightful demos become irritating tools. This single rule prevents most motion mistakes.
3. **Fast and springy over slow and smooth.** Desktop motion lives in the 120-260ms range with ease-out (fast start, settling end) so the interface feels like it responds, then rests. Ease-in on entrances reads as hesitation. Springs (modest stiffness, near-critical damping, no bounce for utility UI) make motion interruptible and natural.
4. **Animate transforms and opacity only.** Position, scale, opacity: compositor-cheap, always smooth. Animating width, height, top, or box-shadow directly causes jank; use transform-based FLIP techniques for layout changes. Performance is part of taste; a dropped frame ruins a perfect curve.
5. **Origin-aware motion.** Things scale and fade from where they were invoked: a popover grows from its trigger, a dialog from the center or the initiating element, a toast slides from the edge it lives on. Motion that ignores origin breaks the physical model.

## Signature moves to steal

- **The 150ms utility transition.** Panels, popovers, menus: opacity 0 to 1 plus a 4-8px translate or 0.97 to 1 scale, ease-out, ~150ms. Enough to explain, too fast to wait for. The workhorse of desktop motion.
- **Exit faster than enter.** Dismissals at roughly 2/3 the entrance duration. Users have finished with the thing; do not make them watch it leave.
- **Stacked, swipeable, self-managing toasts** (the Sonner pattern): notifications collapse into a stack, expand on hover, pause timers on hover, and never block work. Steal the behavioral spec, not the library's exact look.
- **Continuity morphs for hierarchy changes.** When an item expands into a detail view, morph the shared elements (title, status) between states instead of cross-fading two unrelated screens. This is the highest-value place to spend motion budget.
- **Respect reduced-motion.** `prefers-reduced-motion` swaps movement for opacity-only transitions. Non-negotiable.

## Never copy

- Scroll-driven storytelling, parallax, and landing-page choreography inside tool UI. That grammar belongs to marketing (see fantasy.md) and reads as noise in an instrument.
- Bounce and overshoot on utility surfaces. Playful physics on a dropdown menu makes a serious tool feel like a toy.

## Interrogation questions

For each animation: what does it explain, and what is its frequency of exposure? Is anything on the hot path longer than 120ms? Do exits outpace entrances? Does everything move from its origin? What happens with reduced motion on?
