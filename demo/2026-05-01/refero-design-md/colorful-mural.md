# Mural - Colorful Refero Design MD

- Source: https://styles.refero.design/style/2b6642d9-fa66-4c06-9804-30f56e544a6d
- Original site: https://mural.co
- Theme: `mixed`
- Color rank: **44**
- Colorfulness score: `29.0`
- Recommended fit: **Colorful SaaS accent system**

## North star
Blackboard flipping to whiteboard - same hand, same authority, opposite ground.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Jade CTA | `#00c27a` | brand | Primary CTA buttons, active links, key interactive highlights - jade against black in the hero and against white in bod. |
| Mint Surface | `#b4f5c8` | brand | Card backgrounds, feature highlight areas - pastel counterpoint to jade that reads as 'selected' or 'active' without th. |
| Forest | `#00843f` | brand | Card accent backgrounds, deep green surface variant |
| Badge Leaf | `#d5f8e0` | brand | Blog/category badge backgrounds - near-white green tint that signals categorization without demanding attention |
| Badge Text | `#007b3b` | brand | Badge text and border on leaf background - dark enough on #d5f8e0 to pass contrast without going full black |
| Void | `#000000` | neutral | Hero background, primary text, button borders, icon fills - the dominant surface and text color simultaneously; this du. |
| Paper | `#ffffff` | neutral | Section backgrounds, card surfaces, nav background |
| Fog | `#f3f3f3` | neutral | Secondary button fill, subtle input backgrounds |

```css
:root {
  --colorful-jade-cta: #00c27a;
  --colorful-mint-surface: #b4f5c8;
  --colorful-forest: #00843f;
  --colorful-badge-leaf: #d5f8e0;
  --colorful-badge-text: #007b3b;
  --colorful-void: #000000;
  --colorful-paper: #ffffff;
}
```

## Typography direction
- Primary: **STK Bureau**; substitute `Barlow Condensed Light, or Helvetica Neue Light`.
- Secondary/code: **ABC Social**; substitute `Inter, DM Sans`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
