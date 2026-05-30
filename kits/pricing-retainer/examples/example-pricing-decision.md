# Example: pricing-decision-2026-05-30.md (worked example output)

Generated for the example intake (`example-intake-filled.md`). Fake
prospect: Desert Air Mechanical, Phoenix HVAC contractor, 14 trucks,
owner-operator Carl Mendez.

## Step 1, the build

One sentence: replace Desert Air's dispatcher morning route build plus
midday call chase to confirm tech ETAs with an automation that pulls
from their ServiceTitan CRM and routes the next job (with customer
history attached) to the assigned tech's phone.

## Step 2, setup fee decision

Inputs walked through the decision tree:

- Complexity: moderate. Two systems (ServiceTitan plus Twilio SMS),
  some logic (route assignment rules from existing dispatcher
  conventions). Not multi-API.
- Prospect size: 50-200 employees? No, 18 employees, but $3.5M
  revenue. Treat as 1-50 cell.
- Decision tree cell: Moderate, 1-50 employees, range $1,000-$1,500
  midpoint.
- Adjustments up: pain rated 4 of 5, prospect has tried hiring through
  the problem, dispatcher integration touches ServiceTitan which has
  rate limits to manage. Push to high end.
- Adjustments down: none. Not a first paid client of this offer (user
  has shipped 3 prior builds in this lane).

**Setup fee: $2,000.** Reasoning: the prospect's revenue and pain
rating earn a push above the moderate-cell midpoint, and the
ServiceTitan integration is non-trivial enough that the $1,500 anchor
would underprice the build risk. Per `setup-fee-anchors.md`, $2,000
covers multi-source ingestion with light transformation logic and two
to three integrations, which matches this scope exactly.

## Step 3, retainer decision

Ongoing-work inputs:

- Hours per month after go-live: 3-4 hours (some exception handling
  when ServiceTitan webhooks fail, monthly route-rule tweak)
- Infra cost: ~$45/month (Trigger.dev, Twilio, OpenAI for the
  description summarization)
- Exception triage: user handles end to end, dispatcher does not get
  pinged

Per `retainer-anchors.md`, this lands in the $400/month Starter
Standard tier. The $500 Standard tier would over-promise (only one
automation, not two or more). The $300 floor would under-cover the
exception triage time.

**Monthly retainer: $400.** Covers monitoring, fixes when ServiceTitan
or Twilio change endpoints, and one adjustment per month as the
dispatcher rules evolve. Does not cover net-new automations, dashboard
changes, or training new dispatchers.

## Ratio sanity check

- Setup-to-retainer ratio: $2,000 / $400 = 5x. Healthy.
- Annual recovered value estimate: dispatcher saves ~10 hours/week of
  call chasing, $35/hour loaded rate, 50 weeks = $17,500/year.
- ROI multiple: $17,500 / $4,800 annual retainer = 3.6x. Standard
  send.
- Wallet alignment: prospect benchmarks against $60K/year second
  dispatcher. Setup plus 6 months of retainer ($4,400) is 7 percent
  of one dispatcher year. Surface this line on the call.

## Skool submit block

```
Pricing Lock
Scoped automation: Desert Air dispatcher route plus ETA confirmation
Setup fee: $2,000, because pain is acute and ServiceTitan integration
  warrants the moderate-cell high end
Monthly retainer: $400
Setup-to-retainer ratio: 5x
ROI multiple: 3.6x
Top objection I expect: "Why not just hire another dispatcher"
```
