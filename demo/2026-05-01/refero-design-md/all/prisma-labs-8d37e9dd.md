# Prisma Labs - Refero Design MD

- Source: https://styles.refero.design/style/8d37e9dd-1d6b-4b60-a636-55aa3e0fc238
- Original site: https://prisma-ai.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
High-contrast digital clarity

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Charcoal Text | `#0d0d0d` | neutral | Primary text or dark surface |
| Greyed Text | `#333333` | neutral | Primary text or dark surface |
| Action Yellow | `#ffd600` | brand | Action accent / signal color |
| Highlight Red | `#ff0062` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-charcoal-text: #0d0d0d;
  --ref-greyed-text: #333333;
  --ref-action-yellow: #ffd600;
  --ref-highlight-red: #ff0062;
}
```

## Typography direction
- **Cofo sans**: 400, 600, 700, 10px, 18px, 22px, 72px, 1.00, 1.10, 1.11; substitute `Montserrat`.
- **Arial**: 400, 14px, 1.43; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `84px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1500px`
- Radius: `others: 10px, buttons: 16px`

## Component cues
- **Primary Action Button**: Interactive element
- **Ghost Navigation Button**: Interactive element
- **Hero Headline**: Text element
- **Navigation Item**: Interactive element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
