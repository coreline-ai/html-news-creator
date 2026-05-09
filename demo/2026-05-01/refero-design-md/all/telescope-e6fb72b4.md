# Telescope - Refero Design MD

- Source: https://styles.refero.design/style/e6fb72b4-877d-46ab-8f94-590b971d4dc1
- Original site: https://telescope.fyi
- Theme: `light`
- Industry: `other`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm parchment, scattered Polaroids

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Soft Vanilla | `#f4f3f0` | neutral | Page background or card surface |
| Deep Graphite | `#1a1915` | neutral | Primary text or dark surface |
| Spring Bud | `#e3f794` | brand | Action accent / signal color |
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#82868e` | neutral | Border, muted text, or supporting surface |
| Pure Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-soft-vanilla: #f4f3f0;
  --ref-deep-graphite: #1a1915;
  --ref-spring-bud: #e3f794;
  --ref-white-canvas: #ffffff;
  --ref-ash-gray: #82868e;
  --ref-pure-black: #000000;
}
```

## Typography direction
- **Beausite**: 400, 19px, 23px, 55px, 57px, 1.05, 1.15; substitute `system-ui`.
- **DM Mono**: 400, 12px, 1.10; substitute `Menlo`.
- **CM Geom**: 400, 250px, 1.00; substitute `system-ui`.

## Spacing / shape
- Section Gap: `135px`
- Card Padding: `0px`
- Element Gap: `10px`
- Radius: `cards: 0px, buttons: 0px, default: 2px`

## Surface cues
- **Soft Vanilla Canvas** `#f4f3f0`: Primary page background and default content area.
- **White Canvas** `#ffffff`: Secondary background for specific interactive areas or contained content sections.
- **Spring Bud Accent** `#e3f794`: Highlight surfaces, interactive states, or small decorative fills.

## Component cues
- **Ghost Button**: Secondary action button
- **Accent Filled Button**: Primary action button
- **Information Badge**: Informational tag
- **Floating Content Card**: Visual content container

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
