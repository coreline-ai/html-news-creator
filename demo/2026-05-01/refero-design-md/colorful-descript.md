# Descript - Colorful Refero Design MD

- Source: https://styles.refero.design/style/fe955d4a-c56d-4ab0-a6b3-8d985ab9570c
- Original site: https://descript.com
- Theme: `mixed`
- Color rank: **11**
- Colorfulness score: `42.2`
- Recommended fit: **Colorful editorial / creator page**

## North star
Broadcast booth meets editorial press - deep burgundy theater dark, editorial serif headlines, coral on-air signals.

## Why this fits html-news-creator
Use for richer report storytelling while keeping the reading structure intact.

## Apply to
- Story-led report section variants
- Newsletter-style summaries
- Image evidence callouts

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Broadcast Burgundy | `#390a1a` | brand | Hero backgrounds, primary dark surface - creates the theater-dark immersion that makes coral CTAs read as on-air signals |
| On-Air Coral | `#f73b3b` | brand | Primary CTA buttons, active section labels - the single vivid signal against deep burgundy dark |
| Hot Take Red | `#ff5340` | accent | Inline text highlights, secondary accent emphasis in body copy |
| Plum Mid | `#651a39` | brand | Nav hover states, secondary button backgrounds - one step lighter than Broadcast Burgundy for interactive depth |
| Deep Violet | `#0c0b5f` | accent | Inline links and callout text in light sections - a cool contrast to the otherwise warm palette |
| Soft Violet | `#8787e0` | accent | Underlord AI feature accent - used on AI chat interface send button |
| Pale Peach | `#ffe8db` | neutral | Card backgrounds for feature cards in warm sections |
| Blush Mist | `#f1eaed` | neutral | Card backgrounds for testimonial and feature content cards in light sections |

```css
:root {
  --colorful-broadcast-burgundy: #390a1a;
  --colorful-on-air-coral: #f73b3b;
  --colorful-hot-take-red: #ff5340;
  --colorful-plum-mid: #651a39;
  --colorful-deep-violet: #0c0b5f;
  --colorful-soft-violet: #8787e0;
  --colorful-pale-peach: #ffe8db;
}
```

## Typography direction
- Primary: **Booton**; substitute `Source Sans Pro, IBM Plex Sans`.
- Secondary/code: **Gamuth Display**; substitute `Playfair Display, Fraunces`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
