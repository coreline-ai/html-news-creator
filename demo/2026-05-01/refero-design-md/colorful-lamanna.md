# Lamanna - Colorful Refero Design MD

- Source: https://styles.refero.design/style/057d7c66-76b7-4272-849c-4058543e6799
- Original site: https://lamannabakery.com
- Theme: `light`
- Color rank: **21**
- Colorfulness score: `39.6`
- Recommended fit: **Colorful SaaS accent system**

## North star
Electric Circus Diner: Bold, high-energy, and a little chaotic, like a retro diner bathed in neon.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Big Slice Orange | `#ff4100` | brand | Dominant background, headline accents, active outlines - this orange establishes the brand's energetic and playful tone. |
| Golden Crust Yellow | `#ffc700` | brand | Secondary accent, background for prominent elements, text color for high-contrast headlines against dark backgrounds; W. |
| Playful Pink | `#fdbeba` | brand | Section backgrounds, decorative elements - a softer, warmer background for content blocks |
| Navigation Blue | `#1573dd` | accent | Interactive elements, navigation links, outlined component borders - providing a clear contrast for actionable items |
| Ink Text | `#292a2c` | neutral | Primary body text, bold headings, various borders - a deep, near-black for maximum legibility on light and colored back. |
| Pure Black | `#000000` | neutral | Subtle borders, text on light backgrounds, decorative fills - used sparingly for sharp definition |

```css
:root {
  --colorful-big-slice-orange: #ff4100;
  --colorful-golden-crust-yellow: #ffc700;
  --colorful-playful-pink: #fdbeba;
  --colorful-navigation-blue: #1573dd;
  --colorful-ink-text: #292a2c;
  --colorful-pure-black: #000000;
}
```

## Typography direction
- Primary: **Open Sans**; substitute `system-ui`.
- Secondary/code: **rightgrotesk-spatialblack-webfont**; substitute `Bebas Neue`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
