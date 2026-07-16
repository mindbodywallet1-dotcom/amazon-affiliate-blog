# Cart Abandon Series

## Email 1 — Left something behind (send 1 hour after abandon)

**Subject:** Your cart is waiting
**Preview:** Still thinking it over? Here's what's inside.

**Body:**
Hey {{ first_name | default: "there" }},

You left something in your cart — no pressure, just wanted to make sure it didn't get lost.

{{ cart.items }}

Every Wellthlab formula is third-party tested, made in GMP-certified facilities, and backed by our **30-day happiness guarantee**. If it's not right, we'll make it right.

**CTA:** Complete your order → {{ cart.url }}

---

## Email 2 — Last chance + guarantee (send 24 hours after abandon)

**Subject:** Still on the fence?
**Preview:** 30-day guarantee. Free shipping $75+. Zero risk.

**Body:**
We get it — trying a new supplement brand takes trust.

Here's ours:
- Third-party tested every batch
- 30-day money-back guarantee
- Free shipping on orders $75+
- Subscribe & Save 15% if you want it on repeat

Your cart is still saved:

{{ cart.items }}

**CTA:** Finish checkout → {{ cart.url }}

If you have questions, just reply to this email. We're here.

— Wellthlab
