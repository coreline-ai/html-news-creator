# Volume - Refero Design MD

- Source: https://styles.refero.design/style/edc0c03e-8c20-4e22-badd-2735fcb9f4a8
- Original site: https://vol.co
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial archive, high contrast.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#272727` | neutral | Primary text or dark surface |
| Ash Gray | `#717171` | neutral | Border, muted text, or supporting surface |
| Stone Button | `#949494` | neutral | Border, muted text, or supporting surface |
| Obsidian Pill | `#000000` | neutral | Primary text or dark surface |
| Whisper Text | `#cdcccc` | neutral | Border, muted text, or supporting surface |
| Crimson Pill | `#962921` | accent | Action accent / signal color |
| Scarlet Pill | `#c52910` | accent | Action accent / signal color |
| Blaze Pill | `#e75a00` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #272727;
  --ref-ash-gray: #717171;
  --ref-stone-button: #949494;
  --ref-obsidian-pill: #000000;
  --ref-whisper-text: #cdcccc;
  --ref-crimson-pill: #962921;
  --ref-scarlet-pill: #c52910;
}
```

## Typography direction
- **Messina Sans**: 300, 350, 14px, 18px, 20px, 32px, 50px, 80px, 1.00, 1.18, 1.40, 2.00; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `30px`
- Element Gap: `10px`
- Page Max Width: `1400px`
- Radius: `cards: 0px, pills: 50px, inputs: 0px, buttons: 0px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page and card backgrounds.
- **Stone Button** `#949494`: Background for default interactive elements.
- **Obsidian Pill** `#000000`: Elevated card pill backgrounds for status.

## Component cues
- **Filled Button**: Primary action button for sign-ups or confirmations.
- **Default Card**: Container for products, articles, or featured content.
- **Funding Status Pill (Obsidian)**: Small, rounded label indicating successful funding or status.
- **Funding Status Pill (Crimson)**: Small, rounded label indicating specific campaign status.
- **Funding Status Pill (Scarlet)**: Small, rounded label indicating urgent campaign status.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
