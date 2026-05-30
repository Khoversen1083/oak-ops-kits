# Oak Ops Skills

Claude Code skills that power the kits + a few standalone ones useful for any
operator. Drop one or all into `~/.claude/skills/`, restart Claude Code,
invoke by description ("scrape leads from google maps", "label my gmail
inbox", "make an instagram carousel about X").

## What's in here

| Skill | What it does |
|---|---|
| `agent-browser` | Headless Chrome automation via the agent-browser CLI. Used by many kits. |
| `browser-stealth` | Stealth browsing for sites that block normal automation (Cloudflare, captchas). |
| `carousel` | Generate a viral 8-slide Instagram carousel (1080x1350 JPGs) from a single carousel.json. |
| `casualize-names` | Convert formal names to casual versions for cold email personalization. |
| `classify-leads` | LLM-based lead classification for complex distinctions (SaaS vs agency, etc). |
| `create-proposal` | Generate PandaDoc proposals from client info or sales call transcripts. |
| `design-website` | Generate a premium mockup website for a prospect. |
| `fathom-transcript-pull` | Pull a Fathom call transcript and file it correctly. |
| `gmaps-leads` | Scrape Google Maps for local B2B leads with website enrichment + contact extraction. |
| `instantly-autoreply` | Intelligent replies to incoming Instantly email threads. |
| `instantly-campaigns` | Create cold email campaigns in Instantly with A/B testing. |
| `lead-magnet` | Branded lead magnet PDF generator. |
| `welcome-email` | Send welcome sequence to a new client. |

## Install

### Option A: All at once

```bash
cd ~/Coding/oak-ops-kits
mkdir -p ~/.claude/skills
cp -r skills/* ~/.claude/skills/
```

Restart Claude Code. The skills auto-discover.

### Option B: One at a time

```bash
cp -r skills/gmaps-leads ~/.claude/skills/
```

Restart Claude Code. Invoke by saying "scrape google maps for [niche] in
[city]".

## Verify install

In Claude Code, run `/help` and the new skills should appear in the
auto-discovered list. Or just describe what you want and Claude will pick
the matching skill.

## What each skill needs

Most skills need at least one external tool installed. Each skill's
`SKILL.md` documents its dependencies (Apify, Apollo, Instantly, PandaDoc,
gws CLI, etc). Don't worry about installing them all upfront — install as
you reach for the skill.

## Customizing

Every `SKILL.md` is a markdown file with a YAML frontmatter. Edit freely.
Your changes stay local to your `~/.claude/skills/` and never affect this
repo. To pull updates from this repo:

```bash
cd ~/Coding/oak-ops-kits
git pull
cp -r skills/* ~/.claude/skills/   # re-copy, your edits get overwritten
```

If you want to keep local edits and also pull updates, fork the repo and
diff against your fork.

## Why these specific skills

This is the curated set I use to run lead acquisition, discovery, pricing,
delivery, and content. They map 1:1 to the kits under `../kits/`:

- Lead gen kits → `gmaps-leads`, `classify-leads`, `casualize-names`
- Cold email kits → `instantly-campaigns`, `instantly-autoreply`
- Discovery + content kits → `fathom-transcript-pull`, `create-proposal`
- Brand + funnel → `carousel`, `lead-magnet`, `design-website`
- Foundation → `agent-browser`, `browser-stealth`
- Client work → `welcome-email`

More skills will land here over time. PRs welcome.

## License

MIT, same as the repo root.
