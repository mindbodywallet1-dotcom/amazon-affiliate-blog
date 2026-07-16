# Landing Page Templates

## Review template

```
AffiliateLayout
├── DisclosureBanner
├── Hero (H1 + description + AmazonCTA for primary ASIN)
├── Article body (markdown content)
├── ProsCons (from ASIN YAML)
├── Verdict box
├── AmazonCTA (repeat)
├── StickyCTA (mobile)
└── Footer disclosure
```

Frontmatter requirements: `type: review`, one ASIN in `asins`.

## Roundup template

```
AffiliateLayout
├── DisclosureBanner
├── Hero (H1 + quick pick callout)
├── Quick pick card (quick_pick_asin or first ASIN)
├── Article body (numbered picks)
├── ComparisonTable (all ASINs)
├── FAQ section (from markdown)
├── StickyCTA
└── Footer disclosure
```

Frontmatter requirements: `type: roundup`, 3+ ASINs recommended.

## Comparison template

```
AffiliateLayout
├── DisclosureBanner
├── Hero (H1 + "vs" framing)
├── ComparisonTable (2 ASINs side by side)
├── Article body (deep dive per product)
├── Winner callout (comparison_winner ASIN)
├── Dual AmazonCTA buttons
├── StickyCTA
└── Footer disclosure
```

Frontmatter requirements: `type: comparison`, exactly 2 ASINs.

## Slug and URL

- File: `site/src/content/affiliate/{slug}.md`
- URL: `/{slug}` via `[...slug].astro`
- Homepage links to published pages

## Adding a new page checklist

- [ ] Frontmatter complete
- [ ] ASIN YAML files exist
- [ ] Affiliate links generated
- [ ] Content copied to `site/src/content/affiliate/`
- [ ] `published: true` only after compliance pass
- [ ] Preview with `npm run dev`
