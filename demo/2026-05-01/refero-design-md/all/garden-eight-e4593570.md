# Garden Eight - Refero Design MD

- Source: https://styles.refero.design/style/e4593570-e43f-4eda-8618-0bb704d5ebb7
- Original site: https://garden-eight.com
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
velvety stark minimalism

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#1e1f1f` | neutral | Primary text or dark surface |
| Soft Vanilla | `#dbd6d0` | neutral | Border, muted text, or supporting surface |
| Shadowed Text | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-midnight-ink: #1e1f1f;
  --ref-soft-vanilla: #dbd6d0;
  --ref-shadowed-text: #000000;
}
```

## Typography direction
- **gunsan**: 600, 215px, 0.77; substitute `Playfair Display`.
- **lausanne**: 200, 400, 12px, 14px, 15px, 215px, 1.25, 1.30, 1.42, 1.50, 1.60; substitute `Inter`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `12px`
- Element Gap: `4px`
- Radius: `buttons: 1440px, general: 30px`

## Surface cues
- **Midnight Canvas** `#1e1f1f`: Primary page background and default UI surface.
- **Soft Highlights** `#dbd6d0`: Used for interactive borders and subtle secondary UI elements against the dark canvas.

## Component cues
- **Ghost Navigation Button**: Navigation and secondary actions
- **Pill Outline Button**: Primary interactive element for calls to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
