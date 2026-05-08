# EVOKE - Colorful Refero Design MD

- Source: https://styles.refero.design/style/a69de146-6ff1-4ea8-b4a4-9d182ca2de31
- Original site: https://studioevoke.co.uk
- Theme: `light`
- Color rank: **48**
- Colorfulness score: `27.7`
- Recommended fit: **Colorful SaaS accent system**

## North star
Vibrant billboard clarity

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Dark borders and separators for elevated surfaces and inverted UI. Do not promote it to the primary CTA color |
| Canvas White | `#ffffff` | neutral | Content backgrounds, contrasting text against dark backgrounds. Serves as a neutral canvas or a high-contrast foreground |
| Rosy Flush | `#ff5a46` | brand | Dominant background color, often paired with black text for key sections |
| Sunbeam Yellow | `#ffe100` | brand | Background panels for featured content, providing a bright, energetic lift |
| Sky Cyan | `#00ffff` | brand | Accent background for visual sections, creating a cool, modern backdrop |
| Lavender Mist | `#ebebf5` | brand | Subtle background for panels, offering a softer alternative to the more vivid brand colors |

```css
:root {
  --colorful-midnight-ink: #000000;
  --colorful-canvas-white: #ffffff;
  --colorful-rosy-flush: #ff5a46;
  --colorful-sunbeam-yellow: #ffe100;
  --colorful-sky-cyan: #00ffff;
  --colorful-lavender-mist: #ebebf5;
}
```

## Typography direction
- Primary: **tt_norms_proextrablack**; substitute `Bebas Neue`.
- Secondary/code: **tt_norms_pronormal**; substitute `Inter`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
