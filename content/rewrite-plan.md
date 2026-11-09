# Charter Fishing Tampa Bay: rewrite plan

## Why

Google dropped charterfishingtampabay.com from its index around Aug 26 to 28, 2026, with no technical cause. Search Console lists pages as "Discovered" or "Crawled, currently not indexed." Google judged the site as a whole: generic copy that could belong to any Tampa charter, thin pages, similar fishing reports and weak trust signals. See "SWM Site Quality Guardrails" in Drive (canonical rules).

The goal: every page reads as something only these guides could have written. Fewer, stronger pages. Rewording the old copy keeps the same problem.

## Source material

Rewritten pages draw only on:

- `content/research/directories-and-reviews.md`: booking page, directory listings, Google and other reviews (verbatim)
- `content/research/live-site-social-press.md`: live Wix site text, blog trip facts, Facebook and Instagram, press
- Monthly fishing reports (the real trip record)
- Facts confirmed by Andre or the client

Anything missing gets a `[PLACEHOLDER]`. Never invent facts, numbers, quotes, boats or species.

**Before any rewriting:** the research findings go into a Google Doc in the client's Drive folder ("Capt. William - Charter Fishing Tampa Bay"), titled "Research Findings — Charter Fishing Tampa Bay (Nov 2026)", so the team has them outside the repo.
Done Nov 9, 2026: https://docs.google.com/document/d/1lGBJOi5qnz047LnQC1prqeb2Y_yy4xlzf6e-LxHkb1o/edit

## Sitemap decisions (Nov 9, 2026, with Andre)

| Page | Decision |
|---|---|
| Home, Charters, Our Captains, Contact, FAQ | Keep, rewrite with first-hand detail |
| Inshore, Nearshore, Offshore, Crappie | Keep |
| Redfish, Snook | Keep (major commercial terms) |
| Tarpon, Grouper, Shark | Keep |
| Tampa Bay (`/tampa-bay-fishing/`) | Keep as the single "Where We Fish" page; menu item renamed |
| Apollo Beach, St. Petersburg, Anna Maria | Tabled. Copy saved in `content/tabled/areas/`; old addresses 301 to `/tampa-bay-fishing/`. Bring back only with first-hand detail (confirmed launch, captain, real trips) |
| Ruskin | Tabled (in the Master Content Plan, not built). Same bar as above |
| Season guides (king mackerel, mullet run, snook season) | Merged. Copy saved in `content/tabled/fishing-guides/`; 301 to Nearshore, Inshore and Snook. Fold their useful facts into those pages during the rewrite |
| Crappie report, Jan 2026 | Merged into the January 2026 roundup; 301 |
| Monthly roundups, Wapiti veterans report | Keep |
| Reviews | Keep; fill with real verbatim reviews from the research |
| Gallery, Privacy, Terms, Thank You, 404 | Keep |

Old Wix leftovers redirected: `/copy-of-about`, `/confirmation`, `/profile/*`.

## Progress

- Nov 9: Inshore, Redfish, Snook and Nearshore rewritten from the research (booking page facts, captains' listings, verbatim reviews, report facts). Corrected site wide: guest limits, nearshore from $650, offshore up to 6, crappie guests bring a freshwater license, "Gonzalez" spelling.
- Review quotes in `src/_data/reviews.json` (Eric M., Scott M., Jeff T., Cody G., Caleb C.) don't trace to any source found so far; not used on rewritten pages until confirmed.
- Next: Our Captains (with William/Gatorbacks), Home, Offshore, Crappie, Tarpon, Grouper, Shark, Where We Fish, FAQ, Reviews.

## Decided

- Capt. Gavin O'Neal is no longer with CFTB (Andre, Nov 9, 2026). Remove him everywhere; don't use reviews that name him.
- Google review counts (Andre, Nov 9): Charter Fishing Tampa Bay 12, Gatorbacks Fishing Charters (William Ashmore) 68, FG Charters (Frankie Gonzalez) 37, Barotrauma (Rob Hahn) 10, David Pruner 6. Total 133, plus FishingBooker reviews when found.

- Capt. Rob Hahn is one of our captains (Andre, Nov 9, 2026). He also runs Barotrauma Fishing Charters; treat him the same as the other guides on the site.

## Open decisions

- Real numbers for "[95+] years" and the review count before either goes in copy
- Marinas, guest limits and boat details per captain

## Internal linking (part of every rewritten page)

Kyle at Page Optimizer Pro: 3 to 4 internal links carry about the weight of one outside link, so the rewrite builds a deliberate web of links.

- Every page gets at least 3 to 4 in-text links out to related pages, inside the copy itself. Menu, footer and repeated card blocks don't count.
- Every page gets at least 3 to 4 in-text links in from other pages. Priority targets: Redfish, Snook, Inshore and Nearshore (the commercial pages), then Where We Fish and Our Captains.
- Our Captains links each captain to the trips he runs; each trip page links to the captains who run it.
- Every fishing report links to the trip and species pages for the fish it covers. Trip and species pages link back to their most relevant recent report.
- FAQ answers link to the trip, pricing or captain page that answers them in full.
- Where We Fish links each stretch of water to the trips that fish it.
- Anchors describe the page in plain words and vary naturally ("our redfish trips", "Capt. Ashmore's inshore charters"). No repeated exact-match keyword anchors, and only links that help a reader.
- Check after every build: `python3 scripts/link-report.py` flags any page under 3 in-text links out or in.

Baseline before the rewrite (Nov 9, 2026): Our Captains, FAQ, Contact, Reviews and Gallery had 0 in-text links out; Redfish, Snook and Tarpon had 2 in-text links in; the reports had none in from outside the reports list.

## Fishing reports going forward

Playbook v3: one in-depth report every 2 weeks or monthly, only with real trip details; unique titles; at least 2 to 3 real facts from the captain; thin notes become a monthly roundup; compare drafts against recent reports.
