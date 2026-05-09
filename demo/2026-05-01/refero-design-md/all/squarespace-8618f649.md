# Squarespace - Refero Design MD

- Source: https://styles.refero.design/style/8618f649-6d1c-45ca-aff8-e7f04928d8dd
- Original site: https://www.squarespace.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial White-glove Service

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#2f2f2f` | neutral | Primary text or dark surface |
| Silver Mist | `#898989` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#dddddd` | neutral | Page background or card surface |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-canvas-white: #ffffff;
  --ref-graphite: #2f2f2f;
  --ref-silver-mist: #898989;
  --ref-light-gray: #dddddd;
}
```

## Typography direction
- **Clarkson**: 300, 400, 500, 12px, 13px, 14px, 15px, 20px, 26px, 40px, 64px, 72px, 0.93, 1.00, 1.20, 1.40; substitute `Open Sans`.
- **Clarkson Serif**: 400, 26px, 1.00; substitute `Playfair Display`.
- **sans-serif**: 400, 16px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `12px`
- Radius: `cards: 8px, input: 8px, pills: 100px, buttons: 8px, default: 3px, largeButtons: 30px`

## Surface cues
- **Absolute Zero** `#000000`: Primary background for hero sections and full-width dark blocks, providing a dramatic, elegant canvas.
- **Canvas White** `#ffffff`: Dominant background for main content areas, providing a clean, bright stage for information.
- **Light Gray** `#dddddd`: Subtle background for alternating sections or very faint dividers, offering a slight visual break.

## Component cues
- **Primary Filled Button**: Main call-to-action button for initiating key user flows.
- **Ghost Button**: Subtle, secondary action button, often used in navigation or alongside a primary button.
- **Pill Button**: Decorative or categorized action, such as tags or filter buttons.
- **Dark Card**: Content container for featured sections against a light background.
- **Default Card**: Standard content container, visually distinct through a soft radius.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
