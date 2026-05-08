# Kit - Colorful Refero Design MD

- Source: https://styles.refero.design/style/7f7d24b9-6878-4548-82ca-a26bbf7a6f2c
- Original site: https://kit.com
- Theme: `light`
- Color rank: **10**
- Colorfulness score: `42.4`
- Recommended fit: **Colorful editorial / creator page**

## North star
Warm creator notebook - parchment pages, highlighter-blue ink, heavy type on linen.

## Why this fits html-news-creator
Use for richer report storytelling while keeping the reading structure intact.

## Apply to
- Story-led report section variants
- Newsletter-style summaries
- Image evidence callouts

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Marker | `#44b1ff` | brand | Primary CTA buttons, active nav states, inline keyword highlights - vivid blue on parchment or near-black backgrounds a. |
| Dust Blue | `#a2d1f1` | accent | Hero and section background panels - muted blue used as an atmospheric backdrop, never for text or interaction |
| Blush Mist | `#e7c9f1` | accent | Section background panels - pastel pink used decoratively to vary section rhythm |
| Peach Sand | `#ffd0ad` | accent | Section background panels - muted orange for alternating content band backgrounds |
| Sage Foam | `#b9e9c5` | accent | Section background panels - muted green used as a decorative surface, never for semantic status |
| Amber Flag | `#f2ba41` | accent | Icon fills and inline callout elements - warm yellow used sparingly for small graphic accents, not for text or backgrou. |
| Near Black | `#1e1e1` | neutral | Primary text, nav text, button text, footer text, borders on dark surfaces - near-black rather than pure black softens. |
| Parchment | `#f2efe9` | neutral | Page background, hero section fill, card backgrounds - the defining warm-tinted base that makes the whole site feel lik. |

```css
:root {
  --colorful-sky-marker: #44b1ff;
  --colorful-dust-blue: #a2d1f1;
  --colorful-blush-mist: #e7c9f1;
  --colorful-peach-sand: #ffd0ad;
  --colorful-sage-foam: #b9e9c5;
  --colorful-amber-flag: #f2ba41;
  --colorful-near-black: #1e1e1;
}
```

## Typography direction
- Primary: **KitSansFont**; substitute `Instrument Sans, Plus Jakarta Sans`.
- Secondary/code: **Libre Franklin**; substitute `Libre Franklin is freely available on Google Fonts - use directly`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
