# How to Publish This Repo

The skeleton is staged at `~/Coding/oak-ops-kits/`. It is NOT a git repo yet
and is NOT pushed anywhere. Kevin reviews first, publishes manually.

## Pre-publish checklist

- [ ] Read `README.md` end-to-end. Does it represent you?
- [ ] Read `CLAUDE.md` at root. Does the orientation match how you want
      newcomers to land?
- [ ] Read `lead-acquisition/README.md` + spot-check 2-3 of the 9 lesson
      bodies.
- [ ] Spot-check 2-3 kits in `kits/`. Make sure the Setup Interview (Step 0)
      reads right and the kit-specific steps are clean.
- [ ] Confirm no private paths, no client names, no Skool URLs to private
      lessons, no Calendly direct booking (only kevhov.ai/oak-ops).
- [ ] Decide: is it `oak-ops-kits` or do you want a different name?

## Publish

Once the checklist is clean:

```bash
cd ~/Coding/oak-ops-kits
git init
git add -A
git commit -m "Initial public release of Oak Ops Kits"
gh repo create oak-ops-kits --public --source=. --push --description "Open-source Claude Code kits for lead acquisition, discovery, pricing, delivery, and pipeline"
```

The `gh repo create` flow creates the GitHub repo, sets it public, sets
origin, and pushes main in one step.

## Post-publish

- Add the repo URL to the kevhov.ai funnel
- Add the repo URL to the Skool community Free Training course (top of
  lesson 1)
- Add the repo URL to the Instagram bio link
- Cold email CTA changes from "book a call" to "look at the kits" once a
  prospect is mid-funnel
