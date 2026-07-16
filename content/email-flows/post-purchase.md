# Post-Purchase Series

## Email 1 — Thanks + How to Use (send immediately after order)

**Subject:** You're in — here's how to get started
**Preview:** Your order is confirmed. Quick tips inside.

**Body:**
Hey {{ first_name | default: "there" }},

Your order is confirmed. Thanks for trusting Wellthlab.

**What you ordered:**
{{ order.items }}

**Quick tips:**
- Oral strips: place on tongue, let dissolve. Up to 1 strip/day per tin.
- Capsules: take with water, ideally with a meal.
- Creatine: mix 1 scoop in 8oz water or juice daily.
- Consistency beats intensity — give it a few weeks.

Questions? Reply to this email anytime.

**CTA:** Shop more formulas → https://wellthlab.shop/collections/all

---

## Email 2 — Review + Cross-sell (send 10 days after delivery)

**Subject:** How's it going so far?
**Preview:** We'd love your honest take.

**Body:**
It's been about a week and a half — how are you feeling?

If {{ product.name }} is working for you, a quick review helps other people find formulas they can trust. Takes 30 seconds.

**CTA:** Leave a review → {{ product.review_url }}

**While you're here** — people who grab {{ product.name }} often stack it with:

- **Best Value Bundle** — full day coverage (energy + focus + sleep)
- **NAD+** — long-game cellular energy

**CTA:** Explore stacks → https://wellthlab.shop/collections/bundles

30-day guarantee still applies. We're here if anything's off.

— Wellthlab
