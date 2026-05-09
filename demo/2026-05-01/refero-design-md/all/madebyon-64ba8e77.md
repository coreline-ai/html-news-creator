# Madebyon - Refero Design MD

- Source: https://styles.refero.design/style/64ba8e77-d1be-48a2-a47d-bdd46e139b8f
- Original site: https://www.madebyon.com
- Theme: `dark`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Neon on Obsidian: Precision text and vivid accents against a deep, dark canvas.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Onyx Graphite | `#151515` | neutral | Primary text or dark surface |
| Floral Veil | `#faf9f4` | neutral | Page background or card surface |
| Soft Silver | `#bdbdbd` | neutral | Border, muted text, or supporting surface |
| Warm Gray | `#666666` | neutral | Border, muted text, or supporting surface |
| Switchblade Green | `#dcff4f` | brand | Action accent / signal color |
| Emerald Spark | `#51d287` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-onyx-graphite: #151515;
  --ref-floral-veil: #faf9f4;
  --ref-soft-silver: #bdbdbd;
  --ref-warm-gray: #666666;
  --ref-switchblade-green: #dcff4f;
  --ref-emerald-spark: #51d287;
}
```

## Typography direction
- **Favorit extended**: 400, 40px, 56px, 1.2.
- **Favorit**: 400, 11px, 12px, 13px, 16px, 24px, 1.00, 1.20, 1.30, 1.35, 1.40, 1.42, 1.50; substitute `system-ui, sans-serif`.

## Spacing / shape
- Section Gap: `81px`
- Card Padding: `16px`
- Element Gap: `16px`
- Radius: `tags: 999px, cards: 8px, inputs: 16px, buttons: 50px, navItems: 50px, bodyElements: 24px`

## Component cues
- **Primary Action Button**: Call-to-action button, signaling key interactive elements.
- **Testimonial Card**: Container for client testimonials.
- **Nested Card**: Secondary content container within primary black cards.
- **Input Field**: Form input elements for user data entry.
- **Ghost Navigation Link**: Main navigation links in the header.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
