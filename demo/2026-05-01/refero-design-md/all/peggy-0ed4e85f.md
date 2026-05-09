# Peggy - Refero Design MD

- Source: https://styles.refero.design/style/0ed4e85f-f3e9-438c-bc34-2a726863c602
- Original site: https://peggy.com/royalties
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Gallery Wall

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Fog | `#f4f4f4` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Deep Graphite | `#141414` | neutral | Primary text or dark surface |
| Muted Ash | `#e2e8f0` | neutral | Page background or card surface |
| Soft Stone | `#666666` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-fog: #f4f4f4;
  --ref-midnight-ink: #000000;
  --ref-white-canvas: #ffffff;
  --ref-deep-graphite: #141414;
  --ref-muted-ash: #e2e8f0;
  --ref-soft-stone: #666666;
}
```

## Typography direction
- **Inter**: 400, 500, 12px, 14px, 16px, 1.33, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Reckless**: 300, 400, 20px, 30px, 36px, 48px, 60px, 1.00, 1.11, 1.20, 1.40; substitute `Playfair Display, serif`.
- **Monument Grotesk**: 400, 12px, 1.33; substitute `Chivo, sans-serif`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1280px`
- Radius: `images: 9999px`

## Surface cues
- **Canvas Fog** `#f4f4f4`: Dominant page background, low-prominence background areas for sections and dividers.
- **White Canvas** `#ffffff`: Primary content surfaces like cards, modal backgrounds, and interactive element fills (e.g., light buttons).
- **Deep Graphite** `#141414`: Accent backgrounds for high-contrast elements such as specific buttons or banner notifications.

## Component cues
- **Primary Ghost Button**: Action button with a subtle outline, used for secondary actions or links where emphasis isn't on a filled background.
- **Filled Primary Button**: High-emphasis action button with a dark background, indicating primary actions like 'Join Peggy' or 'Download'.
- **Light Filled Button**: Action button with a light background for contexts requiring less visual weight, such as within dark backgrounds or for less critical actions.
- **Simple Card**: Used for informational display, feature lists, and content grouping. Emphasizes clean content presentation.
- **App Download Banner**: Prominent notification bar for app download. Uses stark black and white for clear call to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
