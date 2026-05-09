# iconwerk - Refero Design MD

- Source: https://styles.refero.design/style/6e22b676-90e0-4e1a-a230-2b52f331d0e4
- Original site: https://www.iconwerk.com
- Theme: `light`
- Industry: `design`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery of crisp forms

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-ink-black: #000000;
}
```

## Typography direction
- **Arial**: 400, 14px, 1.21; substitute `Arial, Helvetica, sans-serif`.
- **Graphik**: 400, 600, 16px, 21px, 22px, 24px, 1.18, 1.19, 1.21; substitute `Inter, ui-sans-serif, system-ui`.

## Spacing / shape
- Section Gap: `45px`
- Card Padding: `18px`
- Element Gap: `5px`
- Radius: `tags: 28px, cards: 28px, buttons: 28px`

## Component cues
- **Icon Card**: Container for individual icon examples
- **Contact Button**: Primary call to action.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
