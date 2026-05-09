# Strava - Refero Design MD

- Source: https://styles.refero.design/style/efdd6d8f-4488-4312-86a7-4ee8e016c83a
- Original site: https://strava.com
- Theme: `light`
- Industry: `other`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Athletic Orange Highlight

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloudburst Gray | `#43423f` | neutral | Border, muted text, or supporting surface |
| Ash Charcoal | `#21211f` | neutral | Primary text or dark surface |
| Whisper White | `#ffffff` | neutral | Page background or card surface |
| Summit Cream | `#f9f8f5` | neutral | Page background or card surface |
| Pebble Gray | `#e0e0de` | neutral | Page background or card surface |
| Strava Orange | `#fc5200` | brand | Action accent / signal color |
| Link Blue | `#0060d0` | semantic | Action accent / signal color |
| Google Red | `#ea4335` | accent | Action accent / signal color |
| Google Green | `#34a853` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-cloudburst-gray: #43423f;
  --ref-ash-charcoal: #21211f;
  --ref-whisper-white: #ffffff;
  --ref-summit-cream: #f9f8f5;
  --ref-pebble-gray: #e0e0de;
  --ref-strava-orange: #fc5200;
  --ref-link-blue: #0060d0;
}
```

## Typography direction
- **Boathouse**: 400, 12px, 14px, 15px, 16px, 32px, 1.00, 1.20, 1.29, 1.30, 1.33, 1.50; substitute `Inter`.
- **Boathouse**: 600, 12px, 14px, 15px, 16px, 32px, 1.00, 1.20, 1.29, 1.30, 1.33, 1.50; substitute `Inter`.

## Spacing / shape
- Radius: `cards: 4px, buttons: 4px, input_fields: 4px`

## Component cues
- **Sign Up Form Card**: Reference component style.
- **Button Group Showcase**: Reference component style.
- **Stat / Feature Banner**: Reference component style.
- **Primary CTA Button**: Main call to action
- **Secondary Outline Button (Social)**: Alternative login/signup

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
