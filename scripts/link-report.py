"""Count in-text internal links per page (run after `npm run build`).

Counts links inside <main> only (header, footer and nav excluded) and
separates links in body copy from links in repeated card blocks.
Usage: python3 scripts/link-report.py
"""
import re, glob, collections

inbound = collections.Counter()
rows = []
for f in glob.glob('_site/**/index.html', recursive=True):
    s = open(f).read()
    m = re.search(r'<main id="main">(.*)</main>', s, re.S)
    if not m:
        continue
    url = f[5:-10] or '/'
    main = m.group(1)
    # card/grid blocks repeated across pages don't count as contextual links
    body = re.sub(r'<(div|ul) class="(mini-cards|trip-grid-cards[^"]*|reports|species-row|areas|captains|gallery[^"]*)".*?</\1>', '', main, flags=re.S)
    body = re.sub(r'<div class="species-row">.*?</ul>\s*</div>', '', body, flags=re.S)
    ctx = {h for h in re.findall(r'href="(/[^"#?]*)"', body) if h != url}
    for h in ctx:
        inbound[h] += 1
    rows.append((url, len(ctx)))

skip = {'/privacy/', '/terms-conditions/', '/thank-you/'}
print(f'{"page":62} in-text-out  in-text-in')
for url, n in sorted(rows, key=lambda r: r[1]):
    if url in skip:
        continue
    flag = '  <-- under 3' if n < 3 or inbound[url] < 3 else ''
    print(f'{url:62} {n:6d} {inbound[url]:10d}{flag}')
