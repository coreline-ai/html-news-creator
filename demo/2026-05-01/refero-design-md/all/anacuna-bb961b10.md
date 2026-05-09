# Anacuna - Refero Design MD

- Source: https://styles.refero.design/style/bb961b10-d437-4023-9201-a44349fe591f
- Original site: https://anacuna.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type-first stark canvas

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Flamingo Pink | `#ffc8c8` | accent | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-flamingo-pink: #ffc8c8;
}
```

## Typography direction
- **ABCMonumentGrotesk-Regular**: 400, 15px, 31px, 94px, 1.00, 1.11; substitute `Space Grotesk, Montserrat, Inter`.

## Spacing / shape
- Card Padding: `14px`
- Element Gap: `7px`
- Radius: `tags: 27.4285px, buttons: 27.4285px`

## Component cues
- **Navigation Button**: Secondary navigation and utility buttons
- **Brand Tag**: Primary brand identifier button in the header
- **Section Separator**: Visual division between list items and main content sections
- **Headline Link with Tag**: Main content items combining a large headline with an associated descriptive tag

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
