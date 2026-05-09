# Fonts In Use - Refero Design MD

- Source: https://styles.refero.design/style/348c83bc-bed3-4562-841a-26a30ee19a9b
- Original site: https://fontsinuse.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Typographic Archive on Vellum. A precise, ordered display of form and content, like a beautifully cataloged library of type specimens.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Inkwell | `#000000` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Mist | `#f0f0f0` | neutral | Page background or card surface |
| Pewter | `#dddddd` | neutral | Page background or card surface |
| Stone | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Ash | `#999999` | neutral | Border, muted text, or supporting surface |
| Granite | `#b3b3b3` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-inkwell: #000000;
  --ref-canvas: #ffffff;
  --ref-mist: #f0f0f0;
  --ref-pewter: #dddddd;
  --ref-stone: #cccccc;
  --ref-ash: #999999;
  --ref-granite: #b3b3b3;
}
```

## Typography direction
- **Benton Sans RE**: 400, 700, 9px, 10px, 12px, 14px, 16px, 1.10, 1.20, 1.60; substitute `Inter`.
- **Relay Cond**: 400, 700, 18px, 36px, 1.00, 1.60; substitute `Oswald`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `20px`
- Element Gap: `10px`
- Page Max Width: `1180px`
- Radius: `inputs: 2px, buttons: 2px`

## Component cues
- **Font Entry Cards Grid**: Reference component style.
- **Search Bar with Filter Controls**: Reference component style.
- **Sponsor Card**: Reference component style.
- **Primary Action Button**: Interactive element
- **Default Input Field**: User input

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
