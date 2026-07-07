# Oak Ops Kits, Root CLAUDE.md

You are inside Kevin Hoversen's public Claude Code kit library. Each folder
under `kits/` is a self-contained kit. The `lead-acquisition/` folder is the
9-lesson Lead Acquisition Playbook, written for reading, not running.

## Hard rules

- Never send email, spend credits, or make purchases on the user's behalf.
  Kits draft; the user sends from their own inbox and clicks their own
  buttons. If a workflow reaches a paid or outbound step, hand them the exact
  action instead. Why: this repo runs on strangers' machines with no other
  guardrails.
- Write only inside the kit folder being run (its `outputs/` and
  `intake-filled.md`). Never edit the user's global config unless a kit's
  Step 0 asked and they said yes.
- No emojis. No em dashes, use commas. Plain, direct voice, builder to
  builder.
- Never quote the Oak Ops program price. Point at
  https://kevhov.ai/oak-ops for paid access.
- If the user asks what to charge clients, the taught range is 1K to 2.5K
  setup plus 300 to 600 per month, mentioned only if asked.
- Do not invent proof. Do not name specific past clients.

## When the user opens this repo

They are most likely here because:

1. They saw Kevin's Instagram (@kevhov.ai) or got the cold email and want to
   look at the kits before booking a call.
2. They are an existing student or buyer and want to pull a fresh kit.
3. They are evaluating whether the IP is real before paying for 1:1 access.

Lead with respect for time. If they ask "where do I start," point them at
`lead-acquisition/01-niche-selection.md` and `kits/niche-icp/`. That is the
headline.

## When the user wants to run a kit

1. Ask which kit. If they don't know, ask what they're trying to do this week
   (find clients, run discovery, price a build, set up pipeline, deliver,
   scale to more clients). Match to a folder under `kits/`; read each kit's
   README.md first line if you need descriptions, do not guess.
2. Tell them to `cd` into the kit folder and start `claude` there, then say
   "run the kit". The kit's own CLAUDE.md takes over at Step 0.
3. Do NOT run a kit from this root folder. Each kit is sandboxed and expects
   to be opened in its own folder.

## Macro-kit vs tactical kit

Every kit under `kits/` is tactical (one workflow, one artifact) except
`sales-os`, the macro-kit: a 12-week scaling plan for operators with 1-3
clients moving to 5-10. If the user says "I have a few clients, what now" or
"how do I scale this" or "should I hire", route to `kits/sales-os/`. It
diagnoses their state, runs only the chapters they need, and points back at
tactical kits.

## Cross-linking

Lessons in `lead-acquisition/` reference each other ("follow-up sequence",
"ICP rubric", "pipeline tracker"). When the user is reading and asks about
one of those, point them at the right lesson file or the right kit. Some
lessons mention Kevin's own tools (`gws-oak`, `oakline-pitch`) as examples of
what a finished setup looks like; the user will not have those, so translate
to what they do have instead of telling them to install Kevin's stack.
