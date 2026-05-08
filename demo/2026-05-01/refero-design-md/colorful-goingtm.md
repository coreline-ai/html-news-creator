# GoingTM - Colorful Refero Design MD

- Source: https://styles.refero.design/style/3461e90e-35d2-4269-9f11-cbe935f0a3a2
- Original site: https://www.going.com
- Theme: `light`
- Color rank: **24**
- Colorfulness score: `39.0`
- Recommended fit: **Colorful SaaS accent system**

## North star
energetic journey on lime

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Lime | `#d7ffc2` | brand | Primary page background, card surfaces, and subtle button accents, evoking a fresh, energetic base |
| Teal Ink | `#004449` | brand | Primary text, navigation links, and outlined button borders - a deep, authoritative voice against the lighter backgroun. |
| Action Violet | `#483cff` | brand | Primary call-to-action buttons, prominent headlines - a vivid, saturated highlight signalling interaction and importance |
| Highlight Green | `#0bff80` | brand | Decorative color for some headlines and accents, adding a vibrant, almost neon touch |
| Pitch Black | `#000000` | neutral | Highly prominent text, borders, and general UI elements requiring maximum contrast |
| Paper White | `#fffef0` | neutral | Button backgrounds, form fields, and secondary text, offering a soft, almost off-white contrast |

```css
:root {
  --colorful-canvas-lime: #d7ffc2;
  --colorful-teal-ink: #004449;
  --colorful-action-violet: #483cff;
  --colorful-highlight-green: #0bff80;
  --colorful-pitch-black: #000000;
  --colorful-paper-white: #fffef0;
}
```

## Typography direction
- Primary: **PP Mori**; substitute `Inter`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
