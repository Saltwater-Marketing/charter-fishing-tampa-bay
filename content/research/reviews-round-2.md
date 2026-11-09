# Reviews and listings, round 2: source material

Collected 2026-11-09 for the charterfishingtampabay.com rewrite. This file collects material only. Nothing here is rewritten copy. It adds to `directories-and-reviews.md` (round 1) and does not repeat the FG Charters and Barotrauma reviews collected there.

Conventions:
- Text in quotation marks is copied character for character from the URL beside it.
- **UNCONFIRMED** means we could not tie the listing or text to our captain.
- "Fetch-tool summary" means the page could only be read through a summarising fetch tool, so the wording is near-verbatim at best and must not be quoted as exact.
- Method: Playwright as an ordinary browser (no login, no challenge solving), WebFetch, WebSearch.

---

## SUMMARY

### The main limit this round: Google Maps "limited view"

Google Maps now serves every place page to a signed-out browser in **"limited view"** ("You're seeing a limited view of Google Maps. See more"). In that view the page shows the name, star rating, category, hours, website and phone, but **no review count, no Reviews tab and no review text**. This applied to every profile tried, including FG Charters, whose reviews round 1 could still read. Signing in or working around this would break the collection rules, so **no Google review text could be collected this round**. The counts in the table below marked "owner" are the figures the account owner gave on 2026-11-09. We could not see them ourselves.

### Summary table

| Business | Captain | Platform | Rating | Count | Verbatim reviews collected this round |
|---|---|---|---|---|---|
| Gatorbacks Fishing Charters | William Ashmore | Google Maps (3 listings share the name, phone and website; see section 1) | 5.0 (shown on all 3) | not shown (owner: **68**) | **0** (limited view) |
| Gatorbacks Fishing Charters | William Ashmore | Own website, gatorbacksfishingcharters.com | "5/5" | "25 reviews" (static text on the site) | **1** (no reviewer name or date on the page) |
| Gatorbacks Fishing Charters | William Ashmore | Vally booking page | none | none | 0 (Vally shows no reviews) |
| Gatorbacks Fishing Charters | William Ashmore | Yelp | blocked (403) | snippet: "New on Yelp" | 0 |
| Gatorbacks Fishing Charters | William Ashmore | Superpages | none | 0 ("Be the first to review!") | 0 |
| Gatorbacks Fishing Charters | William Ashmore | FishAnywhere | blocked (Cloudflare) | unknown | 0 |
| Gatorbacks Fishing Charters | William Ashmore | Facebook (2 pages) | blocked (login wall) | unknown | 0 |
| Gatorbacks Fishing Charters | William Ashmore | FishingBooker | no listing found | none | 0 |
| Charter Fishing Tampa Bay (brand) | all | Google Maps | **profile not found** | owner: **12** | 0 |
| Hooked On Tampa Bay Fishing Charters, LLC | David Pruner | Google Maps | 5.0 | not shown (owner: **6**) | **0** (limited view) |
| Hooked On Tampa Bay Fishing Charters | David Pruner | Own website, hookedontampabayfishingcharters.com | none | "Reviews coming soon!" | 0 |
| Captain Dave | David Pruner | FishingBooker, charters/view/30888 | none ("New") | 0 shown ("Loading...") | 0 |
| FG Charters | Frankie Gonzalez | FishingBooker | no listing found | none | 0 (Google reviews already in round 1) |
| Barotrauma Fishing Charters | Rob Hahn | FishingBooker | no listing found | none | 0 (Google reviews already in round 1) |

**Total new verbatim reviews this round: 1** (unattributed, from the Gatorbacks website).

### Key new facts

