# Duolingo - Colorful Refero Design MD

- Source: https://styles.refero.design/style/7088d695-362b-4e09-b325-fa8136d4f350
- Original site: https://duolingo.com
- Theme: `light`
- Color rank: **05**
- Colorfulness score: `47.0`
- Recommended fit: **Playful visual exploration**

## North star
Playground Starter Kit

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Duo Green | `#58cc02` | brand | Primary CTAs, logos, headlines, interactive highlights - the brand's key signifier of action and identity. |
| Sky Blue | `#1cb0f6` | accent | Secondary outline buttons, inline text links - provides a clear, alternative interactive cue. |
| Duo Green Light | `#d7ffb8` | brand | Background tints for highlighted or active states, often paired with Duo Green. |
| Sunshine Yellow | `#ffc700` | accent | Used exclusively within illustrations for pops of warmth and energy. |
| Grape Soda | `#a570ff` | accent | Used exclusively within illustrations as a cool, playful accent. |
| Bubblegum Pink | `#cc348d` | accent | Used exclusively within illustrations for vibrant, friendly details. |
| Snow White | `#ffffff` | neutral | Page backgrounds, button text, card surfaces. |
| Cloud Gray | `#e5e5e5` | neutral | Borders for secondary buttons and dividers. |

```css
:root {
  --colorful-duo-green: #58cc02;
  --colorful-sky-blue: #1cb0f6;
  --colorful-duo-green-light: #d7ffb8;
  --colorful-sunshine-yellow: #ffc700;
  --colorful-grape-soda: #a570ff;
  --colorful-bubblegum-pink: #cc348d;
  --colorful-snow-white: #ffffff;
}
```

## Typography direction
- Primary: **feather**; substitute `Fredoka One, Baloo 2`.
- Secondary/code: **din-round**; substitute `Nunito Sans, Varela Round`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
