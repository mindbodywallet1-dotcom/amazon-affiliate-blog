# Email Flow Generator

## Trigger
On demand: "Generate email flows" or "Update email flows"

## Instructions
1. Read `brand/voice.md`, `products/catalog.yaml`, `campaigns/active.yaml`
2. Write/update flows in `content/email-flows/`
3. Each email: subject line, preview text, body (HTML-friendly plain text), CTA button text + URL

## Required flows
1. `welcome-series.md` — 3 emails (brand story → bestsellers → bundle offer)
2. `cart-abandon.md` — 2 emails (reminder → urgency + guarantee)
3. `post-purchase.md` — 2 emails (thank you + how to use → review request + cross-sell)
4. `browse-abandon.md` — 1 email
5. `win-back.md` — 1 email (60-day inactive)

## Rules
- Subject lines under 50 chars when possible
- Lead with benefit, not discount (except cart abandon email 2)
- Include free shipping $75+ and 30-day guarantee where relevant
- Flagship CTA: Best Value Bundle for welcome email 3
