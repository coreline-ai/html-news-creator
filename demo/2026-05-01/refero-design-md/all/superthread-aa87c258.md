# Superthread - Refero Design MD

- Source: https://styles.refero.design/style/aa87c258-0eb8-4c14-9f2f-96f16fb926b8
- Original site: https://www.superthread.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Whiteboard with vivid highlighter

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Stormy Night | `#1d2939` | neutral | Primary text or dark surface |
| Midnight Ink | `#101828` | neutral | Primary text or dark surface |
| Cadet Gray | `#667085` | neutral | Border, muted text, or supporting surface |
| Pale Indigo | `#1d2a53` | accent | Action accent / signal color |
| Superthread Yellow | `#ffaa00` | brand | Action accent / signal color |
| Cool Stone | `#475467` | neutral | Border, muted text, or supporting surface |
| Canvas White | `#f9fafb` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Ash Mist | `#e4e7ec` | neutral | Page background or card surface |
| Cloud Gray | `#f2f4f7` | neutral | Page background or card surface |

```css
:root {
  --ref-stormy-night: #1d2939;
  --ref-midnight-ink: #101828;
  --ref-cadet-gray: #667085;
  --ref-pale-indigo: #1d2a53;
  --ref-superthread-yellow: #ffaa00;
  --ref-cool-stone: #475467;
  --ref-canvas-white: #f9fafb;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **sans-serif**: 400, 500, 600, 12px, 16px, 1.2.
- **Vela Sans**: 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 24px, 32px, 80px, 1.10, 1.20, 1.33, 1.40, 1.50, 1.70; substitute `Inter, 'Helvetica Neue', Arial, sans-serif`.
- **Noto Sans**: 400, 500, 700, 16px, 18px, 1.40; substitute `Open Sans, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `25px`
- Element Gap: `10px`
- Radius: `small: 4px, default: 10px, cardLarge: 16px, buttonPill: 50px`

## Surface cues
- **Canvas White** `#f9fafb`: Primary page background
- **Pure White** `#ffffff`: Default card backgrounds and main content panels
- **Cloud Gray** `#F2F4F7`: Alternate section backgrounds or subtle content containers

## Component cues
- **Primary Action Button**: Main call to action button.
- **Secondary Ghost Button**: Outlined button for secondary actions.
- **Tertiary Tab Button**: Buttons for filtering or switching views, often in groups.
- **Navigation Link**: Interactive text link in navigation.
- **Elevated Content Card**: Used for featured content or panels requiring emphasis.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
