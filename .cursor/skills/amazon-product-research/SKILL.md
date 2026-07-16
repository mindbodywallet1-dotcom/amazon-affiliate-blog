---
name: amazon-product-research
description: >-
  Researches Amazon niches, ASINs, and competitor gaps for affiliate content.
  Use when finding products, ASIN research, niche ideas, or evaluating what to
  promote on Amazon Associates pages.
---

# Amazon Product Research

## Inputs

- Niche idea or seed keyword
- `seo/affiliate-keywords.yaml` for existing clusters
- `affiliate/niches/` for prior research

## Research workflow

1. Define the buyer intent: informational, comparison, or transactional
2. Search Amazon for top results in the niche (4+ stars, 500+ reviews ideal)
3. Check competitor affiliate sites for content gaps
4. Shortlist 3-8 ASINs per roundup; 1 ASIN per review; 2 ASINs per comparison
5. Record findings in YAML — never rely on memory

## ASIN selection criteria

| Signal | Good | Avoid |
|--------|------|-------|
| Rating | 4.3+ | Below 4.0 |
| Reviews | 500+ | Under 50 (unless new category) |
| Price | Matches article angle | Wildly off-topic |
| Availability | In stock, not discontinued | Frequent stockouts |
| Commission | Higher price tiers help | Ultra-low ticket spam |

## Output: niche file

Save to `affiliate/niches/{slug}.yaml`:

```yaml
name: niche-slug
description: One-line niche summary
updated: YYYY-MM-DD
target_keywords: []
angles: []
priority_asins: []
```

## Output: ASIN file

Save to `affiliate/asins/{ASIN}.yaml`:

```yaml
asin: B0XXXXXX
title: "Product Name"
niche: niche-slug
price_band: "$XX-YY"
rating: 4.5
review_count: 5000
affiliate_url: ""
researched: YYYY-MM-DD
pros: []
cons: []
best_for: "Who this product suits"
```

## Update keyword queue

Add or update the cluster in `seo/affiliate-keywords.yaml` with
`target_asins` filled in.

## Rules

- Do not copy Amazon product descriptions verbatim
- Note price as a range band, not a guaranteed price
- Flag any product with frequent authenticity complaints
- Prefer products you can write an honest pros/cons list for
