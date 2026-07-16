---
name: amazon-cro
description: >-
  Optimizes Amazon affiliate landing pages for conversions with CTA placement,
  above-fold hooks, trust signals, and A/B test hypotheses. Use when improving
  conversions, running CRO audits, or designing CTA layout.
---

# Amazon CRO

## Landing page anatomy (priority order)

1. **Disclosure** — above fold, non-intrusive but visible
2. **Hook** — answer the query in first sentence
3. **Quick pick** — roundup pages: show winner immediately
4. **Primary CTA** — above fold on mobile and desktop
5. **Social proof** — review counts, ratings (from ASIN data)
6. **Body content** — scannable with bullets and tables
7. **Repeat CTA** — after verdict section
8. **Sticky CTA** — mobile bottom bar

## CTA copy patterns

| Weak | Strong |
|------|--------|
| Click here | Check price on Amazon |
| Buy now | See today's price on Amazon |
| Amazon | View [Product Name] on Amazon |

## Trust signals

- Honest cons section (increases trust and time-on-page)
- "Last updated" date in hero or footer
- Specific product names in CTAs (not generic)
- Author/site credibility line on index page

## Above-fold test

On mobile (375px width), user must see without scrolling:
- H1
- Disclosure
- 1-2 sentences of value
- Primary CTA button

## A/B hypotheses to log

Track ideas in page frontmatter or growth notes:

```yaml
cro_tests:
  - hypothesis: "Sticky CTA increases mobile CTR"
    variant: sticky-cta-on
    status: active
```

## Component mapping

| CRO element | Component |
|-------------|-----------|
| Primary button | `AmazonCTA` |
| Mobile sticky | `StickyCTA` |
| Quick pick card | Hero section in layout |
| Comparison shortcut | `ComparisonTable` |
| Pros/cons scan | `ProsCons` |

## Metrics to watch

Log weekly in `kpi/affiliate-weekly-template.csv`:
- Sessions per page
- Amazon clicks (from Associates dashboard)
- Click-through rate = clicks / sessions

## Additional resources

See [reference.md](reference.md) for the full CRO audit checklist.
