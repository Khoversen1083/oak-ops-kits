# Pricing Decision Tree (read-only source)

The 5-minute path to two numbers after discovery: a setup fee, a monthly retainer, and an ROI sanity check. Pick the cell, take the midpoint, check the math, send the proposal. Every number stays inside the taught range: setup 1,000 to 2,500, retainer 300 to 600 per month.

## The core rule

Price against their savings, never your time. The setup fee is what gets the automation live. The retainer is what keeps it live. You name both numbers in one breath.

## Step 1: Setup fee

Pick the cell from complexity and prospect size. Take the midpoint of the range.

```
Complexity                                      | 1-50 emp      | 50-200 emp
Simple (1 system, 1 trigger, 1 output)          | 1,000         | 1,000-1,500
Moderate (2-3 systems, some logic)              | 1,000-1,500   | 1,500-2,000
Complex (cross-dept, multi-API, custom logic)   | 1,500-2,500   | 2,000-2,500
```

Pick the high end if:
- Multiple stakeholders need to align, which slows you down.
- They want it live in under 2 weeks, which means rushed.
- The API setup is messy: legacy systems, custom auth.

Pick the low end if:
- They are your first paid client and you need the case study.
- The data is already in a clean spreadsheet.
- They are a referral and the relationship matters more than the margin.

Hard cap: the setup fee never goes above 2,500 for a pilot. If complexity seems to call for more, that is a sign there are two builds hiding in one. Scope the second one as a separate engagement later. Never quote a setup above 2,500.

### Setup-fee tiers (reference)

```
1,000  : 1 input to 1 output, fully structured, 1 integration
1,500  : 1-2 inputs, light unstructured (email parsing OK), 2 integrations
2,000  : 2+ inputs, unstructured (calls, photos, transcripts), 2-3 integrations
2,500  : multi-source, full unstructured pipeline, 3+ integrations, custom UI
```

## Step 2: Monthly retainer

The retainer is not passive income. It is the commitment to own the ongoing reliability of what you built. Three things justify it:
1. Monitoring. You watch the failure logs, the client does not.
2. Fixes when external changes break the automation: an API change, a vendor rename, a format shift.
3. One adjustment per month as the business evolves.

Run the math:

```
Hours saved per week x 4.3 weeks x 0.80 (conservative) = monthly hours saved
Monthly hours saved x hourly rate = monthly labor value
Monthly labor value x 0.12 = recommended retainer
```

Then floor and cap inside the taught range:

```
Tier     | Range       | When to use
Starter  | 300-400/mo  | One automation, basic monitoring. Default for first engagements.
Standard | 400-500/mo  | 2-3 automations, regular updates. Use after the second build.
Growth   | 500-600/mo  | Multiple automations, active optimization. Earned, not first-pitched.
```

For a first pilot, land in Starter. 400 per month is a common starter anchor for a simple workflow. Never floor below 300. Never go above 600.

## Step 3: ROI ratio sanity check

```
Annual recovered value / Annual retainer = Multiple
```

```
Multiple | What to do
5x+      | Send proposal. Easy yes.
3-5x     | Send proposal. Standard pitch.
2-3x     | Send proposal, but lean on opportunity cost in the narrative, not just labor savings.
under 2x | Do not send. Find a bigger pain in the business or walk.
```

## Step 4: Tier match

Sanity check the number against what the buyer signaled in discovery.

```
Discovery signal                            | Their pricing expectation
"We pay 50/mo for accounting software"      | 300-400/mo retainer max. Do not over-pitch.
"We spent a lot on software customization"  | 400-600/mo retainer is in their range.
"We have never paid for anything like this" | Lead with the lowest tier. Build trust before upselling.
"We pay an internal IT person"              | They benchmark against employee cost. Setup at 2,500 plus 400/mo is cheaper than one month of an employee. Say that out loud.
```

## Step 5: Do not negotiate against yourself

If they push back, trade scope for price. Never just lower the number.

- "Can you do it for less?" becomes "I can scope a smaller version. What outcome are you most willing to drop?"
- "Why is the retainer so high?" becomes "It covers everything: monitoring, fixes, adjustments. If something breaks, no surprise invoice. This is what it costs to never deal with this again."
- "Can we skip the retainer and just pay setup?" becomes "I do not do that. The automation needs a person watching it. Without the retainer, the first time something breaks neither of us has a clean answer for who fixes it."

## When the deal is too small

If the math lands the retainer below the range entirely, the engagement is not worth it. Pick one:
- Walk politely.
- Look for a second process in the same business and scope both as one engagement.
- Refer them to a templated tool instead of a custom build.

You are not in business to lose money on a small client.

## Installment option

If the buyer flinches at the full setup upfront, offer it as three equal monthly installments. The setup fee does not change, only the payment shape. Do not improvise the math.

## Worked math (generic example)

Discovery surfaced 6 hours per week of manual scheduling at a 25 per hour loaded rate, at a small local-services business.
- Annual savings: 6 x 25 x 52 = 7,800
- Setup at 25 percent: 1,950, round to 2,000, inside the range
- Retainer at 12 percent of setup: 240, floored to 300
- The wallet question: "Setup is 2,000. Monthly is 300."
- ROI ratio: 7,800 / 3,600 = 2.2x. In range. Send the proposal, lean on opportunity cost.
