# The Fascination The Fascination - Refero Design MD

- Source: https://styles.refero.design/style/9c60e0a4-a702-49af-9fc1-52edbc9dd902
- Original site: https://thefascination.com
- Theme: `light`
- Industry: `media`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Editorial content on a crisp canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Storm Gray | `#1a202c` | neutral | Primary text or dark surface |
| Graphite | `#1f2937` | neutral | Primary text or dark surface |
| Silver Ash | `#767676` | neutral | Border, muted text, or supporting surface |
| Sky Blue | `#2ea3f2` | accent | Action accent / signal color |
| Twilight Violet | `#454ad3` | brand | Action accent / signal color |
| Plum Hue | `#4c40e0` | brand | Action accent / signal color |
| Neon Purple | `#9333ea` | accent | Action accent / signal color |
| Ghost White | `#fbfbf7` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight: #000000;
  --ref-storm-gray: #1a202c;
  --ref-graphite: #1f2937;
  --ref-silver-ash: #767676;
  --ref-sky-blue: #2ea3f2;
  --ref-twilight-violet: #454ad3;
  --ref-plum-hue: #4c40e0;
  --ref-neon-purple: #9333ea;
}
```

## Typography direction
- **Graphik**: 100, 400, 500, 700, 12px, 14px, 16px, 18px, 20px, 24px, 30px, 96px, 0.80, 1.00, 1.02, 1.20, 1.33, 1.50, 1.53, 1.70, 1.91, 2.19, 2.55; substitute `system-ui, sans-serif`.
- **Qwitcher Grypen**: 400, 48px, 60px; substitute `cursive`.

## Spacing / shape
- Section Gap: `32px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `links: 6px, buttons: 6px`

## Surface cues
- **Canvas** `#fbfbf7`: Dominant page background, providing a clean white base for all content.

## Component cues
- **Primary Filled Button**: Call-to-action button for core interactions.
- **Ghost Accent Button**: Secondary action button for less prominent interactions.
- **Text Link**: Inline navigation and contextual links.
- **Input Field**: Standard text input element.
- **Card Item**: Container for individual content pieces like articles or product listings.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