1. **Pruner's Google profile is "Hooked On Tampa Bay Fishing Charters, LLC"**, phone +1 813-494-0377, website hookedontampabayfishingcharters.com, 5.0 stars. It is tied to him because his own website names "Captain David Pruner" and his Vally login email is hookedontampabayfishing@gmail.com (Vally `/members` API).
2. **Gatorbacks uses the same phone as the brand: 813-714-5670.** That is the phone on charterfishingtampabay.com, on Gatorbacks' Google listing and site, and on William Ashmore's Vally member record. The brand site's Google map embed is pinned to "Gatorbacks Fishing Charters". So the "Charter Fishing Tampa Bay" phone search lands on Gatorbacks, and the brand's own 12-review profile still has not been found.
3. **Three Google Maps listings named "Gatorbacks Fishing Charters"** show up, each with 5.0, the same website and the same phone. They may be duplicates. We cannot tell which one holds the 68 reviews (limited view hides the counts). One might even be the brand's 12-review profile under another name, but that is a guess and is **UNCONFIRMED**.
4. **The Gatorbacks website is a near-copy of the CFTB site** (same Saltwater Marketing template, the same "Captain Ashmore" bio lines, the same trip list and prices).
5. **Ashmore's Vally account ("Gatorbacks Fishing Charters") lists Frankie Gonzalez and David Pruner as members too**, and has the same "Overflow" calendars as the brand account.

---

## 1. Gatorbacks Fishing Charters (Capt. William Ashmore)

### How it is tied to William Ashmore (CONFIRMED)
- The website names "Captain Ashmore" and repeats his CFTB bio (below).
- The Vally booking page linked from the site, https://book.vallypro.com/p/gatorbacks-fishing-charters (business id 669e715ff5f141c886c00cc3), lists member "William " "Ashmore" (trailing space as stored), email williamdashmore@gmail.com, phone "8137145670". Source: `/api/businesses/669e715ff5f141c886c00cc3/members`, loaded by the public page.
- The owner confirmed on 2026-11-09 that Gatorbacks is William's own business.

### Google Maps
All three listings were loaded in Playwright on 2026-11-09. Each one was in limited view: no review count, no reviews tab, no review text.

| Listing | Place ID | Rating | Phone | Website | Notes |
|---|---|---|---|---|---|
| A (the one the brand site and Gatorbacks site embed and link) | 0x8342fd69edf2df0f:0x6662110eb34d4efc (cid 7377477894421696252) | 5.0 | +1 813-714-5670 | gatorbacksfishingcharters.com | "Fishing charter". No street address shown; it is a service-area listing whose drawn area covers roughly Tampa Bay (Clearwater to Bradenton to Plant City). Hours label: "Sunday, 7 AM to 9 PM"; panel said "Closed · Opens 7 AM Mon". Profile photo: a young angler holding a large grouper on a boat. |
| B | 0x85360e6bd74357fd:0x4fd0f37103e3881c | 5.0 | +1 813-714-5670 | gatorbacksfishingcharters.com | "Closed · Opens 7 AM Mon" |
| C | 0x2b5eaddf4cf6fbe9:0xc0bb8bb1e0d36814 | 5.0 | +1 813-714-5670 | gatorbacksfishingcharters.com | "Closed · Opens 7 AM Mon" |

URLs:
- A: https://www.google.com/maps/place/Gatorbacks+Fishing+Charters/data=!4m7!3m6!1s0x8342fd69edf2df0f:0x6662110eb34d4efc (also https://maps.google.com/maps?cid=7377477894421696252, the "Google reviews" link on gatorbacksfishingcharters.com)
- B: https://www.google.com/maps/place/Gatorbacks+Fishing+Charters/data=!4m7!3m6!1s0x85360e6bd74357fd:0x4fd0f37103e3881c!8m2!3d28.132729!4d-82.1118366!16s%2Fg%2F11srftybt0
- C: https://www.google.com/maps/place/Gatorbacks+Fishing+Charters/data=!4m7!3m6!1s0x2b5eaddf4cf6fbe9:0xc0bb8bb1e0d36814!8m2!3d28.0695286!4d-82.4814605!16s%2Fg%2F11srdwr9q9

Owner-supplied count: **68** reviews. Not visible to us.

