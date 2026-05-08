# SquadEasy - Colorful Refero Design MD

- Source: https://styles.refero.design/style/3e5c272b-8d68-40d8-9726-b4d6914b4b16
- Original site: https://www.squadeasy.com
- Theme: `light`
- Color rank: **04**
- Colorfulness score: `47.8`
- Recommended fit: **Playful visual exploration**

## North star
Playful block playground

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Canvas | `#e1c19e` | brand | Primary page background for hero sections and expansive content zones, evoking a warm, inviting atmosphere |
| Deep Violet | `#adabff` | brand | Background for certain cards and content sections, adding depth and a distinct visual interruption to the warm canvas |
| Electric Lime | `#e4ff60` | accent | Primary action background, indicating interactivity with a high-energy pop, and used for decorative fills |
| Sky Blue | `#7fb6e6` | accent | Secondary button backgrounds and decorative elements, providing a cooler accent hue |
| Hot Pink | `#ea5da3` | accent | Highlight text, decorative fills, and border accents, drawing immediate attention to key phrases and elements |
| Forest Green | `#6fb853` | accent | Green accent for outlined action borders, linked labels, and lightweight interactive emphasis. Use as a supporting acce. |
| Absolute Black | `#000000` | neutral | Primary text, borders, and solid button fills, providing strong contrast against all backgrounds |
| Pure White | `#ffffff` | neutral | Secondary text, button text on dark backgrounds, and footer background, acting as a clean counterpoint |

```css
:root {
  --colorful-amber-canvas: #e1c19e;
  --colorful-deep-violet: #adabff;
  --colorful-electric-lime: #e4ff60;
  --colorful-sky-blue: #7fb6e6;
  --colorful-hot-pink: #ea5da3;
  --colorful-forest-green: #6fb853;
  --colorful-absolute-black: #000000;
}
```

## Typography direction
- Primary: **Body**; substitute `Inter`.
- Secondary/code: **Black**; substitute `Oswald`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
