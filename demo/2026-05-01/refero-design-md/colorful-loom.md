# Loom - Colorful Refero Design MD

- Source: https://styles.refero.design/style/bc2c6ecc-7a0d-4693-86e5-9fa93b165601
- Original site: https://loom.com
- Theme: `light`
- Color rank: **14**
- Colorfulness score: `41.2`
- Recommended fit: **Colorful SaaS accent system**

## North star
Vibrant blue precision on a soft canvas.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Loom Blue | `#1868db` | brand | Primary brand color, used for prominent call-to-action buttons, active navigation states, and key interactive elements.. |
| Deep Sea Blue | `#123263` | brand | Background for accent cards and sections, providing a rich, darker counterpoint to the primary Loom Blue. |
| Bright Blue | `#1558bc` | brand | Accent shade of blue, used for subtle background elements and less prominent interactive details. |
| Violet Berry | `#48245d` | brand | Used for distinctive, moderate contrast backgrounds on specific cards, hinting at a secondary brand accent. |
| Lavender Mist | `#eed7fc` | accent | Light, muted violet background tint, used for subtle visual separation of content blocks or as a cheerful accent. |
| Spring Bud | `#efffd6` | accent | Light, muted green background tint, often for informational or success-oriented card sections. |
| Vivid Green | `#82b536` | semantic | Used for specific highlights or as a semantic positive indicator, highly saturated. |
| Sunset Orange | `#ff613d` | accent | High-visibility accent, used for 'Record' indicators or urgent calls to attention, signaling activity. |

```css
:root {
  --colorful-loom-blue: #1868db;
  --colorful-deep-sea-blue: #123263;
  --colorful-bright-blue: #1558bc;
  --colorful-violet-berry: #48245d;
  --colorful-lavender-mist: #eed7fc;
  --colorful-spring-bud: #efffd6;
  --colorful-vivid-green: #82b536;
}
```

## Typography direction
- Primary: **Charlie Text**; substitute `Inter`.
- Secondary/code: **Charlie Display**; substitute `Inter`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
