# i2Print — Website & Brand Audit

**Site:** https://www.i2print.com/ · **Checked:** 2026-10-20 (read-only; no forms submitted, no account created)
**Prepared by:** Daniel Raxa, RaxaRisk · **Status:** internal pitch research, not shared with client

## 1. Business basics (as published)
| Item | Finding | Confidence |
|---|---|---|
| Legal/display name | i2print inc. | Verified on site |
| Address | 38-19 24th Street, Long Island City, NY 11101 (footer writes "3819, 24th Street") | Verified |
| Phone | +1 (718) 937-8800 · WhatsApp Business +1 (929) 708-6369 | Verified |
| Email | hello@i2print.com | Verified |
| Hours / map | Not published | — |
| Founded | About page says 2000 / "25 years"; third-party data sites say 1990 | **Conflict: confirm in discovery** |
| Owner / team | Not named on site | Ask in discovery |
| Size | Third-party estimates 2–10 employees | Unverified |
| Claims | "1,200+ happy clients", 19 client logos, "partner with more than 50 print on demand suppliers in over 10 countries" | Client's claims, not verified |
| Social | facebook.com/i2print · instagram.com/i2printny · tiktok.com/@i2printny · youtube.com/@I2print | Links on site |

**Products:**
- **Business Stationery:** Standard Business Cards, Bookmarks, Envelopes, Greeting Cards, Letterheads, Notecards.
- **Marketing Materials:** Postcards, Flyers, Brochures, Door Hangers, Posters.
- **Large Format:** Adhesive Vinyl, Backlit Film, Car Magnet, Indoor/Outdoor Banners, PVC Signs, Large Format Service.

The About page also mentions Indigo digital, offset, wide-format and die-cut/packaging.

**Published "Starts from" prices:**

| Product | Starts from |
|---|---|
| Standard Business Cards | $16.67 |
| Envelopes | $97.00 |
| Greeting Cards | $65.85 |
| Letterheads | $55.00 |

Every other product shows no price.

**Promo:** code `NewI2!` gives 50% off the first order of Standard Business Cards.

## 2. Platform
- **Almost certainly OnPrintShop**, a hosted web-to-print SaaS. The evidence:
  - The CDN path is `/i2printon/`.
  - Logo file names follow `retailer_site_logo…`.
  - Pages are `.php`.
  - The site loads the `ops` icon font.
- **What it already does:** cart, required customer login, Request a Quote, file upload, online template designer, PDF proof approval, option-based estimates, and Visa/MC/Amex/Apple Pay/Google Pay. It also runs Google Tag Manager and has robots.txt and sitemap.xml.
- **Implication:** they already pay for ordering infrastructure (third-party sources put it at roughly $199+/mo, unverified). The pitch is to **make it sell and remove friction**, not to build e-commerce from zero.

## 3. Brand as it exists today
- **Logo:**
  - A stopwatch whose face is a full CMYK/rainbow color wheel, beside the wordmark "i2print".
  - The wordmark is charcoal, or white on dark backgrounds.
  - The tagline **"service. speed. success."** is set in cyan / yellow / magenta, the process ink colors.
  - The concept is strong and on-message: speed (stopwatch) + color (wheel) + print (CMY).
- **Web palette** (from `/themes/i2print/css/theme.css`):

  | Role | Color |
  |---|---|
  | Primary blue | `#5680E9` |
  | Light blue | `#6D91EC` |
  | Accent orange | `#FB8500` |
  | Text charcoal | `#36333C` |
  | Pale background | `#F6F8FE` |
  | Banner blue | `#2B7ABB` |
  | Gray | `#8B8B8B` |

- **Type:** Jost (Regular / Medium / SemiBold). Font Awesome 6 Pro icons.
- **Taglines in use:** "Everyone's local printer" · "Best value online printing company. High quality print delivered!" · "Speed, Service, and Quality. Your Success is Our Commitment!"
- **Homepage benefit headings (verified 2026-10-20):** Swift Turnaround · Secure Payment · Best Offers · Help Center. No actual turnaround times are published.
- **Voice:** generic store-template copy, frequent exclamation marks, some awkward grammar ("Subscribe our newsletter…", "Here's what our users speak about us").

## 4. Problems worth fixing (pitch talking points)
1. **Typos in the hero banners**, the first thing visitors see:
   - "BUINESS CARDS" and "busniess cards" in `i2print_banner_3_BC`.
   - "CHOSSE" and lorem-ipsum placeholder text on the flyer mockups in `banner1`.

   This is easy to show and easy to fix, and it hurts trust for a company that sells print quality.
2. **Nothing proves they're local.** There are no photos of the shop, presses or team, no owner story, hours, map, Google reviews, or pickup info. That's despite the tagline "Everyone's local printer."
3. **They compete on price against giants.** "Best value online printing" puts them up against Vistaprint and 4OVER4. Their real edge, local speed, pickup in LIC and a human who checks your file, is never stated.
4. **Local SEO is weak:**
   - No H1, and the title is a generic "Welcome to…".
   - The meta description doesn't mention LIC, Queens or NYC.
   - There's no LocalBusiness schema and no neighborhood/service landing pages.
   - The URL misspells "business-stationary" (should be "stationery"), and URLs carry numeric IDs.
5. **Ordering friction:**
   - An account is required before ordering.
   - Most products show no price.
   - The final price is confirmed "after you place the order."
   - Large format shows no sizes or prices.
6. **File-prep friction:**
   - The FAQ says 300 dpi minimum and accepts JPG/PNG/GIF/EPS/AI/PDF/PSD, with RGB converted to CMYK.
   - **Bleed and safe-zone measurements are never stated.**
   - Max file size, font outlining and reprint policy aren't documented either.
   - This is exactly the pain the "AI file fixer" idea targets.
7. **Weak trust signals:**
   - One undated testimonial ("Jen B").
   - No Google, Yelp or Trustpilot presence found.
   - Client logos are shown without context.
8. **The newsletter is there but gives no reason to join.** The copy is "hints, tips and the latest product news," with no offer attached.
9. **Weight:** the server is fast (about 0.5 s to first byte), but the page loads 22 scripts and 41 images. Run Lighthouse on mobile before the call.

## 5. What already works
- A real ordering stack (upload, designer, proofs, payments).
- A distinctive logo concept.
- Broad product range.
- Mobile viewport and canonical tags.
- An existing newsletter list (size unknown).
- Active social accounts.

## Sources
- https://www.i2print.com/ (homepage, About, FAQ, product pages, theme CSS), checked 2026-10-20
- https://www.atly.com/location/I2print (listing data)
- https://leadiq.com/c/i2printcom/5a1dba042300005b00b6df99 (third-party company data: unverified)
