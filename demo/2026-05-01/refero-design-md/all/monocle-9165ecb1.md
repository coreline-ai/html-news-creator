# Monocle - Refero Design MD

- Source: https://styles.refero.design/style/9165ecb1-f068-4093-8783-1f3c98898b8a
- Original site: https://monocle.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ink-on-paper minimalist; a finely printed journal on pristine stock.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Printer's Black | `#000000` | neutral | Primary text or dark surface |
| Zinc Gray | `#d9d9d9` | neutral | Page background or card surface |
| Cloud Gray | `#e7e7e7` | neutral | Page background or card surface |
| Parchment Cream | `#fdfcf3` | neutral | Page background or card surface |
| Editorial Yellow | `#ffc500` | brand | Action accent / signal color |
| Sky Blue | `#64d5ff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-printer-s-black: #000000;
  --ref-zinc-gray: #d9d9d9;
  --ref-cloud-gray: #e7e7e7;
  --ref-parchment-cream: #fdfcf3;
  --ref-editorial-yellow: #ffc500;
  --ref-sky-blue: #64d5ff;
}
```

## Typography direction
- **Plantin**: 400, 700, 13px, 16px, 18px, 20px, 24px, 28px, 32px, 34px, 40px, 1.00, 1.13, 1.15, 1.20, 1.25, 1.30, 1.38, 1.44, 1.50; substitute `Georgia`.
- **Helvetica Neue**: 400, 700, 13px, 14px, 16px, 24px, 1.00, 1.13, 1.25, 1.29, 1.38, 1.50; substitute `Arial`.
- **Chanel**: 700, 9px, 1.00; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `4px`
- Page Max Width: `1296px`
- Radius: `cards: 8px, buttons: 0px, navBadges: 50%`

## Component cues
- **Monocle Radio Podcast Player Card**: Reference component style.
- **Article Feature Card with Category Label and Read Time**: Reference component style.
- **Podcast Episode Cards Grid**: Reference component style.
- **Primary Navigation Link**: Interactive element
- **Call-to-Action Button**: Primary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
