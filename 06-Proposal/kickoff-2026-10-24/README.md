# i2Print kickoff package — October 24, 2026

Private drafts for Daniel's review. Nothing in this package has been sent to Tom or Lindsay, published, deployed, committed or pushed.

**Artifact updated October 24:** `i2Print-Website-Concept-DRAFT-v3.pdf` now contains the reviewed **15-page white-brand concept** from [the final review package](../final-review-2026-10-24/README.md). Its existing filename is retained so the previously opened artifact points to the current design. The original 14-page PDF is preserved in [archive](archive/i2Print-Website-Concept-DRAFT-v3-before-white-brand-update-20261024-171747.pdf); hashes and provenance are in `concept-artifact-update.json`. The other files and verification notes below describe the historical kickoff package. Use the final review package's source and verification record for the current concept; this folder's old builder would regenerate the earlier design.

## Review these first

- [Website Concept — updated 15 landscape pages](i2Print-Website-Concept-DRAFT-v3.pdf)
- [Website and Automation Direction — 8 portrait pages](i2Print-Website-and-Automation-Direction-DRAFT-v3.pdf)
- [Unsent reply to Tom, including Lindsay](reply-to-tom-DRAFT.md)
- [Interactive local demo](../../05-Mockup/kickoff-v3/index.html)
- [Private Pages review hub](https://chatgpt.com/space/page_887c4c0c92f08191867bd7b114ba2b3d)

The Pages hub was read back and its permissions checked: Daniel is the owner, no direct shares, and no inherited access or workspace links. It contains narrative and decisions; PDFs, image assets, raw email and business records were not uploaded there.

Verification is complete: see [the handoff report](verification.md). Final working-file reviews passed with Claude Sonnet and the configured local fallback. All 22 PDF pages were inspected; the local demo was tested at desktop and 375px phone width. The concept PDF and screenshots contain local client-site imagery and are not approved for repository upload or client distribution yet.

## Run the demo

Open `05-Mockup/kickoff-v3/index.html` in a browser, or run the provided `05-Mockup/kickoff-v3/preview.ps1` and open http://127.0.0.1:8753/05-Mockup/kickoff-v3/index.html. Keep the project folder structure intact: images reference existing local `04-Assets` files. A fresh Git clone will not contain those assets.

The demo includes catalog filters, business-card and custom-size banner requests, editable summaries, local image checks, Fit/Fill/blurred Extend, watermarked PNG output, and simulated proof approval/revision. No backend or live estimate exists. All product choices and file specifications are illustrative. Files and selections stay in browser memory and reset on reload. Use fictional details.

## Sources and scope

- Existing source designs: `05-Mockup/index.html`, `05-Mockup/animated-concepts.html`, and `03-Brand/brand-guidelines.md`; preserved unchanged.
- Existing v2 proposal preserved unchanged. Its prices, dates and screenshot placeholders were not reused.
- Tom's October 21 reply was verified in the existing email thread. The new package summarizes its requests without reproducing the raw email.
- Product imagery and logo: i2Print's existing site, local-only assets. No `client-logos` assets used. The storefront is an explicitly labeled illustration; Paper & Stem is fictional sample artwork.
- Jost: official Google Fonts source, SIL Open Font License copied alongside the local font.
- Primary-source links are embedded in the direction PDF: i2Print About/current site, MOO product presentation, Next.js self-hosting and Shopify hosting. Research informs proposed opportunities, not promised results.
- Sites local-only workflow applied. Remotion/Agents guidance informs later work; this package introduces no video engine, live AI API, database or payment service. Superdesign tools were not available; Stack Overflow for Agents was consulted without publishing a contribution.

## Approval still needed

Daniel reviews the final wording, visuals, proposed attachments and asset use before any client delivery. Tom/Lindsay confirm audience mix, products/specifications, public operating facts, pricing, exports, server control and migration timing. Discovery and technical validation produce a scoped estimate and schedule. Shopify and Vercel remain proposed choices.

`qa/` contains internal evidence, fixtures, page renders, extracted text and reviewer output. It is not part of the proposed client attachments. `screenshots/` holds the actual browser renders used in the concept PDF. `build-pdfs.py` rebuilds both PDFs from those captures and `direction-content.json`.
