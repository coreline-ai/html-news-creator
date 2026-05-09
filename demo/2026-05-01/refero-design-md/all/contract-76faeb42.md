# Contract - Refero Design MD

- Source: https://styles.refero.design/style/76faeb42-b43d-4cc7-ac03-1e4bd74f04b7
- Original site: https://contract.mdfitalia.com/en
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural Blueprint on Marble: Precise lines and forms over a neutral, expansive canvas.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ash Gray | `#e5e7eb` | neutral | Page background or card surface |
| Slate Text | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Medium Gray | `#b3b3b3` | neutral | Border, muted text, or supporting surface |
| Light Gray | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Azure Accent | `#2563eb` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-ash-gray: #e5e7eb;
  --ref-slate-text: #6b7280;
  --ref-medium-gray: #b3b3b3;
  --ref-light-gray: #bbbbbb;
  --ref-azure-accent: #2563eb;
}
```

## Typography direction
- **Plain**: 300, 400, 500, 600, 16px, 18px, 24px, 30px, 50px, 100px, 1.00, 1.07, 1.08, 1.13, 1.25, 1.50, 1.56, 1.63, 1.75; substitute `Inter, Arial, sans-serif`.

## Spacing / shape
- Section Gap: `69px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `inputs: 2px, default: 0px`

## Component cues
- **Primary Ghost Button**: Interactive control for primary actions, presenting as an outlined element to maintain a light visual footprint.
- **Text Link Button**: Minimal interactive control for navigation or secondary actions, appearing as plain text.
- **Text Input Field**: User input area for forms.
- **Office Product Card**: Display individual product categories or offerings.
- **Key Value Circle**: Highlights key features or services within a section.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
