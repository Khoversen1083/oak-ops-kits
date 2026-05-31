# Repeatable Delivery Blueprint

The 80 percent reusable delivery template. Build it once for your niche, customize 20 percent per client. Reference for Step 4.

The goal is your 5th build takes 30 percent of the time your 1st build took. Not because you got faster as a developer, because you stopped solving the same problem from scratch.

For the tactical handoff and maintenance specifics, see `../delivery-handoff/CLAUDE.md` and `../monthly-maintenance/CLAUDE.md`. This file is the structure that wraps them.

## The 4 sections of the template

Every reusable delivery template has these 4 sections. Build each section once for your niche, reuse on every new client.

### Section 1, Kickoff (the first 7 days)

What lives here, once-per-niche:
- A kickoff email template that sets the 7-day plan
- A discovery-recap document template (filled from `../discovery-call/` outputs)
- A scope-of-work template specific to your niche (the 1-2 automations that recur)
- A tech-stack onboarding checklist (which integrations, which credentials, who owns what)
- A 60-minute kickoff call agenda

What gets customized per client (the 20 percent):
- Client name, contact info, specific people in the room
- The custom rules or data quirks that make their version slightly different
- The custom integrations not in your standard stack

### Section 2, Build (days 8 to 21, or until live)

What lives here, once-per-niche:
- The skeleton code repository (forked from a template repo, not from scratch)
- The standard schema (input fields, output fields, error handling)
- The standard monitoring layer (Trigger.dev jobs or equivalent, alerting wired)
- The standard test data set (sample inputs that exercise the happy path and 3 edge cases)
- The standard "stuck" escalation pattern (when to ping the client vs solve it yourself)

What gets customized per client:
- The client-specific business rules (their pricing tiers, their vendor list, their workflow quirks)
- The visual or report formatting per client's stakeholders
- Any custom integrations beyond your stack

### Section 3, Handoff (last 3 days before go-live)

What lives here, once-per-niche:
- A handoff document template (what they own, what you own, the SLA)
- A go-live checklist (who is on the call, what gets tested live, rollback plan)
- A training video template structure (10 minutes max, screen-recorded, sent in writing)
- The first-30-days check-in cadence (3 touch points, scheduled at kickoff)

What gets customized per client:
- The training video itself (recorded fresh per client, the structure is the template)
- Their specific stakeholder list for the handoff call
- Their internal docs and naming conventions in the handoff document

### Section 4, Maintenance (month 2+)

What lives here, once-per-niche:
- The monthly maintenance checklist (see `../monthly-maintenance/`)
- The standard monthly report template
- The escalation pattern for things that break (your 4-hour response SLA, what counts as urgent)
- The standard "small adjustment vs new scope" decision rule

What gets customized per client:
- Their specific monitoring thresholds
- Their preferred reporting cadence (monthly is default, some want weekly)
- Their specific Slack channel or email loop for alerts

## How to build the template the first time

1. Pick your most recent build in the niche, the one that worked
2. Document everything you did, in the 4 sections above
3. Strip out the client-specific names, data, and quirks (leave placeholders)
4. Test by walking the template against the OTHER 2 builds in your niche, does 80 percent of it apply? If yes, ship as v1. If no, the niche is wider than you think, narrow it (see `niche-validation-5-tests.md`)
5. Use v1 on the next sale. Note where you had to deviate, fold those back into v2 at the end of that build
6. By v3 the template is stable, by v5 it is your moat

## What the template is NOT

- It is not a SaaS product. You are still selling custom delivery, with a high-reuse template. See `productize-decision-tree.md` for when to consider productizing.
- It is not generic ("a workflow template for any business"). It is specific to your one niche.
- It is not a sales asset. Do not show clients the template. They are paying for the build, not the structure behind it.
- It is not static. Every 3rd build, you reread and update the template.

## When to stop adding to the template

If the template starts having more "if client A, do X, if client B, do Y" branches than core flow, the template has fragmented. Either narrow the niche, or split into 2 templates for 2 sub-niches. Do not let a single template carry 4 branching paths, it stops being a template.

## Template debt

Like code debt. If you do 3 builds in a row without updating the template after each, the template drifts from reality. Set a rule: every 3rd build ends with a 60-minute template review and update.
