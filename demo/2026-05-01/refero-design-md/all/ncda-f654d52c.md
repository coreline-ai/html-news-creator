# NCDA - Refero Design MD

- Source: https://styles.refero.design/style/f654d52c-42de-4f3b-a377-9287b1536ad0
- Original site: https://ncda.biz
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprint on white marble

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| NCDA Black | `#191919` | neutral | Primary text or dark surface |
| Absolute Zero | `#000000` | neutral | Primary text or dark surface |
| Ghost Gray | `#808080` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ncda-black: #191919;
  --ref-absolute-zero: #000000;
  --ref-ghost-gray: #808080;
}
```

## Typography direction
- **TWK Everett**: 400, 11px, 15px, 21px, 32px, 62px, 0.80, 1.20, 1.35, 1.40, 1.44; substitute `Inter`.
- **TWK Everett Mono**: 400, 21px, 0.80; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `28px`
- Element Gap: `15px`
- Radius: `none: 0px`

## Component cues
- **Navigation Link**: Primary navigation item
- **Menu Link**: Menu trigger and secondary navigation
- **Body Text Block**: Standard paragraph content
- **Section Heading**: Major content section titles
- **Monospace Time Display**: Displaying time or highly precise data

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
