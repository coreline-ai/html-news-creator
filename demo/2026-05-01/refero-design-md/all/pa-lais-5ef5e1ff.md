# Pa'lais - Refero Design MD

- Source: https://styles.refero.design/style/5ef5e1ff-3cb3-4383-9f66-26474409d9ae
- Original site: https://www.palais.bio
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
organic, hand-drawn vitality

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ghost Frost | `#fbf9f6` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Shadow Tint | `#d6d6d6` | neutral | Border, muted text, or supporting surface |
| Ocean Blue | `#234386` | brand | Action accent / signal color |
| Sunny Yellow | `#ffc400` | accent | Action accent / signal color |
| Lagoon Blue | `#6aa8dc` | accent | Action accent / signal color |
| Desert Ochre | `#d2b68c` | accent | Action accent / signal color |
| Harvest Orange | `#ed7328` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ghost-frost: #fbf9f6;
  --ref-midnight-ink: #000000;
  --ref-shadow-tint: #d6d6d6;
  --ref-ocean-blue: #234386;
  --ref-sunny-yellow: #ffc400;
  --ref-lagoon-blue: #6aa8dc;
  --ref-desert-ochre: #d2b68c;
}
```

## Typography direction
- **Times**: 400, 8px, 1.20; substitute `Serif`.
- **Delivery Note DEMO**: 400, 16px, 28px, 32px, 56px, 58px, 0.86, 0.90, 0.91, 1.14, 1.20; substitute `Montserrat`.
- **hwt-artz**: 400, 32px, 33px, 46px, 0.87, 1.00, 1.18, 1.20; substitute `Playfair Display SC`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `tags: 12px, cards: 8px, other: 16px, buttons: 32px`

## Component cues
- **Primary Filled Button**: Main call to action
- **Secondary Outlined Button**: Alternative call to action, less prominent actions
- **Neutral Outlined Button**: General informational or secondary navigations
- **Text Link Button**: Inline actions or navigational links without a background
- **Elevated Recipe Card**: Showcasing recipes or product features with a subtle lift

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
