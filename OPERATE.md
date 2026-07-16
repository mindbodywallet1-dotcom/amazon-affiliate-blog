# How to run this (3 commands)

This is not a content library. It's a **machine** that runs tasks.

## Setup once

```bat
run install
```

## Your weekly loop

### 1. Claude Code makes videos
Export to `posts/media/` with these names:
- `day-01-energy.mp4`
- `day-02-bundle.mp4`
- ... (see `posts/queue.yaml`)

### 2. You run one command

```bat
run schedule
```

This will:
- Upload each video to Blotato
- Queue to TikTok + Instagram (next free slot)
- Mark posts as `scheduled` in `posts/queue.yaml`

### 3. Glance at Blotato app
Confirm queue looks right. Done.

---

## Other commands

| Command | What it does |
|---------|--------------|
| `run sync` | Pull latest products from wellthlab.shop |
| `run status` | Show Blotato accounts + scheduled posts |
| `run dry-run` | Preview schedule without posting |
| `run schedule --id day-01-energy` | Schedule one post only |

---

## Amazon Affiliate loop

### Setup once

```bat
run affiliate-install
```

Copy `affiliate/config.example.yaml` to `affiliate/config.yaml` and set your Amazon Associates tracking ID.

### Weekly affiliate loop

1. **Cursor** — "Run affiliate weekly content" or "Build affiliate landing page for {topic}"
2. **Validate** — `run affiliate-validate`
3. **Build** — `run affiliate-build`
4. **Deploy** — upload `site/dist/` to Vercel or Netlify

### Affiliate commands

| Command | What it does |
|---------|--------------|
| `run affiliate-install` | Install Astro/npm deps in `site/` |
| `run affiliate-link B0XXXXXX` | Build one affiliate URL |
| `run affiliate-link --all` | Build URLs for all ASINs |
| `run affiliate-validate` | Compliance + SEO validation |
| `run affiliate-dev` | Local preview at localhost:4321 |
| `run affiliate-build` | Production build |

See [AGENTS.md](AGENTS.md) for the full specialist team and skills.

---

## Split with Claude Code

| Claude Code | This project (Cursor) |
|-------------|----------------------|
| Write + film videos | Upload + schedule to Blotato |
| Fix Shopify in admin | `run sync` keeps catalog fresh |
| Creative one-offs | `run status` — what's queued |

**No copy-paste between AIs.** Claude Code drops files in `posts/media/`. You run `run schedule`.

---

## In Cursor chat

- "Run schedule" → I execute `run schedule`
- "Sync my store" → I execute `run sync`
- "What's queued on Blotato?" → I execute `run status`

---

## Reset a post

In `posts/queue.yaml`, change `status: scheduled` back to `status: pending` to re-run.
