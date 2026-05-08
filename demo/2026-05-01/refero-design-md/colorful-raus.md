# Raus - Colorful Refero Design MD

- Source: https://styles.refero.design/style/d28732de-1b7a-4d37-b7aa-edfa7caf428b
- Original site: https://www.raus.life
- Theme: `light`
- Color rank: **33**
- Colorfulness score: `32.2`
- Recommended fit: **Colorful SaaS accent system**

## North star
Warm rustic minimalism: soft natural tones meet crisp, understated typography.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#006434` | brand | Brand logo, primary text elements where emphasis is needed, subtle accents |
| Midnight Pine | `#23212c` | neutral | Primary text, deep gray backgrounds for secondary buttons and interactive elements, prominent borders |
| Vanilla Cream | `#ffffff` | neutral | Clean canvas for cards and UI elements, text on dark backgrounds, active indicator borders |
| Sunflower Gold | `#fcbd1c` | accent | Yellow wash for highlight backgrounds, decorative bands, and soft emphasis behind content. Do not promote it to the pri. |
| Sky Mist | `#a6dfff` | accent | Soft background for informational sections or subtle highlights, providing a cool contrast |
| Charred Orange | `#dd5000` | accent | Primary action button background, highlight text for important messages, icon fills - a vivid, earthy accent |

```css
:root {
  --colorful-forest-green: #006434;
  --colorful-midnight-pine: #23212c;
  --colorful-vanilla-cream: #ffffff;
  --colorful-sunflower-gold: #fcbd1c;
  --colorful-sky-mist: #a6dfff;
  --colorful-charred-orange: #dd5000;
}
```

## Typography direction
- Primary: **neue-haas-unica**; substitute `Helvetica Neue`.
- Secondary/code: **fonts**; substitute `PT Sans Caption`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
