# Dyotanya - Colorful Refero Design MD

- Source: https://styles.refero.design/style/1b13360a-cdca-4798-969d-57ebb20a3b30
- Original site: https://dyotanya.com/en
- Theme: `light`
- Color rank: **50**
- Colorfulness score: `26.3`
- Recommended fit: **Color-coded data dashboard**

## North star
Playful blueprint on textured paper.

## Why this fits html-news-creator
Use for source health, cluster scores, confidence labels, and stateful admin screens that need clearer semantic color.

## Apply to
- Source ledger states
- Cluster/category badges
- Run status and alert panels

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#f5f5f3` | neutral | Page backgrounds, card surfaces, secondary text background. This off-white ensures high contrast with text while provid. |
| Ink Black | `#000000` | neutral | Primary text, strong borders, icons. Used for maximum contrast and emphasis against light backgrounds |
| Deep Charcoal | `#333333` | neutral | Secondary text, input text, subtle borders, some interactive element backgrounds. Provides good readability without the. |
| Cloud White | `#ffffff` | neutral | Button text (especially on accent colors), some subtle element borders |
| Sky Blueprint | `#81aed9` | brand | Outline borders, button backgrounds, input borders, interactive states. This muted blue is the primary accent, providin. |
| Sunset Orange | `#ff8562` | accent | Link text, decorative accents. This vivid orange creates warmth and draws attention to clickable elements |
| Vivid Blue | `#55a1ea` | brand | Accent borders, occasional decorative elements. A more saturated blue than Sky Blueprint, used for subtle visual differ. |

```css
:root {
  --colorful-canvas-white: #f5f5f3;
  --colorful-ink-black: #000000;
  --colorful-deep-charcoal: #333333;
  --colorful-cloud-white: #ffffff;
  --colorful-sky-blueprint: #81aed9;
  --colorful-sunset-orange: #ff8562;
  --colorful-vivid-blue: #55a1ea;
}
```

## Typography direction
- Primary: **Simeiz**; substitute `Playfair Display`.
- Secondary/code: **Manrope**; substitute `Inter`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
