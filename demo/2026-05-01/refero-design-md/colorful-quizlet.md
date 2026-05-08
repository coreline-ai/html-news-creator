# Quizlet - Colorful Refero Design MD

- Source: https://styles.refero.design/style/528eb1d4-8508-4dc6-87b4-c7b92d648dac
- Original site: https://quizlet.com
- Theme: `light`
- Color rank: **09**
- Colorfulness score: `43.3`
- Recommended fit: **Playful visual exploration**

## North star
Academic Playground on Soft Gray. Like a well-organized desk scattered with colorful learning tools.

## Why this fits html-news-creator
Use for bolder demo pages, visual report cards, and subscriber-facing moments that can tolerate a more expressive tone.

## Apply to
- Visual Board and Focus Cards variants
- Empty states and onboarding moments
- Subscriber UI accent experiments

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Stormcloud Ink | `#282e3` | neutral | Primary text, deep context elements, input text, prominent icons. |
| Quizlet Violet | `#4255ff` | brand | Primary interactive elements, main CTA buttons, active links, important icons, defining Quizlet's brand identity. |
| Sky Study | `#98e3ff` | accent | Decorative background for 'Learn' card, adding a moderate, fresh accent. |
| Flashcard Pink | `#eeaaff` | accent | Decorative background for 'Study Guides' card, adding a playful, vivid accent. |
| Night Violet | `#423ed8` | accent | Decorative background for 'Flashcards' card, a darker, more intense variant of the brand violet. |
| Practice Orange | `#ffc38c` | accent | Decorative background for 'Practice Tests' card, a moderate, warm accent. |
| Slate Text | `#586380` | neutral | Secondary text, less prominent icons, button outlines, subtle informational text. |
| Light Slate | `#939bb4` | neutral | Subtle borders, inactive states, lighter text elements for hierarchical distinction. |

```css
:root {
  --colorful-stormcloud-ink: #282e3;
  --colorful-quizlet-violet: #4255ff;
  --colorful-sky-study: #98e3ff;
  --colorful-flashcard-pink: #eeaaff;
  --colorful-night-violet: #423ed8;
  --colorful-practice-orange: #ffc38c;
  --colorful-slate-text: #586380;
}
```

## Typography direction
- Primary: **hurme_no2-webfont**; substitute `system-ui, sans-serif`.
- Secondary/code: **monospace**; substitute `monospace`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
