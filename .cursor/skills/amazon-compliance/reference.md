# Amazon Associates Compliance Checklist

## Pre-publish (every page)

- [ ] FTC disclosure visible above the fold
- [ ] Full disclosure in footer
- [ ] All links contain `tag={associate_tag}`
- [ ] All links have `rel="nofollow sponsored"`
- [ ] Link text is descriptive
- [ ] No price guarantees
- [ ] No "Amazon recommends" or implied endorsement
- [ ] No incentivized click language
- [ ] Content is original (not copied from Amazon listings)
- [ ] `published: true` only after validation passes

## Site-wide (once)

- [ ] `affiliate/config.yaml` has valid associate tag
- [ ] Privacy policy page (when email capture added)
- [ ] About page with affiliate relationship explained
- [ ] Associates tag in Amazon dashboard matches config

## Periodic review (quarterly)

- [ ] Re-read Amazon Associates Operating Agreement for policy changes
- [ ] Check for broken ASINs / discontinued products
- [ ] Update disclosure if FTC guidance changes
- [ ] Verify all outbound links still include tracking tag

## Red flags — stop and fix

| Issue | Action |
|-------|--------|
| Missing disclosure | Add `DisclosureBanner` immediately |
| Link without tag | Re-run `build_affiliate_link.py` |
| Copied Amazon description | Rewrite content |
| Fake review claims | Remove or substantiate with real testing |
| Coupon/deal page violating pricing rules | Remove price claims |

## Social media

- Include #ad or "affiliate link" in captions
- Do not post affiliate links directly in Instagram/TikTok captions
  (link in bio to your landing page instead)
