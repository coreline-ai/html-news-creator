# Linktr - Colorful Refero Design MD

- Source: https://styles.refero.design/style/b04c379c-7c33-4d69-8882-8d85d7768654
- Original site: https://linktr.ee
- Theme: `light`
- Color rank: **06**
- Colorfulness score: `46.1`
- Recommended fit: **Playful visual exploration**

## North star
Vibrant digital playground: link in bio as a personal, colorful hub

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Green | `#254f1a` | brand | Decorative card backgrounds, accent text on light backgrounds - conveys growth and natural energy |
| Chartreuse Pop | `#d2e823` | brand | Primary action button backgrounds, highlighted card accents, energetic background fill. This vivid lime serves as the m. |
| Hydrangea Blue | `#2665d6` | brand | Hero section backgrounds, prominent links, accent for specific UI elements - a complementary, strong color that frames. |
| Dahlia Purple | `#502274` | brand | Decorative background sections, signaling depth and richness |
| Currant Red | `#780016` | brand | Decorative card backgrounds, strong accent where high contrast and intensity are desired |
| Lavender Mist | `#e9c0e9` | brand | Elevated card backgrounds, soft button fills, decorative section backgrounds |
| Iris Blue | `#061492` | brand | Button backgrounds, card backgrounds, a profound, darker blue for functional elements |
| Goldenrod | `#d6a337` | accent | Distinct card backgrounds for callouts or special features |

```css
:root {
  --colorful-forest-green: #254f1a;
  --colorful-chartreuse-pop: #d2e823;
  --colorful-hydrangea-blue: #2665d6;
  --colorful-dahlia-purple: #502274;
  --colorful-currant-red: #780016;
  --colorful-lavender-mist: #e9c0e9;
  --colorful-iris-blue: #061492;
}
```

## Typography direction
- Primary: **Arial**; substitute `Helvetica Neue`.
- Secondary/code: **Linksans Linksansvf**; substitute `Inter`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
