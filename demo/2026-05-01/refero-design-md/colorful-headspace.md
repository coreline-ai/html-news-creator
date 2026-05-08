# Headspace - Colorful Refero Design MD

- Source: https://styles.refero.design/style/035a098b-5a27-48a3-8a3a-c68a698e3eab
- Original site: https://headspace.com
- Theme: `light`
- Color rank: **23**
- Colorfulness score: `39.3`
- Recommended fit: **Playful visual exploration**

## North star
Warm Modern Playfulness - like a friendly, brightly lit studio full of soft shapes and uplifting colors.

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Sky Connect | `#0061ef` | brand | Primary interactive elements (buttons, links, active states) - a bold commitment to guidance and support amidst the sof. |
| Sunshine Burst | `#ffce00` | accent | Accent for illustrations, banners, and hero backgrounds - injects energetic warmth and optimism. |
| Deep Plum | `#3b197f` | accent | Accent for illustrations and thematic sections - provides a rich, grounding counterpoint to brighter accents. |
| Ocean Glimmer | `#00a4ff` | accent | Accent for iconography and illustrations, suggesting clarity and serenity. |
| Blush Petal | `#ffa1cc` | accent | Accent in illustrations, adding softness and a touch of playfulness. |
| Forest Calm | `#02873` | accent | Accent in illustrations, symbolizing growth and tranquility. |
| Inkwell Gray | `#4b4c4d` | neutral | Dominant body text, strong headings, button text - balances the soft background with clear readability. |
| True Black | `#000000` | neutral | Highest contrast text, input text - used sparingly for emphasis. |

```css
:root {
  --colorful-sky-connect: #0061ef;
  --colorful-sunshine-burst: #ffce00;
  --colorful-deep-plum: #3b197f;
  --colorful-ocean-glimmer: #00a4ff;
  --colorful-blush-petal: #ffa1cc;
  --colorful-forest-calm: #02873;
  --colorful-inkwell-gray: #4b4c4d;
}
```

## Typography direction
- Primary: **Headspace Apercu**; substitute `system-ui, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
