# Example: pipeline.csv (worked example, 15 fake prospects)

Generated for the example intake. Niche: boutique vet clinics in the
Twin Cities metro. 15 prospects, all fictional, distributed across
stages so the daily standup and weekly review have something to show.

Today in this example is 2026-05-30. All dates and counts are relative
to that.

## Rendered table

| id | company | owner | icp | tier | status | last touch | reply_type | next_action |
|---|---|---|---|---|---|---|---|---|
| 1 | Lakeside Animal Hospital | Sarah Pham | 9 | A | awaiting_fu1 | 2026-05-26 | | Send FU1 today |
| 2 | Eastside Vet Clinic | Michael Tran | 8 | A | awaiting_reply | 2026-05-27 | | Wait, day 3 is tomorrow |
| 3 | Cedar Creek Animal Care | Rachel Olsen | 9 | A | replied | 2026-05-29 | interested | Send Calendly link |
| 4 | Northgate Veterinary | Ben Carlsen | 7 | B | awaiting_fu2 | 2026-05-22 | | Send FU2 today |
| 5 | Highland Pet Hospital | Anna Walsh | 8 | A | booked | 2026-05-28 | interested | Run discovery 2026-06-03 |
| 6 | Riverwood Vet | Karen Diaz | 6 | B | awaiting_fu3 | 2026-05-15 | | Move to closed_no_response |
| 7 | Oakdale Animal Clinic | Tom Rivera | 7 | B | replied | 2026-05-28 | info_request | Send 1-paragraph + Calendly |
| 8 | Birchwood Vet | Lisa Park | 9 | A | discovered | 2026-05-26 | interested | Send pilot scope today |
| 9 | Sunset Pet Care | David Cho | 8 | A | pilot_scoped | 2026-05-25 | | Close window 2026-06-01 |
| 10 | Maple Grove Vet | Erin Schultz | 6 | B | soft_no | 2026-03-20 | soft_no | Re-engage 2026-06-18 |
| 11 | Pinecrest Animal | Greg Olsen | 5 | C | hard_no | 2026-05-10 | hard_no | None |
| 12 | Willow Creek Vet | Megan Liu | 7 | B | closed_no_response | 2026-05-10 | | None |
| 13 | Brookside Pet Clinic | Nick Voss | 8 | A | awaiting_reply | 2026-05-29 | | Wait |
| 14 | Glenwood Veterinary | Amy Tran | 7 | B | closed_won | 2026-05-20 | interested | Deliver week 1 |
| 15 | Forestview Animal | Paul Kim | 6 | B | awaiting_fu1 | 2026-05-24 | | Send FU1 today |

## Raw CSV (first 5 rows shown, same shape for all 15)

```csv
id,company,owner,title,email,linkedin_url,city_state,source,icp_score,tier,pain_hypothesis,first_send_date,fu1_date,fu2_date,fu3_date,reply_date,reply_type,status,next_action,next_action_date,deal_value,retainer,notes
1,Lakeside Animal Hospital,Sarah Pham,Owner,sarah@lakesidevet.com,https://linkedin.com/in/sarahpham,Saint Paul MN,apollo,9,A,Front desk runs 6 hours a week of reminder calls,2026-05-26,,,,,,awaiting_fu1,Send FU1 today,2026-05-30,,,
2,Eastside Vet Clinic,Michael Tran,Owner,mtran@eastsidevet.com,https://linkedin.com/in/michaeltran,Minneapolis MN,apollo,8,A,Post-visit follow-ups still in-house,2026-05-27,,,,,,awaiting_reply,Wait,2026-05-31,,,
3,Cedar Creek Animal Care,Rachel Olsen,Owner,rachel@cedarcreekvet.com,https://linkedin.com/in/rachelolsen,Edina MN,google maps,9,A,Dental month recall list manual,2026-05-26,2026-05-29,,,2026-05-29,interested,replied,Send Calendly link,2026-05-30,,,
4,Northgate Veterinary,Ben Carlsen,Owner,bcarlsen@northgatevet.com,,Bloomington MN,apollo,7,B,Hiring second front desk for confirmations,2026-05-19,2026-05-22,,,,,awaiting_fu2,Send FU2 today,2026-05-30,,,
5,Highland Pet Hospital,Anna Walsh,Owner,anna@highlandpet.com,https://linkedin.com/in/annawalsh,Roseville MN,referral,8,A,Post-op call list eating reception time,2026-05-22,2026-05-25,,,2026-05-28,interested,booked,Run discovery,2026-06-03,,,2026-05-28: booked via Calendly
```

The remaining 10 rows follow the same column shape with realistic dates,
status values from `resources/stage-definitions.md`, and pain hypotheses
matched to the niche.
