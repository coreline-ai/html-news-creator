# Smiling Wolf - Refero Design MD

- Source: https://styles.refero.design/style/75be52f8-4dbe-45da-9a0e-a11bc92f6927
- Original site: https://www.smilingwolf.co.uk
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic editorial precision

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#000000` | neutral | Primary text or dark surface |
| Paper White | `#f7f3f0` | neutral | Page background or card surface |
| Charcoal | `#131713` | neutral | Primary text or dark surface |
| Muted Ash | `#bebcb9` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#858582` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-ink-black: #000000;
  --ref-paper-white: #f7f3f0;
  --ref-charcoal: #131713;
  --ref-muted-ash: #bebcb9;
  --ref-stone-gray: #858582;
}
```

## Typography direction
- **Bagoss Standard**: 385, 400, 520, 14px, 20px, 59px, 63px, 0.98, 1.00, 1.15, 1.40; substitute `serif`.
- **General Grotesque Mono**: 400, 9px, 10px, 1.60; substitute `monospace`.
- **sans-serif**: 400, 12px, 1.20; substitute `Arial`.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `20px`
- Element Gap: `10px`
- Radius: `cards: 4px, buttons: 4px, default: 4px`

## Surface cues
- **Paper White Canvas** `#f7f3f0`: Dominant background for the overall page and most content sections, providing a soft, almost tactile base.
- **Charcoal Surface** `#131713`: Used for distinct dark sections, such as hero blocks or footers, creating a strong visual contrast against the Paper White canvas. Content surfaces…

## Component cues
- **Text Link**: Navigation, inline actions, and footer links
- **Ghost Button**: Secondary calls to action and interactive elements displayed as text links with subtle borders.
- **Footer Item**: Structured list items in the footer
- **Featured Project Card**: Showcasing project previews
- **Navigation Bar**: Main site navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
