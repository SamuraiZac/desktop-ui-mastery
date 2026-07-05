# Apple / macOS - Platform Conventions and When to Break Them

The relevant Apple for desktop apps is not the brand or the keynotes: it is the macOS Human Interface Guidelines and forty years of accumulated desktop convention (menu bar, windows, drag and drop, undo) that users have in their muscle memory. Apple's deepest lesson is that consistency is a gift you give users: convention spent wisely buys you attention for the places you genuinely innovate.

## What to internalize

1. **Conventions are pre-paid usability.** Cmd+S, Cmd+Z, Cmd+F, Cmd+W, Cmd+, for settings; Escape cancels; Return confirms; Space previews; drag and drop between apps; contextual menus everywhere. Honoring these costs nothing and violating any one of them creates friction the user blames on your whole product. Budget rule: break at most one deep convention per product, and only for a 10x payoff (Raycast broke "apps have windows"; that was its one break).
2. **The menu bar is the app's complete vocabulary.** Even in a custom-shell app, an exhaustive menu bar (or its equivalent command inventory) means every capability is discoverable, searchable (Help menu search), and shortcut-labeled. Design the full verb inventory before designing screens.
3. **Deference: content first, chrome recessive.** macOS renders controls in muted materials so documents and data carry the color and contrast. Match: chrome in tones, content in full contrast, accent color reserved for interactive emphasis.
4. **Windows are real objects.** Resizable with sensible minimums, state restored on relaunch, full-screen and split-view behaving correctly, multiple windows when the domain benefits (compare two records side by side). Apps that fight the window system feel like ports.
5. **Progressive disclosure, Apple-style.** Simple by default, powerful on demand: Option-key revealing alternate menu items, disclosure triangles, inspector panels. Complexity is layered, never amputated.
6. **Accessibility as architecture.** Full keyboard access, VoiceOver labeling, Dynamic Type respect, contrast compliance. In the HIG these are structural requirements; treat them the same way.

## Signature moves to steal

- **The inspector pattern.** Selection on the left/center, editable properties in a right-hand inspector, live-applied. The canonical desktop editing model (Finder, Keynote, Xcode, Figma all use it).
- **The source list.** Left sidebar of navigable collections with counts, disclosure, and drag-to-reorganize. Steal its behaviors (spring-loaded drop targets, inline rename) not just its look.
- **Toolbar as curated verbs.** A small, user-customizable set of high-frequency actions with named icons, never a dump of every feature.
- **Sheet vs window vs popover discipline.** Document-blocking confirmations as sheets attached to their window; independent tasks as windows; lightweight transient options as popovers anchored to their control. Choosing the right container is half of desktop interaction design.

## Never copy

- The marketing-site language (hero typography, product photography scale) into tool UI.
- Liquid/translucent materials on non-Apple platforms or in web-delivered apps where they render as low-contrast grey soup. Materials only where the platform renders them properly.
- Apple's occasional own violations (hidden scroll bars harming discoverability, buried settings). The HIG is the teacher, current Apple apps are imperfect students.
