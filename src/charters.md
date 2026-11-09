---
layout: page.njk
permalink: /charters/
seoTitle: "Fishing Trips & Prices | Charter Fishing Tampa Bay"
description: "Compare every Tampa Bay fishing charter we run: inshore, nearshore, offshore, crappie & species trips, with prices by length. Reserve with a 10% deposit."
h1: Tampa Bay Fishing Charters
wide: true
intro: "Calm flats at sunrise, a cooler of snapper off Gulf bottom, a tarpon in the air in July, or specks in the grass on a quiet lake. Pick the kind of day you want, and we'll put you with the captain who fishes it."
---
## Fishing charters by the water you want

<div class="trip-grid-cards wide">{% for t in trips %}{% if t.group == "water" %}{% include "trip-card.njk" %}{% endif %}{% endfor %}</div>

## Fishing charters by the fish you want

<div class="trip-grid-cards wide">{% for t in trips %}{% if t.group == "fish" %}{% include "trip-card.njk" %}{% endif %}{% endfor %}</div>

## Every trip includes

Your captain, rods, reels, tackle and bait, plus bottled water and ice. Saltwater fishing licenses are covered; crappie anglers bring a Florida freshwater license. Reserve with a 10% deposit, refunded if weather cancels the trip.

## Where trips leave from

Marinas around metro Tampa, depending on the captain and the trip. [DEPARTURE MARINAS] Crappie trips launch from whichever lake the fish are on that week.
