# mymind - Refero Design MD

- Source: https://styles.refero.design/style/5bfe6c1d-1b15-4f8d-b0c9-677a33291c5d
- Original site: https://mymind.com
- Theme: `light`
- Industry: `productivity`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Sunlit personal archive — a warm afternoon light spilling across a private collection of saved thoughts, images, and bookmarks, curated without folders.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ember Orange | `#ff5924` | brand | Action accent / signal color |
| Cobalt Link | `#1573dd` | accent | Action accent / signal color |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#f9fafc` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Blush Tint | `#fff1f1` | neutral | Page background or card surface |
| Mist | `#e2e2e2` | neutral | Page background or card surface |
| Slate Blue Card | `#e5eaf2` | neutral | Action accent / signal color |
| Parchment Card | `#f3f0e7` | neutral | Page background or card surface |
| Sage Card | `#dde9d3` | neutral | Page background or card surface |

```css
:root {
  --ref-ember-orange: #ff5924;
  --ref-cobalt-link: #1573dd;
  --ref-midnight-ink: #000000;
  --ref-canvas-white: #f9fafc;
  --ref-pure-white: #ffffff;
  --ref-blush-tint: #fff1f1;
  --ref-mist: #e2e2e2;
  --ref-slate-blue-card: #e5eaf2;
}
```

## Typography direction
- **Open Sans**: 400, 18px, 22px, 1.00–1.67; substitute `Open Sans (Google Fonts)`.
- **Louize-Regular-205TF**: 400, 18px, 32px, 36px, 42px, 52px, 54px, 80px, 96px, 140px, 0.80–1.30; substitute `Freight Display Pro, or Playfair Display at weight 400`.
- **Louize-Italic-205TF**: 400, 80px, 84px, 0.88; substitute `Freight Display Pro Italic`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `50px`
- Element Gap: `20px`
- Page Max Width: `1440px`
- Radius: `nav: 30px, tags: 36px, cards: 16px, buttons: 100px, cardsAlt: 12px, buttonsAlt: 120px`

## Surface cues
- **Canvas** `#f9fafc`: Base page background — barely-off-white, receives the warm bloom gradient in hero
- **Section Warm** `#fff1f1`: Alternating section backgrounds — warm blush tint for rhythm
- **Card White** `#ffffff`: Elevated card surfaces — full white against tinted backgrounds
- **Card Blue** `#e5eaf2`: Content category card — cool-tinted for tech/productivity content
- **Card Parchment** `#f3f0e7`: Content category card — warm off-white for notes/writing content

## Component cues
- **Content Category Tags (Hero Inline Pills)**: Reference component style.
- **Platform Download Buttons (Ghost Slate Pills)**: Reference component style.
- **Inline Checklist Card (Pastel Parchment Feature Card)**: Reference component style.
- **Ember Outlined Pill Button**: Primary brand action button — outlined, never filled
- **Ghost Slate Pill Button**: Secondary platform download buttons (iPhone app, Browser Extension, Android app)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
