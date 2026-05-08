# Playdate - Colorful Refero Design MD

- Source: https://styles.refero.design/style/2175034b-96d7-417e-886f-ff5a4d8551ae
- Original site: https://play.date
- Theme: `mixed`
- Color rank: **36**
- Colorfulness score: `30.1`
- Recommended fit: **Playful visual exploration**

## North star
Lemon Drop Arcade. Bright, blocky, and instantly recognizable, like a classic handheld console that makes a statement.

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Playdate Yellow | `#ffc500` | brand | Primary brand color, highlights, accents, and section backgrounds - a distinctively vivid and playful yellow that defin. |
| Crank Violet | `#7700ff` | brand | Key interactive elements like CTA buttons and active navigation links - a vivid violet provides a playful yet authorita. |
| Seafoam Teal | `#21c6a9` | accent | An additional accent color, used sparingly, possibly for status indicators or secondary highlights. |
| Deep Teal | `#127866` | accent | Darker variant of Seafoam Teal, likely for subtle accents or text on lighter backgrounds. |
| Charcoal Text | `#312f27` | neutral | Primary text color and darker element backgrounds - a very dark, slightly desaturated near-black that grounds the vibra. |
| Pure White | `#ffffff` | neutral | Backgrounds, inverse text, and contrast elements - providing stark contrast to Charcoal Text and Playdate Yellow. |
| Midnight Absolute | `#000000` | neutral | Shadows, outlines, and occasionally bold text - its pure black presence adds weight and definition. |
| Default Gray | `#788086` | neutral | Subtle background tones or secondary text. |

```css
:root {
  --colorful-playdate-yellow: #ffc500;
  --colorful-crank-violet: #7700ff;
  --colorful-seafoam-teal: #21c6a9;
  --colorful-deep-teal: #127866;
  --colorful-charcoal-text: #312f27;
  --colorful-pure-white: #ffffff;
  --colorful-midnight-absolute: #000000;
}
```

## Typography direction
- Primary: **Roobert**; substitute `system-ui, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
