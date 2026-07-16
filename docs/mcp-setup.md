# MCP Setup for Wellthlab (Cursor)

MCP = how Cursor talks to outside tools (Blotato, Higgsfield, etc.) so agents can post and generate video for you.

**Time:** ~10 minutes for Blotato

---

## Step 1 — Get your Blotato API key

1. Go to [my.blotato.com](https://my.blotato.com)
2. **Settings → API**
3. Click **Generate API Key**

**Note:** Generating a key ends your free trial and starts paid Starter ($29/mo). API is required for MCP.

4. Under **"Other MCP Clients"**, click **Copy MCP Config** — easiest path; Blotato gives you ready-to-paste JSON.

**Important:** If your key ends with `=`, copy the **full** key including those characters. Dropping `=` causes 401 errors.

---

## Step 2 — Connect TikTok + Instagram in Blotato

Before agents can post:

1. Blotato → **Settings → Social Accounts**
2. Connect **TikTok** and **Instagram**
3. Confirm both show as connected

---

## Step 3 — Add MCP to Cursor

### Option A — UI (easiest if you're new)

1. Open Cursor
2. Press **Ctrl + Shift + J** (Settings)
3. Go to **Tools & MCP**
4. Click **+ Add New MCP Server**
5. Fill in:
   - **Name:** `blotato`
   - **Transport:** Streamable HTTP (or SSE)
   - **URL:** `https://mcp.blotato.com/mcp`
   - **Header:** key = `blotato-api-key`, value = your API key
6. Save

### Option B — Edit mcp.json (what Blotato's "Copy MCP Config" gives you)

**Global** (works in every project): edit `C:\Users\mindb\.cursor\mcp.json`

```json
{
  "mcpServers": {
    "blotato": {
      "url": "https://mcp.blotato.com/mcp",
      "headers": {
        "blotato-api-key": "PASTE_YOUR_FULL_KEY_HERE"
      }
    }
  }
}
```

**Project-only** (just wellthlab-marketing): create `.cursor/mcp.json` in the project with the same block.

---

## Step 4 — Restart Cursor

MCP servers load on startup.

1. Close Cursor completely
2. Reopen
3. Go to **Settings → Tools & MCP**
4. Blotato should show **connected** with tools listed

---

## Step 5 — Test it

Open the `wellthlab-marketing` project and ask:

> "Using Blotato, list my connected social accounts."

If it returns your TikTok/IG accounts, you're wired.

Then try:

> "Schedule a test post to TikTok for tomorrow at 9am: 'Testing Wellthlab automation' — use next free slot."

Review the queue in Blotato before letting test posts go live.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| 401 invalid API key | Re-copy full key including trailing `=` |
| Auth unsupported / OAuth error | Use API key config above, NOT OAuth URL alone |
| No tools showing | Restart Cursor; check URL is `https://mcp.blotato.com/mcp` |
| Account not found | Connect social accounts in Blotato Settings |
| Server disconnected | Settings → Tools & MCP → toggle server off/on |

Blotato debug dashboard: [my.blotato.com/api-dashboard](https://my.blotato.com/api-dashboard)

---

## Optional — Higgsfield (video generation)

Higgsfield uses a different setup (CLI or MCP at `https://mcp.higgsfield.ai/mcp`).

**CLI route (works with agents):**
```powershell
npm install -g @higgsfield/cli
higgsfield auth
```

Then agents can run: `higgsfield generate create --prompt "..." --wait`

Add Higgsfield MCP later if you want chat-based video gen inside Cursor.

---

## What you can say once Blotato is connected

| Prompt | What happens |
|--------|--------------|
| "Read content/week-01/blotato-schedule.md and schedule all 7 posts to TikTok and Instagram" | Queues your week |
| "Post Energy Strips caption from week-01 social.md to Instagram using next free slot" | Single post |
| "List my scheduled Blotato posts this week" | Review queue |

Always review supplement captions for FDA compliance before autopost goes fully hands-off.
