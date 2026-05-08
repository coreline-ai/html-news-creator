# Flowmapp - Colorful Refero Design MD

- Source: https://styles.refero.design/style/caca412f-7fc7-4510-aacc-5664d4f8ce9f
- Original site: https://flowmapp.com
- Theme: `light`
- Color rank: **37**
- Colorfulness score: `30.0`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Architectural blueprint on white marble, accented with soft, glowing energy.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page backgrounds, card surfaces, primary button backgrounds. |
| Ink Black | `#000000` | neutral | Primary text, prominent icons, dark button backgrounds. |
| Steel Gray | `#8c9baa` | neutral | Secondary text, subtle borders, inactive elements. |
| Highlight Blue | `#0080ff` | brand | Call-to-action buttons, interactive elements, key iconography - signaling action and attention. |
| Subtle Blue | `#c5e0fb` | brand | Light background details, subtle button fills, card elements, supporting the primary blue without competing. |
| Gradient Violet | `#0050ff` | accent | Used as the border for cards, it provides a subtle visual lift and defines interactive sections with a touch of color. |
| Pebble Gray | `#dee0e4` | neutral | Subtle borders, dividers, and background accents. |
| Charcoal Text | `#222222` | neutral | Navigation text, less prominent black text for hierarchical distinction. |

```css
:root {
  --colorful-canvas-white: #ffffff;
  --colorful-ink-black: #000000;
  --colorful-steel-gray: #8c9baa;
  --colorful-highlight-blue: #0080ff;
  --colorful-subtle-blue: #c5e0fb;
  --colorful-gradient-violet: #0050ff;
  --colorful-pebble-gray: #dee0e4;
}
```

## Typography direction
- Primary: **Inter**; substitute `Inter`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
