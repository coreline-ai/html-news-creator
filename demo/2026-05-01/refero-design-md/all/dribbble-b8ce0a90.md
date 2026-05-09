# Dribbble - Refero Design MD

- Source: https://styles.refero.design/style/b8ce0a90-40c6-4518-940c-8c97ccf9c1a0
- Original site: https://dribbble.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall on White Linen — content as art, neutrally framed.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Stormy Night | `#0d0c22` | brand | Action accent / signal color |
| Anchor Black | `#060318` | brand | Action accent / signal color |
| Ghost Gray | `#6e6d7a` | neutral | Border, muted text, or supporting surface |
| Dribbble Pink | `#ea4c89` | accent | Action accent / signal color |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Canvas Light | `#f3f3f6` | neutral | Page background or card surface |
| Chrome Gray | `#9e9ea7` | neutral | Border, muted text, or supporting surface |
| Hint Frost | `#e2e8f2` | neutral | Page background or card surface |
| Deep Plum | `#3a3546` | neutral | Primary text or dark surface |
| Sapphire Glow | `#956bcd` | accent | Action accent / signal color |

```css
:root {
  --ref-stormy-night: #0d0c22;
  --ref-anchor-black: #060318;
  --ref-ghost-gray: #6e6d7a;
  --ref-dribbble-pink: #ea4c89;
  --ref-arctic-white: #ffffff;
  --ref-canvas-light: #f3f3f6;
  --ref-chrome-gray: #9e9ea7;
  --ref-hint-frost: #e2e8f2;
}
```

## Typography direction
- **Mona Sans**: 400, 450, 500, 600, 700, 800, 12px, 13px, 14px, 16px, 48px, 1.00 - 2.33; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `40px`
- Element Gap: `4px`
- Radius: `cards: 8px, input: 12px, links: 4px, badges: 12px, buttons: 10000px`

## Component cues
- **Search Bar with Popular Tags**: Reference component style.
- **Shot Card with Designer Info**: Reference component style.
- **Category Filter Bar with New Badge Banner**: Reference component style.
- **Primary Navigation Link**: Interactive element
- **Auth Button**: Call to action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
