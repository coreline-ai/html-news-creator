# Wallpaper Projects - Refero Design MD

- Source: https://styles.refero.design/style/0a2bcda6-b5b9-463d-bc8d-2c7ccaa2b776
- Original site: https://wallpaperprojects.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Textured architectural canvas on fine paper.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Charcoal | `#1e1e1e` | neutral | Primary text or dark surface |
| Alabaster White | `#ffffff` | neutral | Page background or card surface |
| Cloud Cream | `#fbf9f3` | neutral | Page background or card surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-deep-charcoal: #1e1e1e;
  --ref-alabaster-white: #ffffff;
  --ref-cloud-cream: #fbf9f3;
  --ref-pure-black: #000000;
}
```

## Typography direction
- **Cardinal Fruit**: 400, 500, 36px, 48px, 132px, 180px, 1.00, 1.20, 1.24; substitute `Playfair Display`.
- **Soehne Breit Buch**: 400, 600, 10px, 12px, 14px, 72px, 80px, 1.00, 1.50; substitute `Inter`.
- **Soehne Mono Buch**: 400, 12px, 14px, 1.00, 1.24, 1.30, 1.50, 1.60; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `100px`
- Card Padding: `24px`
- Element Gap: `20px`
- Radius: `buttons: 20px`

## Surface cues
- **Alabaster White** `#ffffff`: Primary page background, base canvas.
- **Cloud Cream** `#fbf9f3`: Secondary background for content sections, subtle distinction from the base canvas.

## Component cues
- **Primary Filled Button - Dark**: Call to action.
- **Secondary Ghost Button - Dark**: Subtle interactive element.
- **Secondary Filled Button - Light**: Subtle call to action on dark backgrounds.
- **Text Input - Dark**: Form element.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
