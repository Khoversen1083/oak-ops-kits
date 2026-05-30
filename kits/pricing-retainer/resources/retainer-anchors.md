# Retainer anchors

The four monthly retainer tiers inside the taught range. The decision
tree (`pricing-decision-tree.md`) tells you which tier to land in. This
file tells you exactly what each tier covers and what it does not.

The retainer is not passive income. It is the commitment that the
automation stays alive. Three things justify it: monitoring, fixes
when external changes break the automation, one adjustment per month
as the business evolves.

## $300/month, Starter floor

When to land here:
- One simple automation, single integration
- You are spending less than 2 hours per month on this client after
  build
- Infrastructure cost (Trigger.dev, OpenAI, email send) is under
  $30/month
- Client handles exception triage, you only get pinged on hard failures

What it covers:
- Monitoring the failure logs, you see breakage before the client does
- Fixes when an upstream API changes, when a vendor renames an
  endpoint, when a format shifts
- One small adjustment per month (a field rename, a new email template)

What it does not cover:
- A second automation
- Net-new logic or a workflow change
- Training new staff on the dashboard

Floor rule: do not go below $300/month. If the math points lower, the
deal is too small, walk or bundle.

## $400/month, Starter standard

When to land here:
- Default for a first-engagement pilot
- One automation with light parsing, 2-3 hours per month maintenance
- Infrastructure cost $30-50/month
- You handle some exception triage but most failures are silent

What it covers:
- Everything in $300 tier
- Up to 3 hours per month of operator attention from you
- One adjustment per month as the workflow shifts

What it does not cover:
- Onboarding new integrations
- Building a second automation

## $500/month, Standard tier

When to land here:
- Two or more automations live for this client, or one moderate-complex
  build
- You are spending 3-4 hours per month
- Infrastructure cost $50-80/month
- You own exception triage end to end

What it covers:
- Everything in $400 tier
- Two adjustments per month across the automations you manage
- Quarterly review call (30 min) on what to tune next

What it does not cover:
- A third automation
- Building a custom dashboard

## $600/month, Growth tier ceiling

When to land here:
- Multiple automations, active optimization, you are the operator
- Spending 4-6 hours per month on this client
- Infrastructure cost $80-150/month
- Client treats you as their automation owner, not a vendor
- Earned, not first-pitched

What it covers:
- Everything in $500 tier
- Active optimization, you are looking for the next thing to automate
- Monthly review call (30 min)

What it does not cover:
- A net-new automation build (scoped separately as a setup fee)

## Above $600

The taught range stops here. If you find yourself wanting to charge
more, the relationship has graduated to a custom engagement, take it
to Kevin live at `https://kevhov.ai/oak-ops`.
