# Desktop Craft - Mandatory Mechanics

Read this every time. These are the mechanics that distinguish a desktop application from a website in a large window. They apply regardless of which masters are chosen as lenses. Treat violations as bugs, not style choices.

## 1. Layout and density

- **Edge-to-edge tool anatomy.** The canonical shell: optional top bar (40-52px), left rail or sidebar (200-280px, resizable, collapsible), main content area, optional right inspector (260-320px), optional bottom status bar (24-28px). Content fills the space; no centered 720px column, no page margins.
- **Density targets.** List rows 28-40px; table rows 28-36px; toolbar controls 28-32px; base spacing unit 4px, common gaps 8/12/16. Desktop users sit at arm's length with precise pointers; mobile touch metrics (44px targets, 24px padding) waste half the screen.
- **Resizable everything that holds content.** Panels have drag handles with sensible min-widths, and remember their sizes. Layout persistence is part of the design.
- **Responsive means panel behavior, not reflow.** As the window narrows: inspectors collapse to toggles, sidebars to icon rails, columns hide by priority. The design must specify these breakpoints (typically ~1440, ~1100, ~900px).
- **Design at realistic load.** Every screen validated with: maximum plausible data (400+ rows), longest plausible strings (+40% for German), zero data (designed empty state with a next action), and error/partial states.

## 2. Keyboard

- **Complete keyboard path.** Every action reachable without the mouse. Tab order logical; focus always visible (2px offset ring); focus trapped correctly in dialogs and returned on close.
- **The standard contract, unbroken:** Cmd/Ctrl+Z undo (and Shift redo), Cmd+F find, Cmd+S save (or visible autosave state), Cmd+W close, Cmd+, settings, Escape cancels/closes, Enter confirms, Space toggles/previews, arrows navigate lists, Home/End jump, type-ahead selects in lists.
- **Command palette (Cmd+K)** exposing every verb with fuzzy search and shortcut labels; contextual menus mirror the same verbs and names.
- **Shortcuts taught in place:** shown in menus, tooltips, and palette rows, so mastery is learnable through use.

## 3. Selection and manipulation

- Lists and tables support: click select, Shift+click range, Cmd/Ctrl+click toggle, drag-select where spatial, Cmd+A select all, arrow-key movement with Shift extension.
- Multi-select changes the inspector/action bar to bulk mode with an explicit count ("14 selected").
- Drag and drop with live drop-target feedback, spring-loaded containers, and Escape to cancel mid-drag.
- Inline editing (double-click or Enter to rename/edit in place) preferred over edit dialogs.
- Right-click always produces a relevant contextual menu. An inert right-click is a broken promise on desktop.

## 4. State, persistence, latency

- **Sub-100ms perceived response** for local actions via optimistic updates; spinners only for genuinely remote waits, skeletons only above ~300ms expected.
- **Everything restores:** window size/position, panel layout, scroll positions, selections, unsaved drafts, last route. Relaunch should feel like resuming, not restarting.
- **Undo as the universal safety net,** covering destructive and bulk actions, with confirmation ceremony reserved for the truly irreversible (see n26.md on friction asymmetry).
- **Honest sync state.** Saved/saving/offline/conflict conditions visible in one calm, consistent location; never a modal panic.

## 5. Typography and color mechanics

- Interface typeface at 13px base (11-15px range) with tabular figures in all numeric columns; full spec in `designers/rasmus-andersson.md`.
- **Tokens from day one:** semantic roles (bg/surface/raised, text primary/secondary/muted, border subtle/strong, accent, success/warning/danger) defined for light and dark simultaneously. Hierarchy by tone steps before borders; borders before shadows; shadows only for true elevation (menus, dialogs, dragged items).
- Contrast: 4.5:1 minimum for text, 3:1 for large text and essential UI shapes, in both themes, verified not eyeballed.

## 6. Motion mechanics

- Utility transitions 120-200ms ease-out; exits ~2/3 of entrances; transforms and opacity only; origin-aware; interruptible; reduced-motion respected. Full doctrine in `designers/emil-kowalski.md`.
- Zero animation on the highest-frequency loop is a legitimate and often correct choice.

## 7. Windows, dialogs, containers

- Correct container per job: **popover** for transient anchored options, **dialog/sheet** for blocking decisions (rare), **panel/inspector** for persistent properties, **new window** for parallel independent work, **toast** for non-blocking outcomes (with action, e.g. Undo).
- Dialogs: primary action right (macOS convention) or platform-appropriate, Enter/Escape wired, initial focus on the least destructive control.
- Never stack modals. A modal spawning a modal is an architecture error; redesign the flow.

## 8. The desktop feel checklist (final pass)

Run before delivering any design:

1. Tab through everything; focus visible and ordered?
2. Unplug the mouse mentally; can a full session happen?
3. Load 400 rows; still calm, still fast-feeling?
4. Resize to 900px wide; do panels degrade by design?
5. Right-click three random things; useful menus?
6. Quit and relaunch; is everything where it was?
7. Squint; does hierarchy survive?
8. Count accent-colored elements; more than a handful means the accent is spent.
