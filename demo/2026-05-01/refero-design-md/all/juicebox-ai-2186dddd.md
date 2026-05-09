# Juicebox.ai - Refero Design MD

- Source: https://styles.refero.design/style/2186dddd-60ee-4898-b11d-88483daf477e
- Original site: https://juicebox.ai
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Vivid Analyst Workspace

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud Canvas | `#f8f6f8` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Ink | `#000000` | neutral | Primary text or dark surface |
| Deep Plum | `#1d161d` | neutral | Primary text or dark surface |
| Graphite | `#574e57` | neutral | Border, muted text, or supporting surface |
| Border Fog | `#d9d9d9` | neutral | Page background or card surface |
| Dusty Gray | `#786c78` | neutral | Border, muted text, or supporting surface |
| Obsidian | `#2a232a` | neutral | Primary text or dark surface |
| Juicebox Purple | `#6a2f8d` | brand | Action accent / signal color |
| Highlight Violet | `#da9efd` | accent | Action accent / signal color |

```css
:root {
  --ref-cloud-canvas: #f8f6f8;
  --ref-paper-white: #ffffff;
  --ref-ink: #000000;
  --ref-deep-plum: #1d161d;
  --ref-graphite: #574e57;
  --ref-border-fog: #d9d9d9;
  --ref-dusty-gray: #786c78;
  --ref-obsidian: #2a232a;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Roobert Medium**: 400, 28px, 40px, 48px, 64px, 72px, 1.00, 1.13, 1.15, 1.25; substitute `Montserrat`.
- **Haas Grot Text Web**: 400, 700, 10px, 12px, 14px, 16px, 18px, 20px, 1.00, 1.08, 1.20, 1.25, 1.29, 1.33, 1.43, 1.56; substitute `Inter`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `14px`
- Element Gap: `10px`
- Radius: `cards: 6px, buttons: 4px, elements: 2px`

## Component cues
- **Primary Filled Button**: Interactive element for primary actions.
- **Secondary Ghost Button**: Interactive element for secondary actions, or when a less prominent call to action is needed.
- **Solid White Button**: Interactive element for alternative actions, provides strong contrast on dark backgrounds.
- **Juicebox Purple Filled Button**: Primary branded action.
- **Product Feature Card**: Container for showcasing features or information blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
