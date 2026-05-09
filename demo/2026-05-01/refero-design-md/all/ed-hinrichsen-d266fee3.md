# Ed Hinrichsen - Refero Design MD

- Source: https://styles.refero.design/style/d266fee3-7479-4725-b727-e343ccefb576
- Original site: https://www.edwardh.io
- Theme: `light`
- Industry: `other`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Retro terminal interface.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Vanilla Dust | `#f6d4b1` | accent | Action accent / signal color |
| System Gray | `#525252` | neutral | Border, muted text, or supporting surface |
| Pixel Black | `#000000` | neutral | Primary text or dark surface |
| Warm Sand | `#cdb499` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-vanilla-dust: #f6d4b1;
  --ref-system-gray: #525252;
  --ref-pixel-black: #000000;
  --ref-warm-sand: #cdb499;
}
```

## Typography direction
- **chill**: 400, 700, 12px, 18px, 1.20, 1.50; substitute `IBM Plex Mono`.
- **public-pixel**: 400, 700, 22px, 36px, 1.20; substitute `Press Start 2P`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `8px`
- Element Gap: `16px`
- Radius: `buttons: 0px, default: 0px`

## Component cues
- **Outlined Terminal Button**: Primary Call to Action
- **Project Card**: Content Display Card
- **Dashed Divider**: Visual Separator
- **Page Header Nav Item**: Navigation Link
- **Tag / Skill Badge**: Categorization Label

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
