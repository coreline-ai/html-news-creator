# Leif Products - Refero Design MD

- Source: https://styles.refero.design/style/3f56ea4d-ed9d-4a36-8fb5-a801519ef80b
- Original site: https://leifproducts.com
- Theme: `light`
- Industry: `ecommerce`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black script on white canvas

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#fafaf9` | neutral | Page background or card surface |
| Pebble Gray | `#e5e2dc` | neutral | Page background or card surface |
| Alabaster | `#edede7` | neutral | Page background or card surface |
| Shadow Tone | `#595959` | neutral | Border, muted text, or supporting surface |
| Stone Line | `#d6d1c7` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ink: #000000;
  --ref-paper-white: #fafaf9;
  --ref-pebble-gray: #e5e2dc;
  --ref-alabaster: #edede7;
  --ref-shadow-tone: #595959;
  --ref-stone-line: #d6d1c7;
}
```

## Typography direction
- **Söhne**: 400, 500, 10px, 12px, 13px, 15px, 16px, 18px, 20px, 22px, 26px, 1.00, 1.15, 1.18, 1.22, 1.27, 1.33, 1.35, 1.38; substitute `Inter`.
- **Söhne Mono**: 400, 11px, 12px, 13px, 1.17, 1.18, 1.20, 1.23; substitute `Space Mono`.
- **PP Right Grotesk**: 200, 500, 34px, 52px, 75px, 1.00; substitute `Cabinet Grotesk`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `12px`
- Element Gap: `20px`
- Radius: `links: 6px, buttons: 6px, bodyElements: 3px`

## Surface cues
- **Paper White Canvas** `#fafaf9`: Dominant background for the entire application, providing a clean, bright foundation.

## Component cues
- **Ghost Navigation Link**: Primary navigation links and text-based buttons.
- **Primary Filled Button**: Call-to-action buttons for key interactions.
- **Outlined Text Button**: Secondary action buttons with a visual emphasis without filling.
- **Product Display Card**: Container for individual product listings.
- **Transparent Input Field**: Form input elements.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