### Website: https://www.gatorbacksfishingcharters.com/ (marketing copy, "Charter Fishing Solutions from Saltwater Marketing")
Single-page Wix site (the sitemap lists only the home page). Rendered with Playwright. Verbatim:
- Headline: "Your Tampa Fishing Adventure Awaits" / "Tampa Bay's Most Exciting Charter Fishing!" / "Captain Ashmore Puts You On the Redfish!"
- Score badges: "5/5 Boat" "5/5 Crew" "5/5 Experience"
- Bio: "As a Florida native, Captain Ashmore has over 40 years of experience fishing Tampa Bay Area and Central Florida"
- Licence: "Captain Ashmore holds a USCG Master's License for 100 GRT and all applicable credentials"
- Trip cards: Inshore "From $600"; Nearshore "From $850"; Offshore "From $950"; Crappie Lake Trips "From $550" ("Our Crappie trips around the Kissimmee area lakes are perfect for a day of fun for new & experienced anglers."); Grouper "From $650"; Redfish "From $600"; Shark "From $600"; Snook "From $600"; Tarpon "From $650".
- Reviews block: "Happy Customer Reviews" / "5/5" / "25 reviews" / then one quote (see below) / "View All Reviews" (links to the Google listing A).
- Areas We Fish: "Tampa Bay" / "Anna Maria" / "Kissimmee" / "Saint Petersburg"
- Contact: "To Book With Gatorbacks: Send Us a Message Using the Form Above Or Text Us at 813-714-5670" / "All Messages Will Be Returned Once the Captain Is Off the Water"
- Footer: "Providing unforgettable experiences on the Tampa Bay waters for fishing charter trips." / "REACH US HERE" / "Holloway Rd, Plant City," / "FL 33567, United States" / "Phone :  813-714-5670" / "Copyright © 2025 Gatorbacks Fishing Charters - All Rights Reserved."
- Promo: "Give the gift of fishing this holiday season! Purchase a gift card in any amount!"
- Links: Facebook https://www.facebook.com/gatorbacksfishingcharters and https://www.facebook.com/gatorbacksbait ; gift cards https://book.vallypro.com/p/gatorbacks-fishing-charters/cart/gift-card
- Boat: **not stated anywhere on the site.**

**Verbatim review on the site (no reviewer name, no date, no platform named):**
> "Lots of knowledge with a calm cool demeanor. Caught fish all day every spot we stopped at! Great trip, highly recommend."

Source: https://www.gatorbacksfishingcharters.com/ (Happy Customer Reviews block). Tied to Gatorbacks, but the reviewer is unknown, so it cannot be attributed to a named guest.

### Vally booking page: https://book.vallypro.com/p/gatorbacks-fishing-charters
Data from the public page and the JSON it loads (`/services`, `/members`, `/calendar-groups`).
- Members: William Ashmore (phone 8137145670), Frankie Gonzalez, David Pruner, and two "Admin User" entries. Calendar groups: "Vally - William", "Vally - David Pruner", "Vally - Admin User", "Vally - Frankie", "Overflow", "Overflow 2". Every active trip is assigned to "Vally - William" plus the two Overflow calendars.
- Active trips shown on the page (verbatim card text): "Inshore Fishing Charters From $600 All Year 1-6"; "Nearshore Fishing Charters From $750 All Year 1-6"; "Shark Trips From $600 All Year 1-6"; "Tarpon Fishing Trips From $750 Apr 1 - Aug 31 1-4"; "Offshore Fishing Charter From $950 All Year 1-6"; "Gift Cards".
- Prices from the JSON (all start 8:00):
  - Inshore: 4h $600, 6h $750, 8h $950. 5th guest +$75, 6th +$150.
  - Nearshore: 6h $750, 8h $950. 5th +$75, 6th +$150. (The Gatorbacks site says "From $850".)
  - Shark: 4h $600, 6h $800, 8h $1,000. 5th +$75, 6th +$150.
  - Tarpon: 4h $750, 6h $900, 8h $1,150. 3rd guest +$75, 4th +$150. Minimum age 10. Season 1 April to 31 August. (The Gatorbacks site says "From $650".)
  - Offshore: 6h $950, 8h $1,150. **The group-size options look misconfigured:** "4 people" carries +$950, and "5 people" and "6 people" carry +$75 each.
  - Inactive (hidden): "Inshore Grouper trip" (4h $650/$550, 6h $800/$750, 8h $1,000) and "Crappie Lake Trips" (4h $550, 6h $650, 1–4 guests). The Gatorbacks site still advertises both.
