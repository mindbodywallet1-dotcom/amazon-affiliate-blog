# Wellthlab content stack

## Current tools
| Tool | Role |
|------|------|
| **Claude Code** | Store build, Canva asset creation, Higgsfield AI video |
| **Canva** | Static graphics, carousels, thumbnails |
| **Higgsfield AI** | Video generation / UGC-style clips |
| **Blotato** | Schedule + publish to TikTok, Instagram, etc. |
| **Cursor (this project)** | Scripts, captions, UTMs, email copy, catalog, weekly planning |
| **Astro** | Amazon affiliate SEO landing pages (`site/`) |
| **Vercel / Netlify** | Deploy affiliate static site |
| **Amazon Associates** | Affiliate tracking + commission reporting |

## Stage (Jul 2026)
- Site live: wellthlab.shop (new)
- Sales: pre-revenue / not selling yet
- Social: small existing presence, building up

## Weekly pipeline

```
Cursor generates scripts + captions (content/week-XX/social.md)
        ↓
Claude Code + Canva + Higgsfield → video/image assets
        ↓
Blotato → schedule to TikTok / Instagram
        ↓
Track link clicks + profile visits (before pixel data exists)
```

## Blotato upload checklist (per post)
- [ ] Video file from Higgsfield or Canva
- [ ] Caption from `content/week-XX/social.md`
- [ ] Link in bio → product URL with UTM from script
- [ ] Post time: test 7am, 12pm, 6pm local — note what wins

## Pre-revenue priorities (first 30 days)
1. **Post consistently** — 5–7x/week beats perfect content
2. **One hero product per week** — don't promote all 11 at once
3. **Link in bio** → Best Value Bundle or Energy Strips (clearest hook)
4. **Get 3–5 reviews** — friends/family beta or launch discount for honest review
5. **Fix store bugs** (see store fix list) before pushing paid traffic
6. **Email capture** — popup/flyout live; Klaviyo welcome flow ready
7. **Don't run paid ads yet** — until pixels fire + at least 10 organic posts live

## Amazon affiliate priorities (parallel track)
1. **Set Associates tag** — `affiliate/config.yaml`
2. **Publish 1 landing page** — `run affiliate-build` → deploy
3. **One niche cluster** — 3+ interlinked pages before expanding
4. **Validate every page** — `run affiliate-validate` before go-live
5. **Track weekly** — `kpi/affiliate-weekly-template.csv`

## What to tell Cursor each week
- `Run weekly social workflow` → fresh scripts for Blotato
- `Make this Blotato-ready` → strips shot lists into short caption-only cards
- `Sync catalog from wellthlab.shop` → after any product changes
