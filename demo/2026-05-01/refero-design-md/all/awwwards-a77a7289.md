# Awwwards - Refero Design MD

- Source: https://styles.refero.design/style/a77a7289-3438-46ba-8194-214739e47514
- Original site: https://awwwards.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Monochrome Grid Blueprint

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Graphite | `#222222` | neutral | Primary text or dark surface |
| Arctic White | `#ffffff` | neutral | Page background or card surface |
| Pale Ash | `#e9e9e9` | neutral | Page background or card surface |
| Deep Pewter | `#808080` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#dedede` | neutral | Page background or card surface |
| Sunset Orange | `#fa5d29` | accent | Action accent / signal color |
| Lemon Zest | `#fff083` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-graphite: #222222;
  --ref-arctic-white: #ffffff;
  --ref-pale-ash: #e9e9e9;
  --ref-deep-pewter: #808080;
  --ref-silver-mist: #dedede;
  --ref-sunset-orange: #fa5d29;
  --ref-lemon-zest: #fff083;
}
```

## Typography direction
- **Inter Tight**: 300, 400, 500, 600, 10px, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 19px, 21px, 22px, 24px, 32px, 42px, 127px, 0.93, 1.00, 1.10, 1.17, 1.20, 1.27, 1.29, 1.36, 1.44, 1.45, 1.50, 1.70, 1.75, 1.87, 2.00, 2.15, 2.40, 3.00; substitute `Inter`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `8px`
- Element Gap: `4px`
- Radius: `none: 0px, small: 4px, default: 8px, cardInteractive: 14px`

## Component cues
- **Site of the Day Header Card**: Reference component style.
- **Bottom Navigation Tab Bar**: Reference component style.
- **Search Input Field**: Reference component style.
- **Primary Ghost Button**: Navigation, secondary actions
- **Solid Dark Button**: Call-to-action, primary action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
