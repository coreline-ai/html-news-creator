# Pitch - Colorful Refero Design MD

- Source: https://styles.refero.design/style/da332394-784c-4df2-9e66-c3f7b1d28f28
- Original site: https://pitch.com
- Theme: `light`
- Color rank: **34**
- Colorfulness score: `31.8`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Vibrant Violet Gradient Canvas

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Pitch Violet | `#8d49f7` | brand | Primary brand color, used for active links, icons, and significant accents. It provides visual energy and indicates int. |
| Deep Violet | `#6b53ff` | brand | Secondary brand color, appearing in badges, card elements, and as a strong accent. It provides depth to the violet pale. |
| Midnight Graphite | `#1e1d28` | neutral | Darkest text and card backgrounds, providing high contrast against light surfaces. Used where information density or vi. |
| Action Yellow | `#ffd02c` | accent | Accentuating specific card backgrounds or illustrative elements that require high visibility, often paired with gradien. |
| Faded Shadow | `#b5b3cd` | neutral | Used for subtle card shadows, providing a soft lift without harshness. |
| Medium Gray | `#3f4250` | neutral | Mid-tone text and borders, offering a slightly softer alternative to Midnight Graphite for less prominent text. |
| Button Gray | `#6f7387` | neutral | Default text color for secondary buttons, balancing visibility with a muted appearance. |
| Bright Violet | `#586ee0` | accent | Used for illustrative fills and minor accent details within graphics, adding vibrancy. |

```css
:root {
  --colorful-pitch-violet: #8d49f7;
  --colorful-deep-violet: #6b53ff;
  --colorful-midnight-graphite: #1e1d28;
  --colorful-action-yellow: #ffd02c;
  --colorful-faded-shadow: #b5b3cd;
  --colorful-medium-gray: #3f4250;
  --colorful-button-gray: #6f7387;
}
```

## Typography direction
- Primary: **Eina01**; substitute `Inter`.
- Secondary/code: **Mark Pro**; substitute `Montserrat`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
