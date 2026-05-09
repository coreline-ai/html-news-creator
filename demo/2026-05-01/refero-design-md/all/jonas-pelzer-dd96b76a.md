# Jonas Pelzer - Refero Design MD

- Source: https://styles.refero.design/style/dd96b76a-b691-49e7-ba8f-1cdc8f7172e6
- Original site: https://jonaspelzer.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
dot-matrix digital blueprint

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#d4d6dd` | neutral | Border, muted text, or supporting surface |
| Digital Violet | `#3502ff` | brand | Action accent / signal color |
| Muted Lilac | `#d7ccff` | brand | Action accent / signal color |
| Action Grape | `#5d35ff` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-ghost-gray: #d4d6dd;
  --ref-digital-violet: #3502ff;
  --ref-muted-lilac: #d7ccff;
  --ref-action-grape: #5d35ff;
}
```

## Typography direction
- **Scope**: 400, 13px, 14px, 17px, 22px, 42px, 1.00, 1.10, 1.20; substitute `IBM Plex Mono`.
- **Signifier**: 400, 15px, 16px, 18px, 22px, 25px, 42px, 1.00, 1.20; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `14px`
- Element Gap: `5px`
- Radius: `cards: 12px, navbar: 8.26px, buttons: 12px, default: 12px, navbarItem: 3.5px`

## Component cues
- **Ghost Button**: Navigation and secondary actions
- **Outlined Violet Button**: Primary Call to Action
- **Work Card**: Portfolio item container
- **Navigation Link (Active)**: Current page indicator
- **Navigation Wrap**: Container for primary navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
