# i2Print brand-preserving final proposal implementation plan

**Goal:** Produce Daniel's final review package using Claude's white i2Print concept, purposeful animation and clearer customer guidance.

**Authority / spec:** Daniel's October 24 instruction explicitly selects Claude's mockups, white background, original logo/colors, more animation, equipment explanations, business and personal audiences, and a final proposal. This supersedes the earlier brainstorming pause. No further direction-selection gate is needed.

**Architecture:** Copy the tested kickoff-v3 local journey into final-v4; retain original Claude and v3 files. Add a focused presentation/motion layer and capabilities route. Keep existing quote/image/proof behavior and local-only CSP. No new framework or backend is needed for this concept.

**Tech stack:** Buildless HTML, plain CSS, JavaScript, local Jost; proposed production stack remains Next.js, React, TypeScript, plain CSS, Node.js. Sites local-only workflow. Remotion guidance reviewed; the requested website interactions use CSS/SVG, not a video renderer.

## Constraints
- Exact tokens: white #FFFFFF, blue #3A62C9, brand blue #5680E9, orange #FB8500, ink #36333C; CMY #00A6D6/#E0007A/#FFD400. No automatic dark mode.
- Existing local i2Print logo and permitted product assets. No third-party client marks, fabricated equipment photography, prices, turnaround, testimonials or customer counts.
- Equipment categories are company-published capabilities, not independently verified equipment models/capacity. Explain these distinctions in the proposal and private notes.
- Retain original materials; no commit, push, sending, publication or deployment. Daniel reviews final attachments.

## Tasks
- [x] Review both PDFs, live site including its animated customization example, and existing proposal. Record source boundaries and remove obsolete pricing/timing assumptions.
- [x] Build final-v4 homepage, customer paths, capabilities explorer and motion: color registration, product movement, drag/upload illustration, preview guides, keyboard-equivalent hover states. Include Play/Pause, respect reduced motion by default and allow explicit user playback.
- [x] Verify desktop and 375px, keyboard, dark system theme remains white, motion controls, no network submissions; regress quote validation/summary, upload warnings, Fit/Fill and proof states.
- [x] Capture real browser screenshots; generate 15-page landscape concept (one added capabilities page) and 8-page portrait proposal with updated research-aware narrative and email draft.
- [x] Render and inspect every PDF page, run full working-file AI review, resolve material findings, record final hashes and update TASKS. Preserve source artifacts and audit record.

## Review focus
Motion preference changes while the page is open; off-screen or infinite movement; keyboard-only tabs/menu; small-screen overflow; illustrative machine graphics accidentally presented as installed equipment. Also check no claims of replacing missing features when the current FAQ already advertises pricing/proof/tracking.

## Execution rulings
Use the user-requested separate concept folder in the existing workspace, preserving uncommitted files; do not create commits or move the work into a new checkout. Use behavior verification for the substantial interactions; no redundant unit tests for decorative CSS. Final AI review covers actual uncommitted working files rather than a commit diff.
