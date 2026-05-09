# Tailwind CSS - Refero Design MD

- Source: https://styles.refero.design/style/8f79ab5b-a91a-4bf4-a64f-4a5ba3ada7d5
- Original site: https://tailwindcss.com
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Type specimen as product demo — a typographer's proof sheet where the headline IS the interface, bold black at 96px demanding attention through size alone.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ink Black | `#030712` | neutral | Primary text or dark surface |
| Slate Mist | `#4a5565` | neutral | Border, muted text, or supporting surface |
| Slate Mid | `#6a7282` | neutral | Border, muted text, or supporting surface |
| Slate Cool | `#364153` | neutral | Border, muted text, or supporting surface |
| Steel Veil | `#90a1b9` | neutral | Border, muted text, or supporting surface |
| Fog Line | `#cad5e2` | neutral | Border, muted text, or supporting surface |
| Slate Deep | `#1e2939` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Off White | `#bfbfbf` | neutral | Border, muted text, or supporting surface |
| Syntax Sky | `#00a6f4` | brand | Action accent / signal color |

```css
:root {
  --ref-ink-black: #030712;
  --ref-slate-mist: #4a5565;
  --ref-slate-mid: #6a7282;
  --ref-slate-cool: #364153;
  --ref-steel-veil: #90a1b9;
  --ref-fog-line: #cad5e2;
  --ref-slate-deep: #1e2939;
  --ref-pure-white: #ffffff;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 700, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 30px, 36px, 40px, 96px, 1.00–2.00 (tightest at large display sizes, 1.5–1.75 at body sizes); substitute `Inter (Google Fonts — this is already Inter)`.
- **IBM Plex Mono (plexMono)**: 400, 500, 600, 12px, 13px, 14px, 17px, 1.33–2.15 (loose line height for code readability); substitute `IBM Plex Mono (Google Fonts)`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1280px`
- Radius: `tags: 16px, cards: 8px, modals: 12px, buttons: 32px (pill CTA), 4px (code/tag badges), codeBlocks: 8px`

## Surface cues
- **Page Canvas** `#ffffff`: Primary marketing page background — pure white, no tint
- **Code Editor Dark** `#030712`: Dark code demo blocks, simulating a terminal or code editor window
- **Card Surface** `#ffffff`: White cards with inset 1px ring shadow to lift from page canvas
- **Elevated Overlay** `#ffffff`: Cards with compound inset+outer shadow for maximum elevation

## Component cues
- **CTA Button Group with Search Bar**: Reference component style.
- **Sponsors Section**: Reference component style.
- **Version Pill Badge + Inline Code Tags**: Reference component style.
- **Primary CTA Button**: Main calls to action — 'Get started', 'Become a sponsor'
- **Dark Code Badge Button**: Version label and secondary tags inside dark sections

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
