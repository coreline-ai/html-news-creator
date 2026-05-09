# Delphi - Refero Design MD

- Source: https://styles.refero.design/style/43c1b150-0dab-42f9-9bce-fe0be3dde26c
- Original site: https://delphi.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cognac-Stained Parchment – A sense of aged wisdom and quiet authority, inviting deep contemplation.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Parchment White | `#fdf6ee` | neutral | Page background or card surface |
| Deep Cognac | `#2b180a` | brand | Action accent / signal color |
| Muted Stone | `#94877c` | neutral | Border, muted text, or supporting surface |
| Pressed Cacao | `#7f6e60` | neutral | Border, muted text, or supporting surface |
| Burnt Umber | `#3e2407` | accent | Action accent / signal color |
| Warm Ash | `#a99d93` | neutral | Border, muted text, or supporting surface |
| Cloud Fog | `#f0e6dc` | neutral | Page background or card surface |
| Fire Opal | `#f65726` | accent | Action accent / signal color |
| Sunset Orange | `#ff5c00` | accent | Action accent / signal color |
| White | `#ffffff` | neutral | Page background or card surface |

```css
:root {
  --ref-parchment-white: #fdf6ee;
  --ref-deep-cognac: #2b180a;
  --ref-muted-stone: #94877c;
  --ref-pressed-cacao: #7f6e60;
  --ref-burnt-umber: #3e2407;
  --ref-warm-ash: #a99d93;
  --ref-cloud-fog: #f0e6dc;
  --ref-fire-opal: #f65726;
}
```

## Typography direction
- **Martina Plantijn Light**: 300, 400, 700, 10px, 12px, 14px, 15px, 20px, 24px, 40px, 56px, 64px, 1.00, 1.20, 1.22, 1.32, 1.34; substitute `Source Serif Pro`.
- **Inter**: 400, 500, 10px, 13px, 14px, 15px, 17px, 1.00, 1.20, 1.40; substitute `Inter`.
- **sans-serif**: 400, 12px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `75px`
- Card Padding: `20px`
- Element Gap: `8px`
- Radius: `small: 4px, buttons: 12px, default: 12px, testimonials: 70px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Cards — Why Delphi**: Reference component style.
- **Trust Feature Cards Grid**: Reference component style.
- **Primary Button (Filled)**: Call to action.
- **Secondary Button (Outlined)**: Secondary action or ghost button.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
