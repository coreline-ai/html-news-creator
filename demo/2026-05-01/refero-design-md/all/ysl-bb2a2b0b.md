# Ysl - Refero Design MD

- Source: https://styles.refero.design/style/bb2a2b0b-c84e-48ee-9dd9-7b623f81a422
- Original site: https://ysl.com
- Theme: `dark`
- Industry: `ecommerce`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Black Tie Photography — a high-contrast canvas for arresting visuals.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Polar White | `#ffffff` | neutral | Page background or card surface |
| Accent Blue | `#007aff` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-polar-white: #ffffff;
  --ref-accent-blue: #007aff;
}
```

## Typography direction
- **SaintLaurent sans-serif**: 12px, 14px, 1; substitute `Arial, Helvetica, sans-serif`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `0px`
- Element Gap: `4px`
- Radius: `all: 0px`

## Component cues
- **Product Card**: Reference component style.
- **Button Group**: Reference component style.
- **Campaign Caption Banner**: Reference component style.
- **Primary Navigation Link**: Header and footer navigation elements.
- **Standard Button - Default**: Interactive elements, calls to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
