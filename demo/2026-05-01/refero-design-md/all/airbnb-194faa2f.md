# Airbnb - Refero Design MD

- Source: https://styles.refero.design/style/194faa2f-2f69-4bbf-9e29-290f28fa8ca2
- Original site: https://airbnb.org
- Theme: `light`
- Industry: `other`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast editorial canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon Black | `#222222` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Faint Gray | `#f7f7f7` | neutral | Page background or card surface |
| Storm Gray | `#6a6a6a` | neutral | Border, muted text, or supporting surface |
| Pale Drift | `#ebebeb` | neutral | Page background or card surface |
| Dust Bunny | `#a6a6a6` | neutral | Border, muted text, or supporting surface |
| Soft Divider | `#dddddd` | neutral | Page background or card surface |

```css
:root {
  --ref-carbon-black: #222222;
  --ref-canvas-white: #ffffff;
  --ref-faint-gray: #f7f7f7;
  --ref-storm-gray: #6a6a6a;
  --ref-pale-drift: #ebebeb;
  --ref-dust-bunny: #a6a6a6;
  --ref-soft-divider: #dddddd;
}
```

## Typography direction
- **Airbnb Cereal VF**: 400, 500, 700, 14px, 16px, 18px, 22px, 26px, 48px, 52px, 72px, 1.13, 1.14, 1.15, 1.18, 1.19, 1.20, 1.25, 1.27, 1.29, 1.33, 1.43, 1.56; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `48-64px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `links: 4px, buttons: 8px, default: 12px`

## Component cues
- **Primary Action Button**: Main call to action, drawing immediate attention.
- **Video Player Control Button**: Overlay controls for embedded video content.
- **Ghost Header Button**: Secondary actions in the header navigation.
- **Content Card**: Container for distinct blocks of information or media.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
