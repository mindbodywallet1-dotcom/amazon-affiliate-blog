---
name: amazon-link-builder
description: >-
  Builds and validates canonical Amazon affiliate URLs with associate tag
  injection. Use when creating affiliate links, building Amazon URLs, or
  working with ASIN links.
---

# Amazon Link Builder

## Canonical URL format

```
https://www.amazon.com/dp/{ASIN}?tag={associate_tag}
```

Optional UTM params (for your analytics, not Amazon's):
```
&utm_source={source}&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}
```

## Build links

Single ASIN:
```bash
python scripts/build_affiliate_link.py B0C1H26V4V
```

All ASINs in `affiliate/asins/`:
```bash
python scripts/build_affiliate_link.py --all
```

## Config source

Reads `affiliate/config.yaml` (falls back to `config.example.yaml`):
- `associate_tag` — required
- `default_utm` — optional UTM defaults

## Output

- Updates `affiliate_url` field in `affiliate/asins/{ASIN}.yaml`
- Saves plain URL to `affiliate/links/{ASIN}.txt`

## Link rules

| Rule | Requirement |
|------|-------------|
| Domain | `www.amazon.com` (or locale-specific) |
| Path | `/dp/{ASIN}` |
| Tag | Must match `associate_tag` in config |
| rel | `nofollow sponsored` in HTML |
| target | `_blank` with `noopener noreferrer` |

## HTML pattern (AmazonCTA component)

```html
<a href="{url}" rel="nofollow sponsored" target="_blank" rel="noopener noreferrer">
  Check price on Amazon
</a>
```

## Validation

After building links:
```bash
python scripts/validate_affiliate_page.py
```

Checks every Amazon link in `site/src/content/` includes the associate tag.

## Do not

- Use bit.ly or other shorteners that hide the Amazon URL
- Hardcode tag in content — always inject from config
- Link to amazon.com without your tag (missed commission)
