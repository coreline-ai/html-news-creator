# PORTO ROCHA - Refero Design MD

- Source: https://styles.refero.design/style/701c8312-5e98-49a8-b2c4-25f1cb66de15
- Original site: https://portorocha.com
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial Grid on Canvas White

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Storm Gray | `#808080` | neutral | Border, muted text, or supporting surface |
| Accent Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-storm-gray: #808080;
  --ref-accent-blue: #007aff;
}
```

## Typography direction
- **sf-pro-text**: 400, 14px, 1.25; substitute `system-ui, sans-serif`.
- **sf-pro-display**: 400, 23px, 1.17; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `default: 8px, prominent: 38px`

## Component cues
- **Ghost Button**: Interactive element
- **Pill Button**: Interactive element
- **Feature Card (Ghost)**: Content display
- **Project Preview Card**: Interactive content preview
- **Navigation Item**: Navigation element

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
