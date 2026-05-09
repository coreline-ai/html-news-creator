# Silencio - Refero Design MD

- Source: https://styles.refero.design/style/e67ac20e-6497-4756-b7e2-17859a794fb6
- Original site: https://silencio.es
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Archival Text on White. A single page from a carefully curated, minimalist document, demanding close attention.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Paper Gray | `#dbdad9` | neutral | Page background or card surface |
| Border Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Subtle Fade | `#dbdad9` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-paper-gray: #dbdad9;
  --ref-border-gray: #808080;
  --ref-subtle-fade: #dbdad9;
}
```

## Typography direction
- **HaasR**: 100, 400, 700, 12px, 16px, 19px, 22px, 39px, 58px, 0.90, 1.00, 1.10, 1.20, 1.40; substitute `Inter`.
- **HaasT**: 100, 400, 141px, 0.90, 1.20; substitute `Inter`.
- **PT Mono**: 400, 11px, 1.20; substitute `PT Mono`.

## Spacing / shape
- Card Padding: `29px`
- Element Gap: `6-14px`
- Radius: `large: 43.2px, buttons: 129.6px, default: 7.2px`

## Component cues
- **Ghost Button Group**: Reference component style.
- **Reference / Metadata Block**: Reference component style.
- **Content Section Heading with Caption**: Reference component style.
- **Ghost Button**: Primary Call to Action
- **Content Section Heading**: Secondary section titles

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
