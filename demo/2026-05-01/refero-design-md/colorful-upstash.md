# Upstash - Colorful Refero Design MD

- Source: https://styles.refero.design/style/e050061c-346d-44cc-92ba-6b22beb4a91f
- Original site: https://upstash.com
- Theme: `light`
- Color rank: **46**
- Colorfulness score: `28.2`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Crisp alpine air and digital green fields. A refreshing clarity guides every element, grounded by natural gradients.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Pine | `#022c22` | neutral | Primary text across the site, interactive elements in their default state, navigation links. Creates a deep, serious fo. |
| Spring Bud | `#00bc7d` | brand | Primary action buttons, prominent icons, and key highlights. Its vividness signals interaction and success against the. |
| Evergreen | `#007a55` | brand | Subtle interactive states for links and icons, offering a slightly muted version of Spring Bud for secondary actions or. |
| Sky Mist | `#e5e7eb` | neutral | Borders for cards, buttons, and other UI elements, creating soft definition. Also used as background for subtle seconda. |
| Paper White | `#ffffff` | neutral | Dominant page background, text on dark backgrounds, and card surfaces. Establishes the light theme. |
| Graphite | `#71717b` | neutral | Secondary text, muted interactive elements, and navigation items. Provides softer contrast than Forest Pine for less cr. |
| Obsidian | `#000000` | neutral | Code block backgrounds and specific high-contrast text elements. Used sparingly for maximum impact. |
| Gradient Aura | `#00bc7d` | brand | Used for significant hero headings, subtly transitioning brand colors to a warm accent. Commands attention with a moder. |

```css
:root {
  --colorful-forest-pine: #022c22;
  --colorful-spring-bud: #00bc7d;
  --colorful-evergreen: #007a55;
  --colorful-sky-mist: #e5e7eb;
  --colorful-paper-white: #ffffff;
  --colorful-graphite: #71717b;
  --colorful-obsidian: #000000;
}
```

## Typography direction
- Primary: **Inter**; substitute `Inter`.
- Secondary/code: **__Inter_Tight_a3c0d3**; substitute `Inter Tight`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
