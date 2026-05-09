# Magicbeans - Refero Design MD

- Source: https://styles.refero.design/style/5af8ba79-c73f-4388-8ea8-b805e24599f8
- Original site: https://magicbeans.app
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Notion-esque productivity canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghostly Gray | `#faf9f7` | neutral | Page background or card surface |
| Carbon Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#1a1a19` | neutral | Primary text or dark surface |
| Charcoal | `#333331` | neutral | Primary text or dark surface |
| Light Steel | `#e5e7eb` | neutral | Page background or card surface |
| Fog | `#f0f0f0` | neutral | Page background or card surface |
| Subtle Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Magic Orange | `#ff5310` | brand | Action accent / signal color |
| Magic Green | `#44c67f` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghostly-gray: #faf9f7;
  --ref-carbon-black: #000000;
  --ref-graphite: #1a1a19;
  --ref-charcoal: #333331;
  --ref-light-steel: #e5e7eb;
  --ref-fog: #f0f0f0;
  --ref-subtle-gray: #808080;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 13px, 14px, 15px, 16px, 17px, 24px, 40px, 64px, 0.90, 1.00, 1.18, 1.20, 1.33, 1.41, 1.43, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `8px`
- Radius: `cards: 12px, forms: 9999px, buttons: 9999px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default surface for elevated cards or clean UI sections.
- **Ghostly Gray** `#faf9f7`: Secondary background for sections or cards needing a subtle differentiation from the main canvas.

## Component cues
- **Primary Filled Button**: Main call-to-action button
- **Feature Card (Subtle Shadow)**: Container for showcasing features or information
- **Feature Card (Ghostly Background)**: Alternative container for features or as a secondary content block
- **Notificaton Banner**: Top-level communication for important updates
- **Notion-style Dashboard Card**: Internal UI component for displaying summarized data

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
