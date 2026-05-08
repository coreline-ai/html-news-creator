# Chat for impact - Colorful Refero Design MD

- Source: https://styles.refero.design/style/18975f37-2e5d-47ca-9367-8b201d20390d
- Original site: https://www.turn.io
- Theme: `mixed`
- Color rank: **12**
- Colorfulness score: `41.5`
- Recommended fit: **Colorful SaaS accent system**

## North star
WhatsApp chat through a forest canvas

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Canopy | `#0a3922` | brand | Hero background, prominent section backgrounds, deep green accent for various elements. Conveys growth and trust |
| Vivid Green | `#1dbf73` | brand | Green outline accent for tags, dividers, and focused UI edges |
| Sunset Orange | `#ff643b` | brand | Primary call-to-action button background. Commands attention with warmth and urgency |
| Deep Violet | `#460095` | brand | Violet outline accent for tags, dividers, and focused UI edges. Do not promote it to the primary CTA color |
| Misty Rose | `#47264c` | brand | Muted background tones, secondary accents. Adds a subtle, complementary warmth |
| Sky Blue | `#00b4dc` | brand | Supportive accent, informational highlights. Suggests clarity and technology |
| Midnight Teal | `#003642` | brand | Dark text for headlines on light backgrounds, subtle accent colors. Provides a deep, authoritative tone |
| Lavender Mist | `#eee2ff` | neutral | Light background fill, card backgrounds on light sections. Softens the overall palette |

```css
:root {
  --colorful-forest-canopy: #0a3922;
  --colorful-vivid-green: #1dbf73;
  --colorful-sunset-orange: #ff643b;
  --colorful-deep-violet: #460095;
  --colorful-misty-rose: #47264c;
  --colorful-sky-blue: #00b4dc;
  --colorful-midnight-teal: #003642;
}
```

## Typography direction
- Primary: **DM Sans**; substitute `system-ui`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
