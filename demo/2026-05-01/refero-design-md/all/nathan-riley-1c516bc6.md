# Nathan Riley - Refero Design MD

- Source: https://styles.refero.design/style/1c516bc6-278b-4cf6-bfe8-c5a39118e730
- Original site: https://www.nrly.co
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Gallery of softly lit dreams.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ash Gray | `#393939` | neutral | Primary text or dark surface |
| Ethereal Pink | `#fce0db` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #000000;
  --ref-canvas-white: #ffffff;
  --ref-ash-gray: #393939;
  --ref-ethereal-pink: #fce0db;
}
```

## Typography direction
- **font1**: 300, 400, 12px, 238px, 0.8, 1.1.
- **Playfair Display**: use as primary family; substitute `Playfair Display`.
- **Inter**: use as primary family; substitute `Inter`.

## Spacing / shape
- Section Gap: `38px`
- Card Padding: `16px`
- Element Gap: `6px`
- Radius: `buttons: 9999px, socialLinks: 9999px`

## Component cues
- **Social Link Button**: Interactive element for social media links
- **Bio Section Card**: Container for biographical text
- **Gallery Thumbnail Grid Item**: Visual content display

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
