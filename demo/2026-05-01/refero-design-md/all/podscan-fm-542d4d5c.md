# Podscan.fm - Refero Design MD

- Source: https://styles.refero.design/style/542d4d5c-fd8f-4a8b-a4f7-4694728f7e12
- Original site: https://podscan.fm
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard with digital highlights

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Absolute Zero | `#f4f4f5` | neutral | Page background or card surface |
| Graphite | `#52525b` | neutral | Border, muted text, or supporting surface |
| Mid Grey | `#71717a` | neutral | Border, muted text, or supporting surface |
| Silver Pine | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Cloud Whisper | `#d4d4d8` | neutral | Border, muted text, or supporting surface |
| Ash Felt | `#e5e7eb` | neutral | Page background or card surface |
| White Smoke | `#fafafe` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#18181b` | neutral | Primary text or dark surface |
| Emerald Spark | `#059669` | brand | Action accent / signal color |

```css
:root {
  --ref-absolute-zero: #f4f4f5;
  --ref-graphite: #52525b;
  --ref-mid-grey: #71717a;
  --ref-silver-pine: #a1a1aa;
  --ref-cloud-whisper: #d4d4d8;
  --ref-ash-felt: #e5e7eb;
  --ref-white-smoke: #fafafe;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Inter Tight**: 400, 600, 700, 14px, 20px, 24px, 30px, 36px, 60px, 1.00, 1.11, 1.20, 1.33, 1.40, 1.43; substitute `system-ui`.
- **ui-sans-serif**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 30px, 1.20, 1.33, 1.38, 1.40, 1.43, 1.50, 1.56; substitute `system-ui`.
- **ui-monospace**: 400, 12px, 1.33; substitute `monospace`.

## Spacing / shape
- Section Gap: `72px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 9999px, cards: 12px, icons: 8px, inputs: 12px, buttons: 8px`

## Surface cues
- **Pure White Canvas** `#ffffff`: Primary page background and default component surface
- **White Smoke Surface** `#fafafe`: Subtle background for specific UI elements like inputs and tertiary buttons, slightly distinct from canvas
- **Absolute Zero Background** `#f4f4f5`: Alternative background for sections and larger containers, providing a slight contrast to the main canvas without introducing significant color

## Component cues
- **Primary Call to Action Button**: Filled button indicating the primary path forward.
- **Secondary Ghost Button**: Subtle action, less prominent than primary.
- **Tertiary Tab Button**: Small, information-based button for categories or filtering.
- **Floating Card**: Elevated container for content sections, usually informative.
- **Clean Card**: Basic container for grouped content, minimal elevation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
