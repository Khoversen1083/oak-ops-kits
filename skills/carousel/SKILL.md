---
name: carousel
description: Generate a viral 8-slide Instagram carousel (1080x1350 JPGs) for @kevhov.ai from a single carousel.json input. Renders an obsidian/indigo magazine-style slideshow with the locked 8-slide viral arc (hook, stakes, system, 3 steps, payoff, CTA). Trigger on "carousel", "slideshow", "/carousel", "build the carousel for [keyword]", "make the slideshow", or whenever Kevin wants an IG feed carousel paired with (or independent of) a reel.
---

# IG Carousel Skill

## What this is

Kevin posts three pieces of content per day on @kevhov.ai: one talking reel, one showing reel, one slideshow carousel. This skill builds the slideshow carousel.

Output is a numbered sequence of 8 JPGs at 1080x1350, landed in iCloud `00-Post Today/<keyword>-carousel/carousel/` so Kevin can swipe them onto his phone and post via the Instagram app (same flow as his reels).

No Drive upload. No auto-post. The slideshow is the artifact, posting stays manual on phone.

## When to use

- "Build the carousel for ENGINE"
- "Make the slideshow for today's reel"
- "/carousel"
- Whenever there's a topic that fits the 8-slide arc (system + steps + payoff)
- Paired mode: a reel already shipped today, mirror it into a carousel
- Independent mode: standalone topic that isn't tied to a reel

## The locked 8-slide arc

This is the IP. Do not deviate. Research keeps confirming the arc is what converts, not the visual:

| Slide | Slot | Rule |
|-------|------|------|
| 01 | hook | 5-8 word headline. Pattern interrupt. Curiosity gap. No CTA. |
| 02 | stakes | One sentence under 12 words. Frame the cost of NOT having this. |
| 03 | system | Name the system + one-liner. Three named blocks shown as a row. |
| 04 | step | Step 01. Concrete beat with bolded keywords. |
| 05 | step | Step 02. Concrete beat. |
| 06 | step | Step 03. Concrete beat. |
| 07 | payoff | What changes. Specific outcome, not vibes. |
| 08 | cta | "comment KEYWORD" pill + @kevhov.ai signature. |

Slides 1-2 share a continuous-canvas diagonal stripe (forces swipe).

## Markdown shortcuts inside JSON strings

- `*text*` -> indigo accent span (use 1-2 per headline, never more)
- `**text**` -> bold ink in body copy (use to land the keyword in each step)

## Voice rules (from CLAUDE.md)

- Terse, lowercase fragments where possible
- No em dashes, no emojis
- No hype words ("game-changer", "revolutionary", "unlock", "the future is here")
- Threat-framed hooks beat benefit-framed hooks (see memory: feedback_threat_framing_hooks)
- Hook headline: 5-8 words, ideally one accent span

## Workflow

### 1. Collect inputs

Ask Kevin if not provided (one question, all at once):
- **Keyword** (ENGINE, STACK, OS, etc.) — the ManyChat trigger
- **Hook** (5-8 words, what's the threat or curiosity gap)
- **Stakes** (under 12 words, what's the cost of not having this)
- **System name + one-liner + three named blocks** (the framework)
- **3 steps** (each: title + 1-sentence body with bolded keyword)
- **Payoff** (specific outcome)
- **CTA body** (one sentence teasing what the lead magnet contains)

Paired mode: if Kevin says `/carousel` from inside a reel folder (e.g. `content/reels/2026-05-17-engine/`), read `caption.txt` and `SCRIPT.md` from that folder, draft the 8 fields, then write `carousel.json` next to them. Always show Kevin the drafted JSON for review before rendering.

### 2. Write carousel.json

Place at one of:
- Paired mode: `<reel-folder>/carousel.json`
- Independent mode: `00-Post Today/<date>-<keyword>-carousel/carousel.json`

Reference schema in `examples/carousel-engine/carousel.json`. Required keys: `keyword`, `hook`, `stakes`, `system_name`, `steps` (exactly 3), `payoff`. Optional: `hook_sub`, `system_oneliner`, `system_blocks`, `cta_body`.

### 3. Render

Run:

```bash
python3 ~/.claude/skills/carousel/render.py <path/to/carousel.json>
```

Or from a reel folder containing carousel.json:

```bash
python3 ~/.claude/skills/carousel/render.py <path/to/reel-folder>
```

The script:
1. Validates the JSON against the schema (8 slots, 3 steps required)
2. Renders 8 HTML files to `/tmp/carousel-<keyword>-<date>/`
3. Chrome headless `--screenshot` each at 1080x1350 @ 2x DPI
4. `sips` converts PNG -> JPG at quality 92, resized to exactly 1080x1350
5. Writes `01.jpg` ... `08.jpg` to iCloud output folder

Takes ~30-60 seconds end to end.

### 4. Return deliverables to chat

- Output folder path (so Kevin can swipe to phone via Files app)
- The 8 JPG paths in order
- A paste-ready IG caption (lowercase fragments, no emojis, no CTA in caption — the CTA is the slide)
- Reminder: pin the keyword comment via ManyChat after posting

## Hard rules

- Never write to `~/Desktop/`
- Never deviate from the 8-slide arc
- Never invent statistics or client quotes
- Never use em dashes or emojis in rendered slides
- Always exactly 3 steps in `steps[]` (render.py will fail otherwise)
- Hook headline must be 5-8 words after stripping markdown

## Output location

iCloud Drive:
```
~/Library/Mobile Documents/com~apple~CloudDocs/@kevhov.ai/00-Post Today/<date>-<keyword>-carousel/carousel/
  01.jpg
  02.jpg
  ...
  08.jpg
```

In paired mode (from inside a reel folder), output is `<reel-folder>/carousel/01.jpg ... 08.jpg`.

## Files

- `render.py` — renderer (Carousel class, CLI entry point)
- `slide-magazine.html` — single base template with 6 slot variants in CSS
- `tokens.json` — brand spec (obsidian/indigo, 1080x1350, arc definition)
- `examples/carousel-engine/carousel.json` — worked example, the "Two-Skill Engine"

## Related skills

- `lead-magnet` — the PDF that ManyChat DMs after a comment. Pairs with this skill but is independent.
- `v2-write` — drafts the reel package; same brain that should draft the carousel.json fields
- `daily-content` — daily reel caption + CTA
- `morning-post` — routes daily content; may trigger this skill when the day has a slideshow slot

## v2 backlog (do not build in v1)

- Full-bleed (noevarner-style) preset alongside Obsidian
- Compress 8 slides to 6 for system-less topics
- Auto-pull content from v2-signal Notion DB (Subsystem B)
- Auto-post via Graph API or agent-browser
- AI-generated illustrations / character art
