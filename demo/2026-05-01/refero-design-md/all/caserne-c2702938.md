# Caserne - Refero Design MD

- Source: https://styles.refero.design/style/c2702938-b670-414c-ba47-94618212085e
- Original site: https://caserne.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Grid, Dark Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Ghost White | `#f2f2f2` | neutral | Page background or card surface |
| Cloud Burst | `#ffffff` | neutral | Page background or card surface |
| Steel Gaze | `#858484` | neutral | Border, muted text, or supporting surface |
| Deep Graphite | `#333333` | neutral | Primary text or dark surface |
| Ember Glow | `#ff4513` | accent | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #000000;
  --ref-ghost-white: #f2f2f2;
  --ref-cloud-burst: #ffffff;
  --ref-steel-gaze: #858484;
  --ref-deep-graphite: #333333;
  --ref-ember-glow: #ff4513;
}
```

## Typography direction
- **ABC Oracle**: 100, 400, 700, 13px, 14px, 1.29, 1.38, 1.43; substitute `Inter`.

## Spacing / shape
- Section Gap: `90px`
- Card Padding: `5px`
- Element Gap: `5px`
- Radius: `default: 0px`

## Component cues
- **Navigation Link**: Top-level navigation items
- **Work Item Title**: Titles for portfolio pieces or content cards
- **Work Item Subtitle**: Descriptive text for portfolio pieces or content cards
- **Info / Contact Link**: Small, functional links in footer or secondary sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
