# Scaling Diagnostic

20 questions. Each maps to one of 8 strategic chapters. Score 1 (broken for me) to 5 (handled). Average per chapter. The 3 lowest chapters become the focus areas for Steps 2-7.

## Scoring rule

- 1 = I have no system, this is improvised every time
- 2 = I have a half-baked approach, it works sometimes
- 3 = I have a system, it works most of the time, not documented
- 4 = I have a documented system, I follow it consistently
- 5 = This is dialed in, I am not thinking about it day to day

If a chapter scores 4 or 5, the coach skims that step. If it scores 1, 2, or 3, the coach runs the step in full.

## The 20 questions

### Chapter 1, Niche validation (Q1-Q3)

1. If I had to describe my exact niche in one sentence (industry, size, role), I can do it without hedging.
2. I have closed 3+ clients in this exact niche, not "similar" ones.
3. New prospects in this niche book a call without me explaining what I do for half the call.

### Chapter 2, Retainer scaling (Q4-Q5)

4. Every current retainer is priced at 300 per month or higher and the scope is documented in writing.
5. I know which clients I would raise on next quarter and which I would drop.

### Chapter 3, First setter hire (Q6-Q7)

6. I have a clear comp model and recruiting plan for hiring a setter when I am ready.
7. I know the exact client count and cash threshold that triggers the setter hire.

### Chapter 4, Capacity planning (Q8-Q10)

8. I know how many hours per week each current client costs me on average.
9. I have enough weekly hours headroom to add 2 more clients without dropping quality.
10. If I had to fire my worst client tomorrow, I could name them and the reason in one sentence.

### Chapter 5, Cash flow (Q11-Q13)

11. I know my monthly fixed cost burn to the dollar.
12. I have at least 3 months of fixed costs in operating cash on hand.
13. I have a 12-week cash forecast I have updated in the last 30 days.

### Chapter 6, Repeatable delivery (Q14-Q16)

14. I have a documented kickoff, build, and handoff process I follow on every project.
15. My last 3 builds reused 80 percent of the same template, only 20 percent was custom.
16. A new client can be onboarded in under 5 hours of my time, not 15.

### Chapter 7, Pricing power (Q17-Q18)

17. I have raised my setup fee or retainer in the last 6 months, by at least 30 percent.
18. I have killed at least one low-margin client in the last year without losing sleep.

### Chapter 8, Productize or custom (Q19-Q20)

19. I know whether my current niche should go custom-per-client or get productized, and why.
20. If I went productized today, I have the 3+ sold builds to base the product on.

## Output

The coach writes results to `outputs/diagnostic-<date>.md` like this:

```
Chapter                    | Avg score | Focus?
1. Niche validation        | 2.3       | YES
2. Retainer scaling        | 3.5       | no
3. First setter hire       | 1.0       | YES
4. Capacity planning       | 4.0       | no
5. Cash flow               | 2.7       | YES
6. Repeatable delivery     | 3.2       | no
7. Pricing power           | 3.5       | no
8. Productize or custom    | 3.0       | no
```

Focus = the 3 lowest-scoring chapters. The coach runs Steps 2-7 in full for those, skims for the rest.
