# Workflow - Refero Design MD

- Source: https://styles.refero.design/style/71451d9e-9a8a-4858-9a91-fbe44047e110
- Original site: https://www.workflow.design
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Ink | `#1a1a1a` | neutral | Primary text or dark surface |
| Ash | `#6a6a6a` | neutral | Border, muted text, or supporting surface |
| Fog | `#f6f6f6` | neutral | Page background or card surface |
| Pebble | `#ececec` | neutral | Page background or card surface |
| Frost | `#e3e3e3` | neutral | Page background or card surface |
| Driftwood | `#4d3f32` | brand | Action accent / signal color |
| Success Green | `#547e69` | accent | Action accent / signal color |
| Success Pale | `#60886f` | accent | Action accent / signal color |
| Error Red | `#923d56` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-ink: #1a1a1a;
  --ref-ash: #6a6a6a;
  --ref-fog: #f6f6f6;
  --ref-pebble: #ececec;
  --ref-frost: #e3e3e3;
  --ref-driftwood: #4d3f32;
  --ref-success-green: #547e69;
}
```

## Typography direction
- **Inter**: 400, 500, 11px, 12px, 13px, 14px, 15px, 16px, 1.00 - 1.91; substitute `system-ui, sans-serif`.
- **Crimson Pro**: 300, 26px, 32px, 1.00; substitute `Georgia, serif`.
- **Georgia**: 400, 13px, 1.35, 1.62.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `pill: 9999px, cards: 12px, input: 8px, badges: 6px, buttons: 8px`

## Surface cues
- **Canvas** `#ffffff`: Base page background and principal surface for content.
- **Fog** `#f6f6f6`: Secondary background for sections, buttons, and badges to add subtle differentiation.
- **Pebble** `#ececec`: Tertiary background for elevated cards and feature blocks, providing a slightly darker context.

## Component cues
- **Primary Ghost Button**: Interactive element
- **Pill Button**: Interactive element
- **Feature Card**: Container
- **Section Card**: Container
- **Pill Badge**: Content label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
