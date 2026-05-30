# Reply Handler Kit

Paste any cold-email reply, get the right response back in your voice,
in seconds. Operationalizes lesson 8 of the Lead Acquisition Playbook.

## What this kit does

You open it in Claude Code, answer 10 intake questions once, and from
then on you paste any reply that lands in your inbox and the coach
classifies it (interested, not now, send info, remove me, hostile, or
one of 12 named objections) and drafts the response in your voice with
your calendar link, your niche, your pain hypothesis already wired in.

## Before / After

| Without kit | With kit |
|---|---|
| Freeze on a "what does it cost" reply for 20 minutes | Drafted response in 30 seconds |
| Pitch in the reply, lose the call | Get the call first, every time |
| Respond fast and badly, or 3 days late | 4-hour business-hour rule, drafted right |
| Forget to log the status, lose the thread | Coach writes the pipeline status update with every reply |

## Install in 3 steps

```bash
git clone https://github.com/Khoversen1083/oak-ops-kits.git
cd oak-ops-kits/kits/reply-handler
claude
```

Then type: `run the kit` and paste the reply you got.

## What you'll have when you're done

- A reply triage card (5 reply types plus 12 objections) pre-loaded
  with your niche, pain hypothesis, calendar link, and signature, in
  `outputs/reply-triage-card-<date>.md`
- A drafted response for the specific reply you pasted, in
  `outputs/reply-draft-<date>.md`
- The pipeline status to log (Booked, Engaged, Pricing shared, Soft
  no, Hard no, Routed) so the tracker stays clean
- A re-engage queue for every soft no, dated 90 days out

## What you need

- [Claude Code](https://claude.com/claude-code) installed
- The Cold Email kit already run, so you have a niche and an offer
  locked
- A calendar link, a business email, and 15 minutes for the first run

## How long does it take

- First run, full triage card built: 15 minutes
- Every reply after that: 30 seconds to paste, 30 seconds to send
- Re-run for a new niche later: 5 minutes, intake is already filled

## Want me to run this with you

If you want me live with you, watching the reply land in real time,
calibrating the response to your voice, talking through the borderline
ones, that's the paid layer.

[Apply at https://kevhov.ai/oak-ops](https://kevhov.ai/oak-ops)
