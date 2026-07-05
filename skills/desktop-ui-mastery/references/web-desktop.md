# Web-Tech Desktop - Electron, Tauri, and the Uncanny Valley

Most desktop apps built today ship web technology in a native window (Electron, Tauri, and kin). This is where the "stretched website" anti-pattern is born, and where a handful of platform mechanics decide whether the app feels native or feels like a browser tab wearing a costume. Read this whenever the target is a web-tech desktop app.

## The mechanics that decide native feel

1. **The titlebar is yours now, so do the whole job.** Custom titlebars (hiddenInset on macOS, custom on Windows/Linux) mean you must reimplement everything the OS gave for free: a draggable region (`-webkit-app-region: drag` or Tauri's `data-tauri-drag-region`) covering the visual titlebar with interactive controls carved out (`no-drag`); double-click on the drag region to zoom/maximize; correct traffic-light or window-control placement per OS; and a visibly different (dimmed) state when the window is unfocused. Half-done titlebars are the number one tell of a careless port.
2. **Per-OS divergence is a design deliverable, not a build flag.** Window controls left (macOS) vs right (Windows/Linux); Cmd vs Ctrl in every shortcut and every shortcut label; menu bar in the system bar (macOS) vs in-window (Windows/Linux); sentence-case buttons and dialog button order differ. Write the divergence table into the spec.
3. **The native menu is still mandatory.** An Electron/Tauri app without a real application menu (with role-based items: Edit with working Undo/Cut/Copy/Paste, Window, Help with search on macOS) breaks system-level muscle memory and accessibility. The in-app command palette complements the menu; it never replaces it.
4. **Kill the browser reflexes that leak through.** Disable pinch/ctrl-zoom of the whole UI unless zoom is a feature; no pull-to-refresh or rubber-band overscroll on the app frame (contained scrollers only); no text-cursor on labels, no accidental text selection on chrome (`user-select: none` on chrome, selection preserved in content); context menus everywhere a right-click lands (an inert right-click screams web page); no visible focus flash of the whole window; external links open in the system browser, never inside the app.
5. **Real windows, real state.** Multiple windows where the domain benefits; size, position, and display remembered per window; graceful behavior on display disconnect; correct full-screen behavior per OS. Web-tech apps that support only one immortal window feel like sites.
6. **Performance discipline the browser will not give you.** Cold start under ~2s to interactive with the last session restored; virtualized lists for anything past a few hundred rows; no layout thrash on window resize (test by dragging the corner continuously); GPU-cheap animation only (transforms and opacity, see emil-kowalski.md). Tauri's lighter footprint is a real feel advantage; Electron demands stricter discipline for the same result.
7. **OS integration is where trust forms.** Native notifications through the system center with correct app identity; dock/taskbar badges and progress; file associations and drag-out (dragging a file from the app to the Finder/Explorer); the system tray/menu-bar extra only if the app genuinely lives in the background; respect OS light/dark and accent where the design's token system allows.

## The uncanny-valley rule

Users forgive an app that is honestly its own design system executed with desktop mechanics (Linear, Figma). They punish an app that imitates native widgets badly. Either adopt the platform's real conventions fully, or commit to a coherent own-brand system that still honors every behavioral convention in desktop-craft.md. The unforgivable zone is in between.

## Checklist before shipping a web-tech desktop app

Drag the titlebar; double-click it; unfocus the window; right-click five random places; hit Cmd/Ctrl+Z in every input; open a link; resize continuously for five seconds; quit and relaunch. Every one of these should behave like the OS, not like Chrome.
