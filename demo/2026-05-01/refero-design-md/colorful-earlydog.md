# Earlydog - Colorful Refero Design MD

- Source: https://styles.refero.design/style/707a1648-eaef-4629-9c5a-b835cedde250
- Original site: https://www.earlydog.com
- Theme: `light`
- Color rank: **03**
- Colorfulness score: `49.5`
- Recommended fit: **Playful visual exploration**

## North star
Academic-chic abstract playground

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#fff9f0` | neutral | Page backgrounds, card surfaces, ghost button backgrounds, default text for dark surfaces |
| Midnight Ink | `#000609` | neutral | Primary text, headings, outlined button borders, filled button backgrounds, structural borders |
| Electric Blue | `#0a65db` | brand | Accent for selected headings, navigation highlights, footer backgrounds, and code snippets - creates a focal point agai. |
| Vivid Orange | `#ff6600` | accent | Illustrative accent color |
| Sunshine Yellow | `#f5c500` | accent | Illustrative accent color |
| Bubblegum Pink | `#f8b7d0` | accent | Illustrative accent color |

```css
:root {
  --colorful-canvas-parchment: #fff9f0;
  --colorful-midnight-ink: #000609;
  --colorful-electric-blue: #0a65db;
  --colorful-vivid-orange: #ff6600;
  --colorful-sunshine-yellow: #f5c500;
  --colorful-bubblegum-pink: #f8b7d0;
}
```

## Typography direction
- Primary: **usual**; substitute `system-ui`.
- Secondary/code: **degular-display**; substitute `Montserrat`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
