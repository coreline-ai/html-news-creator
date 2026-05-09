# Quin - Refero Design MD

- Source: https://styles.refero.design/style/5dc8ca28-26fe-41f2-979a-cda2669c262a
- Original site: https://www.heyquin.io
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital parchment workflow

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#141414` | neutral | Primary text or dark surface |
| Paper White | `#fffcf2` | neutral | Page background or card surface |
| Greige Mist | `#d0cec6` | neutral | Border, muted text, or supporting surface |
| Aged Paper | `#f0ecdf` | neutral | Page background or card surface |
| Graphite | `#545454` | neutral | Border, muted text, or supporting surface |
| Warm Umber | `#68655b` | neutral | Border, muted text, or supporting surface |
| Deep Ash | `#222222` | neutral | Primary text or dark surface |
| Harvest Gold | `#f7cf49` | brand | Action accent / signal color |
| Muted Wood | `#492812` | brand | Action accent / signal color |
| Sky Blue | `#a9e1ff` | semantic | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #141414;
  --ref-paper-white: #fffcf2;
  --ref-greige-mist: #d0cec6;
  --ref-aged-paper: #f0ecdf;
  --ref-graphite: #545454;
  --ref-warm-umber: #68655b;
  --ref-deep-ash: #222222;
  --ref-harvest-gold: #f7cf49;
}
```

## Typography direction
- **Instrument Sans Variable**: 400, 500, 600, 14px, 16px, 20px, 26px, 28px, 32px, 40px, 44px, 56px, 80px, 96px, 0.75, 0.92, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.35, 1.50, 1.71; substitute `Inter Variable`.
- **Geist Mono**: 300, 400, 12px, 14px, 16px, 26px, 1.00, 1.10, 2.00; substitute `Space Mono`.
- **Font Awesome 7 Sharp**: 900, 26px, 40px, 1.

## Spacing / shape
- Section Gap: `59px`
- Card Padding: `24px`
- Element Gap: `24px`
- Radius: `cards: 0px, badges: 0px, inputs: 0px, buttons: 0px`

## Surface cues
- **Paper Canvas** `#fffcf2`: Dominant page background, providing a warm, off-white foundation.
- **Aged Paper Surface** `#f0ecdf`: Secondary background color for sections and subtle content groupings, adding visual texture.
- **Greige Card** `#d0cec6`: Background for basic cards and contained content sections, visually separating content from the canvas.
- **Midnight Ink Section** `#141414`: Distinct dark sections, providing strong visual contrast or a header/footer background.

## Component cues
- **Primary Filled Button**: Call-to-action button, dark filled
- **Secondary Ghost Button**: Outlined button, light background
- **Accent Tag Button**: Segmented control option / tag
- **Active Navigation Badge**: Active state indicator for navigation/filters
- **Information Badge**: Informational state indicator

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
