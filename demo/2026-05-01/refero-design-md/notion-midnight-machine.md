# Notion - Refero Design MD

- Source: https://styles.refero.design/style/2bf4c61f-de10-4614-ba1b-20c0453bd2a9
- Original site: https://notion.so
- Theme: `dark`
- Recommended fit: **Dark premium dashboard**

## North star
Midnight machine hum - a deep indigo backdrop with precise, glowing elements that guide action.

## Why this fits html-news-creator
Useful as a high-contrast alternative for operator and executive views.

## Apply to
- Dark dashboard shells
- Premium subscriber surfaces
- Status-heavy UI states

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#02093a` | neutral | Primary background for dark sections, elevated card surfaces, and navigation elements. Provides depth as a foundational. |
| Canvas Dark | `#000000` | neutral | Base page background, navigation borders, and primary text on light surfaces. Serves as the darkest neutral in the syst. |
| Ghost White | `#f6f5f4` | neutral | Light background for sections or secondary buttons. Provides contrast against darker neutrals. |
| Paper White | `#ffffff` | neutral | Text on dark backgrounds, interactive elements' text, and card backgrounds in light sections. Acts as the primary light. |
| Deep Graphite | `#0b0b0b` | neutral | Dark text and borders on light surfaces, providing heavier visual weight than standard Canvas Dark. |
| Blue Frost | `#62aef0` | brand | Highlight elements, decorative accents, and subtle background fills. Evokes a cool, digital glow. |
| Ocean Glimmer | `#0075de` | accent | Interactive link text, borders for ghost buttons, and secondary action calls. A vibrant blue for clarity. |
| Sky Surge | `#097fe8` | semantic | Informational badges, active navigation states, and subtle decorative fills. Slightly brighter than Ocean Glimmer, for. |

```css
:root {
  --ref-midnight-ink: #02093a;
  --ref-canvas-dark: #000000;
  --ref-ghost-white: #f6f5f4;
  --ref-paper-white: #ffffff;
  --ref-deep-graphite: #0b0b0b;
  --ref-blue-frost: #62aef0;
  --ref-ocean-glimmer: #0075de;
}
```

## Typography direction
- Primary: **NotionInter**; substitute `Inter`.
- Secondary/code: **Lyon Text**; substitute `Georgia`.

## Spacing / shape
- Section gap: `32px`
- Card padding: `24px`
- Element gap: `8px`
- Radius: `{'cards': '12px', 'badges': '9999px', 'inputs': '4px', 'buttons': '8px', 'general': '5px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
