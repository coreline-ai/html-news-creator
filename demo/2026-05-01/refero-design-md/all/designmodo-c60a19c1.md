# Designmodo - Refero Design MD

- Source: https://styles.refero.design/style/c60a19c1-259a-4001-95d9-6a3826f5c06e
- Original site: https://designmodo.com
- Theme: `mixed`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Forest clearing at dawn — dark canopy above, open light below, a single green glow marking the path forward.

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Forest Floor | `#0e231c` | neutral | Primary text or dark surface |
| Canopy Shadow | `#1a3029` | neutral | Primary text or dark surface |
| Pine Border | `#233630` | neutral | Primary text or dark surface |
| Slate Ink | `#313942` | neutral | Primary text or dark surface |
| Ash | `#656a75` | neutral | Border, muted text, or supporting surface |
| Mist | `#c3cecb` | neutral | Border, muted text, or supporting surface |
| Fog | `#879b93` | neutral | Border, muted text, or supporting surface |
| Parchment | `#f4f7f2` | neutral | Page background or card surface |
| Dew | `#e4ebe2` | neutral | Page background or card surface |
| Sprout | `#27ae60` | brand | Action accent / signal color |

```css
:root {
  --ref-forest-floor: #0e231c;
  --ref-canopy-shadow: #1a3029;
  --ref-pine-border: #233630;
  --ref-slate-ink: #313942;
  --ref-ash: #656a75;
  --ref-mist: #c3cecb;
  --ref-fog: #879b93;
  --ref-parchment: #f4f7f2;
}
```

## Typography direction
- **InterVariable**: 400, 500, 600, 700, 11px, 14px, 15px, 16px, 18px, 19px, 20px, 21px, 24px, 28px, 32px, 40px, 41px, 48px, 56px, 57px, 1.1–1.7 for headings; 1.5–1.65 for body; 1.0 for display numerics; substitute `Inter (Google Fonts) with feature-settings applied`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `50px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `tags: 5px, cards: 32px, chips: 17px, badges: 6px, images: 12px, buttons: 999px`

## Surface cues
- **Hero Dark** `#0e231c`: Full-bleed hero, dark nav bar, footer — the deepest surface
- **Elevated Dark** `#1a3029`: Dark-zone secondary surfaces, inner cards within the hero
- **Page Light** `#f4f7f2`: Default page background in light sections
- **Card White** `#ffffff`: Blog cards, stats cards, explicit white cards on the light page background
- **Mint Card** `#edf9f2`: Product feature cards — subtly tinted to tie the card to the brand green

## Component cues
- **Stats Counter Cards**: Reference component style.
- **Product Feature Card (Postcards)**: Reference component style.
- **Article Cards with Category Badges**: Reference component style.
- **Primary CTA Button**: Main call-to-action, most prominent interactive element
- **Ghost Green Button**: Secondary CTA beside primary button, typically 'See more' or 'Learn more'

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
