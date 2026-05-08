# Navigate - Colorful Refero Design MD

- Source: https://styles.refero.design/style/045e9f2b-91d3-44cc-bc99-1ce5f3fd4ed6
- Original site: https://nvg8.io
- Theme: `dark`
- Color rank: **25**
- Colorfulness score: `38.5`
- Recommended fit: **Colorful SaaS accent system**

## North star
Neon Playroom

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Abyss | `#141414` | neutral | Page background, primary text, prominent borders, and deep element fills - provides a high-contrast dark foundation |
| Ghost White | `#fdf9f0` | neutral | Secondary page and card backgrounds, body text on dark surfaces, border accents - offers a soft, warm contrast to Midni. |
| Lime Squeeze | `#c7ff69` | brand | Primary action buttons, active navigation elements, and interactive text links - creates a highly visible, energetic ca. |
| Amethyst Glow | `#7a78ff` | accent | Decorative card backgrounds, abstract graphics, and illustrative elements - adds a vibrant, playful accent hue |
| Sunset Orange | `#ff6d38` | accent | Illustrative fills, decorative backgrounds, and occasional icon strokes - provides warmth and visual interest |
| Emerald Sprint | `#00a652` | accent | Decorative card backgrounds and abstract graphics - delivers a fresh, natural accent |
| Skybound Blue | `#478bff` | accent | Illustrative elements and graphic fills - a cool, vivid complement to the warm accents |
| Golden Rod | `#ffc412` | accent | Illustrative elements and graphic fills - adds a touch of brightness and playful contrast |

```css
:root {
  --colorful-midnight-abyss: #141414;
  --colorful-ghost-white: #fdf9f0;
  --colorful-lime-squeeze: #c7ff69;
  --colorful-amethyst-glow: #7a78ff;
  --colorful-sunset-orange: #ff6d38;
  --colorful-emerald-sprint: #00a652;
  --colorful-skybound-blue: #478bff;
}
```

## Typography direction
- Primary: **Aeonik**; substitute `Inter`.
- Secondary/code: **OldschoolGrotesk**; substitute `Bebas Neue`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
