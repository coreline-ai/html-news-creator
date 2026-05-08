# Voiceflow - Colorful Refero Design MD

- Source: https://styles.refero.design/style/03b3d707-2a30-4f53-a524-347d1b70eb2c
- Original site: https://www.voiceflow.com
- Theme: `light`
- Color rank: **28**
- Colorfulness score: `34.6`
- Recommended fit: **Color-coded data dashboard**

## North star
AI Blueprint on White Canvas

## Why this fits html-news-creator
Use for source health, cluster scores, confidence labels, and stateful admin screens that need clearer semantic color.

## Apply to
- Source ledger states
- Cluster/category badges
- Run status and alert panels

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Skybound Blue | `#397dff` | brand | Primary Call-to-Action buttons and interactive elements, representing activation and core functionality |
| Amber Pop | `#f55c15` | accent | Accent for badges, status indicators, and subtle highlights - a burst of energy to draw attention to key information |
| Impact Red | `#ff0000` | accent | Red outline accent for tags, dividers, and focused UI edges. Use as a supporting accent, not as a status color |
| Ultramarine | `#1956f3` | accent | A deeper, more saturated blue used sparingly for large background fills, providing a dramatic accent |
| Inkwell | `#171717` | neutral | Primary heading text and critical information, providing strong contrast on light backgrounds |
| Deep Graphite | `#262626` | neutral | Secondary text, dark backgrounds for subtle distinctions, and focused elements like secondary buttons |
| Anchor Gray | `#333333` | neutral | Muted text, borders, and dividers where a softer presence is desired than Deep Graphite |
| Slate Text | `#525252` | neutral | Body copy and standard informational text, ensuring readability without being overly stark |

```css
:root {
  --colorful-skybound-blue: #397dff;
  --colorful-amber-pop: #f55c15;
  --colorful-impact-red: #ff0000;
  --colorful-ultramarine: #1956f3;
  --colorful-inkwell: #171717;
  --colorful-deep-graphite: #262626;
  --colorful-anchor-gray: #333333;
}
```

## Typography direction
- Primary: **Tiempos Headline**; substitute `Playfair Display`.
- Secondary/code: **Selecta**; substitute `Inter`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
