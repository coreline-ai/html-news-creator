# Craft Docs - Refero Design MD

- Source: https://styles.refero.design/style/9f228e72-997a-4410-9190-68359028e3d0
- Original site: https://craft.do
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital Scrapbook Collage. The design feels like a thoughtful, tactile scrapbook where structured digital notes meet soft, organic textures.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas | `#fff3e7` | neutral | Page background or card surface |
| Ink | `#030302` | neutral | Primary text or dark surface |
| White | `#ffffff` | neutral | Page background or card surface |
| Linen | `#f7f7f7` | neutral | Page background or card surface |
| Cloud | `#efefef` | neutral | Page background or card surface |
| Ash | `#e1e1e1` | neutral | Page background or card surface |
| Stone | `#bebbba` | neutral | Border, muted text, or supporting surface |
| Graphite | `#41413f` | neutral | Border, muted text, or supporting surface |
| Mint | `#9bd8a9` | brand | Action accent / signal color |
| Marigold | `#fde99b` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas: #fff3e7;
  --ref-ink: #030302;
  --ref-white: #ffffff;
  --ref-linen: #f7f7f7;
  --ref-cloud: #efefef;
  --ref-ash: #e1e1e1;
  --ref-stone: #bebbba;
  --ref-graphite: #41413f;
}
```

## Typography direction
- **UntitledSerifFont**: 400, 24px, 28px, 30px, 32px, 36px, 46px, 54px, 56px, 66px, 1.05-1.2; substitute `Lora, Merriweather`.
- **UntitledSansFont**: 400, 500, 700, 12px, 14px, 16px, 18px, 20px, 24px, 1.4-1.5; substitute `Inter, Figtree`.

## Spacing / shape
- Section Gap: `96-120px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1280px`
- Radius: `cards: 16-24px, pills: 9999px, inputs: 14px, buttons: 14px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Feature Category Pills**: Reference component style.
- **Testimonial Quote Card**: Reference component style.
- **Primary Pill Button**: The main 'Try Craft Free' call-to-action in the sticky navigation header.
- **Navigation Link**: Standard links within the main header navigation.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
