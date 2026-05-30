# Score Before You Spend a Minute

## What you're building

An ICP scoring rubric that filters every prospect to a 0-10 score, so you only spend your best 20-minute emails on companies that were ever going to buy.

## Before you start

- Locked niche from the previous lesson
- The ICP Scoring Calculator downloaded from Resources
- A list of 25 candidate businesses (any source, raw)

## Steps

1. Open the ICP Scoring Calculator. Five weighted dimensions: owner-operated, revenue size, headcount, tech stack signal, pain signal. Each scored 0, 1, or 2. Max 10.
2. Pull signals from LinkedIn (owner tenure), the company About page (revenue + headcount), job postings (tech stack), and founder posts (pain).
3. Score each candidate. Sort descending.
4. Tier the list:
   - **A (8 to 10):** personalize hard, 20 minutes per email
   - **B (6 to 7):** hook variants with field swaps
   - **C (5):** light sequence, low effort
   - **Kill (under 5):** delete the row so it never tempts you again
5. Re-score weekly. Your filter sharpens as you see what types of businesses actually reply.

## Drop into Claude Code

```
Read icp-scoring-rubric.md and score this prospect list against my locked niche: [paste your 25 candidates]. Return the top 8 with one-line reasoning per row.
```

Skill: install `classify-leads` from Resources. Runs the rubric on a CSV.

## Scribe

`[Loom URL — recording queued]`

## Resources

- `icp-scoring-calculator.xlsx` — 5-dimension scoring sheet
- `icp-scoring-rubric.md` — the reference doc
- `classify-leads-skill.zip` — drop into `.claude/skills/`

## Work With Me 1:1

Want help getting your first client and building the system with me?

[Apply for 1:1 coaching](https://kevhov.ai/oak-ops)
