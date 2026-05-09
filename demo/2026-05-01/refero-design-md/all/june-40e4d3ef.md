# June - Refero Design MD

- Source: https://styles.refero.design/style/40e4d3ef-cd28-483b-8c8a-b9cf44281b03
- Original site: https://www.june.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard with purple ink

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Cloud Gray | `#e9ecef` | neutral | Page background or card surface |
| Haze White | `#f0f0fe` | neutral | Page background or card surface |
| Inkwell Text | `#151531` | neutral | Primary text or dark surface |
| Midnight Violet | `#2a2a63` | neutral | Action accent / signal color |
| Shadow Blue-Gray | `#343a40` | neutral | Action accent / signal color |
| Purple Accent | `#6868f7` | accent | Action accent / signal color |
| Cloud Shadow | `#cfd0d1` | neutral | Border, muted text, or supporting surface |
| Soft Shadow | `#c3c4c6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-cloud-gray: #e9ecef;
  --ref-haze-white: #f0f0fe;
  --ref-inkwell-text: #151531;
  --ref-midnight-violet: #2a2a63;
  --ref-shadow-blue-gray: #343a40;
  --ref-purple-accent: #6868f7;
  --ref-cloud-shadow: #cfd0d1;
}
```

## Typography direction
- **SF Pro Rounded**: 400, 700, 900, 12px, 14px, 16px, 18px, 24px, 40px, 60px, 1.00, 1.17, 1.19, 1.25, 1.43, 1.50, 1.56; substitute `Avenir Next Rounded`.
- **Inter**: 400, 700, 16px, 1.00, 1.50; substitute `system-ui`.

## Spacing / shape
- Section Gap: `24-80px`
- Card Padding: `48px`
- Element Gap: `24px`
- Radius: `cards: 12px, prominentCard: 20px`

## Surface cues
- **Canvas White** `#fafafa`: Base page background
- **Haze White** `#f0f0fe`: Default slightly elevated card backgrounds
- **Purple Accent** `#6868f7`: Prominent accent cards

## Component cues
- **Navigation Link**: Global navigation item
- **Subtle Elevated Card**: Content container for secondary information
- **Default Content Card**: Primary content container within sections
- **Prominent Accent Card**: Highlighting key messages or calls to action
- **Signature Line Divider**: Used in the 'The June Team' section for visual separation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
