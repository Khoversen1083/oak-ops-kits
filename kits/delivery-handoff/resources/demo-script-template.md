# Demo script template

The 15-minute walkthrough call. The point is not to impress the
client, it is to make them comfortable. They should see the input,
the trigger, the output, the failure path. They should leave the call
trusting that you will catch failures before they do.

## Rules

- 15 minutes total. If it runs long, you are over-explaining.
- Screen-share the whole time. No slides.
- Run it live on their real data, not a demo dataset.
- Trigger one real error so they see the alert flow work.
- Close with the scope check, not "any other questions".

## Template

```
DEMO SCRIPT, [Client placeholder] / [Automation name]
Call length: 15 minutes
Attendees: you, [client contact, role]
Format: screen-share, live build, no slides

OPEN (1 min)
"Quick walkthrough so you know what this looks like before it goes
live Monday. I'll show you four things: where it reads from, what it
does, what you'll see, and what happens if it breaks. About 15
minutes."

1. THE INPUT (2 min)
[Share screen, open the input source]
"This is where the automation reads from. Every morning at [time],
it pulls [what] from here. Nothing changes on your end, this is the
same [sheet / inbox / system] your team already uses."

Confirm:
[ ] They recognize the input source
[ ] They are okay with the read-access scope

2. LIVE TRIGGER (3 min)
[Trigger the automation manually, narrate as it runs]
"Watch, I am running it now. It pulls the data, processes it, drops
the output here. Takes about [X seconds]."

Stay quiet while it runs. Let them watch.

Confirm:
[ ] They see the run complete
[ ] They see the output land where it lands

3. THE OUTPUT (3 min)
[Show the output, walk every section]
"This is what you'll see [day, time], in your [inbox / dashboard].
Three sections: [section 1], [section 2], [section 3]. Numbers are
current as of [freshness window]."

Pause and ask:
"Does the format work? Anything you want renamed or reordered?"
If "looks great," continue.
If "can we change X," note it, decide on the call if it is a
10-minute tweak or a separate scope.

4. THE FAILURE PATH (3 min)
[Trigger a real error, show the alert email landing in YOUR inbox]
"If it breaks, this is what happens. This email goes to me, not
you. I get the alert, fix it, email you when it's sorted. You do
not get woken up at 2am, you do not have to chase me, you find out
when it's already fixed."

Confirm:
[ ] They saw the alert email arrive in YOUR inbox, not theirs
[ ] They are clear they are never on the alert list

5. SCOPE CHECK AND CLOSE (3 min)
"Two things to lock in before we go live:

First, the schedule. Going live Monday [date] at [time], first real
run lands by [time + buffer]. Sound right?

Second, the handoff doc. I'm sending a one-pager today, save it
somewhere you can find it. Explains how to use this, what to do if
something looks wrong, what's covered in the monthly. Read it once,
then forget about it."

Then the scope close:
"If something comes up later, 'can it also do X', email me and I'll
tell you up front whether it's a 10-minute add or a separate scope.
No surprises."

[ ] Go-live date confirmed
[ ] Handoff doc send scheduled
[ ] Scope check stated out loud

WRAP
"That's it. First run lands [day, time]. I'll be watching it. Talk
[next contact day]."
```

## What to do mid-call

If they ask a tool question ("what is this built on?"): answer in
one sentence, do not deep-dive. They asked because they were curious,
not because they want training.

If they push on adding something: "Good question, let me think about
whether that is a tweak or a separate scope, I'll write back by [time
today]." Never agree on the call, never refuse on the call.

If something breaks during the demo: "Good, this is actually the
failure path, watch what happens." Most demos do not get the
failure-path demo for free, take the gift.

## After the call

- Send the handoff doc email same day, from the template
- Log the demo in the build README (date, attendees, anything raised)
- Block the launch-day calendar to watch the first run
