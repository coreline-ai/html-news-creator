# Zendesk - Refero Design MD

- Source: https://styles.refero.design/style/240234ba-9cf5-4a91-b618-76963551d425
- Original site: https://zendesk.com
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Lime signal in a forest clearing — precision SaaS dressed in warm organic ink, where the single electric-green accent cuts through like a backlit leaf.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Electric Lime | `#d1f470` | brand | Action accent / signal color |
| Forest Canopy | `#203524` | brand | Action accent / signal color |
| Deep Grove | `#2d4c33` | brand | Action accent / signal color |
| Lime Fade | `#d1f470` | accent | Action accent / signal color |
| Near-Black Ink | `#11110d` | neutral | Primary text or dark surface |
| Warm White | `#f5f5f2` | neutral | Page background or card surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Midnight | `#000000` | neutral | Primary text or dark surface |
| Stone Divider | `#90918c` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-electric-lime: #d1f470;
  --ref-forest-canopy: #203524;
  --ref-deep-grove: #2d4c33;
  --ref-lime-fade: #d1f470;
  --ref-near-black-ink: #11110d;
  --ref-warm-white: #f5f5f2;
  --ref-pure-white: #ffffff;
  --ref-midnight: #000000;
}
```

## Typography direction
- **Vanilla Sans**: 300, 400, 500, 600, 700, 14px, 15px, 16px, 18px, 26px, 32px, 42px, 48px, 68px, 74px, 1.00–1.68 (tight 1.00–1.05 at display sizes, 1.39–1.56 at body sizes); substitute `Inter, DM Sans`.

## Spacing / shape
- Section Gap: `80-120px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `tags: 4px, cards: 0px, inputs: 12px, buttons: 16px, iconButtons: 100%, eventBannerCards: 40px`

## Surface cues
- **Page Canvas** `#ffffff`: Hero sections and primary page background
- **Warm Surface** `#f5f5f2`: Content cards, feature sections, testimonial backgrounds
- **Forest Canopy** `#203524`: Event promo cards, announcement banners — signals special/featured context
- **Deep Grove** `#2d4c33`: Secondary dark surfaces within event or feature blocks

## Component cues
- **Email Signup CTA with Input**: Reference component style.
- **Zendesk Relate Event Promo Card**: Reference component style.
- **Testimonial Carousel Block**: Reference component style.
- **Primary Lime CTA Button**: Main conversion action — email signup, trial start
- **Ghost Link Button**: Secondary actions — 'Ver en línea', 'Más información'

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
