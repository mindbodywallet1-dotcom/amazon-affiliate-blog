# Affiliate Landing Page Workflow

## Trigger
"Build affiliate landing page for {topic}"

## Instructions

1. Read `amazon-affiliate-orchestrator` skill
2. Confirm ASIN research exists or run `affiliate-product-research` workflow
3. Read `amazon-seo-master` — lock slug and primary keyword in `seo/affiliate-keywords.yaml`
4. Read `amazon-content-writer` — draft to `content/affiliate/{type}/{slug}.md`
5. Read `amazon-link-builder` — run `python scripts/build_affiliate_link.py --all`
6. Read `amazon-landing-pages` — copy content to `site/src/content/affiliate/{slug}.md`
7. Read `amazon-seo` — verify title, meta, schema
8. Read `amazon-cro` — verify CTAs and above-fold layout
9. Preview: `run affiliate-dev`

## Content frontmatter

```yaml
title: string
description: string
type: review | roundup | comparison
primary_keyword: string
asins: []
published: false  # true only after publish checklist
```

Filename in `site/src/content/affiliate/` becomes the URL (e.g. `best-widgets.md` → `/best-widgets`).

## Output

- Content draft in `content/affiliate/`
- Published Astro content in `site/src/content/affiliate/`
- Preview URL at `http://localhost:4321/{slug}`
