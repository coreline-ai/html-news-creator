# Klarna - Colorful Refero Design MD

- Source: https://styles.refero.design/style/49dba9e1-0d9d-4997-805a-bfea7525252d
- Original site: https://klarna.com
- Theme: `light`
- Color rank: **17**
- Colorfulness score: `40.7`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Friendly finance. A vibrant pink against deep violet, like a surprising bloom in a nighttime garden.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Plum | `#0b051d` | brand | Primary text, prominent page backgrounds (hero), interaction states for links and buttons. It creates a sense of depth. |
| Bubblegum Pop | `#ffa8cd` | brand | Call-to-action buttons, prominent accents, and brand elements. This color provides a high-contrast, energetic focal poi. |
| Candy Floss | `#ffd0e2` | brand | Subtle background accents, often used in smaller blocks or to hint at interactive states. A lighter, softer version of. |
| Amethyst | `#2c2242` | brand | The darkest of the card background colors, used for a soft, elevated look. |
| Lavender Mist | `#aa89f2` | brand | A vibrant card background, suggesting freshness and modernity. |
| Mint Leaf | `#e6ffa9` | brand | A bright, energetic card background, adding a touch of playfulness. |
| Off-White Canvas | `#f9f8f5` | neutral | Main page background, default card surfaces. Provides a soft, clean base for content. |
| Pure White | `#ffffff` | neutral | Navigation backgrounds, key content containers, elevated card surfaces. Offers crisp contrast and a sense of lightness. |

```css
:root {
  --colorful-midnight-plum: #0b051d;
  --colorful-bubblegum-pop: #ffa8cd;
  --colorful-candy-floss: #ffd0e2;
  --colorful-amethyst: #2c2242;
  --colorful-lavender-mist: #aa89f2;
  --colorful-mint-leaf: #e6ffa9;
  --colorful-off-white-canvas: #f9f8f5;
}
```

## Typography direction
- Primary: **Klarna Title**; substitute `Montserrat`.
- Secondary/code: **Klarna Text**; substitute `Open Sans`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
