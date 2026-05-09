# Paragraph - Refero Design MD

- Source: https://styles.refero.design/style/37dd9612-4df0-4cdd-b942-bd97dd0efbd2
- Original site: https://mirror.xyz
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whisper-soft sepia canvas with quiet elevation.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#dbd5d2` | neutral | Border, muted text, or supporting surface |
| Inkwell | `#271f1b` | neutral | Primary text or dark surface |
| Snow | `#ffffff` | neutral | Page background or card surface |
| Silver Mist | `#ededed` | neutral | Page background or card surface |
| Stone Gray | `#888786` | neutral | Border, muted text, or supporting surface |
| Cloud Wash | `#f1f5fe` | neutral | Page background or card surface |
| Distant Sky | `#c9c7c6` | neutral | Border, muted text, or supporting surface |
| Shadow Blue | `#524c49` | neutral | Action accent / signal color |
| Action Azure | `#4a83f5` | brand | Action accent / signal color |
| Horizon Glow | `#b1cafb` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #dbd5d2;
  --ref-inkwell: #271f1b;
  --ref-snow: #ffffff;
  --ref-silver-mist: #ededed;
  --ref-stone-gray: #888786;
  --ref-cloud-wash: #f1f5fe;
  --ref-distant-sky: #c9c7c6;
  --ref-shadow-blue: #524c49;
}
```

## Typography direction
- **Google Sans Flex**: 400, 500, 600, 14px, 16px, 18px, 1.25, 1.43, 1.50, 1.56, 1.63; substitute `system-ui`.
- **IvyOra**: 400, 18px, 24px, 64px, 1.00, 1.33, 1.56; substitute `serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1400px`
- Radius: `cards: 28px, badges: 24px, images: 16px, buttons: 24px`

## Surface cues
- **Canvas** `#dbd5d2`: Base page background
- **Silver Mist** `#ededed`: Secondary card backgrounds, badge backgrounds
- **Snow** `#ffffff`: Primary card and elevated element backgrounds

## Component cues
- **Ghost Navigation Item**: Neutral, interactive navigation menu item.
- **Pill Button (Outlined)**: Secondary action button with rounded corners.
- **Feature Card (Primary)**: Content card for displaying articles or features.
- **Callout Card (Secondary)**: Highlight card with muted background.
- **Article Card (Minimal)**: Minimal container for article listings, using transparent background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
