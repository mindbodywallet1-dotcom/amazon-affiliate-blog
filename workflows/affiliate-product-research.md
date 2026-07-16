# Affiliate Product Research Workflow

## Trigger
"Run affiliate product research" or "Research ASINs for {niche}"

## Instructions

1. Read `amazon-product-research` skill
2. Read `seo/affiliate-keywords.yaml` for existing clusters
3. Research the target niche on Amazon (4+ stars, 500+ reviews where possible)
4. Save niche brief to `affiliate/niches/{slug}.yaml`
5. Save each product to `affiliate/asins/{ASIN}.yaml`
6. Update `seo/affiliate-keywords.yaml` with `target_asins`
7. Run `python scripts/build_affiliate_link.py --all`

## Output checklist

- [ ] Niche YAML with keywords and angles
- [ ] 1+ ASIN YAML files with pros/cons
- [ ] Keyword cluster updated
- [ ] Affiliate links generated

## Rules

- No copied Amazon descriptions
- Price as range band, not guaranteed price
- Flag products with authenticity complaints
