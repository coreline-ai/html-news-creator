# Paper - Refero Design MD

- Source: https://styles.refero.design/style/01771d1f-43c6-4e91-88c5-e4d213fe4ff2
- Original site: https://paper.design
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble. Light, precise, and structural.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#efefe4` | neutral | Page background or card surface |
| Surface Frost | `#fcfcf9` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Cloud Grey | `#f3f3f4` | neutral | Page background or card surface |
| Outline Slate | `#d7d7d6` | neutral | Border, muted text, or supporting surface |
| Charcoal Black | `#181818` | neutral | Primary text or dark surface |
| Ink Grey | `#222222` | neutral | Primary text or dark surface |
| Mid Grey | `#909090` | neutral | Border, muted text, or supporting surface |
| Stone Grey | `#a8a8a8` | neutral | Border, muted text, or supporting surface |
| Icon Blue | `#5d8cd7` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-parchment: #efefe4;
  --ref-surface-frost: #fcfcf9;
  --ref-paper-white: #ffffff;
  --ref-cloud-grey: #f3f3f4;
  --ref-outline-slate: #d7d7d6;
  --ref-charcoal-black: #181818;
  --ref-ink-grey: #222222;
  --ref-mid-grey: #909090;
}
```

## Typography direction
- **Matter**: 360, 400, 480, 500, 550, 14px, 18px, 48px, 64px, 1.00, 1.56, 2.00.
- **Inter**: 400, 500, 600, 12px, 14px, 16px, 18px, 24px, 36px, 1.00, 1.14, 1.17, 1.20, 1.29, 1.30, 1.33, 1.40, 1.56, 1.75, 2.00, 2.33.
- **Paper Mono**: 400, 11px, 12px, 1.33, 2.55.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `40px`
- Element Gap: `8px`
- Radius: `tags: 20px, cards: 12px, buttons: 4px, inputElements: 4px`

## Surface cues
- **Canvas Parchment** `#efefe4`: Primary page background, foundation of the entire interface.
- **Surface Frost** `#fcfcf9`: Slightly elevated general interface elements like headers or prominent background sections.
- **Paper White** `#ffffff`: Foreground elements like cards, tool panels, or specific UI components requiring crisp visual separation.

## Component cues
- **Primary Filled Button**: Action button with solid background
- **Ghost Button**: Secondary action button with transparent background
- **Elevated Content Card**: Informational card with shadow
- **Section Card**: Content card as a section container
- **Tool Panel Card**: UI panel with internal padding

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
