# Websmith Studio - Refero Design MD

- Source: https://styles.refero.design/style/11cfc460-807b-42c5-b10a-7b042c60f3e8
- Original site: https://websmith.studio
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Artisanal precision on a calm canvas: a meticulously crafted UI using refined typography and a neutral palette, where subtle interactions and product imagery take center stage.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas | `#f8f8f2` | neutral | Page background or card surface |
| Fog | `#ffffff` | neutral | Page background or card surface |
| Deep Space | `#000000` | neutral | Primary text or dark surface |
| Mint | `#a4f4cf` | accent | Action accent / signal color |
| Sky Tint | `#bedbff` | accent | Action accent / signal color |
| Blush | `#ffc9c9` | accent | Action accent / signal color |
| Online Green | `#00c950` | accent | Action accent / signal color |

```css
:root {
  --ref-ink: #1a1a1a;
  --ref-canvas: #f8f8f2;
  --ref-fog: #ffffff;
  --ref-deep-space: #000000;
  --ref-mint: #a4f4cf;
  --ref-sky-tint: #bedbff;
  --ref-blush: #ffc9c9;
  --ref-online-green: #00c950;
}
```

## Typography direction
- **-apple-system**: 400, 500, 600, 700, 14px, 16px, 20px, 30px, 48px, 88px, 96px, 1.00, 1.20, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `64-96px`
- Card Padding: `32px`
- Element Gap: `16px`
- Page Max Width: `1340px`
- Radius: `cards: 12px, images: 12px, buttons: 8px, elements: 24px`

## Surface cues
- **Canvas** `#f8f8f2`: Primary page background, setting a warm, desaturated base.
- **Fog** `#ffffff`: Elevated card backgrounds, providing a crisper surface for contained content.

## Component cues
- **Primary Filled Button**: Main call-to-action button for initiating key actions
- **Content Card - Default**: Container for product showcases, case studies, and informational blocks
- **Content Card - Mint Accent**: Alternative content card for visual variation or thematic grouping
- **Content Card - Sky Accent**: Alternative content card for visual variation or thematic grouping
- **Content Card - Blush Accent**: Alternative content card for visual variation or thematic grouping

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
