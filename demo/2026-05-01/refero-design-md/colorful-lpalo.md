# Lpalo - Colorful Refero Design MD

- Source: https://styles.refero.design/style/79b4ebc4-30f6-45b6-b2d2-922e28e05ca9
- Original site: https://lpalo.com
- Theme: `light`
- Color rank: **49**
- Colorfulness score: `27.0`
- Recommended fit: **Playful visual exploration**

## North star
Blush Playground: A soft, inviting canvas for bold, playful content.

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Pink | `#f6e0db` | neutral | Primary page background, light surface |
| Surface White | `#ffffff` | neutral | Card backgrounds, secondary surface |
| Charcoal Text | `#000000` | neutral | Primary text, borders, active navigation outlines |
| Pumpkin Accent | `#ef724f` | accent | Orange wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the pri. |
| Lemon Highlight | `#e7db4c` | accent | Decorative splashes, card accents, playful iconography |
| Bubblegum Pink | `#981082` | accent | Card backgrounds, decorative accents, secondary navigation hover states |
| Spring Green | `#6ed311` | accent | Decorative iconography, small accent fills |
| Seafoam Accent | `#ace2df` | accent | Background for subtle accents and illustrations, card backgrounds |

```css
:root {
  --colorful-canvas-pink: #f6e0db;
  --colorful-surface-white: #ffffff;
  --colorful-charcoal-text: #000000;
  --colorful-pumpkin-accent: #ef724f;
  --colorful-lemon-highlight: #e7db4c;
  --colorful-bubblegum-pink: #981082;
  --colorful-spring-green: #6ed311;
}
```

## Typography direction
- Primary: **Alfa Slab One**; substitute `Bebas Neue`.
- Secondary/code: **Manrope**; substitute `Inter`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
