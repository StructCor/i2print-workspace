# Verification record — October 24, 2026

## Result and limits

The local concept, two PDFs and unsent email are complete for Daniel's review. This is a static demonstration, not production software. No client email, quote, order, payment, production job, DNS change, deployment, commit or push was performed.

## Browser and interaction checks

Tested in the real in-app browser at 1440px desktop and 375px phone widths. Route measurements are retained in `screenshots/desktop-qa.json` and `screenshots/mobile-qa.json`.

- Home, catalog, both product details, quote flow/summary, file check, proof, business, events, visit, capabilities, roadmap and motion routes: no horizontal document overflow or broken loaded images.
- White background retained under the system's dark appearance. Computed body background: `rgb(255, 255, 255)`.
- Keyboard Menu and Play/Pause controls work. Default reduced motion pauses animation; explicit Play enables it locally. Pause disables animations, transitions, smooth scrolling and image-hover movement. Reloaded the final files and checked Play/Pause and image loading again.
- Quantity zero is rejected. Business-card quantity 500, heavy stock, artwork help and shipping preference reach the summary accurately. Banner 96 × 36, quantity 2, hems only persists through Back navigation.
- Sample Fit reports 300 effective ppi; Fill reports 240 and warns. A real file-chooser upload of a small PNG reports 40 ppi and warns. PDF input is rejected with an explicit future-work explanation.
- Simulated proof approval requires acknowledgement; revision requests change state; changed artwork resets the decision. Extend is a simulated preview and downloads are demonstration output.
- A review found a race where approval during image decoding could survive when the image appeared. `qa/proof-decode-regression.cjs` reproduced the defect before the correction, then passed against the corrected actual function. The fix resets the decision after decoding and refreshes an open proof page.
- No browser errors/warnings observed. Application source has no network API or persistent-storage calls. CSP restricts `connect-src` and `form-action` to `none`; interactions do not submit externally. No real customer information was used.
- JavaScript syntax checks passed. No framework build is applicable to this buildless local concept.

These checks are not a substitute for production preflight, assistive-technology testing, a full usability study, pricing validation or integration/security work.

## PDF and research review

- Website Concept: 15 landscape pages. Website and Automation Proposal: 8 portrait pages.
- Rendered and inspected all 23 final pages for legibility, missing images, clipping, placeholder copy and screenshot accuracy. Rendered pages and contact sheets are retained under `qa/`.
- Corrected initial stale browser captures: catalog images, valid quote quantity/material, actual request summary, Fit/Fill results and capability illustration. Recaptured, rebuilt and inspected the corrected pages. Some viewport screenshots intentionally show the beginning of longer pages.
- Reviewed both supplied 10-page research PDFs. Extracted text and corresponding rendered pixels are identical. See `research-review.md` for source boundaries and changes to the proposal.
- Existing public FAQ features are acknowledged; capability categories are attributed to the company's public description. Exact equipment models and capacities are not claimed. Audience priorities, hosting and commerce choices remain proposed/owner-pending. No historical price ranges or delivery promises were imported.

## AI reviews and disposition

The complete new working-file implementation and proposal copy were reviewed directly, not through a commit diff. Retained evidence:

- `qa/final-review-claude.md`: Claude CLI full review — PASS with nonblocking polish.
- `qa/final-review-local.md` and status JSON: local Gemma review — PASS.
- `qa/final-review-packet.txt` and `qa/final-review-manifest.json`: the reviewed snapshot before later fixes. Preserved as the original audit record.
- `qa/fresh-review.md`: independent full code/copy review plus final narrow recheck — PASS after the image-decode proof fix. Includes current source hashes and explicitly distinguishes primary-agent PDF inspection from independent code review.
- `qa/proof-decode-regression.cjs`: targeted regression, observed failing before and passing after the fix.
- `qa/final-hashes.json`: final delivery/source fingerprints.

Resolved the material proof-loading defect and the motion button/pause suggestions. Remaining nonblocking prototype polish includes small secondary captions, some heading hierarchy, a shared trim/safe guide dash style, automatic orientation behavior, and the need for JavaScript. No new production capability is implied.

The configured `I2Print-Review` folder was unavailable at both documented locations. Its commit-based gate was not run and is not represented as passing. Full working-file AI review was completed as above; no commit, push or client delivery occurred.

## Preservation and private review hub

Claude's original HTML and motion concepts, v2 proposal PDFs, and kickoff-v3 remain intact. Existing unrelated Git changes are preserved. The private Pages hub was updated with the final filenames, selected white-brand direction, demonstrated interactions and open discovery decisions; read-back confirmed the changes. Sharing remained private. No raw emails, customer records or local assets were uploaded.

Daniel must approve the visuals, image use, wording and final attachments before client delivery. The local preview server is stopped after verification; `05-Mockup/final-v4/preview.ps1` restarts it when needed.
