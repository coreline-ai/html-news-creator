# Danilo Rodrigues - Refero Design MD

- Source: https://styles.refero.design/style/0d68dc70-15ec-494a-855d-fdb6a4e7c982
- Original site: https://danilorodrigues.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital minimalist

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Fog Gray | `#eaeaea` | neutral | Page background or card surface |
| Steel Gray | `#878787` | neutral | Border, muted text, or supporting surface |
| Carbon | `#1e1e1e` | neutral | Primary text or dark surface |
| Neon Green | `#00ff00` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-paper-white: #ffffff;
  --ref-fog-gray: #eaeaea;
  --ref-steel-gray: #878787;
  --ref-carbon: #1e1e1e;
  --ref-neon-green: #00ff00;
}
```

## Typography direction
- **Neue Haas Grotesk**: 400, 18px, 19px, 23px, 26px, 31px, 71px, 1.00, 1.10, 1.20, 1.30; substitute `Inter`.
- **Times**: 400, 13px, 1.20; substitute `Times New Roman`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `26px`
- Element Gap: `13px`
- Radius: `default: 0px, circular: 9999px`

## Component cues
- **Primary Heading**: Hero section large text
- **Body Text**: General paragraph text
- **Muted Subheading**: Secondary section titles or context
- **Navigation Link**: Top navigation menu items
- **Accent Circle**: Interactive visual element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
