---
name: amazon-seo
description: >-
  Optimizes on-page SEO for Amazon affiliate landing pages including titles,
  meta descriptions, headings, schema markup, and internal links. Use when
  optimizing page SEO, meta tags, keyword placement, or structured data.
---

# Amazon SEO (On-Page)

## Checklist per page

```
- [ ] Title tag: 50-60 chars, primary keyword near front
- [ ] Meta description: 150-160 chars, includes keyword + CTA hook
- [ ] One H1 matching search intent (not identical to title tag)
- [ ] H2/H3 hierarchy with secondary keywords
- [ ] Primary keyword in first 100 words
- [ ] Internal links to 2+ related cluster pages
- [ ] Canonical URL set via SEOHead
- [ ] JSON-LD schema (Product, Review, or ItemList)
- [ ] OG tags for social sharing
```

## Title tag formula

| Type | Pattern |
|------|---------|
| Roundup | Best [Product] for [Use Case] (2026) |
| Review | [Product] Review: [Key verdict hook] |
| Comparison | [Product A] vs [Product B]: Which Is Better? |

## Meta description formula

`[Keyword] — [value prop]. [Social proof or count]. [Soft CTA].`

Example: "Best air fryers for small kitchens — tested picks for apartments and dorms. Compare top-rated compact models. Updated 2026."

## Schema by type

| Type | Schema |
|------|--------|
| review | `Product` + `Review` with rating |
| roundup | `ItemList` with `ListItem` per product |
| comparison | `Product` x2 + comparison attributes |

Implemented in `site/src/components/SEOHead.astro`.

## Internal linking

1. Read `seo/affiliate-keywords.yaml` for sibling pages in the cluster
2. Link using descriptive anchor text (not "click here")
3. Every new page should link to at least one existing page and be linked from one

## Files to edit

- Frontmatter in `site/src/content/affiliate/{slug}.md`
- `SEOHead.astro` if schema needs custom fields
- `seo/affiliate-keywords.yaml` — update `status: published` after go-live

## Avoid

- Keyword stuffing
- Duplicate titles across pages
- Multiple H1 tags
- Thin content under 800 words for roundups
