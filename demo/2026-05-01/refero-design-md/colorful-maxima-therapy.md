# Maxima Therapy - Colorful Refero Design MD

- Source: https://styles.refero.design/style/a122b132-2259-41ca-a301-4468dd17a386
- Original site: https://maximatherapy.com
- Theme: `light`
- Color rank: **27**
- Colorfulness score: `34.9`
- Recommended fit: **Colorful SaaS accent system**

## North star
Vibrant, rounded play-world. All surfaces are soft, every color is a smile.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text, critical UI elements, high-contrast outlines. |
| Paper White | `#ffffff` | neutral | UI backgrounds, button text on primary accents, badge backgrounds. |
| Light Linen | `#fff6ed` | neutral | Subtle background shading, neutral illustration fills. |
| Sunshine Yellow | `#fdcb40` | brand | Dominant page background, hero accents, main headings - establishes the core playful and optimistic tone. |
| Ocean Blue | `#006cff` | brand | Navigation active states, interactive card elements, secondary brand accent in illustrations. |
| Action Orange | `#fd4401` | accent | Call-to-action buttons, key interactive elements, highlighted card backgrounds - provides high-energy contrast against. |
| Grass Green | `#00b351` | accent | Decorative elements, illustration accents, and occasional secondary brand highlights. |
| Bubblegum Pink | `#f780d4` | accent | Decorative illustration accents, adding to the playful and diverse color palette. |

```css
:root {
  --colorful-midnight-ink: #000000;
  --colorful-paper-white: #ffffff;
  --colorful-light-linen: #fff6ed;
  --colorful-sunshine-yellow: #fdcb40;
  --colorful-ocean-blue: #006cff;
  --colorful-action-orange: #fd4401;
  --colorful-grass-green: #00b351;
}
```

## Typography direction
- Primary: **ABC Diatype Rounded Plus**; substitute `Outfit`.
- Secondary/code: **Robuck Rounded**; substitute `Fredoka One`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
