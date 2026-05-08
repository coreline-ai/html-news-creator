# beehiiv - Colorful Refero Design MD

- Source: https://styles.refero.design/style/350b1557-56f0-4361-8c8b-b7a88081982b
- Original site: https://beehiiv.com
- Theme: `dark`
- Color rank: **45**
- Colorfulness score: `28.3`
- Recommended fit: **Colorful SaaS accent system**

## North star
Galactic Command Center. Deep space blues and purples punctuated by bright digital flares against a crisp, dark UI.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#060419` | neutral | Page background, primary dark surface. |
| Shadow Violet | `#0d0b28` | neutral | Card backgrounds, secondary dark surface for contained content, subtle borders. |
| Storm Gray | `#4e4e6c` | neutral | Disabled states, subtle text, and secondary icon fills. |
| Cloud Whisper | `#c4c2d6` | neutral | Tertiary body text, inactive links, and subtle icon details. |
| Ghost White | `#f7f5ff` | neutral | Secondary body text, content in specific UI elements. |
| Starfield White | `#ffffff` | neutral | Primary text on dark backgrounds, icon fills, button text. |
| Electric Blue | `#2f39ba` | brand | Primary brand accent, main call-to-action buttons, active states, and interactive elements. |
| Cosmic Magenta | `#ff5ec4` | brand | Secondary brand accent, highlights within specific sections, and subtle decorative elements. |

```css
:root {
  --colorful-midnight-ink: #060419;
  --colorful-shadow-violet: #0d0b28;
  --colorful-storm-gray: #4e4e6c;
  --colorful-cloud-whisper: #c4c2d6;
  --colorful-ghost-white: #f7f5ff;
  --colorful-starfield-white: #ffffff;
  --colorful-electric-blue: #2f39ba;
}
```

## Typography direction
- Primary: **Satoshi**; substitute `Inter`.
- Secondary/code: **Clash Grotesk**; substitute `Archivo`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