- Trip descriptions (verbatim):
  - Inshore: "4-Hour - Fast Trip - Tons of Action!\r\n6-Hour - Allows for More Site Casting in Search of the Perfect Bite\r\n8-Hour - Perfect Day on the Water Likely Fishing Two Tides"
  - Nearshore: "Fishing from the mouth of Tampa bay out to nine miles. When we bottom fish we will be targeting grouper and snapper. We can also run into blackfin tuna, king mackerel, cobia, and an occasional wahoo."
  - Shark: "Shark Trips!!! We will be targeting all local species. Some of the species we target are Blacktip, Bonnet Head, Bulls, Tiger, Lemons, and Hammerheads."
  - Tarpon: "Our summertime brings in an amazing amount of migratory tarpon. We will target them on bridges and around the passes. Sometimes we will also target them on the beach as well."
  - Offshore: "This trip will starts where the near shore trip ends. 9 miles and further,  All your favorite bottom fish and we are always looking for those pelagics as well."
  - Provided (inshore, nearshore, shark, tarpon): "• All rods, reels, bait and tackle. • All necessary safety equipment. • A cooler with cold water and ice. • All fishing licenses needed."
- No meeting point or address is set on any trip.

### Directory listings
- **Superpages** (https://www.superpages.com/plant-city-fl/bpp/gatorbacks-fishing-charters-501378293), fetch-tool summary: "3206 Holloway Rd, Plant City, FL 33567"; "Main - (813) 714-5670"; hours "Mon - Sun: 7:00 am - 5:00 pm"; "18 Years in Business"; no rating; "Be the first to review!"; listed under the wrong category, "Architects & Builders Services".
- **MapQuest** (https://www.mapquest.com/us/florida/gatorbacks-fishing-charters-659760312): page came back empty to the fetch tool. The search result title gives "3206 Holloway Rd, Plant City, FL 33567".
- **Boaterslist** (https://www.boaterslist.com/vendors/gatorbacks-fishing-charters-107959), fetch-tool summary: "Led by Captain Ashmore, a Florida native with over 40 years of professional fishing experience"; no rating, count or reviews.
- **Yelp** (https://www.yelp.com/biz/gatorbacks-fishing-charters-plant-city): **blocked** (403 to both the fetch tool and Playwright). Search snippets only: "New on Yelp", "We fish Tampa Bay and surrounding areas year round, offering inshore, nearshore and offshore fishing." One search summary said Yelp gives the year established as 2015 (not verified).
- **FishAnywhere** (https://fishanywhere.com/charters-guides/gatorbacks-fishing-charters): **blocked** (Cloudflare "Performing security verification"). Search summaries said the listing is in Ruskin with a "23-foot bay boat", up to 4 passengers, and a $450 starting price. **UNCONFIRMED.** A 23' bay boat in Ruskin matches **Pruner's** boat and departure point, not anything known about Ashmore, so this listing may mix the two captains. Do not use it.
- **Roadtrippers** (https://maps.roadtrippers.com/us/plant-city-fl/sports/gatorbacks-fishing-charters-plant-city-fl--0): blocked (403).
- **Facebook** https://www.facebook.com/gatorbacksfishingcharters and https://www.facebook.com/gatorbacksbait: **blocked** (login wall).
- A search summary also mentioned a Gatorbacks listing at "2401 19th Ave NW, Ruskin". A search for that address found other charters there (Ransom, True Story, Matthew 14:17, Tampa Bay Guide Services) but no Gatorbacks page. **UNCONFIRMED.**

### Launch point and address: notes for the rewrite
- The website footer gives only "Holloway Rd, Plant City, FL 33567". Directories give the street number 3206. This is probably a home or base address, not a launch ramp. **Check with William before publishing it.**
- No launch ramp or marina is named anywhere for Ashmore. Areas named: Tampa Bay, Anna Maria, Kissimmee, Saint Petersburg.

---

## 2. Charter Fishing Tampa Bay (brand) Google profile

**Not found.** The owner says it has 12 reviews.

Maps searches run in Playwright on 2026-11-09, none of which returned a listing named "Charter Fishing Tampa Bay":
- "Charter Fishing Tampa Bay"; "Charter Fishing Tampa Bay Plant City"; "Charter Fishing Tampa Bay Tampa FL fishing charter"; "\"Charter Fishing Tampa Bay\" Ruskin"; "Charter Fishing Tampa Bay Apollo Beach"; "Charter Fishing Tampa Bay Saint Petersburg"; "Charter Fishing Tampa Bay Kissimmee"; "Charter Fishing Tampa Bay LLC"; "Charter Fishing Tampa Bay Brandon"; "Charter Fishing Tampa Bay Anna Maria"; "Charter Fishing Tampa Bay Bayport"; "(813) 714-5670"; "8137145670"; "charterfishingtampabay.com".
- The phone 813-714-5670 belongs to the **Gatorbacks** listings (section 1).
- Web search for "Charter Fishing Tampa Bay" plus "714-5670" returned only the brand's own site pages.

Possible explanations, all **UNCONFIRMED**: the brand profile is one of the three "Gatorbacks Fishing Charters" listings under another name; it is unverified or suspended and hidden from search; or it uses a different name. **The owner should send the profile's share link (Google Business Profile > Share).**

---

## 3. Capt. David Pruner: Hooked On Tampa Bay Fishing Charters

### How it is tied to Pruner (CONFIRMED)
- The website names "Captain David Pruner" throughout.
- Pruner's Vally member record (on the Gatorbacks, FG Charters and brand accounts) uses the email hookedontampabayfishing@gmail.com.
- Same boat as his FishingBooker listing (23' Sea Pro, 200 hp Suzuki).

### Google Maps
- Listing: **"Hooked On Tampa Bay Fishing Charters, LLC"**, **5.0**, "Fishing charter", website hookedontampabayfishingcharters.com, phone **+1 813-494-0377**, "Closed · Opens 7 AM Mon". Limited view: no count and no reviews visible.
- URL: https://www.google.com/maps/place/Hooked+On+Tampa+Bay+Fishing+Charters,+LLC/data=!4m7!3m6!1s0x6c5c2396ab473173:0x273a8ab26e025d78!8m2!3d27.76388!4d-82.408286!16s%2Fg%2F11y6nw4h40
- The pin coordinates (27.764, -82.408) are in the Ruskin area, which fits his FishingBooker departure at 611 Destiny Drive, Ruskin.
- Owner-supplied count: **6** reviews. Not visible to us.
- Searches for "Captain Dave Pruner" on Maps returned other operators only.

### Website: https://hookedontampabayfishingcharters.com/ ("Powered by: INNOVATIVE MARKETING EXPERTS", © 2023)
Verbatim:
- Home headline: "Experience the BEST Fishing Charters in Tampa Bay!" / "Tampa's Top Fishing with Captain David Pruner"
- Trips: "Custom Fishing Charter Trip 8 hrs |Pricing Varies"; "6-Hour Fishing Charter Trip 6 hrs |$675"; "4-Hour Fishing Charter Trip 4 hrs |$550". (The 4-hour card reuses the 6-hour card's teaser text.)
- Home: "At Hooked on Tampa Bay Fishing Charters, our journey started over 25 years ago in the serene waters of Indiana, where I, Captain David Pruner, learned the art of fishing. This passion led me to the vibrant and diverse waters of Tampa Bay, where I realized my dream of sharing the exhilaration of fishing with others."
- Home: "On our 23’ Sea Pro Bay Boat, equipped for inshore fishing experiences, we offer not just a day of fishing, but an opportunity to create lasting memories and forge a deep connection with nature."
- What We Do: "Hooked on Tampa Bay Fishing Charters specializes in inshore and nearshore fishing adventures, offering a personalized and educational approach to sport fishing." ... "Beyond fishing, our charters often encounter stunning Florida wildlife, from playful dolphins to majestic seabirds, making every trip with us a unique encounter with the wonders of Tampa Bay."
- About (https://hookedontampabayfishingcharters.com/about): "I'm Captain David Pruner, your go-to guy for all things fishing in and around the bountiful waters of Tampa Bay. My journey with the rod and reel started 25 years ago, but the seeds were sown much earlier in the quiet lakes of Indiana with my Dad."
- About: "He was the one who taught me that patience and persistence aren't just virtues, they're the secret ingredients to reeling in success, both in life and fishing!"
- About: "My love for fishing grew from a cherished pastime to a full-blown career – talk about living the dream! Every day on the water still feels like a new adventure, and I'm a firm believer in the mantra, 'you never stop learning.'"
- About (boat): "The real star of the show (apart from the fish, of course) is my trusty vessel, a sleek 23’ Sea Pro Bay Boat powered by a robust 200 hp Suzuki. She's not just a beauty to behold; she's fully equipped for all inshore and nearshore escapades. We've got top-of-the-line safety gear, state-of-the-art equipment, and a ship-to-shore radio to keep us connected no matter where our fishing tales take us."
- About, reviews section: "Reviews coming soon!"
- Contact: "813.494.0377"; hours "By Appointment" every day. No address shown.

### Other Pruner-like listings
- Facebook "Hooked On Tampa Fishing Charter" (https://www.facebook.com/people/Hooked-On-Tampa-Fishing-Charter/61550528454792/): per a search summary, phone 813-770-6083, trips on artificial lures and flies, 1 review. **UNCONFIRMED.** The phone does not match Pruner's, and the page was not opened (Facebook login wall).

---

## 4. FishingBooker

- **Pruner, "Captain Dave"** (https://fishingbooker.com/charters/view/30888):
  - Playwright: **blocked** (Cloudflare "Performing security verification", HTTP 403).
  - WebFetch returned a summarised page. Fetch-tool summary: no rating or review count next to the title; "Customer reviews" followed by "Loading..."; the listing card is labelled "New". **No reviews visible.**
  - Bio opens (quoted by the fetch tool): "Captain Dave Pruner leads exciting trips stretching from Bradenton Beach to Tampa Bay." The rest could not be obtained verbatim.
  - Fetch-tool summary of facts: member since October 2022; boat 23 ft Sea Pro bay boat, center console, capacity 6, built 2004, restored 2018, 1 x 200HP Suzuki; departure "611 Destiny Drive, Ruskin, FL 33570, United States"; "Half Day Trip" 4h 8:00 AM US $700; "3/4 Day Trip" 6h 8:00 AM US $875 (whole boat, up to 6). Included (quoted by the fetch tool): "Rods, reels & tackle", "Live bait", "Lures", "Catch cleaning & filleting", "Drinks", "First mate", "Fishing license". Pickup (quoted by the fetch tool): "Transfer from hotels or jetties in Ruskin to departure site is available and included in trip rates."
  - Prices differ across his channels: FishingBooker 4h $700 / 6h $875; his own site 4h $550 / 6h $675.
  - Profile https://fishingbooker.com/profile/view/928961 ("Captain David Pruner, Ruskin"): 403.
  - **Wayback Machine:** a snapshot exists (http://web.archive.org/web/20260607041852/https://fishingbooker.com/charters/view/30888, per the archive.org availability API), but web.archive.org could not be reached from this session (the tunnel closed, then "upstream request failed" 502; WebFetch refuses the domain). **Not read.**
- **Ashmore / Gatorbacks:** no FishingBooker listing found (site-restricted searches for Ashmore, Gatorbacks and Plant City).
- **Frankie Gonzalez / FG Charters:** no listing found (as in round 1).
- **Rob Hahn / Barotrauma:** no listing found.

---

## 5. Blocked or not reachable

| Source | Result |
|---|---|
| Google Maps reviews (all profiles, including FG Charters, which worked in round 1) | "Limited view" for signed-out browsers: no review counts, no reviews tab, no text |
| Google Maps embed (on the CFTB and Gatorbacks sites) | Map only; no rating or reviews |
| FishingBooker (Playwright and curl) | Cloudflare challenge (403) |
| FishingBooker profile 928961 (WebFetch) | 403 |
| web.archive.org | Unreachable from this session (tunnel closed / 502); WebFetch refuses the domain |
| Yelp (Gatorbacks) | 403 |
| FishAnywhere (Gatorbacks) | Cloudflare challenge |
| Roadtrippers | 403 |
| Facebook (gatorbacksfishingcharters, gatorbacksbait, Hooked On Tampa) | Login wall |
| MapQuest | Empty page to the fetch tool |

## 6. What the owner could supply to finish this

1. The share links (or screenshots) of the four Google profiles: Charter Fishing Tampa Bay (12), Gatorbacks (68; and which of the 3 listings it is), Hooked On Tampa Bay Fishing Charters (6). Alternatively, an export from each Google Business Profile manager.
2. Whether the 3 Gatorbacks Maps listings are duplicates to merge.
3. Whether "3206 Holloway Rd, Plant City" may be published, and the real launch ramps for William and David.
