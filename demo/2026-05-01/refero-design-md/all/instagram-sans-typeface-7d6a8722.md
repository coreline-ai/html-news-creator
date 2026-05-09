# Instagram Sans Typeface - Refero Design MD

- Source: https://styles.refero.design/style/7d6a8722-a6f4-40de-a761-16ea479630a9
- Original site: https://about.instagram.com/brand/type
- Theme: `light`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vibrant typographic canvas.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Fuchsia Burst | `#f689ff` | brand | Action accent / signal color |
| Violet Dream | `#385898` | brand | Action accent / signal color |
| Licorice Ink | `#1c1e21` | neutral | Primary text or dark surface |
| Achromatic Black | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Silver Whisper | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Gradient Sunset | `#ff0169` | brand | Action accent / signal color |

```css
:root {
  --ref-fuchsia-burst: #f689ff;
  --ref-violet-dream: #385898;
  --ref-licorice-ink: #1c1e21;
  --ref-achromatic-black: #000000;
  --ref-canvas-white: #ffffff;
  --ref-silver-whisper: #cccccc;
  --ref-gradient-sunset: #ff0169;
}
```

## Typography direction
- **Helvetica**: 400, 12px, 224px, 1.20, 1.34; substitute `Arial`.
- **Instagram Sans**: 400, 12px, 16px, 24px, 32px, 40px, 46px, 62px, 72px, 121px, 205px, 224px, 389px, 1.00, 1.05, 1.20, 1.34; substitute `Inter`.
- **Instagram Sans Headline**: 400, 468px, 1.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 16px, shapes: 36.3636px, default: 3px, elements: 3px`

## Component cues
- **Text Only Button (Ghost)**: Interactive element for navigation or secondary actions, appearing as plain text that darkens on hover.
- **Filled White Call to Action**: Primary action button, providing strong visual emphasis without heavy branding color.
- **Minimal Input Field**: Form input elements for collecting user data, designed to be unobtrusive.
- **Hero Headline**: Large, impactful text for hero sections, defining page presence.
- **Feature Card**: Container for showcasing key features or content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
