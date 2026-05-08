# Tella - Colorful Refero Design MD

- Source: https://styles.refero.design/style/41547c7a-3bbe-49f0-95d6-9701c9df9a5e
- Original site: https://tella.tv
- Theme: `mixed`
- Color rank: **13**
- Colorfulness score: `41.2`
- Recommended fit: **Gradient / luminous dashboard**

## North star
Violet broadcast signal - the design feels like a TV network's on-air package: full-bleed chromatic fields, bold compressed display type, hard cuts between saturated and white.

## Why this fits html-news-creator
Use for premium dashboards, boardroom decks, and hero surfaces where the product needs a stronger visual identity.

## Apply to
- Boardroom deck covers
- Trend overview hero sections
- Premium dashboard headers

## Color tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Signal Violet | `#5e51f8` | brand | Primary brand color - hero backgrounds, CTAs, interactive states, logo mark. The electric quality (vivid, high-chroma). |
| Deep Nebula | `#251544` | brand | Hero section footer tone and gradient terminus. Paired with Signal Violet for the dark-to-darker hero gradient that cre. |
| Iris Mid | `#4b41c6` | brand | Button shadow underlay and hover states on the hero. Creates tactile depth on dark surfaces via box-shadow layering. |
| Soft Amethyst | `#cfcbfd` | brand | Secondary headline text on dark violet backgrounds - brand color carried into typography so the hero never loses chroma. |
| Lavender Mist | `#d5a8f5` | accent | Pill button accent variant - appears as a pastel contrast button against the violet hero. Black text on this color deli. |
| Powder Violet | `#d7d3fd` | accent | Feature card illustration tints and ghost typography in the white sections - keeps brand hue present without saturating. |
| Periwinkle Glow | `#867dfa` | accent | Icon fills and glow halos (box-shadow on interactive elements). The lighter violet relative of Signal Violet - used for. |
| Celestial Cyan | `#99eeff` | accent | Decorative accent surface - appears sparingly as a cool counterpoint to the warm violet system. |

```css
:root {
  --colorful-signal-violet: #5e51f8;
  --colorful-deep-nebula: #251544;
  --colorful-iris-mid: #4b41c6;
  --colorful-soft-amethyst: #cfcbfd;
  --colorful-lavender-mist: #d5a8f5;
  --colorful-powder-violet: #d7d3fd;
  --colorful-periwinkle-glow: #867dfa;
}
```

## Typography direction
- Primary: **NaN Jaune Midi Bold**; substitute `Cabinet Grotesk ExtraBold or Clash Display Bold`.
- Secondary/code: **Inter**; substitute `Inter (freely available via Google Fonts)`.

## Guardrails
- Treat these as accent and exploration references. Do not turn the production report into a rainbow UI without a separate migration request.
- Use color semantically: category, status, confidence, evidence type, or section emphasis.
- Keep report readability first; colorful surfaces should support hierarchy, not compete with source evidence.
