# Bōjka Studio - Refero Design MD

- Source: https://styles.refero.design/style/286b6ba8-a45d-48e0-b556-ff6aeac68058
- Original site: https://bojka.studio
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon Green Canvas, Bold Black Type

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Neon Green | `#0af500` | brand | Action accent / signal color |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Dark Charcoal | `#282828` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Sunset Orange | `#ff4600` | accent | Action accent / signal color |

```css
:root {
  --ref-neon-green: #0af500;
  --ref-ink-black: #000000;
  --ref-dark-charcoal: #282828;
  --ref-canvas-white: #ffffff;
  --ref-sunset-orange: #ff4600;
}
```

## Typography direction
- **custom_15364**: 400, 22px, 44px, 157px, 1.00, 1.09, 2.73; substitute `Archivo Black`.
- **-apple-system**: 400, 16px, 1.00; substitute `Inter`.
- **Roboto**: 400, 18px, 1.44; substitute `Inter`.

## Spacing / shape
- Card Padding: `0px`
- Element Gap: `16px`
- Radius: `cards: 68px, buttons: 68px, default: 20px`

## Surface cues
- **Page Canvas** `#0af500`: Dominant background for interactive sections and hero areas, defining the primary brand color.
- **Content Surface (White)** `#ffffff`: Secondary background for navigation and some content cards, providing a stark neutral contrast.
- **Content Surface (Black)** `#000000`: Background for feature cards and elevated content blocks, creating depth and a strong visual anchor.

## Component cues
- **Hero Headline Block**: Primary attention-grabber on the landing page.
- **Navigation Link**: Interactive navigation elements in footers and headers.
- **Dark Card**: Container for content sections, often displaying project previews.
- **White Card**: Alternative content container, offering visual break.
- **Body Text Block**: Standard textual content for descriptions and paragraphs.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
