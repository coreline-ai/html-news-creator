# GRAZA - Colorful Refero Design MD

- Source: https://styles.refero.design/style/f2a84e0f-cf77-41fa-ade0-b062a3a42495
- Original site: https://graza.co
- Theme: `light`
- Color rank: **15**
- Colorfulness score: `41.2`
- Recommended fit: **Colorful SaaS accent system**

## North star
Artisanal provisions on a sunny countertop. The distinct 'GT Alpina Typewriter' font paired with the classic 'ITC Garamond Condensed' creates a blend of retro-modern warmth against a palette of creamy whites and food-in.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Buttermilk | `#fff4ec` | neutral | Page backgrounds, card surfaces, primary text color on dark accents - foundational creamy base that feels warmer than p. |
| Farmhouse Gray | `#f6e6d9` | neutral | Secondary background, subtle dividers - a slightly deeper, warmer neutral that adds depth without stark contrast, like. |
| Grove Green | `#3c422` | brand | Primary text, interactive elements, borders, icons - the dominant dark anchor, a sophisticated, desaturated green that. |
| Zest Yellow | `#d1e030` | accent | Primary call-to-action buttons, active states, highlights - a vibrant, natural yellow that injects energy and directs a. |
| Avocado Cream | `#9eef80` | accent | Secondary accent color, background for playful sections - a lighter, softer green that complements the Zest Yellow and. |
| Sunbeam Yellow | `#fbd535` | accent | Tertiary accent, often used for background blocks - a warm, sunny yellow for more emphatic accent sections, used sparin. |
| Harvest Ochre | `#e8d6c8` | neutral | Subtle shading in backgrounds, decorative elements - a warm, faint brown used for subtle visual texture or background v. |

```css
:root {
  --colorful-buttermilk: #fff4ec;
  --colorful-farmhouse-gray: #f6e6d9;
  --colorful-grove-green: #3c422;
  --colorful-zest-yellow: #d1e030;
  --colorful-avocado-cream: #9eef80;
  --colorful-sunbeam-yellow: #fbd535;
  --colorful-harvest-ochre: #e8d6c8;
}
```

## Typography direction
- Primary: **ITC Garamond Condensed**; substitute `Garamond (or similar humanist serif with condensed variant)`.
- Secondary/code: **GT Alpina Typewriter**; substitute `Roboto Mono, Space Mono (for a strong typewriter feel)`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
