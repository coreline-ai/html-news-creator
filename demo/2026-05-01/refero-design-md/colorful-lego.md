# Lego - Colorful Refero Design MD

- Source: https://styles.refero.design/style/7e21f6e1-deec-4bc4-a30e-f2c9d3320314
- Original site: https://lego.com
- Theme: `light`
- Color rank: **22**
- Colorfulness score: `39.3`
- Recommended fit: **Playful visual exploration**

## North star
Primary-color toy aisle - the brightness of a freshly opened set box on a white table.

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| LEGO Yellow | `#FFD502` | brand | Logo background, badges, active nav indicators, brand accent - the single chromatic constant that appears regardless of. |
| Brick Orange | `#F47D20` | brand | Primary CTA buttons ('Buy now', 'Add to Bag', 'Become a member') - warm against white product backgrounds, the only pil. |
| Ember Dark | `#E96F14` | brand | Orange hover/pressed state for CTA buttons - 1 step darker than Brick Orange. |
| LEGO Navy | `#201D48` | brand | Footer background, deep brand surface - the only dark chromatic surface, anchoring the page bottom with brand identity. |
| Link Blue | `#006DB7` | accent | Body copy links, inline hyperlinks within editorial text - vivid blue on white for maximum contrast. |
| Action Blue | `#005AD2` | accent | Secondary action buttons ('Become a member', 'Learn more'), interactive link emphasis - the outlined pill button border. |
| Flag Red | `#D0021B` | semantic | 'New' nav badge text - used sparingly to flag newness in navigation. |
| Off Black | `#141414` | neutral | Primary text, card titles, prices, icon fills - the dominant foreground color across all light surfaces. |

```css
:root {
  --colorful-lego-yellow: #FFD502;
  --colorful-brick-orange: #F47D20;
  --colorful-ember-dark: #E96F14;
  --colorful-lego-navy: #201D48;
  --colorful-link-blue: #006DB7;
  --colorful-action-blue: #005AD2;
  --colorful-flag-red: #D0021B;
}
```

## Typography direction
- Primary: **Cera Pro**; substitute `Nunito, Poppins`.
- Secondary/code: **Cera Pro Italic**; substitute `Nunito Italic`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
