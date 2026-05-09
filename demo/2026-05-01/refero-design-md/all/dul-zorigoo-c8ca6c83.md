# Dul Zorigoo - Refero Design MD

- Source: https://styles.refero.design/style/c8ca6c83-3197-4b19-af1c-b29d6f829c5f
- Original site: https://dzrgo.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome, text-first workbench.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#ffffff` | neutral | Page background or card surface |
| Tarmac | `#252525` | neutral | Primary text or dark surface |
| Fog | `#ebebeb` | neutral | Page background or card surface |
| Asphalt | `#a8a8a8` | neutral | Border, muted text, or supporting surface |
| Pebble | `#8e8e8e` | neutral | Border, muted text, or supporting surface |
| Midnight | `#000000` | accent | Action accent / signal color |
| Ivory | `#fbfbfb` | neutral | Page background or card surface |

```css
:root {
  --ref-canvas: #ffffff;
  --ref-tarmac: #252525;
  --ref-fog: #ebebeb;
  --ref-asphalt: #a8a8a8;
  --ref-pebble: #8e8e8e;
  --ref-midnight: #000000;
  --ref-ivory: #fbfbfb;
}
```

## Typography direction
- Use the project default stack: Pretendard / Inter / system-ui.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `8px`
- Element Gap: `6px`
- Page Max Width: `1137px`
- Radius: `links: 8px, buttons: 8px`

## Component cues
- **Ghost Filter Button**: Used for navigation and filtering categories
- **Pill Filter Button**: Used for navigation and filtering categories
- **Active Pill Button**: Indicates the currently selected filter or category.
- **Thumbnail Card**: Displays content previews, typically an image with a text label below.
- **Subtle Link**: Standard inline links and navigation items within sidebars.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
