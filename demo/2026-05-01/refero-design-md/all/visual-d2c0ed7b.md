# Visual - Refero Design MD

- Source: https://styles.refero.design/style/d2c0ed7b-c649-4d77-91de-1bd69dd10a9e
- Original site: https://designstripe.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial blueprint on parchment

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#f6f6f4` | neutral | Page background or card surface |
| Surface White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Ink | `#2c2c26` | neutral | Primary text or dark surface |
| Content Black | `#000000` | neutral | Primary text or dark surface |
| Muted Stone | `#d0d0c8` | neutral | Border, muted text, or supporting surface |
| Warm Gray | `#e8e7d9` | neutral | Page background or card surface |
| Icon Gray | `#aaab9c` | neutral | Border, muted text, or supporting surface |
| Border Khaki | `#57584b` | neutral | Border, muted text, or supporting surface |
| Accent Lime | `#fff347` | accent | Action accent / signal color |
| Muted Gold | `#aaa674` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #f6f6f4;
  --ref-surface-white: #ffffff;
  --ref-charcoal-ink: #2c2c26;
  --ref-content-black: #000000;
  --ref-muted-stone: #d0d0c8;
  --ref-warm-gray: #e8e7d9;
  --ref-icon-gray: #aaab9c;
  --ref-border-khaki: #57584b;
}
```

## Typography direction
- **fontSerif**: 300, 400, 24px, 32px, 48px, 64px, 96px, 0.94, 1.00, 1.13; substitute `Playfair Display`.
- **fontMono**: 300, 400, 500, 12px, 14px, 16px, 20px, 28px, 48px, 1.00, 1.33, 1.41, 1.50; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1200px`
- Radius: `cards: 8px, buttons: 9999px, navigation: 3px`

## Surface cues
- **Canvas Parchment** `#f6f6f4`: Primary page and main content area background.
- **Surface White** `#ffffff`: Used for content cards and specific blocks nested within the main canvas, adding a subtle layer distinction.
- **Charcoal Ink** `#2c2c26`: Used for footers and occasional rich content sections for strong contrast, acting as a background for inverse colors.

## Component cues
- **Primary Ghost Button**: Outlined action button
- **Filled Pill Button**: Secondary action button/Tag
- **Light Pill Button**: Neutral secondary button
- **Light Muted Pill Button**: Tertiary or ghost action button
- **Content Card**: Container for content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
