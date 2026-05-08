# Dopper - Colorful Refero Design MD

- Source: https://styles.refero.design/style/734ab03c-a326-43e3-a463-c5f90247404f
- Original site: https://dopper.com
- Theme: `light`
- Color rank: **26**
- Colorfulness score: `35.2`
- Recommended fit: **Colorful SaaS accent system**

## North star
Playful Marine Minimalism - like sunshine bouncing off clear blue water.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pale Sand | `#f6ecc8` | neutral | Major background areas, accent panels on cards, giving a warm and inviting base. |
| Ocean Deep | `#000f2` | brand | Primary text, headings, and key structural elements. Its depth anchors the brighter palette. |
| True Black | `#000000` | neutral | Headings, body text, and icons; provides maximum contrast and legibility against light backgrounds. |
| Sky Blue | `#0067e5` | accent | Primary call-to-action buttons, interactive elements, and illustrations; conveys trust and freshness. |
| Teal Splash | `#116973` | brand | Accent background on specific product cards; adds a cool, sophisticated touch. |
| Sea Mist | `#8ab1e6` | brand | Accent background on specific product cards; a lighter, softer blue that complements `Sky Blue`. |
| Sunbeam Yellow | `#fed200` | brand | Accent background on specific product cards, drawing attention with its vivid warmth. |
| Slate Gray | `#515a8a` | neutral | Secondary text and subtle interactive states, providing hierarchy without stark contrast. |

```css
:root {
  --colorful-pale-sand: #f6ecc8;
  --colorful-ocean-deep: #000f2;
  --colorful-true-black: #000000;
  --colorful-sky-blue: #0067e5;
  --colorful-teal-splash: #116973;
  --colorful-sea-mist: #8ab1e6;
  --colorful-sunbeam-yellow: #fed200;
}
```

## Typography direction
- Primary: **Gilroy**; substitute `system-ui (e.g., Arial, Helvetica)`.
- Secondary/code: **Dopper**; substitute `Poppins, Montserrat`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
