# Samara - Colorful Refero Design MD

- Source: https://styles.refero.design/style/934a61aa-50ff-4e90-852b-4ad0b8262d54
- Original site: https://samara.com
- Theme: `light`
- Color rank: **35**
- Colorfulness score: `31.3`
- Recommended fit: **Color-coded data dashboard**

## North star
Sunlit architectural model. The design combines the precision of a blueprint with the warmth and airiness of natural light.

## Why this fits html-news-creator
Use for source health, cluster scores, confidence labels, and stateful admin screens that need clearer semantic color.

## Apply to
- Source ledger states
- Cluster/category badges
- Run status and alert panels

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Blue | `#0096f7` | brand | Primary CTAs, interactive links, iconography - a single point of vivid color signifying action. |
| Signal Orange | `#ff4000` | accent | Secondary high-visibility CTAs, often used in dark contexts for urgent calls to action. |
| Ink | `#000000` | neutral | Headlines, body text, UI labels. |
| Pure White | `#ffffff` | neutral | Text on dark or colored backgrounds, button text. |
| Parchment | `#fdfdf7` | neutral | Primary page background, giving a warm, tactile feel. |
| Warm Sand | `#f5f2de` | neutral | Card backgrounds. |
| Driftwood | `#e7e3e1` | neutral | Button surfaces for secondary or tertiary actions. |
| Ash | `#d3d3d3` | neutral | Decorative elements, disabled states. |

```css
:root {
  --colorful-sky-blue: #0096f7;
  --colorful-signal-orange: #ff4000;
  --colorful-ink: #000000;
  --colorful-pure-white: #ffffff;
  --colorful-parchment: #fdfdf7;
  --colorful-warm-sand: #f5f2de;
  --colorful-driftwood: #e7e3e1;
}
```

## Typography direction
- Primary: **regola**; substitute `Plus Jakarta Sans, Manrope`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
