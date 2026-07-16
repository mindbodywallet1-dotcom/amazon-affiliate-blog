# Affiliate Publish Checklist Workflow

## Trigger
"Publish affiliate page" or "Go live with {slug}"

## Pre-publish checklist

```
Compliance (amazon-compliance):
- [ ] Short disclosure above fold
- [ ] Full disclosure in footer
- [ ] All links have rel="nofollow sponsored"
- [ ] Descriptive CTA text
- [ ] No price guarantees

SEO (amazon-seo):
- [ ] Title 50-60 chars
- [ ] Meta description 150-160 chars
- [ ] Primary keyword in description
- [ ] Internal links to related pages

CRO (amazon-cro):
- [ ] Primary CTA above fold on mobile
- [ ] Sticky CTA on mobile
- [ ] Quick pick on roundup pages
- [ ] Verdict section present

Technical:
- [ ] published: true in frontmatter
- [ ] python scripts/validate_affiliate_page.py passes
- [ ] run affiliate-build succeeds
```

## Publish steps

1. Set `published: true` in `site/src/content/affiliate/{slug}.md`
2. Run `run affiliate-validate`
3. Run `run affiliate-build`
4. Deploy `site/dist/` to Vercel or Netlify
5. Update `seo/affiliate-keywords.yaml` → `status: published`
6. Log baseline in `kpi/affiliate-weekly-template.csv`

## Post-publish

- Submit URL to Google Search Console
- Share on Pinterest or other discovery channels (no direct affiliate links in IG/TikTok captions — link to your page)
