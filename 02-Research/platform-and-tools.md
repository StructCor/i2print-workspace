# i2Print — Platform, File-Fix and Email Tooling

**Checked:** 2026-10-20. Most prices come from third-party aggregators. **Confirm on each vendor's own pricing page before you quote them to the client.**

## 0. DECISION UPDATE (2026-10-20): i2Print wants to leave OnPrintShop
Daniel confirmed with the client that i2Print is looking to move away from OnPrintShop. They're also unhappy with their current developer (about $100k spent without the results they wanted) and are in a contract. **Path A (keep OnPrintShop) is no longer the recommendation.** It stays below for reference.

### Recommended: a phased move (front first, store second)
| Phase | What happens | Why |
|---|---|---|
| **1. Discovery & exit planning** | Confirm which contract they're in and its end date (their attorney handles the exit). List everything to export. Choose the target platform. | Never break the contract early. Know what data you can get out before promising a date. |
| **2. New marketing site + file check, live alongside the old store** | Next.js on Vercel at `www.i2print.com`: local SEO pages, the file-check tool, email signup. "Order" buttons link to the existing OnPrintShop store until cutover. | Quick visible wins. Builds trust after the $100k experience. **Changes nothing in OnPrintShop**, so it's contract-safe. |
| **3. Store migration (timed to the contract end)** | Move products and pricing, customers and templates to the new commerce backend one product family at a time, starting with business cards. Run both stores side by side briefly. Redirect every old URL. | Lowest-risk cutover. Done in their slow season. |
| **4. Email & growth** | Welcome offer, pickup and reorder emails, review requests. | Turns the new site into repeat orders. |

### Target platform for the store (recommendation: Shopify as the commerce backend)
| Option | Pros | Cons | Fit |
|---|---|---|---|
| **Shopify** (theme, or headless with the Next.js front end) | Shopify handles checkout, payments and card security. Staff-friendly admin. Huge app ecosystem (Filecheck preflight, product options, design tools). The client owns the account. | Print pricing by size × stock × quantity needs an options/pricing app or custom logic: **prototype this first.** Monthly app fees. | **Recommended.** Keeps payment and security risk off you. |
| Another web-to-print platform (shopVOX, DecoNetwork, PressWise, etc.) | Built-in print pricing, proofs and job tickets | Same lock-in risk they're escaping. Less design control. | Consider if Shopify can't handle their pricing |
| Fully custom (Next.js + Stripe + database) | Total control | You own payments, the pricing engine, security and uptime, with $250K E&O | **Not for a first client** |
| WooCommerce + wp2print | Cheap per month | Plugin and security upkeep falls on you | Second choice if budget is very tight |

### Migration checklist (verify in discovery; export ability is unconfirmed)
- [ ] **Contract:** who it's with (the developer, OnPrintShop, or both), end date, notice terms, early-exit cost. Their attorney reviews it.
- [ ] **Exports from OnPrintShop:** products and options, pricing rules, customer list (emails), order history, saved templates, customer-uploaded artwork. Get sample exports early.
- [ ] **Ownership:** templates, designs and custom code the previous developer built. Who owns them, under the contract?
- [ ] **Accounts:** domain registrar, DNS, Google Business/Analytics/Search Console, email sending, all in i2Print's name.
- [ ] **SEO:** list every current URL so each one can be redirected to its new page (keeps Google rankings).
- [ ] **Customers:** passwords won't carry over. Plan a "set your new password" email and a reorder path.
- [ ] **Payments:** new merchant account or Shopify Payments set up and tested before cutover.
- [ ] **Production:** how orders reach the shop floor today, and how they will afterward.

### Pricing implication
The migration is the riskiest, most variable part of the job. **Price it separately, after the export review**, not inside the build range. The earlier Path B range ($8,000–15,000) assumed a simple catalog. Complex pricing rules or hundreds of products push it higher.

## 1. The big decision: keep OnPrintShop or replace it?
i2Print already runs OnPrintShop. Two realistic paths:

