# Anything - Refero Design MD

- Source: https://styles.refero.design/style/edf7f95d-da5f-42bf-94c5-b33ade0a2ba2
- Original site: https://www.createanything.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cloud-swept dreamscape

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Sky Mist | `#f9f9f9` | neutral | Page background or card surface |
| Whisper Gray | `#f2f2f2` | neutral | Page background or card surface |
| Slate Ink | `#18191b` | neutral | Primary text or dark surface |
| Abyssal Black | `#000000` | neutral | Primary text or dark surface |
| Soft Stone | `#acadae` | neutral | Border, muted text, or supporting surface |
| Stone Whisper | `#6a6a6c` | neutral | Border, muted text, or supporting surface |
| Slate Border | `#bbbbbb` | neutral | Border, muted text, or supporting surface |
| Cool Gray | `#c4c4c4` | neutral | Border, muted text, or supporting surface |
| Pale Silver | `#dbdbdb` | neutral | Page background or card surface |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-sky-mist: #f9f9f9;
  --ref-whisper-gray: #f2f2f2;
  --ref-slate-ink: #18191b;
  --ref-abyssal-black: #000000;
  --ref-soft-stone: #acadae;
  --ref-stone-whisper: #6a6a6c;
  --ref-slate-border: #bbbbbb;
}
```

## Typography direction
- **Inter**: 300, 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 29px, 1.33, 1.40, 1.43, 1.50, 1.56; substitute `system-ui, sans-serif`.
- **Instrument Serif**: 400, 500, 16px, 24px, 1.00, 1.40, 1.50; substitute `serif`.
- **Instrument Sans**: 400, 600, 16px, 24px, 42px, 1.20, 1.40, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `40px`
- Element Gap: `12px`
- Radius: `cards: 20px, images: 20px, inputs: 0px, buttons: 9999px, elements: 8px`

## Component cues
- **Primary Action Button**: Filled button for primary calls to action
- **Naked Pill Button**: Softly styled button, often for secondary actions or tags.
- **Ghost Chip Button**: Subtle, non-prominent button for filtering or alternative actions.
- **Minimal Card**: Standard content container, light elevation.
- **Flat Card**: Container for content without elevation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
