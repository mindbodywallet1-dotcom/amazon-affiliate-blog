---
name: amazon-landing-pages
description: >-
  Scaffolds Astro affiliate landing pages from content drafts. Use when
  building landing pages, creating Astro pages, or working in the site/
  directory for Amazon affiliate content.
---

# Amazon Landing Pages

## Stack

- Astro 5 in `site/`
- Content collections in `site/src/content/affiliate/`
- Tailwind CSS for styling
- Components in `site/src/components/`

## Page creation workflow

1. Read content draft from `content/affiliate/{type}/{slug}.md`
2. Copy or write to `site/src/content/affiliate/{slug}.md`
3. Verify frontmatter matches schema in `site/src/content/config.ts`
4. Pick template by `type` field: review, roundup, comparison
5. Run `cd site && npm run dev` to preview at `/slug`

## Required frontmatter fields

```yaml
title: string
description: string
type: review | roundup | comparison
primary_keyword: string
asins: string[]
published: boolean
```

URL slug = filename without extension in `site/src/content/affiliate/`.

## Optional frontmatter

```yaml
hero_cta_text: "Check Price on Amazon"
verdict: "One-line recommendation"
quick_pick_asin: B0XXXXXX
comparison_winner: B0XXXXXX
```

## Component usage

| Component | When |
|-----------|------|
| `DisclosureBanner` | Every page — above fold |
| `AmazonCTA` | Primary purchase buttons |
| `ProsCons` | Review and roundup items |
| `ComparisonTable` | Comparison and roundup pages |
| `StickyCTA` | Mobile sticky bottom CTA |
| `SEOHead` | Meta + JSON-LD in layout |

## Templates

See [templates.md](templates.md) for per-type layout patterns.

## Config injection

Read `affiliate/config.yaml` (or `config.example.yaml` as fallback) for:
- `associate_tag`
- `disclosure_short`
- `site_url`

## Rules

- Every Amazon link uses `AmazonCTA` or passes through link builder
- `rel="nofollow sponsored"` on all affiliate links
- Disclosure banner renders before main content
- Do not hotlink Amazon product images — use `public/images/` or placeholders
