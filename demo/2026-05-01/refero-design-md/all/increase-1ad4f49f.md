# Increase - Refero Design MD

- Source: https://styles.refero.design/style/1ad4f49f-275a-4268-8ed1-677dc3c6e475
- Original site: https://increase.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Angular neon blueprint

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1a2b3b` | brand | Action accent / signal color |
| Storm Gray | `#314352` | neutral | Border, muted text, or supporting surface |
| Oceanic Deep | `#0d1726` | brand | Action accent / signal color |
| Stone Whisper | `#8995a1` | neutral | Border, muted text, or supporting surface |
| Smoke Light | `#687887` | neutral | Border, muted text, or supporting surface |
| Electric Lime | `#e4ff33` | accent | Action accent / signal color |
| Aqua Glow | `#31f2bf` | accent | Action accent / signal color |
| Cloud Canvas | `#edf0f2` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #1a2b3b;
  --ref-storm-gray: #314352;
  --ref-oceanic-deep: #0d1726;
  --ref-stone-whisper: #8995a1;
  --ref-smoke-light: #687887;
  --ref-electric-lime: #e4ff33;
  --ref-aqua-glow: #31f2bf;
  --ref-cloud-canvas: #edf0f2;
}
```

## Typography direction
- **Untitled Sans**: 400, 500, 700, 14px, 16px, 20px, 24px, 32px, 40px, 90px, 1.00, 1.10, 1.13, 1.17, 1.40, 1.43, 1.50; substitute `system-ui, sans-serif`.
- **Input Mono**: 400, 10px, 13px, 14px, 20px, 1.43, 1.50, 1.54, 1.60; substitute `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `tags: 4px, cards: 12px, pills: 999px, buttons: 8px`

## Surface cues
- **Cloud Canvas** `#edf0f2`: Primary page background, base layer.
- **Polar White** `#ffffff`: Default card backgrounds, content blocks, secondary surface.
- **Pale Stone** `#e1e5e9`: Subtly elevated card backgrounds, distinct yet light content areas.
- **Midnight Ink** `#1a2b3b`: Dark card backgrounds, prominent UI elements requiring high contrast.
- **Oceanic Deep** `#0d1726`: Accentuated dark panels, code editor backgrounds, for visual separation.

## Component cues
- **Primary Filled Button**: Main call-to-action button for sign-ups and key actions.
- **Ghost Sales Button**: Secondary call-to-action for sales inquiries, subtly presented.
- **Secondary Outlined Button**: Alternative action button, visually distinct but less prominent than primary.
- **Icon Link Button**: Text link style button, used for navigation or supplementary actions.
- **Hero Code Card**: Displays technical code examples against a dark background.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
