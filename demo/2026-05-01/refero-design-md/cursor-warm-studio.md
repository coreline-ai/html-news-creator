# Cursor - Refero Design MD

- Source: https://styles.refero.design/style/4e3b4717-84c8-4599-baaf-a343c3d619b6
- Original site: https://cursor.com
- Theme: `light`
- Recommended fit: **Developer-facing Webapp / Focus Cards**
- Priority: **P2**

## Why this fits html-news-creator
Warm developer-tool studio direction for admin screens and demo browsing: compact density, tactile surfaces, and precise technical type.

## Apply to
- New report option panel
- Compact source ledger
- Demo index cards and editor-like screens

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas Parchment | `#f7f7f4` | neutral | Page backgrounds, card backgrounds, neutral button backgrounds - provides a soft, warm foundation. |
| Inkwell | `#262510` | neutral | Primary text, strong borders, navigation text - grounds the lighter surfaces with significant contrast. |
| Muted Stone | `#7a7974` | neutral | Secondary text, subtle borders, icon fills - a mid-tone gray for less prominent information or structural lines. |
| Deep Shadow | `#141414` | neutral | Deepest text variant - for maximum contrast on headlines or critical information. |
| Pebble Gray | `#e6e5e0` | neutral | Hover states on neutral buttons, subtle card backgrounds - visually lighter than Canvas Parchment, indicating elevation. |
| Onyx Outline | `#f54e00` | accent | Outlined action button borders and link text - a vibrant orange indicating interactive elements without a solid fill. |
| Chartreuse Alert | `#4ade80` | accent | supporting accents, small interactive text snippets - a vivid green for positive or noteworthy cues, often within code examples. |
| Goldenrod Accent | `#c08532` | accent | Accent for specific interactive states or icons, often found in button backgrounds for 'Build' actions. |

```css
:root {
  --ref-canvas-parchment: #f7f7f4;
  --ref-inkwell: #262510;
  --ref-muted-stone: #7a7974;
  --ref-deep-shadow: #141414;
  --ref-pebble-gray: #e6e5e0;
  --ref-onyx-outline: #f54e00;
  --ref-chartreuse-alert: #4ade80;
}
```

## Typography direction
- Primary: **CursorGothic**; substitute `system-ui`.
- Secondary/code: **berkeleyMono**; substitute `monospace`.

## Spacing / shape
- Section gap: `43px`
- Card padding: `12px`
- Element gap: `8px`
- Radius: `{'cards': '4px', 'buttons': '4px', 'general': '4px', 'prominent': '8px'}`

## Agent notes
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- Keep the project content hierarchy first: section title, why it matters, source evidence, confidence, and image evidence.
