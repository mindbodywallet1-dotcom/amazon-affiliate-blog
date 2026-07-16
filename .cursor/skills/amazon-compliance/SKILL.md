---
name: amazon-compliance
description: >-
  Enforces FTC disclosure and Amazon Associates Program compliance on affiliate
  content. Use for compliance checks, disclosure requirements, Associates
  operating agreement rules, or pre-publish legal review.
---

# Amazon Compliance

**Gate rule:** No affiliate page publishes without passing this checklist.

## Required on every page

1. Short disclosure above the fold (`DisclosureBanner` component)
2. Full disclosure in footer (from `affiliate/disclosure.md`)
3. All Amazon links have `rel="nofollow sponsored"`
4. All Amazon links include your `associate_tag`
5. Descriptive link text (not "click here" alone)

## Prohibited content

- Guaranteed prices or "always lowest price" claims
- "Click here to buy" as the only link text
- Incentivized click language ("click to support me")
- Misleading claims about Amazon endorsement
- Amazon logo or trademark misuse
- Hiding or obscuring disclosure
- Content targeting children under 13 for affiliate links
- Email/SMS with affiliate links (Amazon policy restriction)

## FTC requirements

- Clear and conspicuous disclosure before affiliate links
- Use plain language: "I earn a commission if you buy through my links"
- Social posts need #ad or equivalent where required
- Video content needs verbal + written disclosure

## Amazon Associates specific

- Do not use link shorteners that obscure Amazon URL
- Do not offer rebates or incentives for purchases
- Do not claim to represent Amazon
- Product images: use your own or Amazon-provided assets per program rules
- Keep privacy policy on site if collecting emails (future)

## Validation

```bash
python scripts/validate_affiliate_page.py
```

Fix all errors before setting `published: true`.

## Canonical copy

Always pull disclosure text from:
- `affiliate/disclosure.md`
- `affiliate/config.yaml` → `disclosure_short`, `disclosure_full`

## Additional resources

See [reference.md](reference.md) for the full policy checklist.
