# Capacity Planning Worksheet

Real hours-per-client estimates, the math for current vs projected load, and the hire-or-fire decision rule. Reference for Step 5.

## Hours-per-client baseline (use these, not your guess)

Operators consistently underestimate the hours each client costs them. These are the calibrated numbers based on watching this pattern across paid students.

| Client phase | Hours per week (active) | Hours per month (build delta) |
|---|---|---|
| Onboarding (months 1-2) | 4 | 6 |
| Active build (months 1-3, beyond onboarding) | 2 | 4 |
| Steady-state retainer (months 4+) | 1 | 2 |
| Painful client (any phase, +50 percent) | +50 percent on the above | +50 percent on the above |

## Total weekly load formula

For each current client:

```
weekly_hours = active_phase_hours + (build_delta_hours / 4.3)
```

Then sum across all clients. Add 5 hours per week for sales (cold outreach + discovery calls + proposals) and 3 hours per week for admin (invoicing, follow-ups, ops).

```
total_weekly_hours = sum(per_client_weekly_hours) + 5 + 3
```

## Worked example

Operator has 3 clients:
- Client A, month 5 (steady): 1 + (2/4.3) = 1.5 hours/week
- Client B, month 2 (active build): 2 + (4/4.3) = 2.9 hours/week
- Client C, month 1 (onboarding, painful): (4 + (6/4.3)) * 1.5 = 8.1 hours/week

Total per-client: 12.5 hours/week
Sales overhead: 5 hours/week
Admin overhead: 3 hours/week
**Total weekly load: 20.5 hours/week**

## Projected load at target

Repeat the formula for the target client count. Assume new clients land in onboarding for 2 months, then drop to active for 3 months, then to steady.

```
projected_weekly_hours = (target_steady_clients * 1.5)
                      + (target_active_clients * 2.9)
                      + (target_onboarding_clients * 5.4)
                      + 5 + 3
```

If projected > weekly hours available (from intake Q7), you have a capacity problem. Pick one of the 4 decisions below.

## The 4 decisions

### Decision A, Fire 1-2 low-margin clients first

Trigger: you have at least one client where (retainer / weekly hours) is below 100 per hour, OR is in the "painful" column. Drop them this quarter. Capacity created by firing is free (no hire cost).

Always run this BEFORE considering a hire. The kit refuses to authorize a hire if you have firing-candidates still on the books.

### Decision B, Hire a setter

Trigger: you have 5+ paying clients, 3+ months cash, and sales overhead is eating 10+ hours per week of your time. See `first-setter-hire-guide.md` for the spec.

### Decision C, Hire ops (VA or contractor)

Trigger: admin overhead is over 8 hours per week, AND you have 7+ clients. Ops hire offloads invoicing, scheduling, client communications, monitoring triage. Cheap (15-25 per hour part-time contractor) and frees you to do delivery and sales.

Run this BEFORE a second technical hire. Ops scales further than a junior dev.

### Decision D, Neither, you have headroom

Trigger: projected weekly hours at target is still under your cap (intake Q7). You do not have a capacity problem yet, you have a pipeline problem. Run the cold-email kit (`../cold-email/`), not the hiring conversation.

## Hours-per-client gotchas

- The "active" phase is shorter than operators think (about 3 months, not 6)
- The "steady-state" phase requires that you have actually built a monitoring layer. If you are eyeballing dashboards manually, steady-state is 3-4 hours per month, not 2.
- "Painful" is not a feeling, it is a measurement. If the client cost you more than 50 percent above baseline this month, they are painful, mark them.
- Onboarding hours include all the kickoff calls, integration tickets, and "wait did we hook up Slack?" friction. Real number is closer to 4 per week for 2 months, then it drops.

## Cap rule (the math behind "do not hire before 5 clients")

A part-time setter costs about 600-1000 per month (5-7 booked qualified calls per month at the per-call rate, plus the time you spend managing them). To cover that cost from new clients, you need 1.5-2 new closed clients within the first 90 days. To close 1.5-2 new clients in 90 days, your existing base needs to be both: showing pull (referrals coming in) and producing enough revenue that you can ride out a 60-day setter ramp.

Both of those happen reliably at 5+ clients, not before. Do not override this rule, you will run out of cash before the setter pays for themselves.
