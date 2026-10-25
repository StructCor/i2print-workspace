**[MAJOR] `app.js` `visit()` (Shop and contact page): contact details are tagged as verified but weren't.**
The tag reads "Address published on i2Print's website". Only Long Island City and the Oct 21 business addresses are verified. The street address (38-19 24th Street, 11101), the phone number (718 937 8800) and `hello@i2print.com` are not.
Fix: confirm each against the live site or the thread. Until then, change the tag to "Placeholder contact details, owner to confirm" or show only "Long Island City, New York".

**[MAJOR] `direction-extracted.txt` p2: unverified statements sit under "Verified" headings.**
"Your current site presents product categories, artwork upload or templates, and design-proof approval" is labelled Verified. Only the About page's B2B/B2C/reseller groups were checked. The MOO presentation reference and its source line are also unchecked.
Fix: verify against the site, or relabel "Observed, to confirm". Drop the MOO line unless the source is confirmed.

**[MAJOR] `app.js` `motion()`: the eyebrow "BUILDING ON CLAUDE'S MOTION CONCEPTS" and the notice "Adapted from the existing CSS/SVG motion direction".**
These are internal tooling and process references on a client-facing page. They are also unclear to the reader.
Fix: use "Motion concepts" and remove the "adapted from" sentence. Disclose AI assistance in the proposal if you want to, not on this page.

**[MAJOR] Pages review hub: the mockup depends on assets outside its folder, and "local only" stops being true once it is published.**
- `app.js:3` and `index.html` (favicon, logo) point to `../../04-Assets/scraped-2026-10-20/…`, outside `kickoff-v3`. A deploy of the mockup folder alone will break every image.
- Deploying means publishing the scraped i2Print photos and logos. Daniel hasn't approved sharing them, and the footer note still says the imagery is used "locally".
- `noindex` does not provide privacy.

Fix:
- Confirm the hub is access-restricted before deploying. GitHub Pages sites are public unless the plan supports private Pages.
- Copy only the approved images into the deploy folder and update the paths.
- Reword the footer note to match how the files are hosted.
- Check whether the product images include third-party stock or template art.

**[MINOR] `app.js` `printSpec()`: square images flip portrait specs to landscape.**
`(h>w)!==(p.h>p.w)` is `false!==true` for a square image against Flyer. The spec swaps to 11 × 8.5.
Fix: swap only when the image is clearly non-square, for example `Math.abs(w-h)/Math.max(w,h)>.02`.

**[MINOR] `app.js` `route()`: reloading on `#main` renders a blank page.**
The skip link sets the hash to `#main`, and `route()` returns early for it.
Fix: return early only when `state.route` is already rendered. Otherwise fall through to home.

**[MINOR] `app.js` `fileCheck()`: the upload label doesn't match its accessible name.**
The visible text is "Choose an image" but the input's `aria-label` is "Choose a local image". That fails label-in-name.
Fix: remove the `aria-label`, or make it start with the visible text.

**[MINOR] `app.js` `result()`: status is conveyed only by the glyphs "i", "!" and "×".**
Fix: add `aria-hidden` to the glyph and put "Note:", "Warning:" or "Problem:" in the text.

**[MINOR] `app.js` proof handlers: focus and typed notes are lost on re-render.**
Approve and revision both rebuild `main`. Focus drops to the page body, the `aria-live` region is recreated, and a typed revision note is discarded on approve.
Fix: re-render only `#proof-state` and the tag, or refocus `#proof-state`. Save the textarea value before re-rendering.

**[MINOR] `styles.css`: the focus ring fails contrast on dark backgrounds.**
The 3px `#3a62c9` outline is nearly invisible on the `.callout` (blue) and `.concept-bar` (ink).
Fix: set `outline-color:#fff` for `.callout :focus-visible` and `.concept-bar :focus-visible`.

**[MINOR] `styles.css` and `index.html`: the key disclaimers are the smallest text, and print hides them.**
- `.concept-bar` is 9–10px and is the only visible disclosure on mobile. The `.footer-note` disclaimer is 10–11px in a muted colour.
- `@media print` hides `.concept-bar` and `.footer`, so printed pages lose all demo labelling.

Fix: use at least 12px for these. Keep a "Concept — nothing submitted" line in print.

**[MINOR] `app.js` `summary()`: "Pricing pending shop review" implies the request is queued.**
Nothing is sent, so the wording contradicts "Nothing has been submitted".
Fix: use "No price calculated in this demo".

**[MINOR] `app.js` `journey()` and the home audience card: wording overclaims.**
- "clear next steps when something needs attention" overstates what the check does. It only shows generic warnings.
- "Cards, invitations and event details" presents invitations as a product, but they aren't in the catalog.

Fix: "see what the check flags", and "Cards and event printing, to confirm with the shop".

**[MINOR] `concept-extracted.txt` p3: "Existing i2Print logo, Jost type, accessible blue".**
This implies Jost and the blue are existing i2Print identity. The CSS defines `--blue:#3a62c9`, different from `--blue-brand:#5680e9`.
Fix: "Existing logo; proposed type and accessible blue".

**[MINOR] `concept-extracted.txt` p10: the 300 / 240 ppi figures name no spec.**
They only hold for the business-card spec (3.75 × 2.25 in with bleed) and the 900 × 675 sample.
Fix: state the spec and the pixel size.

**[MINOR] `app.js` `sampleArt()` and `loadSample()`: "Paper & Stem" may be a real business name.**
Fix: do a quick name check, or use an obviously generic name.

**[MINOR] `styles.css`: `fonts/Jost-Variable.ttf` ships without its OFL license text.**
Fix: include `OFL.txt` beside the font file.

**[MINOR] `app.js` `compose()`: Extend mode uses `ctx.filter`, which Safari may ignore.**
There it would silently show a sharp enlarged copy rather than a blur.
Fix: feature-detect it and show a note, or test in Safari.

**[MINOR] `app.js`: the roadmap and audience pages name individuals ("TOM'S AUTOMATION GOALS", "Tom and Lindsay").**
Fix: use "Client goals" and "i2Print" if the hub link is ever shared beyond them.

**[MINOR] `reply-to-tom-DRAFT.md`: three issues.**
- The PDFs refer to "local interactions" and "the existing prototype", but the draft gives no way to see them.
  Fix: offer a screen-share demo, or include the hub link once it is access-restricted.
- "move away from OnPrintShop" names a vendor. Confirm it is in Tom's Oct 21 email. If not, use "move to a platform you own".
- The approval notes don't flag that both PDFs embed the scraped site photos. Add "Daniel to approve image use" to the attachment check.

**[MINOR] `app.js` `motion()`: Replay buttons do nothing under reduced motion.**
The animations are disabled but the buttons stay.
Fix: hide them or disable them with an explanation when `prefers-reduced-motion` is set.

**[MINOR] `app.js` `detail()`, `quoteSummary()`, `motion()`: heading levels skip.**
The pages jump from H1 straight to H3.
Fix: make the section titles H2.

VERDICT: CONCERNS
