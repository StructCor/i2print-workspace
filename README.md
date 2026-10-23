# i2Print — Client Pitch Workspace

**Client (prospect):** i2print inc. · 38-19 24th St, Long Island City, NY 11101 · https://www.i2print.com/
**Prepared by:** Daniel Raxa, RaxaRisk · **Started:** 2026-10-20 · **Stage:** Phase One, pre-discovery
**Rules:** Portfolio = Commercial Crab Pots only, with **no FBM work** (litigation hold). Nothing is sent to the client without Daniel's review. Scraped assets are for the internal pitch mockup only.

## Contents
| Folder / file | What it is | Status |
|---|---|---|
| `00-Admin/insurance-summary.md` | Insurance lines for the proposal, plus risk notes | Draft: **verify against the policies** |
| `01-Discovery/discovery-agenda.md` | 45–60 min discovery-call script | Ready |
| `01-Discovery/questionnaire.md` | Pre-call questions to send the client | Ready to send (after your review) |
| `01-Discovery/interview-guide.md` | Live questions only Daniel asks: probes, reaction test, red flags, pre-call self-check | Ready |
| `01-Discovery/research-plan.md` | Usability test of the current site, customer calls, survey, synthesis method and notes template | Ready |
| `02-Research/brand-audit.md` | Audit of i2print.com (business, platform, brand, problems) | Done 2026-10-20 |
| `02-Research/competitors.md` | Local competitors + national printer patterns | Done |
| `02-Research/platform-and-tools.md` | Keep or replace OnPrintShop, file-fix tech, email platforms, pricing | Done (third-party prices; verify) |
| `03-Brand/brand-guidelines.md` | Brand voice and visual guidelines draft v1 | Draft; QA-reviewed and corrected; v2 after discovery |
| `04-Assets/scraped-2026-10-20/` | 51 public images from i2print.com + `manifest.csv` | Done. `client-logos/` = archive only, **do not use** |
| `05-Mockup/index.html` | Homepage concept + working Free File Check demo | Done; tested at desktop and 375px mobile |
| `05-Mockup/screenshots/` | Hero, file-check and full-page screenshots for the deck | Done |
| `06-Proposal/` | Gamma deck (https://gamma.app/docs/d1i57t4cw4qi770) + PDF export | Draft; see `06-Proposal/README.md` |
| `TASKS.md` + `dashboard.html` | Task list and productivity dashboard (open `dashboard.html` in a browser) | 7 active, 2 waiting |
| `CLAUDE.md` + `memory/` | Working memory: terms, people, project, how Daniel works | Started 2026-10-20 |

## Viewing the mockup
The page loads images from `../04-Assets`, so serve the whole folder:
```
python -m http.server 8742 --directory "C:/Users/raxad/Documents/I2Print"
```
Then open http://127.0.0.1:8742/05-Mockup/index.html. Opening the file directly also works in most browsers.

## Open items before anything goes to the client
- [ ] **Edit the price ranges** in the Gamma deck (the "Investment" card is marked DRAFT; remove the marker)
- [ ] **Verify the insurance wording** against the declarations/COI (WC/EL split; E&O covers web/software services)
- [ ] **Drop the screenshots into the deck** (2 cards have `[Insert screenshot …]` markers)
- [ ] Confirm the deck's sharing settings in Gamma before sending a link
- [ ] Schedule the discovery call; send the questionnaire 2–3 days before
- [ ] After the call: confirm turnaround times, hours/pickup, file specs and founding year, then update the brand guidelines to v2 and replace every `CONFIRM` tag in the mockup
- [ ] Ask for vector logo files, and permission for a shop photo shoot
- [ ] Terms/agreement: not written yet (proposal only). Get a legal review before signing.
