# Mailchimp - Colorful Refero Design MD

- Source: https://styles.refero.design/style/24929007-7e62-4c96-a940-7de65438a578
- Original site: https://mailchimp.com
- Theme: `light`
- Color rank: **40**
- Colorfulness score: `29.8`
- Recommended fit: **Colorful editorial / creator page**

## North star
Vintage press meets electric yellow - an editorial print house with one neon switch.

## Why this fits html-news-creator
Use for richer report storytelling while keeping the reading structure intact.

## Apply to
- Story-led report section variants
- Newsletter-style summaries
- Image evidence callouts

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Press Black | `#231e15` | brand | Primary text, headings, button borders, backgrounds of dark sections - the near-black with a warm brown undertone that. |
| Voltage Yellow | `#ffe01b` | brand | Primary CTA buttons and nav 'Iniciar gratis' - one saturated hit of color on an otherwise near-monochrome page; impossi. |
| Teal Ink | `#004e56` | accent | Links, icon fills, image accents - muted teal provides navigational contrast against warm-neutral backgrounds without r. |
| Warm Parchment | `#ebe1cd` | neutral | Section backgrounds for GDPR and feature callout bands - warm cream that reads as aged newsprint, warmer than gray |
| Sand Footer | `#e7b75f` | neutral | Footer background - deeper gold-tan that anchors the page base with warmth |
| Ash White | `#f5f5f5` | neutral | Card backgrounds, secondary section fills |
| Pure White | `#ffffff` | neutral | Page backgrounds, card surfaces, reversed text on dark sections |
| Graphite | `#706d67` | neutral | Secondary body text, captions, supporting copy |

```css
:root {
  --colorful-press-black: #231e15;
  --colorful-voltage-yellow: #ffe01b;
  --colorful-teal-ink: #004e56;
  --colorful-warm-parchment: #ebe1cd;
  --colorful-sand-footer: #e7b75f;
  --colorful-ash-white: #f5f5f5;
  --colorful-pure-white: #ffffff;
}
```

## Typography direction
- Primary: **Graphik Web**; substitute `Inter, Aktiv Grotesk`.
- Secondary/code: **Means Web**; substitute `Freight Display, Canela, Playfair Display`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
