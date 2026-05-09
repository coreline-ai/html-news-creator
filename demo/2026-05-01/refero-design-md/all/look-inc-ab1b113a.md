# Look inc - Refero Design MD

- Source: https://styles.refero.design/style/ab1b113a-ed21-4512-acc2-d10c8927c410
- Original site: https://look.inc
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial canvas, bold type

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Smoke Grey | `#878787` | neutral | Border, muted text, or supporting surface |
| Whisper White | `#e5e5e5` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-paper-white: #ffffff;
  --ref-smoke-grey: #878787;
  --ref-whisper-white: #e5e5e5;
}
```

## Typography direction
- **Old Standard**: 400, 18px, 21px, 32px, 1.10, 1.40; substitute `Lora`.
- **GT America**: 400, 700, 18px, 21px, 23px, 1.20, 1.30, 1.70; substitute `Public Sans`.
- **-apple-system**: 400, 15px, 1.65; substitute `system-ui`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `26px`
- Element Gap: `19px`
- Radius: `none: 0px`

## Component cues
- **Hero Headline**: Primary page title
- **Navigation Link**: Top navigation item
- **Info Block Text**: Descriptive text accompanying hero
- **Project Card Title**: Title for individual portfolio projects
- **Project Card Description**: Brief description of a portfolio project

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
