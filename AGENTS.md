# i2Print Workspace — Agent Guide

Read this first, then `README.md` (file index) and `TASKS.md` (open work). Written 2026-10-24 as a handoff from Claude Code. The primary agent for this phase is **Codex**; Claude Code may pick it up later.

## How to use this document
- It's modeled on the Commercial Crab Pots (CCP) agent guide, because i2Print should be built and run the CCP way.
- **Hard rules** (below) are not optional. Everything else is context and recommended practice. If something here looks wrong for the task in front of you, say so rather than silently complying.
- This is a Windows machine: use PowerShell syntax, and quote paths with spaces.
- Before finishing any task:
  - Update `TASKS.md`: move done items, add new ones.
  - For anything client-facing, note what still needs Daniel's approval.

## What this is
- **Daniel Raxa (RaxaRisk, LLC)** is pitching a website rebuild to **i2print inc.**, a commercial printer at 38-19 24th St, Long Island City, NY.
- **Client contacts:** Tom (tom@i2print.com) and Lindsay (Lindsay@i2print.com). Their roles aren't confirmed yet.
- This is Daniel's first paying client outside family work.

## Where things stand (2026-10-24)
1. **Intro email sent** 2026-10-20 from daniel.raxa@raxarisk.com, with 5 screenshots and a motion video. It offered a 30–45 min discovery call and asked about their contract end date (or whether they're month to month) and what data they keep. **Waiting on a reply.**
2. **"Proposed Direction" doc**, private, not yet shared: https://claude.ai/artifact/FhjBFGzojCYAkbH8JcKwE6
   - 11 decisions, each with an Agree / Disagree / Let's discuss dropdown.
   - Also the staged plan, a client checklist, concept images and the animation GIF.
   - **No pricing.** Daniel is reviewing it before sharing.
3. **Gamma proposal deck v2** (private): https://gamma.app/docs/d1i57t4cw4qi770
   - PDF: `06-Proposal/i2Print-Website-Proposal-DRAFT-v2-phased-move.pdf`.
   - Pricing is **DRAFT** and not yet sent.

## The plan (agreed direction, pending client confirmation)
- The client wants to **leave OnPrintShop**, their current hosted print store, and own a platform they control.
- **The move happens in stages:**
  1. Discovery and exit planning.
  2. Design.
  3. A new **Next.js site on Vercel** runs alongside the current store. Its "Order" buttons link to the old store until the switch.
  4. The store moves to **Shopify**, account in i2Print's name, one product family at a time, timed to their contract end.
  5. Email and growth.
  6. Ongoing care.
- **Before promising Shopify:** prototype their hardest pricing (banners or cards priced by size, paper and quantity).
- **Free File Check:** deterministic size, DPI and bleed checks plus Fit/Fill. AI is only used to extend backgrounds, and the customer always approves a proof.
- Details: `02-Research/platform-and-tools.md` §0.

## Hard rules (do not break)
- **Nothing goes to the client without Daniel's explicit approval:** no email, no shared link, no file. Leave everything as drafts.
- **Never mention in client-facing material:** the previous developer, the ~$100k they spent, any dispute, or advice on getting out of their contract. Their attorney handles the contract. We only ask about timing.
- **Portfolio = Commercial Crab Pots only.** Never reference, reuse or rebuild anything from Daniel's prior employment: no former-employer tools, work, data or names. If a task seems to need it, stop and ask Daniel.
- **Label every claim** verified / owner-pending / proposed. Don't invent stats, results, turnaround times, prices or testimonials. Items marked `CONFIRM` in the mockup need real facts from i2Print.
- **Insurance** (CGL $1M · WC statutory / EL $500K · E&O $250K) is as Daniel stated it and **not yet checked against the policy or COI**. Never call it "verified."
- **`04-Assets/scraped-*/`** is the client's own site material: local only, kept out of git by `.gitignore`. **`client-logos/` is third-party marks and must never be used** in mockups or published material.
- **Gamma decks:** use the Icebreaker theme (the current deck's) or a standard theme. Never use Daniel's custom theme named after his former employer.
- **Daniel is still deciding on flagged items.** Don't rewrite them unless he asks: the contract/exit wording in the proposal PDFs and the email draft, and the "insurance verified" wording in `06-Proposal/README.md`.

## Git
- Private repo `StructCor/i2print-workspace`, branch `main`.
- **Push only as StructCor:** `GH_TOKEN=$(gh auth token -u StructCor)`. **Never** run `gh auth switch`.
- A pre-push hook runs a rules-only review (free, no AI). **Do not run the full AI review (`review.ps1` without `-RulesOnly`, or any extra reviewer such as Claude, OpenRouter, Gemma or a Codex review) on commits, pushes or new commits you notice. Run it only when Daniel asks, normally once before something goes to the client.** One reviewer at a time; never several in parallel. Each review costs Daniel tokens.
- `I2Print-Review/` (the review gate) sits in this folder but is not part of the repo. Don't commit it or edit it.
- Commit or push only when Daniel asks.

## Building it the CCP way (for when the build starts)
The CCP site (`StructCor/commercial-crab-pots-site`) is the reference build. Match its stack and habits unless Daniel decides otherwise. Its agent guide (`AGENTS.md` in that repo) has the details.

**Stack:**
- Next.js 16 (App Router), React 19, TypeScript, plain CSS (one global stylesheet, design tokens in `:root`).
- Hosted on Vercel.
- GitHub Actions runs `npm run check` (tests, lint, typecheck, public-copy scan, build). Production deploys only from `main`, after the check passes.
- Node 24.

**Conventions to carry over:**
- Prefer `type` over `interface`; images use `next/image`.
- Content lives in `const` arrays at the top of a page.
- Flat kebab-case class names.
- Motion respects `prefers-reduced-motion`, and hover-only effects sit behind `(hover: hover) and (pointer: fine)`.

**i2Print design tokens (from the mockup):**

| Token | Value |
|---|---|
| `--blue` | `#3A62C9` (accessible blue for text and buttons) |
| `--blue-brand` | `#5680E9` |
| `--orange` | `#FB8500` (put dark text on it) |
| `--ink` | `#36333C` |
| `--pale` | `#F6F8FE` |
| CMY accents | `#00A6D6` / `#E0007A` / `#FFD400` |

Font: Jost. Source of truth: `03-Brand/brand-guidelines.md`.

**Next.js version note:** Next 16 has breaking changes from older versions. Read the guides in `node_modules/next/dist/docs/` before writing framework code, and heed deprecation notices.

**Standing check before calling a change done:**
- [ ] `npm run check` passes (once the site exists)
- [ ] You looked at the page on desktop and at phone width (375px)
- [ ] No internal notes, `CONFIRM` placeholders or unconfirmed claims in customer-facing copy
- [ ] No real customer data, no real orders or form submissions, no payment test charges outside test mode
- [ ] No DNS, domain or production deploy without Daniel's approval
- [ ] The commit is scoped, and the rules-only review passed (it runs automatically on push)

## Running the mockups
```
python -m http.server 8742 --directory "C:/Users/raxad/Documents/I2Print"
```
- **Homepage concept + file-check demo:** http://127.0.0.1:8742/05-Mockup/index.html
  - Add `?view=client` to hide the internal CONFIRM tags.
- **Motion concepts:** http://127.0.0.1:8742/05-Mockup/animated-concepts.html
- **Images load from `../04-Assets/`.** They only show on Daniel's PC, not from a fresh clone of the repo.
- **Daniel's Windows has reduce-motion on.** Turn on Settings → Accessibility → Visual effects → Animation effects to see the animations and hover effects.

## Next steps, in order
1. When Tom and Lindsay reply: book the call. Trim and send `01-Discovery/questionnaire.md` 2–3 days before it.
2. Before the call:
   - Run the 5-person usability test of i2print.com (`01-Discovery/research-plan.md`).
   - Daniel answers the "questions for yourself" in `01-Discovery/interview-guide.md`: walk-away price, capacity, payment terms.
3. On the call, use `01-Discovery/discovery-agenda.md`, prioritized for 30 minutes, plus interview-guide §C2 (leaving OnPrintShop).
4. After the call:
   - Notes go in `01-Discovery/notes-YYYY-MM-DD.md`.
   - Brand guidelines v2.
   - Replace the CONFIRM tags.
   - Fixed Phase 1 price.
   - Then the service agreement, with legal review before signing.
