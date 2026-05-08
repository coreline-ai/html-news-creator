# Front - Colorful Refero Design MD

- Source: https://styles.refero.design/style/3281b445-805b-4dc7-933f-42b544a6d798
- Original site: https://front.com
- Theme: `dark`
- Color rank: **29**
- Colorfulness score: `33.6`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Deep Violet Command Center. An enterprise platform that feels personal and approachable through color and shape.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Violet | `#300c41` | brand | Major surface backgrounds, key branding elements. Its depth provides a canvas for lighter text and vibrant accents. |
| Accented Plum | `#5b1f76` | brand | Background for secondary elements and subtle brand accents. A richer, slightly more saturated version of the primary vi. |
| Primary White | `#ffffff` | neutral | Primary text color against dark backgrounds, button foregrounds, and key interactive elements. Provides strong contrast. |
| Warm Lemon | `#dee948` | accent | Primary call-to-action button background, active state indicators. Its vividness grabs attention against the deep viole. |
| Bright Lavender | `#e2dcf6` | neutral | Light text on dark backgrounds, secondary button backgrounds, and subtle highlight elements. A near-gray with a cool, v. |
| Rich Plum | `#0d1d39` | neutral | Primary text on light backgrounds, headers. A very dark, desaturated violet that reads as a sophisticated dark gray. |
| Soft Indigo | `#d0c6f0` | neutral | Text for secondary actions, subtle borders, and placeholder text. A muted violet that adds a touch of color to neutral. |
| Jet Black | `#1c1e20` | neutral | Dominant body text, subtle borders, and icons on light backgrounds. A highly prominent near-black for content. |

```css
:root {
  --colorful-deep-violet: #300c41;
  --colorful-accented-plum: #5b1f76;
  --colorful-primary-white: #ffffff;
  --colorful-warm-lemon: #dee948;
  --colorful-bright-lavender: #e2dcf6;
  --colorful-rich-plum: #0d1d39;
  --colorful-soft-indigo: #d0c6f0;
}
```

## Typography direction
- Primary: **Suisse Intl**; substitute `Inter`.
- Secondary/code: **Suisse Works**; substitute `IBM Plex Serif`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
