# Vantage Weekly Public Signal Sweep

**Goal**: Deliver ~90% of PitchBook + Crunchbase value using only public, compliant sources + agentic AI workflows.

This is the minimal viable foundation. Once this runs successfully, we expand the registry with new sources from DeepSeek, ChatGPT, etc.

## Quick Start (15 minutes to first successful run)

### 1. Create the 4 secrets (Settings → Secrets and variables → Actions)

| Secret Name       | Value                                      |
|-------------------|--------------------------------------------|
| `GROK_API_KEY`    | Your xAI Grok API key (from console.x.ai)  |
| `CLAUDE_API_KEY`  | Your Anthropic key (optional for now)      |
| `SUPABASE_URL`    | Your Supabase project URL (optional)       |
| `SUPABASE_KEY`    | Your Supabase anon key (optional)          |

You can run the first sweep **without** any secrets — it will still work and print output.

### 2. Run first manual sweep (this proves everything works)
1. Go to your repo → **Actions** tab
2. Click **"Vantage Weekly Public Signal Sweep"**
3. Click **"Run workflow"** → green button

You should see green checkmarks + output showing all 12 sources.

## What this version does
- Loads the 12 core public sources (Companies House, EDGAR, OpenCorporates, TechCrunch, GitHub, YC, etc.)
- Prints a clean summary of what each source provides
- Proves the full pipeline works end-to-end

## Next (after first successful run)
Reply **"rails are live"** and we immediately:
- Add real Grok/Claude structured extraction
- Write results to Supabase
- Add Slack/email summary
- Expand the registry with your DeepSeek/ChatGPT sources

---

**This is the foundation. First successful sweep = rails complete.**
