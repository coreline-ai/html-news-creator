# Videoconferencia - Colorful Refero Design MD

- Source: https://styles.refero.design/style/206c6c51-df38-425f-8d07-b0cc9dd065cf
- Original site: https://microsoft.com/teams
- Theme: `light`
- Color rank: **41**
- Colorfulness score: `29.6`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Collaborative daylight workspace - every surface a white panel under fluorescent clarity, single violet pulse marking where to act.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Teams Violet | `#5d5bd4` | brand | Primary CTA buttons, active nav underlines, badge backgrounds - the single saturated signal on an otherwise achromatic. |
| Teams Midnight | `#333275` | brand | Hover and pressed states for Teams Violet buttons, nav link active text - darker violet that deepens without shifting h. |
| Teams Deep | `#424197` | brand | Button pressed/focus states - intermediate violet between Teams Violet and Teams Midnight. |
| Microsoft Blue | `#0067b8` | accent | Link text, icon fills, navigation affordances - the legacy Microsoft hyperlink blue used on informational elements, nev. |
| Ink Navy | `#17253d` | neutral | Primary text, headings, body copy, icons - near-black with a distinct blue cast that avoids pure black harshness. |
| Abyss Navy | `#0e1726` | neutral | Darkest heading weight, button text on transparent dark-background variants. |
| Steel | `#616161` | neutral | Secondary body text, captions, placeholder text, icon color for inactive states. |
| Graphite | `#262626` | neutral | Nav link text, body text at medium emphasis. |

```css
:root {
  --colorful-teams-violet: #5d5bd4;
  --colorful-teams-midnight: #333275;
  --colorful-teams-deep: #424197;
  --colorful-microsoft-blue: #0067b8;
  --colorful-ink-navy: #17253d;
  --colorful-abyss-navy: #0e1726;
  --colorful-steel: #616161;
}
```

## Typography direction
- Primary: **Segoe UI Variable Text**; substitute `Inter Variable`.
- Secondary/code: **Segoe UI Variable Display**; substitute `Inter Variable (display instance)`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
