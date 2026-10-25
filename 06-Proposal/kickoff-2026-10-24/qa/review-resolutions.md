# Review disposition — private working files

The configured commit-based gate cannot inspect uncommitted files. No commit was authorized, so the same reviewer roles were run against a hash-recorded working-file packet without changing the gate. Claude Sonnet returned CONCERNS. OpenRouter GLM-5.3 returned no usable verdict; the configured local Gemma fallback also returned an empty answer on its initial thinking-enabled run. A final review uses corrected working files and disables thinking on the local fallback to obtain an actual answer.

## Findings resolved in code/content

- Reloading `#main` now renders Home instead of a blank page.
- Square/near-square uploads preserve the selected specification's orientation.
- Proof actions preserve typed notes and move focus to the decision state.
- Upload accessible name contains its visible label. Status symbols are hidden from assistive technology with explicit Note/Warning/Problem text.
- Focus rings on dark/blue areas are white. Demo labels are at least 12px and remain in print styles.
- Reduced-motion viewers get still compositions and an explanatory note; inactive Replay buttons are hidden.
- Internal Claude/CSS implementation wording removed from the motion page. Section headings corrected.
- Replaced image bitmaps are closed. Extend falls back to padding if canvas blur is unavailable; the UI explains this.
- Concept PDF identifies proposed type/colors and names the exact pixel and physical dimensions behind its PPI comparison.
- Draft email offers a screen-share demo and explicitly requires Daniel's approval of image use.
- Direction page 3 now includes a concrete discovery question for each automation area.

## Findings resolved by evidence or scope

- Public contact details are confirmed on [i2Print's homepage](https://www.i2print.com/) and [About page](https://www.i2print.com/aboutus.html), rechecked October 24: 3819/38-19 24th Street, Long Island City NY 11101; 718 937-8800; hello@i2print.com. This verifies what is published, not current hours or pickup availability.
- The current homepage explicitly presents templates/artwork upload and design-proof approval. The About page describes B2B, B2C and resellers. [MOO business cards](https://www.moo.com/us/business-cards) shows paper/finish choices. The direction document accurately characterizes these observations, not independently verified performance results.
- Pages means the private ChatGPT Pages document, not GitHub Pages. Owner Daniel, no shares and complete empty inherited-access lists were verified. No site is deployed. External asset paths are intentional for the user-requested local-only workflow; no scraped assets were copied to Git or uploaded.
- Jost's OFL.txt already exists beside the font. It was outside the initial text-only packet, not missing from the deliverable.
- "Pricing pending shop review" is the user's requested wording and appears alongside "nothing submitted"/"no prices calculated". It does not claim the request was sent or queued.
- Paper & Stem is explicitly fictional sample artwork, not a claim about a customer or affiliation. No real logo or customer data is used.
- OnPrintShop transition is directly user-authorized and documented project context, phrased as Daniel's understanding/proposal, not a claim that it was in Tom's October 21 email. No contract advice is included.
- Business/personal paths are audience options to validate, not evidence of actual revenue mix. Proposed event services still need approval.

Browser retests confirmed #main reload, square 600×600 image on 8.5×11 flyer, PDF rejection, proof focus/note retention, and final desktop/mobile layout. Safari and a full screen-reader audit were not performed. All 22 PDF pages were rendered and inspected; diagrams and screenshots are illustrative discussion material.
