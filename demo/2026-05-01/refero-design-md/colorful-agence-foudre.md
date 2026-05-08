# Agence Foudre - Colorful Refero Design MD

- Source: https://styles.refero.design/style/c1534c74-f7b8-44de-a913-586d0f78fb08
- Original site: https://www.agencefoudre.com
- Theme: `light`
- Color rank: **20**
- Colorfulness score: `40.1`
- Recommended fit: **Playful visual exploration**

## North star
Vibrant Pink Playground - heavy type dances on a clean white stage, punctuated by electric color accents.

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pale Canvas | `#fff8f6` | neutral | Page backgrounds, body text in specific contexts, button text against strong colors. |
| Deep Forest | `#00522d` | brand | Primary text, interactive elements, button background in specific contexts - provides grounding contrast to the vibrant. |
| Foudre Pink | `#db3c8a` | brand | Key branding color for headlines, badges, and prominent interactive elements - injects energy and distinctiveness. It's. |
| Ash Whisper | `#fce5df` | neutral | Subtle background for badges and secondary text elements, a lighter pinkish-gray that softens areas without losing bran. |
| Bubblegum Blush | `#f29ebd` | accent | Softer background for buttons and decorative elements, maintaining the energetic pink theme but with less intensity. |
| Slate Tint | `#d1cfe4` | neutral | Rarely used for headings or secondary text, a cool gray providing a hint of contrast to the warm palette. |
| Midnight Ink | `#000000` | neutral | Used for utility text, icons, and some card elements - provides maximum contrast against lighter backgrounds. |

```css
:root {
  --colorful-pale-canvas: #fff8f6;
  --colorful-deep-forest: #00522d;
  --colorful-foudre-pink: #db3c8a;
  --colorful-ash-whisper: #fce5df;
  --colorful-bubblegum-blush: #f29ebd;
  --colorful-slate-tint: #d1cfe4;
  --colorful-midnight-ink: #000000;
}
```

## Typography direction
- Primary: **Clash Grotesk**; substitute `Inter`.
- Secondary/code: **Beni**; substitute `Bebas Neue`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
