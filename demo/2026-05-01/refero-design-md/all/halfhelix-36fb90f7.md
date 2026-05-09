# Halfhelix - Refero Design MD

- Source: https://styles.refero.design/style/36fb90f7-3547-4dfd-a34e-592aa140078a
- Original site: https://www.halfhelix.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast monochrome, violet punctuation

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Lead | `#484a4c` | neutral | Border, muted text, or supporting surface |
| Fog | `#ededed` | neutral | Page background or card surface |
| Stone | `#808080` | neutral | Border, muted text, or supporting surface |
| Platinum | `#dbdbdb` | neutral | Page background or card surface |
| Charcoal | `#262626` | neutral | Primary text or dark surface |
| Steel | `#686c6d` | neutral | Border, muted text, or supporting surface |
| Silver | `#a5a7a8` | neutral | Border, muted text, or supporting surface |
| Violet Impulse | `#2749ff` | brand | Action accent / signal color |

```css
:root {
  --ref-ink: #000000;
  --ref-canvas: #ffffff;
  --ref-lead: #484a4c;
  --ref-fog: #ededed;
  --ref-stone: #808080;
  --ref-platinum: #dbdbdb;
  --ref-charcoal: #262626;
  --ref-steel: #686c6d;
}
```

## Typography direction
- **Suisse Intl**: 400, 12px, 13px, 14px, 16px, 18px, 24px, 32px, 40px, 48px, 1.00, 1.10, 1.20; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `15px`
- Element Gap: `5px`
- Radius: `default: 3px, circular: 1440px`

## Surface cues
- **Canvas** `#ffffff`: Base page background
- **Fog** `#ededed`: Secondary backgrounds, informational cards
- **Stone** `#808080`: Tertiary backgrounds, muted interactive elements
- **Ink Overlay** `#000000`: Hero background, footer background, overlay panels, interactive overlays

## Component cues
- **Primary Dark Button**: Call-to-action button for dark contexts.
- **Ghost Dark Button**: Secondary action button for dark contexts.
- **Neutral Light Button**: Default action button for light contexts.
- **Neutral Disabled Button**: Disabled or less prominent action button for light contexts.
- **Image Card**: Displaying project images or content teasers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
