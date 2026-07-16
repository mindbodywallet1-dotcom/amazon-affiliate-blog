# SEO Master Reference

## Cluster template: product category

```yaml
- name: best-{product-category}
  niche: {niche-slug}
  primary:
    - "best {product} {year}"
  long_tail:
    - "best {product} for {use case}"
    - "best {product} under {price}"
    - "{product} reviews"
  article_queue:
    - title: "Best {Product} ({Year})"
      type: roundup
      slug: best-{product}-{year}
      status: queued
      target_asins: []
    - title: "Best {Product} for {Use Case}"
      type: roundup
      slug: best-{product}-{use-case}
      status: queued
      target_asins: []
    - title: "{Top Product} Review"
      type: review
      slug: {product-slug}-review
      status: queued
      target_asins: []
```

## Topical map example: kitchen-gadgets

```
best-air-fryers (pillar)
├── best-air-fryers-small-kitchen (spoke roundup)
├── cosori-lite-review (spoke review)
├── cosori-vs-ninja-air-fryer (spoke comparison)
└── best-air-fryers-under-100 (spoke roundup)
```

## Refresh cadence

| Page age | Action |
|----------|--------|
| 0-3 months | Monitor rankings, fix technical issues |
| 3-6 months | Update intro, check ASIN availability |
| 6-12 months | Full content refresh, re-date title |
| 12+ months | Consider merge, redirect, or rewrite |

## Multi-niche rotation

Keep 2-3 active clusters at a time. Do not start a 4th until the oldest
cluster has at least 3 published interlinked pages.
