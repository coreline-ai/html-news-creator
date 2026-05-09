# Campsite - Refero Design MD

- Source: https://styles.refero.design/style/e8589e7c-5ba9-4923-aa7f-0f1bf0d679be
- Original site: https://campsite.design
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Desktop OS window pane, minimalist and functional.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#171717` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Fog | `#f5f5f5` | neutral | Page background or card surface |
| Steel | `#a3a3a3` | neutral | Border, muted text, or supporting surface |
| Graystone | `#737373` | neutral | Border, muted text, or supporting surface |
| Ember | `#451a03` | brand | Action accent / signal color |
| Lagoon | `#3b82f6` | accent | Action accent / signal color |
| Warning Red | `#ef4444` | semantic | Action accent / signal color |
| Pale Yellow | `#fef3c7` | semantic | Action accent / signal color |

```css
:root {
  --ref-ink: #171717;
  --ref-canvas: #ffffff;
  --ref-fog: #f5f5f5;
  --ref-steel: #a3a3a3;
  --ref-graystone: #737373;
  --ref-ember: #451a03;
  --ref-lagoon: #3b82f6;
  --ref-warning-red: #ef4444;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 29px, 58px, 1.00, 1.20, 1.33, 1.40, 1.43, 1.50, 1.56, 1.63, 1.80; substitute `system-ui, sans-serif`.
- **ui-monospace**: 400, 600, 12px, 1.00; substitute `monospace`.

## Spacing / shape
- Section Gap: `72px`
- Element Gap: `4px`
- Radius: `cards: 8px, fields: 4px, modals: 12px, buttons: 9999px`

## Component cues
- **Announcement Banners**: Reference component style.
- **Post Feed Card**: Reference component style.
- **Testimonial Block**: Reference component style.
- **Primary Navigation Button (Text)**: Interactive element
- **Secondary Action Button (Filled)**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
