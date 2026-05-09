# Bpowell - Refero Design MD

- Source: https://styles.refero.design/style/7afd842e-44d4-4f01-9ef5-683c31d820c9
- Original site: https://www.bpowell.co
- Theme: `mixed`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
gallery wall typography

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Black | `#111111` | neutral | Primary text or dark surface |
| Deep Gray | `#2b2b2b` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #000000;
  --ref-charcoal-black: #111111;
  --ref-deep-gray: #2b2b2b;
}
```

## Typography direction
- **Diatype**: 500, 700, 26px, 58px, 1.04, 1.05, 1.15; substitute `Inter`.
- **Beatricedisplay**: 500, 600, 26px, 1.15; substitute `PP Editorial New`.
- **Teg**: 500, 600, 58px, 86px, 1.04, 1.05; substitute `Monument Grotesk`.

## Spacing / shape
- Section Gap: `104px`
- Card Padding: `24px`
- Element Gap: `16px`
- Radius: `none: 0px`

## Component cues
- **Navigation Bar Item**: Header and footer navigation (text links)
- **Project Title Link**: Interactive project list items
- **Section Heading (Uppercase)**: Categorical section headers
- **Subsection Label**: Subtle visual separators for content blocks

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