| | **Path A: Keep OnPrintShop, fix the front** | **Path B: New marketing site + ordering backend** |
|---|---|---|
| What changes | Theme/CSS refresh, homepage and product copy, local SEO pages, schema, fixed typos and banners, real photos, file-check page, newsletter offer | Next.js site on Vercel (Daniel's CCP stack) for marketing and SEO; orders hand off to OnPrintShop or move to Shopify |
| Pros | Lowest cost and risk; staff workflow unchanged; fastest to launch | Full design control, speed, custom tools (configurator, file fixer), and Daniel owns the code quality |
| Cons | Limited by the OnPrintShop theme system | Two systems to keep in sync, or a platform migration (products, pricing rules, customer accounts) |
| Questions for discovery | What do they pay? Contract term? What frustrates them? Can the theme be customized, and does OnPrintShop have an API? | Will they leave OnPrintShop? Who manages product pricing day to day? |

**Default recommendation going into the call:** Path A first, with the file-fix tool and email as add-ons. Revisit Path B after 90 days of data.

### Other web-to-print platforms (third-party pricing, unverified)
| Platform | Starting price (approx.) | Notes |
|---|---|---|
| OnPrintShop | ~$199/mo base (one user reported ~$500/mo) | Storefront + designer + upload: **current platform** |
| shopVOX | Express ~$99/mo, PRO ~$199/mo + ~$19–39/user | Shop management + quotes |
| Printavo | Conflicting: $49–149 or $199–329/mo | Shop management, not a full storefront |
| DecoNetwork | ~$199/mo | Apparel/decoration focus |
| PressWise | ~$495/mo (may be dated) | Enterprise W2P |
| wp2print (WooCommerce) | ~$70–100/mo | Price calculators, designer |
| Shopify + apps | Shopify plan + Filecheck ($0/$39/$99), Zakeke (~$29.90), Customily (~$49 + fees), Custom Upload Studio ($9–29) | Filecheck does preflight, auto-fixes bleed/low-res/RGB, shows a soft proof, and blocks add-to-cart on failure |

## 2. The "AI file fixer": how it really works
Most of this is **deterministic image math, not AI**. Being honest about that keeps it cheap and reliable.

| Step | Technique | Tool | AI? |
|---|---|---|---|
| Read size and effective DPI at the chosen print size | pixels ÷ inches | sharp (Node), or the browser canvas for a demo | No |
| Check aspect ratio against the product (e.g., 3.5×2" card = 1.75:1) | ratio compare | same | No |
| Add bleed (typically 0.125" per side, **confirm i2Print's spec**) and draw the safe zone | geometry | same | No |
| **Fit** (pad with a background color) or **Fill** (center crop) | resize/crop | sharp | No |
| **Extend** the background to the new ratio without cropping | generative outpainting | Cloudinary `b_gen_fill`, Gemini image editing, Adobe Firefly Generative Expand | **Yes** |
| Upscale low-res images | AI super-resolution | Claid.ai ($15/mo for 500 credits; older pricing), Cloudinary | **Yes** |
| PDF checks (TrimBox/BleedBox, fonts, color space) | PDF parsing | pdf-lib; Ghostscript/poppler (Ghostscript is AGPL, so commercial use may need an Artifex license) | No |
| Industrial preflight | rules engine | callas pdfToolbox (from ~€625 desktop / ~€5,000 server), Enfocus PitStop | No. Overkill for a small shop |

**Rules for the tool:**
- AI never silently changes customer artwork.
- Every fix produces a **proof the customer approves**.
- Text and logos are never regenerated.
- Low-res warnings are shown, not hidden.

**Rough per-use cost:** deterministic steps are effectively free at small-shop volume. AI extend/upscale runs about cents per image on credit plans; confirm with the chosen vendor.

## 3. Email / newsletter platforms (third-party pricing)
| Platform | Approx. price | Fit |
|---|---|---|
| Klaviyo | Free ≤250 profiles; ~$20/mo @500; ~$100/mo @5,000 | Best automations (welcome, win-back, reorder reminders) |
| Mailchimp Standard | ~$20/mo @500 (unsubscribed contacts still count unless archived) | Familiar, easy for staff |
| ActiveCampaign Starter | ~$15–19/mo @1,000 | Strong automation |
| Shopify Messaging (formerly Shopify Email) | 10k free emails/mo, then ~$1/1,000 | Only if they move to Shopify |
| Resend + React Email | Marketing tier from ~$40/mo (free tier reported ≤1,000 contacts in 2025) | Developer-managed; Daniel already uses Resend on CCP |

**Suggested starter flows:**
1. Welcome email with the first-order offer (the existing `NewI2!` code).
2. "Your order is ready for pickup" with a review request.
3. A 60/90-day reorder reminder for business cards.
4. A monthly promo or seasonal campaign (graduation, holidays, election season, restaurant menus).

## Sources
- OnPrintShop pricing: https://zoftwarehub.com/products/onprintshop/pricing · https://signs101.com/threads/onprintshop-b2c-b2b-software.160991/
- shopVOX: https://softwareconnect.com/roundups/best-print-shop-management-software/
- Printavo: https://www.capterra.co.uk/software/154421/printavo · https://saasrat.com/products/printavo
- DecoNetwork: https://us.fitgap.com/products/033621/deconetwork
- PressWise: https://www.krowdbase.com/software/presswise
- wp2print: https://www.capterra.com/p/173857/wp2print/
- Filecheck: https://apps.shopify.com/filecheck · Upload-by-size: https://apps.shopify.com/upload-by-size-v2 · comparison: https://www.designnbuy.com/?p=270029
- Cloudinary generative fill: https://cloudinary.com/documentation/generative_fill
- Adobe Firefly enterprise: https://redresscompliance.com/adobe-firefly-enterprise-pricing-2026
- callas pdfToolbox: https://pdfa.org/callas-software-releases-pdftoolbox-14/ · Enfocus: https://enfocus.com/en/node/2200
- Claid.ai: https://help.claid.ai/en/category/account-billing-dyuznz/
- remove.bg: https://costbench.com/software/ai-media-apis/remove-bg-api/
- Klaviyo: https://www.moengage.com/blog/klaviyo-pricing/ · Mailchimp: https://tinycommand.com/blogs/mailchimp-pricing-explained · Shopify Messaging: https://www.aitrillion.com/blog/shopify-email-marketing-cost-pricing-guide · ActiveCampaign: https://flowium.com/blog/activecampaign-pricing/ · Resend: https://www.usecarly.com/blog/resend-pricing/
