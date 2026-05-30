# Pipeline Schema

The canonical column set for `outputs/pipeline.csv`. Do not add or remove
columns without updating this file first.

## Header row (CSV)

```
id,company,owner,title,email,linkedin_url,city_state,source,icp_score,tier,pain_hypothesis,first_send_date,fu1_date,fu2_date,fu3_date,reply_date,reply_type,status,next_action,next_action_date,deal_value,retainer,notes
```

## Column definitions

- **id**: integer, auto-incremented. Never reuse.
- **company**: legal-ish, the way you would address them. `Acme Concrete`.
- **owner**: full name of the actual decision maker.
- **title**: their role. `Owner`, `Operations Manager`. Plain English.
- **email**: lowercase. One address. If they have two, pick the personal one.
- **linkedin_url**: full URL. Empty if not found, do not invent.
- **city_state**: `Austin, TX`. Helps regional sorting later.
- **source**: where you got them. `apollo`, `google maps`, `referral from
  joe`, `dm on linkedin`.
- **icp_score**: integer 0-10 from your ICP rubric. Threshold for outreach is
  6.
- **tier**: `A`, `B`, `C`. A is top 25, B is next 50, C is filler.
- **pain_hypothesis**: one sentence. The painful manual workflow you think
  they have. `Manually sending invoices in QuickBooks then chasing payment by
  text`.
- **first_send_date**: ISO date `2026-05-30`. Empty until sent.
- **fu1_date**, **fu2_date**, **fu3_date**: same format. Empty until sent.
- **reply_date**: when they replied.
- **reply_type**: `interested`, `info_request`, `soft_no`, `hard_no`,
  `do_not_contact`. Empty until they reply.
- **status**: see `status-flow.md`. Only values from that file.
- **next_action**: short imperative. `Send FU2 with case angle`. `Run
  discovery call`.
- **next_action_date**: ISO date.
- **deal_value**: integer USD setup fee. Empty until scoped.
- **retainer**: integer USD/mo. Empty until scoped.
- **notes**: free text. Date-prefix any addition. `2026-05-30: said callback
  in two weeks`.

## Derived (do not store)

- **days_since_last_touch**: today minus the latest of first_send_date,
  fu1_date, fu2_date, fu3_date, reply_date.

These are computed on the fly when the standup runs.
