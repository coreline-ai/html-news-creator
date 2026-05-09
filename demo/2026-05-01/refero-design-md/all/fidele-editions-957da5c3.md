# Fidèle Editions - Refero Design MD

- Source: https://styles.refero.design/style/957da5c3-7063-4992-9d25-e255752dc9b3
- Original site: https://fidele-editions.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Risographic print workshop: layers of paper and ink, tactile and vibrant.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Faded Paper | `#f8f7ef` | neutral | Page background or card surface |
| Printmaker Blue | `#1664eb` | brand | Action accent / signal color |
| Shop Grid Blue | `#4f89ec` | brand | Action accent / signal color |
| Ink Black | `#121212` | neutral | Primary text or dark surface |
| Dusty Gray | `#e2e2df` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Link Blue | `#006ce5` | accent | Action accent / signal color |

```css
:root {
  --ref-faded-paper: #f8f7ef;
  --ref-printmaker-blue: #1664eb;
  --ref-shop-grid-blue: #4f89ec;
  --ref-ink-black: #121212;
  --ref-dusty-gray: #e2e2df;
  --ref-pure-white: #ffffff;
  --ref-link-blue: #006ce5;
}
```

## Typography direction
- **BaselGrotesk Book**: 400, 14px, 16px, 20px, 22px, 24px, 26px, 28px, 32px, 37px, 38px, 41px, 62px, 0.92, 0.96, 1.00, 1.20, 1.30, 1.50, 1.80; substitute `Inter`.
- **BaselGrotesk Regular**: 400, 14px, 17px, 19px, 32px, 62px, 0.92, 1.00, 1.50; substitute `Inter`.
- **Arial**: 400, 13px, 1.20; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `42px`
- Card Padding: `19px`
- Element Gap: `5px`
- Radius: `default: 0px`

## Surface cues
- **Faded Paper** `#f8f7ef`: Base page background, input fields.
- **Dusty Gray** `#e2e2df`: Section dividers, subtle background distinction for content blocks.
- **Ink Black** `#121212`: Dark mode backgrounds where applicable, solid background buttons for contrast.

## Component cues
- **Outlined Brand Link**: Hypertext link or navigation item with an underline.
- **Ghost Command Button**: A utility button designed for low hierarchy actions or page navigation (e.g. 'Skip to content').
- **Filled Footer Button**: A solid background button for secondary actions usually against dark backgrounds (e.g. newsletter subscribe).
- **Product Input Field**: Input fields for forms (e.g. search, email).
- **Header Nav Link**: Primary navigation items in the header.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
