# Cash Flow Model

Real formulas for runway, MRR target, hire affordability, and the 12-week forecast. Reference for Step 7. No placeholders, every formula resolves to a number you can run.

## The core rule

Keep 3 months of fixed costs in operating cash before any hire. If you are below that, hires are on hold until the cash builds. This rule is non-negotiable, the kit enforces it.

## The 5 core formulas

### Formula 1, Current runway in months

```
runway_months = operating_cash / monthly_fixed_costs
```

Example: 9,000 cash / 3,000 fixed = 3.0 months runway. You are at the floor.

### Formula 2, MRR target (the headline number)

```
MRR_target = (monthly_cash_burn / desired_runway_months) * buffer
```

Where:
- `monthly_cash_burn` = monthly fixed costs + intended owner draw
- `desired_runway_months` = 3 (the floor) or 6 (the safety target)
- `buffer` = 1.5 (covers churn, late payments, seasonal dips)

Example: burn 5,000 (3K fixed + 2K owner draw) / 3 months * 1.5 buffer = MRR target 2,500. But the buffer flips at this scale, you want MRR to cover burn entirely, so the real target is:

```
MRR_target_realistic = monthly_cash_burn * 1.5
```

Example: 5,000 burn * 1.5 = 7,500 MRR target. At 500/month average retainer, that is 15 clients on retainer. At 400/month average, 19 clients.

### Formula 3, Hire affordability

Before you authorize any hire (setter, ops, contractor), the math must hold:

```
post_hire_runway = (operating_cash - hire_3_month_cost) / (monthly_fixed_costs + monthly_hire_cost)
```

If `post_hire_runway < 3`, do not hire. Wait for cash to build or fire a low-margin client first.

Example: 9,000 cash, 3,000 fixed, setter costs 800/month. Hire 3-month cost = 2,400.
```
post_hire_runway = (9,000 - 2,400) / (3,000 + 800) = 6,600 / 3,800 = 1.7 months
```
1.7 < 3. Do not hire. Build cash to at least 13,500 first, then re-check.

### Formula 4, Break-even client count

```
breakeven_clients = monthly_cash_burn / average_retainer
```

Example: 5,000 burn / 450 average retainer = 11.1, round up to 12 clients to break even on retainers alone (setup fees are bonus, not budget).

### Formula 5, 12-week MRR trajectory

For each week of the 12-week plan, the model forecasts MRR like this:

```
week_n_MRR = current_MRR + (new_clients_per_week * avg_retainer * weeks_elapsed) - (churn_rate * current_MRR * weeks_elapsed / 4.3)
```

Where:
- `new_clients_per_week` = realistic new sales pace (target 0.5 to 1 per week for a solo operator at this stage)
- `churn_rate` = monthly retainer churn (use 5 percent if you have no data, your real number after 6 months)

## Worked 12-week forecast (using the example operator)

Current: 3 clients, 1,800 MRR, 3,000 fixed costs, 9,000 cash, 5 percent churn.
Target: 8 clients, 4,000 MRR.
Sales pace: 0.5 new clients per week (2 per month).
Average retainer: 500.

| Week | New | MRR | Cash (assuming MRR collected, fixed paid) | Notes |
|---|---|---|---|---|
| 0 | 0 | 1,800 | 9,000 | Start, 3.0 mo runway |
| 4 | 2 | 2,732 | 8,656 | Cash dips, then recovers |
| 8 | 4 | 3,612 | 9,236 | At target client count by week 10 |
| 12 | 6 | 4,440 | 10,640 | Target hit, runway 3.5 mo |

The model writes the full 12-week table to `outputs/cash-forecast-<date>.md`.

## The "do not hire" red flag

The kit flags any week in the forecast where:
- `runway_months < 3` at any point in the 12 weeks
- `cash` ever drops below 1 month of fixed costs

If either fires, the kit forces a "fire 1 low-margin client first" recommendation before any hire is authorized in Step 6.

## How to use this in real time

You do not need to compute this by hand. The coach runs the formulas during Step 7 using your intake numbers. The output is a table, a runway number, and a hire-or-hold decision. Then you check it monthly against actual cash on hand.

If actuals drift more than 15 percent from forecast in any week, re-run Step 7 with updated numbers, do not just push through. Cash is the only metric where the math is the truth and the gut is wrong.
