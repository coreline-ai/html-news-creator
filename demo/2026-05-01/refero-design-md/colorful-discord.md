# Discord - Colorful Refero Design MD

- Source: https://styles.refero.design/style/faec4b0c-cf93-4150-97de-0a8e7eed1840
- Original site: https://discord.com
- Theme: `dark`
- Color rank: **32**
- Colorfulness score: `32.4`
- Recommended fit: **Colorful SaaS accent system**

## North star
Game world behind a chat bubble - every section is a self-contained environment with its own lighting and cast of characters.

## Why this fits html-news-creator
Use as a controlled accent palette for admin or subscriber screens without changing the whole product language.

## Apply to
- CTA and badge accents
- Category color systems
- Demo card variants

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Blurple | `#5865f2` | brand | Primary CTA buttons, brand icon, active states - the single chromatic anchor in a near-monochrome blue-black space, cre. |
| Dark Blurple | `#3442d9` | brand | Hover state for primary buttons, pressed states |
| Hover Blurple | `#8891f2` | brand | Button hover tint, elevated blurple interactions |
| Spring Green | `#57f287` | semantic | Online status indicators, success states |
| Fuchsia | `#eb459` | accent | Nitro gradient accents, special event highlights |
| Vivid Cerulean | `#00b0f4` | accent | Voice/video channel indicators, info states |
| Ember Orange | `#fda220` | accent | Quest indicators, achievement highlights |
| Ekko Red | `#de2761` | semantic | Destructive actions, critical alerts |

```css
:root {
  --colorful-blurple: #5865f2;
  --colorful-dark-blurple: #3442d9;
  --colorful-hover-blurple: #8891f2;
  --colorful-spring-green: #57f287;
  --colorful-fuchsia: #eb459;
  --colorful-vivid-cerulean: #00b0f4;
  --colorful-ember-orange: #fda220;
}
```

## Typography direction
- Primary: **ABC Ginto Nord Discord**; substitute `Nunito Black, Poppins 800, or Rounded Mplus 1c 800`.
- Secondary/code: **ABC Ginto Discord**; substitute `Inter, DM Sans, or Nunito 400/500`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
