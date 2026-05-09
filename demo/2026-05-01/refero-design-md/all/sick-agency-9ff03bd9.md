# SICK AGENCY - Refero Design MD

- Source: https://styles.refero.design/style/9ff03bd9-2ce0-474c-8c73-1905dbacc23b
- Original site: https://sick.agency
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon Pop Art poster

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Fiery Orange | `#ff4e27` | brand | Action accent / signal color |
| Electric Yellow | `#ffc700` | brand | Action accent / signal color |
| Shocking Blue | `#0029ff` | brand | Action accent / signal color |
| Deep Crimson | `#4d170c` | neutral | Primary text or dark surface |
| Abyss | `#000000` | neutral | Primary text or dark surface |
| Pure Canvas | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-fiery-orange: #ff4e27;
  --ref-electric-yellow: #ffc700;
  --ref-shocking-blue: #0029ff;
  --ref-deep-crimson: #4d170c;
  --ref-abyss: #000000;
  --ref-pure-canvas: #ffffff;
}
```

## Typography direction
- **Morganite**: 900, 229px, 0.70; substitute `Anton, Impact`.
- **Thunder**: 300, 122px, normal; substitute `Bebas Neue, League Gothic`.
- **Sentient**: 400, 12px, 16px, 24px, 1.10, 1.15, 1.33, 1.44, 2.25; substitute `Inter, Montserrat`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `16px`
- Element Gap: `5px`
- Radius: `tags: 999px, icons: 999px, buttons: 999px`

## Component cues
- **Primary Action Button**: Interactive element
- **Accent Highlight Button**: Interactive element
- **Ghost Accent Button**: Interactive element
- **Underlined Text Input**: Form element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
