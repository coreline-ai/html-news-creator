# Paste - Colorful Refero Design MD

- Source: https://styles.refero.design/style/742b500d-3e10-4daa-bb89-d0d26272e5f6
- Original site: https://pasteapp.io
- Theme: `light`
- Color rank: **16**
- Colorfulness score: `41.0`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Amber lantern on white marble - the brand's warm gradient logo floats in vast white space, like a single lit window in a snow-covered building.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Amber Flame | `#f06413` | brand | Logo, brand mark, gradient start - the warm orange anchors the entire identity as the only chromatic element on a monoc. |
| Honey Glow | `#feab30` | brand | Logo gradient end, warm highlight - lifts the amber into golden territory, visible in section headings and brand accents |
| Signal Blue | `#0088ff` | accent | Primary CTA buttons, interactive links - cool blue against warm-amber brand creates intentional temperature contrast th. |
| Bright Blue | `#1c95ff` | accent | Hover/active state for blue CTAs, secondary interactive highlights |
| Pure White | `#ffffff` | neutral | Primary page background, card surfaces, hero sections |
| Snow Gray | `#f5f5f7` | neutral | Alternating section backgrounds, subtle surface differentiation from white |
| Mist | `#f0f0f0` | neutral | Divider backgrounds, subtle containers |
| Silver | `#d0d0d3` | neutral | Borders, decorative dividers |

```css
:root {
  --colorful-amber-flame: #f06413;
  --colorful-honey-glow: #feab30;
  --colorful-signal-blue: #0088ff;
  --colorful-bright-blue: #1c95ff;
  --colorful-pure-white: #ffffff;
  --colorful-snow-gray: #f5f5f7;
  --colorful-mist: #f0f0f0;
}
```

## Typography direction
- Primary: **system-ui**; substitute `SF Pro Display / SF Pro Text (system default on Apple), Inter on non-Apple syst.`.
- Secondary/code: **Inter**; substitute `Inter (Google Fonts)`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
