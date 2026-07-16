# Wellthlab Marketing Ops

**Not a script folder. A machine that runs tasks.**

Project: [wellthlab.shop](https://wellthlab.shop)

## Run this (Windows)

```bat
run install          REM once
run sync             REM pull products from store
run dry-run          REM preview Blotato schedule
run schedule         REM upload videos + queue to TikTok/IG
run status           REM what's connected + queued
```

Full guide: [OPERATE.md](OPERATE.md)

## Amazon Affiliate (new)

Multi-niche Amazon Associates landing pages via Astro static site.

```bat
run affiliate-install    REM once — npm deps in site/
run affiliate-link --all   REM build affiliate URLs from ASINs
run affiliate-validate     REM compliance + SEO checks
run affiliate-dev          REM preview at localhost:4321
run affiliate-build        REM build to site/dist/
```

Team roster and skills: [AGENTS.md](AGENTS.md)

### Affiliate weekly loop

1. **Cursor** — "Run affiliate weekly content" (research → draft → page)
2. **You** — `run affiliate-validate` then `run affiliate-build`
3. **Deploy** — push `site/dist/` to Vercel or Netlify

Copy `affiliate/config.example.yaml` → `affiliate/config.yaml` and set your Associates tracking ID.

## Your weekly loop (Wellthlab DTC)

1. **Claude Code** — makes videos, saves to `posts/media/` (or paste Higgsfield URLs in `posts/queue.yaml`)
2. **You** — `run schedule` (or tell Cursor: "run schedule")
3. **Blotato app** — quick glance at queue. Done.

No copying captions between AIs.

## In Cursor chat

| Say | I run |
|-----|-------|
| `run schedule` | Upload + queue posts |
| `run sync` | Refresh product list from store |
| `run status` | Blotato accounts + queue |

## Project layout

```
posts/queue.yaml         Post queue (captions + video paths)
posts/media/             Drop videos here
affiliate/               Amazon Associates config + ASIN research
site/                    Astro affiliate landing pages
content/affiliate/       Content drafts (reviews, roundups)
AGENTS.md                Amazon affiliate team roster
scripts/                 Automation that actually runs
products/catalog.yaml    Product source of truth
OPERATE.md               How to use everything
```

## Claude Code vs Cursor

| Claude Code | This repo |
|-------------|-----------|
| Write + film videos | Schedule to Blotato |
| Shopify admin | `run sync` from live store |
| Creative | `run status` — what's queued |
