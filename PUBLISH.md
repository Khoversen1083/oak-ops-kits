# How to Publish This Repo

The library is staged at `~/Coding/oak-ops-kits/`. Git is initialized locally.
NOT yet pushed to GitHub. Kevin reviews first, publishes manually.

Library status as of 2026-05-30: 11 kits live (10 tactical + 1 macro), root
README + CLAUDE.md updated, ~180 files total, zero em-dashes across all kits,
zero $3K leaks, bash 3.2 compatible bootstraps.

## Pre-publish checklist

- [ ] Read `README.md` end-to-end. Does it represent you?
- [ ] Read `CLAUDE.md` at root. Does the orientation match how you want
      newcomers to land?
- [ ] Read `lead-acquisition/README.md` + spot-check 2-3 of the 9 lesson
      bodies.
- [ ] Spot-check `kits/cold-email/` end-to-end (the gold standard the other
      kits cloned). Run it with `cd kits/cold-email && claude` then
      `run the kit`. This is the audit.
- [ ] Spot-check `kits/sales-os/` (the macro-kit). Confirm the scaling
      diagnostic + 12-week plan output land correctly.
- [ ] Spot-check 2-3 more kits at random.
- [ ] Confirm no private paths, no client names, no Skool URLs to private
      lessons, no Calendly direct booking (only kevhov.ai/oak-ops).
- [ ] Confirm no `intake-filled.md` files exist in any kit (those are user
      data, ignored by `.gitignore` but worth confirming).
- [ ] Decide: is it `oak-ops-kits` or do you want a different name?

## Publish

Once the checklist is clean (git is already initialized):

```bash
cd ~/Coding/oak-ops-kits
git status
git add -A
git commit -m "Initial public release of Oak Ops Kits, 11 kits"
gh repo create oak-ops-kits --public --source=. --push --description "11 open-source Claude Code kits for lead acquisition, discovery, pricing, delivery, pipeline, and scaling. By Kevin Hoversen."
```

The `gh repo create` flow creates the GitHub repo, sets it public, sets
origin, and pushes main in one step.

## Post-publish

- Add the repo URL to the kevhov.ai funnel (the `/oak-ops` page should
  reference the public repo for "see what you're getting before booking")
- Add the repo URL to the Skool community Free Training course (top of
  lesson 1)
- Add the repo URL to every Skool lesson that has a paired kit (40+ lessons,
  see Workstream H in SESSIONS.md)
- Add the repo URL to the Instagram bio link
- Cold email CTA changes from "book a call" to "look at the kits" once a
  prospect is mid-funnel
- Update the cold-email kit's `resources/3-sentence-email-template.md` to
  use the new repo URL in the proof sentence
