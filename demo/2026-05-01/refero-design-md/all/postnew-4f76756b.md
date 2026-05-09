# PostNew - Refero Design MD

- Source: https://styles.refero.design/style/4f76756b-0f06-47a3-baad-d3846b23e132
- Original site: https://www.postnew.xyz
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight gallery showcase

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Black | `#000000` | neutral | Primary text or dark surface |
| Charcoal Canvas | `#1a1a1a` | neutral | Primary text or dark surface |
| Active Charcoal | `#242424` | neutral | Primary text or dark surface |
| Whisper Gray | `#fafafa` | neutral | Page background or card surface |
| Muted Interaction | `#5d5d5d` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-pitch-black: #000000;
  --ref-charcoal-canvas: #1a1a1a;
  --ref-active-charcoal: #242424;
  --ref-whisper-gray: #fafafa;
  --ref-muted-interaction: #5d5d5d;
}
```

## Typography direction
- **sans-serif**: 400, 12px, 1.20; substitute `system-ui`.
- **ABC Diatype**: 500, 18px, 22px, 1.13, 1.15; substitute `Inter, Arial`.

## Spacing / shape
- Section Gap: `50px`
- Card Padding: `12px`
- Element Gap: `10px`
- Radius: `tabs: 0px, cards: 0px, buttons: 0px`

## Surface cues
- **Charcoal Canvas** `#1a1a1a`: Primary page background layer, serving as the base for all content.
- **Active Charcoal** `#242424`: Subtle elevated surface for interactive components or minor content blocks.
- **Muted Interaction** `#5d5d5d`: Opaque interactive surfaces, such as active states for links or buttons.
- **Whisper Gray Overlay** `#fafafa`: Foreground content or text elements that require maximum contrast.

## Component cues
- **Ghost Navigation Button**: Primary navigation elements
- **Filled Navigation Button**: Contextual navigation or utility buttons

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
