# Skillshare - Refero Design MD

- Source: https://styles.refero.design/style/162e9ba9-7487-4b57-aee8-0bbeadcc586d
- Original site: https://skillshare.com
- Theme: `mixed`
- Industry: `media`
- Recommended fit: **Visual board / colorful report variant**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Poster studio on matte black — bold instructor faces, chalk-white type, single neon pulse.

## Apply to
- Colorful demo variants and visual-board layouts
- Hero cards and image-led sections
- Marketing-style preview pages for generated reports

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Studio Black | `#000000` | neutral | Primary text or dark surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Deep Ink | `#0b1215` | neutral | Primary text or dark surface |
| Graphite Stroke | `#394649` | neutral | Border, muted text, or supporting surface |
| Fog Border | `#e0e0e0` | neutral | Page background or card surface |
| Ash Mid | `#757575` | neutral | Border, muted text, or supporting surface |
| Charcoal Surface | `#232424` | neutral | Primary text or dark surface |
| Skill Green | `#55da9b` | brand | Action accent / signal color |
| Neon Pulse | `#00ff84` | brand | Action accent / signal color |
| Electric Cyan | `#24c2f2` | accent | Action accent / signal color |

```css
:root {
  --ref-studio-black: #000000;
  --ref-pure-white: #ffffff;
  --ref-deep-ink: #0b1215;
  --ref-graphite-stroke: #394649;
  --ref-fog-border: #e0e0e0;
  --ref-ash-mid: #757575;
  --ref-charcoal-surface: #232424;
  --ref-skill-green: #55da9b;
}
```

## Typography direction
- **GT Walsheim Pro**: 100, 400, 500, 600, 700, 11px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 22px, 24px, 28px, 34px, 36px, 38px, 46px, 48px, 0.90–1.55 (tight 0.90–0.96 at display sizes 36px+, 1.20–1.50 at body sizes); substitute `Inter, DM Sans`.
- **Times**: 400, 16px, 1.00; substitute `Georgia`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `16px`
- Element Gap: `8-12px`
- Page Max Width: `1280px`
- Radius: `cards: 4px, pills: 100px, inputs: 4px, buttons: 4px, elevated: 8px`

## Surface cues
- **Pure Black** `#000000`: Dark section backgrounds, hero right panel, feature sections
- **Charcoal Lift** `#232424`: Stat cards and metric tiles floating on pure black sections
- **White Page** `#ffffff`: Light section backgrounds, registration panel, card surfaces
- **Navigation Bar** `#ffffff`: Sticky nav — same white as page background, separated by content not chrome

## Component cues
- **Registration Panel — Auth Buttons**: Reference component style.
- **Stat Counter Cards — Social Proof Metrics**: Reference component style.
- **Feature Checklist — Dark Section**: Reference component style.
- **Primary CTA Button**: Main registration and sign-up actions
- **White Outlined Auth Button**: Social login options (Google, Facebook, Apple)

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
