# Wise Design - Colorful Refero Design MD

- Source: https://styles.refero.design/style/c5326639-873a-4257-ad1a-7da9111e9286
- Original site: https://wise.design
- Theme: `mixed`
- Color rank: **02**
- Colorfulness score: `50.0`
- Recommended fit: **Colorful SaaS accent system**

## North star
Neon market stall on a global street - electric lime signage that shouts across a crowded marketplace, then polished product UI slips in behind it.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Lime Volt | `#87ea5c` | brand | Hero backgrounds, pill button fill, category tag backgrounds - the single most identifiable brand signal; vivid green a. |
| Forest Ink | `#083400` | brand | Primary text, dark headlines on lime, nav links, icon fills - deep forest green instead of black keeps everything on-br. |
| Volt Yellow | `#ffea4b` | accent | Accent headlines, decorative text color on dark backgrounds - electric yellow that pairs with deep burgundy for maximum. |
| Papaya | `#ffbd89` | accent | Warm accent card backgrounds, decorative section highlights |
| Cotton Candy | `#ffd5f0` | accent | Soft accent backgrounds, section highlights in the mosaic grid |
| Aubergine Night | `#2a0831` | accent | Dark card backgrounds, high-contrast panels in the content grid - deep purple-black that isn't neutral |
| Crimson Depth | `#370305` | accent | Dark editorial backgrounds, heading color on light panels - near-black red that reads as richly dark without being neut. |
| Fog | `#58717a` | neutral | Secondary body text, border colors, UI chrome |

```css
:root {
  --colorful-lime-volt: #87ea5c;
  --colorful-forest-ink: #083400;
  --colorful-volt-yellow: #ffea4b;
  --colorful-papaya: #ffbd89;
  --colorful-cotton-candy: #ffd5f0;
  --colorful-aubergine-night: #2a0831;
  --colorful-crimson-depth: #370305;
}
```

## Typography direction
- Primary: **Inter**; substitute `Inter (Google Fonts - this IS Inter)`.
- Secondary/code: **Wise Sans**; substitute `Obviously (similar ultra-compressed display), or Neue Haas Grotesk Display at u.`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
