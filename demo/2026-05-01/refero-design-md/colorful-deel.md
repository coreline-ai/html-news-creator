# Deel - Colorful Refero Design MD

- Source: https://styles.refero.design/style/5ec4eb4f-a37c-4787-b4c1-de49e01770e7
- Original site: https://deel.com
- Theme: `mixed`
- Color rank: **07**
- Colorfulness score: `44.8`
- Recommended fit: **Colorful SaaS accent system**

## North star
Global command split-screen - a war-room purple panel beside a neon product showcase, then warm cream scrolls below.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Cosmos | `#201547` | brand | Hero section background - the darkest brand surface, houses white headlines and violet accent text |
| Violet Mid | `#5938b7` | brand | CTA buttons in hero context, pill backgrounds - saturated mid-violet bridges cosmos and accent |
| Lavender Pulse | `#a98df6` | brand | Headline accent text ('anywhere.') in dark hero - vivid violet pops against #201547 |
| Pale Amethyst | `#c4b1f9` | brand | Soft violet surface tint, used as background on secondary dark panels |
| Indigo Shadow | `#381f89` | brand | Deep violet body text or decorative elements within dark sections |
| Electric Lime | `#ffcf25` | accent | Product screenshot accent, border highlights - the neon counterpoint to deep purple creating visual tension |
| Amber Core | `#faaf00` | accent | Icon fills and body-level accent color in light sections - warm, confident |
| Butter Glow | `#ffe27c` | accent | Light amber for icon strokes, decorative fills - softer version of Amber Core |

```css
:root {
  --colorful-deep-cosmos: #201547;
  --colorful-violet-mid: #5938b7;
  --colorful-lavender-pulse: #a98df6;
  --colorful-pale-amethyst: #c4b1f9;
  --colorful-indigo-shadow: #381f89;
  --colorful-electric-lime: #ffcf25;
  --colorful-amber-core: #faaf00;
}
```

## Typography direction
- Primary: **BagossCondensedFont**; substitute `system-ui`.
- Secondary/code: **BagossExtendedFont**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
