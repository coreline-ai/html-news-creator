# Railway - Refero Design MD

- Source: https://styles.refero.design/style/5c32375f-6ef1-4345-9418-ebbb7e887343
- Original site: https://railway.app
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Cosmic Midnight Express. A calm, powerful journey through a dark, starlit environment, guided by clear signals.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#13111c` | neutral | Primary text or dark surface |
| Surface | `#1a191f` | neutral | Primary text or dark surface |
| Black Hole | `#0d0c14` | neutral | Primary text or dark surface |
| Starlight | `#f7f7f8` | neutral | Page background or card surface |
| Starlight Dim | `#d0cfd2` | neutral | Border, muted text, or supporting surface |
| Comet | `#a1a0ab` | neutral | Border, muted text, or supporting surface |
| Asteroid | `#868593` | neutral | Border, muted text, or supporting surface |
| Cosmic Lilac | `#553f83` | brand | Action accent / signal color |
| Supernova | `#a05fcf` | accent | Action accent / signal color |
| Nebula Haze | `#bf92ec` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #13111c;
  --ref-surface: #1a191f;
  --ref-black-hole: #0d0c14;
  --ref-starlight: #f7f7f8;
  --ref-starlight-dim: #d0cfd2;
  --ref-comet: #a1a0ab;
  --ref-asteroid: #868593;
  --ref-cosmic-lilac: #553f83;
}
```

## Typography direction
- **IBM Plex Serif**: 400, 500, 36px, 40px, 54px, 1.12, 1.20, 1.33; substitute `Georgia, Times New Roman`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 24px, 1.25, 1.33, 1.40, 1.43, 1.50, 1.56, 1.60, 1.63, 1.75; substitute `system-ui, -apple-system`.
- **Inter Tight**: 400, 600, 32px, 40px, 1.20, 1.38; substitute `Inter`.

## Spacing / shape
- Section Gap: `96-160px`
- Card Padding: `32px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `tags: 9999px, cards: 12px, inputs: 6px, buttons: 8px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Deployment Success Toast + Tab Bar**: Reference component style.
- **Testimonial Cards**: Reference component style.
- **Primary CTA Button**: The main call-to-action, like 'Deploy →'.
- **Secondary Button**: Secondary actions, like 'Demo'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
