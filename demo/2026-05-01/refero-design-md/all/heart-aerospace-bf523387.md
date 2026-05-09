# Heart Aerospace - Refero Design MD

- Source: https://styles.refero.design/style/bf523387-03fc-4243-86ca-25af34daa0ce
- Original site: https://heartaerospace.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Overcast Sky, Silent Typography

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Gray | `#716e85` | neutral | Border, muted text, or supporting surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Pure Canvas | `#ffffff` | neutral | Page background or card surface |
| Electric Violet | `#001489` | brand | Action accent / signal color |

```css
:root {
  --ref-cloud-gray: #716e85;
  --ref-midnight-ink: #000000;
  --ref-pure-canvas: #ffffff;
  --ref-electric-violet: #001489;
}
```

## Typography direction
- **NeueHaasText**: 400, 600, 18px, 1.00, 1.30; substitute `Helvetica Neue, Arial`.
- **NeueHaasDisplay**: 600, 46px, 156px, 1.00; substitute `Helvetica Neue, Arial`.

## Spacing / shape
- Section Gap: `70px`
- Card Padding: `20px`
- Element Gap: `18px`
- Radius: `default: 0px`

## Component cues
- **Primary Navigation Link**: Main navigation menu item
- **Hero Headline**: Main page title for hero sections
- **Standard Headline**: Section and content headings
- **Body Text**: Paragraphs and descriptive content
- **Outlined Link**: Interactive links and calls to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
