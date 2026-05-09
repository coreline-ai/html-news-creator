# Waka Waka - Refero Design MD

- Source: https://styles.refero.design/style/ea55601d-e953-48b3-99db-374b39bf2f56
- Original site: https://wakawaka.world
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Catalog: off-white canvas, stark black typography, and carefully placed product visuals.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#edeae4` | neutral | Page background or card surface |
| Ink Jot | `#28282a` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-parchment: #edeae4;
  --ref-ink-jot: #28282a;
}
```

## Typography direction
- **Waka Sans**: 400, 500, 700, 10px, 14px, 18px, 24px, 560px, 0.80, 0.83, 1.00, 1.20, 1.60; substitute `Helvetica Neue`.

## Spacing / shape
- Section Gap: `40-54px`
- Card Padding: `20px`
- Element Gap: `6-20px`
- Page Max Width: `445px`
- Radius: `default: 0px`

## Component cues
- **Page Canvas**: The primary content container
- **Hero Headline**: Prominent display text
- **Navigation Link**: Site navigation
- **Body Text**: :Standard paragraph and descriptive text
- **Functional Details**: Metadata, timestamps, and smaller labels

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
