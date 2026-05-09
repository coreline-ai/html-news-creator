# V–A–C Sreda - Refero Design MD

- Source: https://styles.refero.design/style/b634cbce-b4db-44a6-b2a4-b58d9d2fe93d
- Original site: https://sreda.v-a-c.org
- Theme: `light`
- Industry: `media`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural grid on white

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Diagram Black | `#000000` | neutral | Primary text or dark surface |
| Muted Gray | `#999999` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-diagram-black: #000000;
  --ref-muted-gray: #999999;
}
```

## Typography direction
- **Diagramatika Display**: 400, 16px, 24px, 48px, 80px, 0.80, 1.20; substitute `Montserrat`.
- **Diagramatika Text**: 400, 16px, 20px, 24px, 0.90, 1.00, 1.10, 1.20; substitute `Open Sans`.
- **Arial**: 400, 13px, 20px, 1.20; substitute `system-ui`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `20px`
- Element Gap: `20px`
- Radius: `default: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background
- **Diagram Black** `#000000`: Cookie consent banner (transparent over background)

## Component cues
- **Navigation Link**: Primary navigation and content links
- **Headline Display Text**: Large, prominent text for section titles and branding.
- **Body Text Block**: Descriptive text for articles and content blocks.
- **Interactive Dotted Line**: Visual connectors and indicators for user interaction.
- **Ghost Button**: Subtle, outlined interactive elements.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
