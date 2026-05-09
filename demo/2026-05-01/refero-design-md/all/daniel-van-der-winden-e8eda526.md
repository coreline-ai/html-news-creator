# Daniël van der Winden - Refero Design MD

- Source: https://styles.refero.design/style/e8eda526-d686-4e45-a60d-61b6503a8eda
- Original site: https://www.daniel.pizza
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Ordered Editorial Ink

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Porcelain | `#e5e7eb` | neutral | Page background or card surface |
| Ebony Text | `#111827` | neutral | Primary text or dark surface |
| Graphite Text | `#374151` | neutral | Border, muted text, or supporting surface |
| Midnight Ink | `#1a202c` | neutral | Primary text or dark surface |
| Jet Button | `#222222` | neutral | Primary text or dark surface |
| Shadow Icon | `#000000` | neutral | Primary text or dark surface |
| Slate Text | `#2a2a28` | neutral | Primary text or dark surface |
| Ash Text | `#676867` | neutral | Border, muted text, or supporting surface |
| Fog Border | `#c4c6c8` | neutral | Border, muted text, or supporting surface |
| Stone Text | `#7b7c7c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-porcelain: #e5e7eb;
  --ref-ebony-text: #111827;
  --ref-graphite-text: #374151;
  --ref-midnight-ink: #1a202c;
  --ref-jet-button: #222222;
  --ref-shadow-icon: #000000;
  --ref-slate-text: #2a2a28;
  --ref-ash-text: #676867;
}
```

## Typography direction
- **Degular**: 400, 500, 600, 700, 14px, 16px, 18px, 22px, 24px, 28px, 32px, 40px, 1.25, 1.50; substitute `Inter`.
- **Blanco**: 400, 14px, 20px, 22px, 28px, 1.40, 1.50; substitute `Lora`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `12px`
- Element Gap: `8px`
- Page Max Width: `1600px`
- Radius: `cards: 3px, other: 8px, buttons: 0px, navigation: 3px`

## Component cues
- **Primary Filled Button**: Main call-to-action button, conveying prominence.
- **Email Button**: Secondary action button for personal contacts, slightly softer than primary.
- **Ghost Icon Button**: Subtle interactive button, often for icons or secondary actions, maintaining minimal visual footprint.
- **Navigation Link**: Interactive elements within the left-hand navigation, indicating selectable items.
- **Text Input (Default)**: Standard input field for user data entry.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
