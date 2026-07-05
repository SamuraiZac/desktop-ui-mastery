# Critique and Deslop - Review Modes

Two review procedures. Critique judges a design against the masters' bar and says what to fix. Deslop is narrower: it hunts the specific tells of generated or templated UI and strips them. Run deslop before critique when reviewing AI-produced interfaces.

## The desktop slop list (tells of generated UI)

Generated desktop UI converges on a recognizable statistical center. Hunt these specifically:

**Layout tells**
- Centered content column with page margins inside an app window (the stretched website)
- Every region rendered as a card with identical radius, shadow, and 16-24px padding
- Three-stat cards in a row at the top of every dashboard, each with icon, label, big number, delta badge
- Uniform 8px-multiple spacing applied without hierarchy, so nothing groups
- Sidebar with icon+label rows all at equal weight, no sections, no counts

**Visual tells**
- Default-blue or purple-gradient accent; accent used on 15 elements per screen
- Inter/default font at browser sizes (16px body in a tool UI)
- Borders on everything at full-opacity grey; shadow and border on the same element
- Badge and pill overuse: statuses, counts, and labels all rendered as colored pills
- Icon-per-list-item decoration where the icons encode nothing

**Behavioral tells**
- Hover states missing or opacity-only on interactive rows
- No focus-visible styling anywhere; tab order untested
- Buttons without pressed states; inputs without error states; tables without empty, loading, and overflow states
- Toasts for outcomes that needed no announcement; modals for edits that wanted inline
- Every list the same component regardless of content type

**Content tells**
- Lorem ipsum, "John Doe", "$1,234.56", "Dashboard" as the page title
- Truncation untested: no long-string handling anywhere
- Sentence-case/title-case inconsistency across labels

## Deslop procedure

1. Inventory violations from the list above against the actual screens or code.
2. Fix in this order: content realism, layout anatomy (kill the card-everything and centered column), spacing hierarchy, accent discipline (reduce accent to a handful of uses), type scale (compact desktop sizes, tabular figures), states (hover, focus, pressed, empty, error, loading), then decoration removal (Tufte pass).
3. Do not add style during deslop. Deslop returns the design to honest zero; direction comes after, from the chosen lenses.

## The craft pass (what the linter cannot see)

A design can pass every mechanical check and still be a wireframe wearing tokens. This failure mode is common in model-generated "clean" UI: correct anatomy, dead pixels. Judge the RENDERED output, never the code, against these:

1. **Type has registers, not just sizes.** Somewhere on the screen there is a display moment (a large number, a set sentence, a title with conviction) and somewhere there is quiet meta text, and the distance between them is unmistakable. If every piece of text is 12-13px regular grey, the design has a scale, not a hierarchy.
2. **The signature element dominates the squint test.** Whatever the point of view named as the design's one expressive element must be the first thing a blurred screenshot shows. A signature element nobody would notice is a caption, not a signature.
3. **Controls are designed, not defaulted.** Browser-default selects, checkboxes, and inputs in a crafted surface read as prototype. Either style them as a coherent family (appearance: none, consistent heights, radii, hover/focus/active states) or use the platform's real native controls deliberately, never the unstyled web middle.
4. **Tables and lists have headers, alignment logic, and emphasis rules.** Numbers right and tabular, labels left, one deliberate emphasis channel (weight or color) reserved for the values that matter, everything else recessive.
5. **Zones separate visibly.** Rail, canvas, header, and inspector must read as distinct regions at a glance through tone steps or structure; if the screenshot reads as one continuous field of same-value grey, the tonal ramp is too timid.
6. **Realistic load, always.** Screenshots with six rows and a void are unfinished; fill to a real day's data before judging.
7. **The substitution test on the pixels.** Cover the product name: does the rendered surface itself express the stated point of view, or does only the write-up? A point of view that lives in the comment block and not in the pixels is a wireframe with a manifesto.

If any of these fail, the design goes back for a craft revision before delivery. This pass happens by looking at a render or screenshot, never by re-reading the CSS.

## Critique procedure

Structure every critique in this order, and be willing to fail a design:

1. **Point of view.** Can the design's belief be stated in one sentence from looking at it? If two products could share the read, the design fails here regardless of polish.
2. **The 100x action.** Identify it; measure its friction (clicks, keystrokes, latency). This is the heart of the review.
3. **Desktop mechanics** against `desktop-craft.md` section 8 (the eight-point checklist), reported as pass/fail per point.
4. **Lens fidelity.** Which masters does the design implicitly invoke, and would each sign it? Cite the specific principle upheld or violated (e.g. fails Tufte: legend instead of direct labels; fails Raskin: invisible mode in the editor toggle).
5. **Distance check** from `synthesis.md`: attribution, substitution, novelty ledger.
6. **Verdict and top three.** Approve, approve-with-changes, or redo, plus the three highest-leverage fixes, each tied to a principle, not a preference.

Critique tone: specific, cited, unsparing, and constructive. Never pad with praise; when something is strong, say precisely why in one sentence and move on.
