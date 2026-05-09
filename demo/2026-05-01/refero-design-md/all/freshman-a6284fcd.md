# Freshman - Refero Design MD

- Source: https://styles.refero.design/style/a6284fcd-fa69-4469-ac40-4239e5b84a39
- Original site: https://freshman.tv
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochrome cinematic canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#000000` | neutral | Primary text or dark surface |
| Near Black | `#101010` | neutral | Primary text or dark surface |
| White Frost | `#ffffff` | neutral | Page background or card surface |
| Power Red | `#ff2936` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #000000;
  --ref-near-black: #101010;
  --ref-white-frost: #ffffff;
  --ref-power-red: #ff2936;
}
```

## Typography direction
- **TT Firs Neue**: 400, 16px, 1.00; substitute `Inter`.
- **Editorial New**: 200, 16px, 20px, 1.00, 1.25; substitute `Lora`.
- **Altform**: 400, 700, 14px, 16px, 0.86, 0.88; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `47px`
- Card Padding: `20px`
- Element Gap: `12px`
- Radius: `none: 0px`

## Surface cues
- **Midnight Void** `#000000`: Primary page background and deepest surface level, providing a stark 'black box' for content.
- **Near Black** `#101010`: Slightly lighter background for elevated UI elements like cards or modals, creating minimal visual separation.

## Component cues
- **Ghost Navigation Button**: Top-level navigation element
- **Thumbnail Link Title**: Interactive content title within a grid
- **Footer Cookie Button**: Legal/utility action in the footer
- **Main Headline**: Hero section primary statement
- **Sub-Headline Descriptive Text**: Supporting text for hero sections or key messages

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
