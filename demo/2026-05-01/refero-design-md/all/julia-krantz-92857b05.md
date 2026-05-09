# Julia Krantz - Refero Design MD

- Source: https://styles.refero.design/style/92857b05-1c01-4c7a-b196-beb4e4871998
- Original site: https://juliakrantz.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Dark webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Darkroom contact sheet — a grid of photographic tiles on pure black, identity spelled in barely-visible weight-300 letterforms.

## Apply to
- Dark theme experiments
- Operator-focused widgets
- High-contrast card systems

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void | `#000000` | neutral | Primary text or dark surface |
| Salt | `#f8f8f8` | neutral | Page background or card surface |
| Ash | `#707070` | neutral | Border, muted text, or supporting surface |
| Ghost Line | `#f8f8f8` | neutral | Page background or card surface |
| Veil | `#f8f8f8` | neutral | Page background or card surface |

```css
:root {
  --ref-void: #000000;
  --ref-salt: #f8f8f8;
  --ref-ash: #707070;
  --ref-ghost-line: #f8f8f8;
  --ref-veil: #f8f8f8;
}
```

## Typography direction
- **DM Sans**: 300, 10px, 12px, 13px, 14px, 1.30 – 1.72; substitute `DM Sans (Google Fonts — same family)`.
- **ClashDisplay**: 300, 500, 10px, 12px, 14px, 29px, 44px, 1.00 at display / 1.72 at text sizes; substitute `Cabinet Grotesk (Fontshare) or Space Grotesk (Google Fonts)`.

## Spacing / shape
- Section Gap: `30px`
- Card Padding: `16px`
- Element Gap: `6px`
- Radius: `cards: 0px, tiles: 0px, inputs: 0px, buttons: 0px`

## Surface cues
- **Void Canvas** `#000000`: Base page background, section backgrounds, nav bar
- **Image Tile** `#111111`: Grid project tiles — filled with photography, bordered by Ghost Line 1px

## Component cues
- **Project Grid Tiles**: Reference component style.
- **About Bio Block**: Reference component style.
- **Header Identity + Email CTA**: Reference component style.
- **Project Grid Tile**: Primary portfolio navigation — each tile is a cropped photograph with abbreviated project code overlaid
- **Name Logotype**: Primary identity mark in the top-left header

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
