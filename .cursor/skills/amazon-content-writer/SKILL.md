---
name: amazon-content-writer
description: >-
  Writes Amazon affiliate reviews, roundups, comparisons, and buying guides.
  Use when drafting review content, best-of articles, comparison posts, or
  affiliate page copy.
---

# Amazon Content Writer

## Content types

| Type | Directory | Structure |
|------|-----------|-----------|
| review | `content/affiliate/reviews/` | Intro → features → pros/cons → verdict |
| roundup | `content/affiliate/roundups/` | Intro → quick pick → numbered list → FAQ |
| comparison | `content/affiliate/comparisons/` | Intro → table → deep dive → winner |

## Frontmatter template

```yaml
---
title: "Page Title With Primary Keyword"
description: "150-160 char meta description with keyword and value prop"
type: review | roundup | comparison
primary_keyword: "target keyword phrase"
asins:
  - B0XXXXXX
published: false
---
```

Note: URL slug is the filename in `site/src/content/affiliate/` (e.g. `cosori-lite-review.md`).

## Writing rules

1. Lead with buyer intent — answer "what should I buy?" in the first 100 words
2. Use H2 for major sections, H3 for sub-points
3. Include honest cons for every product — builds trust and complies with FTC
4. Never guarantee prices, availability, or Amazon ranking
5. Use descriptive CTA link text: "Check price on Amazon" not "click here"
6. Write original analysis — do not paraphrase Amazon listings

## Roundup structure

```markdown
## Quick pick: [Product Name]

[2-3 sentences on why it's the top pick]

## 1. [Product Name] — Best for [use case]

[150-200 words + pros/cons bullets]

**[Check price on Amazon →](affiliate_url)**
```

## Review structure

```markdown
## Who is this for?

## Key features

## What we like

## What to consider

## Verdict

**[See current price on Amazon →](affiliate_url)**
```

## Comparison structure

```markdown
## At a glance

[Comparison table reference — filled by Astro component]

## [Product A] overview

## [Product B] overview

## Which should you buy?

## Verdict
```

## After drafting

1. Copy final markdown to `site/src/content/affiliate/{slug}.md`
2. Ensure all ASINs exist in `affiliate/asins/`
3. Hand off to `amazon-link-builder` for URL generation
