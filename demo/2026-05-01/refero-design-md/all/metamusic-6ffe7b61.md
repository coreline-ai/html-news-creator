# MetaMusic - Refero Design MD

- Source: https://styles.refero.design/style/6ffe7b61-a418-4cbd-9e7a-a5129db6c589
- Original site: https://metamusic.ca
- Theme: `light`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White Canvas, Blue Current

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0e2575` | brand | Action accent / signal color |
| Action Blue | `#0066cc` | brand | Action accent / signal color |
| Off-White Canvas | `#f4f1ea` | neutral | Page background or card surface |
| Snowdrift | `#ffffff` | neutral | Page background or card surface |
| Jet Black | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#101820` | neutral | Primary text or dark surface |
| Slate Blue | `#828aa8` | neutral | Action accent / signal color |
| Lavender Mist | `#e6e0f8` | neutral | Page background or card surface |
| Warm Beige | `#f7e1d5` | neutral | Page background or card surface |
| Silver Thread | `#d6d6d6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #0e2575;
  --ref-action-blue: #0066cc;
  --ref-off-white-canvas: #f4f1ea;
  --ref-snowdrift: #ffffff;
  --ref-jet-black: #000000;
  --ref-graphite: #101820;
  --ref-slate-blue: #828aa8;
  --ref-lavender-mist: #e6e0f8;
}
```

## Typography direction
- **Maison Neue**: 400, 500, 600, 12px, 14px, 16px, 19px, 22px, 26px, 32px, 40px, 56px, 80px, 120px, 0.95, 1.05, 1.10, 1.20, 1.35, 1.40, 1.50; substitute `Inter`.
- **Spoof**: 500, 22px, 0.90; substitute `Bebas Neue`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `40px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `body: 36px, links: 16px, badges: 9999px, inputs: 8px, buttons: 9999px, default: 24px`

## Surface cues
- **Off-White Canvas** `#f4f1ea`: Base page background for light sections, providing an open, warm, and default surface for content.
- **Snowdrift** `#ffffff`: Primary surface for cards, modal dialogs, and sections requiring crisp, clean presentation against the Canvas background.
- **Sky Tint** `#e9f4ff`: Subtle elevated surface for specific interactive elements or cards, offering a barely-there blue tint that implies a slight lift.
- **Midnight Ink** `#0e2575`: Dominant background for full-bleed dark sections, providing strong visual contrast and emphasizing featured content.

## Component cues
- **Pill Button**: Standard interactive button, typically for secondary actions.
- **Primary Action Block**: Prominent interactive block for primary calls to action.
- **Tertiary Card**: Informational cards or feature blocks with a substantial background color.
- **Feature Icon Circle**: Decorative circular background for icons within feature sections.
- **Standard Content Card**: General purpose content card for displaying information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
