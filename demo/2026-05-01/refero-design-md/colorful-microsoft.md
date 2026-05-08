# Microsoft - Colorful Refero Design MD

- Source: https://styles.refero.design/style/5f39e778-d204-42a9-8b8b-a1519dbd3971
- Original site: https://microsoft.com
- Theme: `light`
- Color rank: **47**
- Colorfulness score: `28.0`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Retail shelf behind plate glass - products float forward, chrome recedes.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Microsoft Blue | `#0067b8` | brand | All interactive elements - links, primary buttons, icon accents. A single saturated hue against a near-grayscale UI cre. |
| Deep Azure | `#004a7f` | brand | Hover and active states for links and card link colors - darkened variant of Microsoft Blue creating depth without hue. |
| Fluent Icon Blue | `#0078d4` | brand | Card image icon color per CSS token; slightly lighter than Microsoft Blue, used in Fluent UI icon contexts. |
| Amber Badge | `#ffb900` | accent | Badge background (CSS token sc-badge-bg-yellow) with black text - the only warm accent in the system, reserved for prom. |
| Void | `#000000` | neutral | Primary text, borders, SVG fills across heading, body, nav, footer. |
| Graphite | `#171717` | neutral | Ghost button text and border color; near-black for secondary interactive labels. |
| Charcoal | `#262626` | neutral | Body copy, nav text, secondary button labels. |
| Iron | `#333333` | neutral | Tertiary text contexts, muted body copy. |

```css
:root {
  --colorful-microsoft-blue: #0067b8;
  --colorful-deep-azure: #004a7f;
  --colorful-fluent-icon-blue: #0078d4;
  --colorful-amber-badge: #ffb900;
  --colorful-void: #000000;
  --colorful-graphite: #171717;
  --colorful-charcoal: #262626;
}
```

## Typography direction
- Primary: **Segoe UI**; substitute `Segoe UI (system stack: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,.`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
