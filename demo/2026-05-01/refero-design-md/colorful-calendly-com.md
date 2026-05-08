# Calendly.com - Colorful Refero Design MD

- Source: https://styles.refero.design/style/9946887b-ffa9-4276-af81-ae6352795afb
- Original site: https://calendly.com
- Theme: `light`
- Color rank: **01**
- Colorfulness score: `50.3`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Sky Blueprint on Bright Paper - Clarity and precision conveyed through deep blues and crisp whites, like an architect's plan on a fresh sheet.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Indigo | `#0B3558` | brand | Primary text, prominent headings, inactive navigation items - provides a strong, authoritative anchor against the light. |
| Action Blue | `#006BFF` | brand | Primary call-to-action buttons, active navigation links, highlighted interactive elements - signifies interactivity and. |
| Lavender Glow | `#e55cff` | accent | Illustrative accents and background elements - adds an energetic, modern flair without competing with primary UI elemen. |
| Royal Amethyst | `#8247f5` | accent | Secondary accent for graphical elements and supporting links - provides visual diversity while maintaining a vibrant, m. |
| Sunset Gold | `#ffa600` | accent | Secondary accent for graphical elements and supporting links - offers warmth and contrast within the accent palette. |
| Skybound Blue | `#0099ff` | accent | Tertiary accent for graphical elements - contributes to the overall energetic and varied visual language. |
| Ocean Glimmer | `#BB32D5` | accent | Tertiary accent for graphical elements and supporting links - adds depth and variation to the accent tones. |
| Glacier Blue | `#004EBA` | semantic | Informational badges and alerts - a distinct blue hue for communicating status or details without being a primary CTA. |

```css
:root {
  --colorful-midnight-indigo: #0B3558;
  --colorful-action-blue: #006BFF;
  --colorful-lavender-glow: #e55cff;
  --colorful-royal-amethyst: #8247f5;
  --colorful-sunset-gold: #ffa600;
  --colorful-skybound-blue: #0099ff;
  --colorful-ocean-glimmer: #BB32D5;
}
```

## Typography direction
- Primary: **Gilroy**; substitute `Montserrat`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
