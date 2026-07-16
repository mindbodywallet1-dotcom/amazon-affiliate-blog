---
name: amazon-seo-master
description: >-
  Plans Amazon affiliate SEO strategy including keyword clusters, topical
  authority maps, content calendars, and cannibalization checks. Use when
  building SEO strategy, keyword clusters, content plans, or topical maps.
---

# Amazon SEO Master (Strategy)

## Strategy workflow

1. Pick a seed niche or product category
2. Build a keyword cluster (1 pillar + 3-8 supporting pages)
3. Map search intent per keyword
4. Queue articles in `seo/affiliate-keywords.yaml`
5. Check for cannibalization before adding new targets

## Cluster structure

```yaml
clusters:
  - name: cluster-slug
    niche: niche-slug
    primary: ["head term"]
    long_tail: ["supporting terms"]
    article_queue:
      - title: "Pillar: Best X for Y"
        type: roundup
        slug: best-x-for-y
        status: queued | draft | published
        target_asins: []
```

## Pillar + spoke model

| Page type | Role | Example |
|-----------|------|---------|
| Pillar roundup | Head term target | "Best Air Fryers 2026" |
| Spoke review | Long-tail support | "Cosori Lite Review" |
| Spoke comparison | Decision stage | "Cosori vs Ninja Air Fryer" |
| Spoke roundup | Sub-niche | "Best Air Fryers Under $100" |

## Intent mapping

| Intent | Content type | Funnel stage |
|--------|-------------|--------------|
| Informational | How-to, guide | Top |
| Commercial | Roundup, best-of | Mid |
| Transactional | Review, comparison | Bottom |

## Cannibalization check

Before adding a keyword target:
1. Search existing `seo/affiliate-keywords.yaml` clusters for overlap
2. If two pages target the same primary keyword, merge or differentiate angle
3. Prefer one strong page over two weak competing pages

## Content calendar

Plan 1-2 new pages per week. Rotate niches to stay multi-niche:
- Week 1: Kitchen gadget roundup
- Week 2: Home office review
- Week 3: Fitness gear comparison

Track in `kpi/affiliate-weekly-template.csv`.

## Topical authority signals

- 4+ pages interlinked in one cluster before expecting rankings
- Consistent niche naming in `affiliate/niches/`
- Update `updated` dates on refresh passes (quarterly)

## Additional resources

See [reference.md](reference.md) for cluster templates and topical map examples.
