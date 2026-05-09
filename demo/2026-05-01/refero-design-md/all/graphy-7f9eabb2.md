# Graphy - Refero Design MD

- Source: https://styles.refero.design/style/7f9eabb2-3f76-477d-849f-e868e698f421
- Original site: https://graphy.app
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Data on frosted glass

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#f2f4f8` | neutral | Page background or card surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Graphite Ink | `#000000` | neutral | Primary text or dark surface |
| Slate Blue | `#20295a` | brand | Action accent / signal color |
| Action Blue | `#2e62ff` | brand | Action accent / signal color |
| Mid-Tone Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Ghost Gray | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Light-touch Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Ocean Link | `#0099ff` | accent | Action accent / signal color |
| Dusty Violet | `#4a527a` | neutral | Action accent / signal color |

```css
:root {
  --ref-canvas-ice: #f2f4f8;
  --ref-paper-white: #ffffff;
  --ref-graphite-ink: #000000;
  --ref-slate-blue: #20295a;
  --ref-action-blue: #2e62ff;
  --ref-mid-tone-gray: #666666;
  --ref-ghost-gray: #c2c2c2;
  --ref-light-touch-gray: #999999;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.2.
- **Aeonik Medium**: 400, 16px, 20px, 24px, 32px, 40px, 56px, 82px, 0.85, 1.13, 1.15, 1.20, 1.35, 1.40; substitute `Montserrat`.
- **Aeonik Regular**: 400, 700, 12px, 14px, 16px, 18px, 22px, 1.00, 1.05, 1.10, 1.20, 1.30, 1.35, 1.60, 1.83; substitute `Montserrat`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 40px, cards: 8px, input: 8px, buttons: 20px, containers: 16px, roundedElements: 70px, smallInteractive: 4px`

## Surface cues
- **Canvas Ice** `#f2f4f8`: Base page background
- **Paper White** `#ffffff`: Elevated card surfaces, primary content blocks
- **Form Fill** `#eeeeee`: Input field backgrounds

## Component cues
- **Primary Filled Button**: Main call to action.
- **Secondary Ghost Button**: Subtle alternative actions, often next to a primary button.
- **Outline Ghost Button (Product Announcement)**: Outlined button for secondary, less prominent, or informative actions.
- **Base Feature Card**: Informational cards on secondary canvas.
- **Elevated Content Card**: Highlighting content against the main canvas.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
