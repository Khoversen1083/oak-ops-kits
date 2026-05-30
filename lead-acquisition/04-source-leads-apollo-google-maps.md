# Scrape and Enrich

## What you're building

A repeatable sourcing flow that pulls 100+ owner-operated businesses from Google Maps and enriches them with verified owner contacts from Apollo, in 90 minutes.

## Before you start

- Locked niche and geography (start tight: one metro, one vertical)
- Apollo account (free tier to start, $99/mo paid once volume justifies)
- The `gmaps-leads` and `scrape-leads` skills installed in your Claude Code project
- An empty 25-Target List spreadsheet open

## Steps

1. **Maps first, for the company pull.** Run `gmaps-leads` with your niche keyword + city. Returns 200 to 1,000 businesses with website, phone, address. Export CSV.
2. **Filter.** Kill anything that's a chain, a franchise location, or has no website. Owner-operated only.
3. **Apollo for owner contacts.** Upload the Maps CSV via Companies → Import. Apollo enriches with employee count, revenue estimate, owner name.
4. **Filter by title** in Apollo: Owner, Founder, President, CEO, Managing Director. Add headcount 50-500 and revenue $20M-$200M.
5. **Reveal in batches.** Only reveal the top 25 to 50 rows first. Apollo credits are not free. Spend on A-tier rows.
6. **Append to pipeline.** Export Apollo CSV, sort by ICP score, drop into your 25-Target List.

## Drop into Claude Code

```
Use the gmaps-leads skill to pull all [niche] in [city]. Filter to owner-operated. Then use scrape-leads to enrich each one with the owner's name and LinkedIn. Save as CSV. Then use classify-leads to score against the ICP rubric.
```

## Scribe

`[Loom URL — recording queued]`

## Resources

- `gmaps-leads-skill.zip` — Google Maps scraper
- `scrape-leads-skill.zip` — website + LinkedIn enricher
- `apollo-search-recipe.md` — saved searches and filters
- `google-maps-scraper-recipe.md` — full command walkthrough

## Work With Me 1:1

Burning Apollo credits with no replies? The hook is the problem, not the volume.

[Apply for 1:1 coaching](https://kevhov.ai/oak-ops)
