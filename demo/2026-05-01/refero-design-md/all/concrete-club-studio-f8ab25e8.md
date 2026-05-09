# Concrete Club Studio - Refero Design MD

- Source: https://styles.refero.design/style/f8ab25e8-87c1-4d7b-a633-daf3ea39b916
- Original site: https://concreteclub.studio
- Theme: `mixed`
- Industry: `agency`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery Wall Typography

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Onyx Canvas | `#212121` | neutral | Primary text or dark surface |
| Frost Canvas | `#f5f6f5` | neutral | Page background or card surface |
| Gallery White | `#ffffff` | neutral | Page background or card surface |
| Tangerine Flash | `#d9462b` | brand | Action accent / signal color |
| Rose Bloom | `#e296bb` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-onyx-canvas: #212121;
  --ref-frost-canvas: #f5f6f5;
  --ref-gallery-white: #ffffff;
  --ref-tangerine-flash: #d9462b;
  --ref-rose-bloom: #e296bb;
}
```

## Typography direction
- **TRJN DaVinci**: 400, 14px, 16px, 300px, 1.14, 1.19; substitute `Georgia Pro`.
- **HelveticaNeue-Light**: 400, 26px, 48px, 112px, 1.15; substitute `Helvetica Neue`.
- **Neue Montreal**: 400, 12px, 1.17; substitute `Inter`.

## Spacing / shape
- Card Padding: `30px`
- Radius: `elements: 0px`

## Component cues
- **Hero Display Text Block**: Reference component style.
- **Dark Story Section Block**: Reference component style.
- **Ghost Navigation Header**: Reference component style.
- **Ghost Navigation Link**: Primary navigation elements
- **Hero Display Text**: Main page headline

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
