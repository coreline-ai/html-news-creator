# Planhat - Refero Design MD

- Source: https://styles.refero.design/style/94c4fc51-4323-4f06-a4a4-27517e190445
- Original site: https://www.planhat.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp monochrome command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Twilight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Coal Text | `#121211` | neutral | Primary text or dark surface |
| Icon Gray | `#575551` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#958d7e` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-twilight-ink: #000000;
  --ref-canvas-white: #ffffff;
  --ref-coal-text: #121211;
  --ref-icon-gray: #575551;
  --ref-slate-border: #958d7e;
}
```

## Typography direction
- **Geigy LL Duplex Var Variable Reg**: 400, 18px, 24px, 32px, 48px, 60px, 113px, 1.00, 1.10, 1.20, 1.25, 1.40; substitute `Montserrat`.
- **Inter**: 400, 500, 10px, 12px, 14px, 16px, 1.00, 1.20, 1.40, 1.43, 1.50; substitute `Inter`.
- **sans-serif**: 400, 12px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `5px`
- Radius: `cards: 999px, links: 4px, images: 4px, inputs: 4px, buttons: 4px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Subtle Background** `#f6f6f8`: Background for input fields and subtle content containers
- **Twilight Ink** `#000000`: Dark contrast sections and overlays

## Component cues
- **Primary Outlined Button**: Call to action button for significant actions
- **Secondary Outlined Button**: Subtle call to action
- **Pill Card**: Decorative card for badges or small content blocks
- **Ghost Input Field**: Input element with minimal styling, typically for search or filter
- **Subtle Background Input**: Input field for data entry in a form

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
