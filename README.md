# Charter Fishing Tampa Bay (charterfishingtampabay.com)

Static site built with Eleventy, hosted on Netlify. Rebuilt Nov 2026 off Wix.

## Where things live
- `src/_data/site.json`: phone, email, booking link, social links, menu, GTM/GA4 IDs
- `src/_data/prices.json`: the price board on the home page
- `src/_data/trips.json`: the four trip cards on the home page
- `src/_data/reviews.json`: review quotes (real reviews only, word for word)
- `src/*.md`: trip, species, area and other pages. Trip details (prices, guests, departure) are in each page's front matter at the top.
- `src/fishing-reports/`: one file per report. `src/fishing-guides/`: season guides.
- `src/images/`: WebP photos. `src/assets/css/site.css`: all styles.
- `netlify.toml`: build settings and 301 redirects from old Wix blog addresses.

## Update and deploy
Edit a file, commit to `main`, and Netlify rebuilds automatically. Local preview: `npm install`, then `npm start`.

## Before launch
Search the site for `[` to find every placeholder still to fill (marinas, guest limits, review source, gift card link, legal text, GTM ID).
