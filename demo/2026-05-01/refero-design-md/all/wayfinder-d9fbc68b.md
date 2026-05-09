# Wayfinder - Refero Design MD

- Source: https://styles.refero.design/style/d9fbc68b-0d42-4c09-829d-1207b781f46a
- Original site: https://wayfinder.nfb.ca
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Enchanted forest parchment

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ebon | `#000000` | neutral | Primary text or dark surface |
| Graphite | `#1a1a1a` | neutral | Primary text or dark surface |
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Mercury | `#e3e3e2` | neutral | Page background or card surface |
| Stone | `#c0bfbe` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ebon: #000000;
  --ref-graphite: #1a1a1a;
  --ref-canvas: #ffffff;
  --ref-mercury: #e3e3e2;
  --ref-stone: #c0bfbe;
}
```

## Typography direction
- **Enreal**: 300, 400, 700, 14px, 16px, 24px, 1.20, 1.75; substitute `Montserrat`.
- **Arial**: 400, 13px, 1.20; substitute `Helvetica Neue`.
- **Ciutadella-Medium**: 300, 14px, 1.00; substitute `San Francisco Display`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `default: 0px`

## Component cues
- **Ghost Button**: Interactive element for navigation and actions
- **Text Link**: Navigation and informational links
- **Primary Heading**: Main titles and key feature statements
- **Subtle Information Text**: Descriptive text under headings or alongside imagery

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
