# Altason - Refero Design MD

- Source: https://styles.refero.design/style/e99ae628-89df-4de9-ab80-9885b1be4dc0
- Original site: https://atlason.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black & White Gallery

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#b0b0b0` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-ash-gray: #b0b0b0;
}
```

## Typography direction
- **haas-grotesk-tx-pro**: 400, 500, 16px, 18px, 36px, 0.90, 1.00, 1.20, 1.30; substitute `Inter`.
- **haas-grotesk-ds-pro**: 500, 48px, 106px, 230px, 288px, 0.77, 0.80, 1.00, 1.20; substitute `Inter Display`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `20px`
- Element Gap: `8px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and non-interactive content areas.
- **Product Card White** `#ffffff`: Background for product display cards, framed by borders, to separate contained content.
- **Overlay Black** `#000000`: Implicit dark surface for graphic elements or full-bleed imagery, creating strong contrast.

## Component cues
- **Navigation Link (Header)**: Primary navigation links in headers.
- **Product Thumbnail Card**: Displays product images with titles.
- **Contact Information Block**: Lists contact details and address.
- **Footer Section**: Contains navigation links and copyright information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
