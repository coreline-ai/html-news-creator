# Slack - Refero Design MD

- Source: https://styles.refero.design/style/e26cb9b0-f876-41ff-9f24-fd67a6b9776c
- Original site: https://slack.com
- Theme: `light`
- Recommended fit: **Clean SaaS webapp**

## North star
Vibrant digital workbench.

## Why this fits html-news-creator
Useful for the admin webapp and future subscriber UI where clarity and restrained polish are required.

## Apply to
- New report option flows
- Settings and policy screens
- Subscriber dashboard cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Ice | `#fefbff` | neutral | Primary page background, expansive neutral space for content. |
| Surface Frost | `#ffffff` | neutral | Elevated card backgrounds, component containers. |
| Whisper Cloud | `#f9f0ff` | neutral | Subtle background for UI elements, light hovered states. |
| Active Lavender | `#f2defe` | neutral | Background for active navigation items, subtle highlights. |
| Charcoal Black | `#000000` | neutral | Primary text color for headings, body, and high-emphasis elements. |
| Carbon Gray | `#1d1c1d` | neutral | Secondary text and icon color, slightly softer than Charcoal Black. |
| Pewter | `#696969` | neutral | Tertiary text, muted labels, helper text. |
| Cement Gray | `#757575` | neutral | Informational text, list item details. |

```css
:root {
  --ref-canvas-ice: #fefbff;
  --ref-surface-frost: #ffffff;
  --ref-whisper-cloud: #f9f0ff;
  --ref-active-lavender: #f2defe;
  --ref-charcoal-black: #000000;
  --ref-carbon-gray: #1d1c1d;
  --ref-pewter: #696969;
}
```

## Typography direction
- Primary: **Salesforce-Sans**; substitute `Open Sans, Arial, sans-serif`.
- Secondary/code: **Salesforce-Avant-Garde**; substitute `Montserrat, Georgia, serif`.

## Spacing / shape
- Section gap: `98px`
- Card padding: `16px`
- Element gap: `16px`
- Radius: `{'cards': '16px', 'pills': '90px', 'inputs': '4px', 'buttons': '4px', 'default': '8px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
