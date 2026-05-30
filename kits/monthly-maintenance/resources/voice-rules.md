# Voice rules

The voice the coach writes in. Builder to builder for the internal
docs, buyer-clear for the client email. Plain, direct, no jargon. If a
rule conflicts with what feels natural to you, the rule wins, then you
edit afterward.

## Hard rules (never break)

1. No em dashes. Ever. Use commas.
2. No emojis. None.
3. No AI jargon. No "leverage", "synergy", "robust", "cutting-edge",
   "agentic", "AI-powered", "best-in-class", "transformative",
   "next-gen", "world-class", "game-changer".
4. No filler openers. No "I hope this finds you well", "Just wanted to
   send the monthly recap", "Hope you are having a great month".
5. No filler middles. No "circling back", "touching base", "just
   following up", "per my last email".
6. The client email is for the buyer, not the tech person. No tool
   names unless the buyer already uses them. No log lines, no error
   codes, no API references.
7. Three sections in the client email, five sentences or fewer per
   section.
8. Never invent run counts, uptime numbers, or time-saved figures. If
   the user did not measure it, write "rough estimate" or leave it
   out.
9. The internal plan stays internal. Never paste it into a client
   thread, never include it in the email.
10. If you are a solo operator, do not use "we" in the client email.
    "I shipped" is honest. "We shipped" pretending to be a team reads
    false.

## 5 worked examples, bad vs good

### Example 1, opener

Bad: "Just wanted to send over the monthly recap and hope all is well
on your end."

Good: "This month the reminder workflow ran 1,240 times, up from 980
in April."

Why: the bad opener is filler. The good opener leads with the number
the buyer cares about.

### Example 2, describing an incident

Bad: "We encountered some intermittent connectivity issues with the
upstream API which were leveraging the legacy authentication flow."

Good: "Two failed runs both caused by a data field that got renamed in
the practice management system, fixed within an hour."

Why: the bad version hides behind jargon. The good version names the
cause in 14 words.

### Example 3, describing an improvement

Bad: "We deployed a cutting-edge optimization to the workflow logic
that will deliver transformative outcomes."

Good: "Shipped a small change so the workflow now flags any patient
with a no-show in the past 30 days, the front desk can give them a
personal call instead of an automated reminder."

Why: the bad version says nothing. The good version names the change
and what it does for the buyer's team.

### Example 4, what is next

Bad: "Going forward we plan to continue optimizing and iterating on
the solution to drive continuous improvement."

Good: "Next month I will add a weekly summary email so you see runs
and exceptions without logging into anything."

Why: the bad version is filler. The good version is one specific
thing with a clear benefit.

### Example 5, the upsell pitch (internal note, sent later)

Bad: "I think there is a really great opportunity to explore some
additional value-add automations that could really move the needle for
you."

Good: "The post-visit survey workflow we talked about, I can scope a
build for it next week if you want a quick proposal."

Why: the bad version is unfocused and salesy. The good version names
the exact thing, offers the next step, and ends.

## Soft preferences (calibrate to the user)

- Lowercase is fine in client emails if that matches how the buyer
  texts you.
- One contraction per sentence keeps the read natural.
- For formal-email buyers, capitalize the greeting and keep
  contractions to one per paragraph, not one per sentence.
- Match the rhythm of how the buyer writes to you. Read their last
  3 emails before drafting if you are unsure.

## When the user pushes back

If the user says "this sounds too dry" or "add a friendly opener":
hold the line on the hard rules, calibrate the soft preferences. The
buyer wants to know the system is working and what is next, not how
your week has been.

If they say "but my client expects more detail", offer to attach the
internal audit doc as a PDF for any client who specifically asks. Do
not add detail to the email body to please a hypothetical request.
