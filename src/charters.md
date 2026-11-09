---
layout: page.njk
permalink: /charters/
seoTitle: "Fishing Trips & Prices | Charter Fishing Tampa Bay"
description: "Compare every Tampa Bay fishing charter we run: inshore, nearshore, offshore, crappie & species trips, with prices by length. Reserve with a 10% deposit."
h1: Tampa Bay Fishing Charters
wide: true
intro: "Nine trips run by four captains, each on his own boat. Every price is per boat, not per person, and covers your captain, rods, reels, tackle and bait."
---
## Fishing charters by the water you want

<div class="trip-grid-cards wide">{% for t in trips %}{% if t.group == "water" %}{% include "trip-card.njk" %}{% endif %}{% endfor %}</div>

## Fishing charters by the fish you want

<div class="trip-grid-cards wide">{% for t in trips %}{% if t.group == "fish" %}{% include "trip-card.njk" %}{% endif %}{% endfor %}</div>

## Every trip includes

Your captain, rods, reels, tackle and bait, plus bottled water and ice. Saltwater fishing licenses are covered; crappie anglers bring a Florida freshwater license. Reserve with a 10% deposit, refunded if weather cancels the trip.

## Where trips leave from

Capt. Pruner's inshore trips leave from Ruskin, at 611 Destiny Drive. Offshore trips launch from a ramp around Tampa Bay chosen for the day's weather, and crappie trips launch on the Kissimmee area lake we're fishing that week. Your captain confirms the meeting point when you book. More on [where we fish](/tampa-bay-fishing/), and meet the captains on [Our Captains](/about/). Questions? Our [FAQ](/faq/) covers licenses, kids and weather, our [reviews page](/reviews/) shows what guests say, and you can always [contact us](/contact-us/).
