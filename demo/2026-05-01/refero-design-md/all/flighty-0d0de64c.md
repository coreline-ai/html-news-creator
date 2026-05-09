# Flighty - Refero Design MD

- Source: https://styles.refero.design/style/0d0de64c-1891-4984-9e12-8976e042ce11
- Original site: https://flighty.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Inky depths over clear white

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Deep Space | `#05010d` | neutral | Primary text or dark surface |
| Abyssal Black | `#010a1a` | neutral | Primary text or dark surface |
| Shadow Gray | `#333333` | neutral | Primary text or dark surface |
| Muted Ash | `#595959` | neutral | Border, muted text, or supporting surface |
| Ocean Blue | `#007bff` | brand | Action accent / signal color |
| Goldenrod | `#f7be00` | brand | Action accent / signal color |
| Deep Violet | `#0d0021` | accent | Action accent / signal color |
| Forest Green | `#002111` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-midnight-ink: #000000;
  --ref-deep-space: #05010d;
  --ref-abyssal-black: #010a1a;
  --ref-shadow-gray: #333333;
  --ref-muted-ash: #595959;
  --ref-ocean-blue: #007bff;
  --ref-goldenrod: #f7be00;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `Arial`.
- **system-ui**: 400, 500, 600, 700, 13px, 15px, 16px, 17px, 22px, 32px, 56px, 1.00, 1.10, 1.20, 1.38, 1.50, 2.00; substitute `Inter`.
- **EB Garamond**: 700, 24px, 0.90; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `tags: 999px, cards: 12px, images: 12px, buttons: 40px, accentedCards: 20px`

## Surface cues
- **Canvas White** `#ffffff`: Base page background.
- **Raised Card** `#faf8f7`: Slightly elevated background for content blocks, less prominent than standard cards.
- **Standard Card** `#ffffff`: Default card background with subtle shadow for content grouping.
- **Dark Overlay Card** `#05010d`: Dark section overlays or backgrounds, contrasting with the light theme, often with transparent or dark card backgrounds.

## Component cues
- **Primary Action Button**: Filled button for main calls to action.
- **Ghost Button**: Outlined button for secondary actions.
- **Standard Card**: Content container with subtle elevation.
- **Raised Card**: More prominent content container with stronger elevation.
- **Dark Overlay Card**: Card used on dark backgrounds, often in hero sections or feature blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
