# Dashlane - Refero Design MD

- Source: https://styles.refero.design/style/722f32e7-8217-4808-843d-b454eea7320a
- Original site: https://www.dashlane.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
secure data in deep space — a dark, controlled interface with focused light points

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#200f0a` | neutral | Primary text or dark surface |
| Almond Dust | `#e3ccc0` | neutral | Border, muted text, or supporting surface |
| Deep Plum | `#2b2538` | neutral | Primary text or dark surface |
| Burnt Umber | `#4d3f3b` | neutral | Border, muted text, or supporting surface |
| Aquamarine Glow | `#a2f6f5` | brand | Action accent / signal color |
| Indigo Spark | `#858df9` | brand | Action accent / signal color |
| Cadet Violet | `#6c74df` | accent | Action accent / signal color |
| Lavender Mist | `#b6bbfb` | accent | Action accent / signal color |
| Light Ash | `#e5e7eb` | neutral | Page background or card surface |
| Paper White | `#fcfaf9` | neutral | Page background or card surface |

```css
:root {
  --ref-midnight-ink: #200f0a;
  --ref-almond-dust: #e3ccc0;
  --ref-deep-plum: #2b2538;
  --ref-burnt-umber: #4d3f3b;
  --ref-aquamarine-glow: #a2f6f5;
  --ref-indigo-spark: #858df9;
  --ref-cadet-violet: #6c74df;
  --ref-lavender-mist: #b6bbfb;
}
```

## Typography direction
- **Saans**: 300, 500, 12px, 14px, 16px, 18px, 28px, 36px, 48px, 56px, 72px, 100px, 1.10, 1.17, 1.20, 1.50; substitute `Inter`.
- **SaansMono**: 300, 16px, 1.10; substitute `Space Mono`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `12px`
- Page Max Width: `1200px`
- Radius: `tags: 9999px, cards: 8px, buttons: 4px`

## Surface cues
- **Midnight Ink Canvas** `#200f0a`: Primary page background, creating a deep, dark base for content.
- **Deep Plum Card** `#2b2538`: Standard content card background, providing subtle elevation and visual grouping on the dark canvas.
- **Burnt Umber Card Accent** `#4d3f3b`: Alternative card background for specific content, subtly differentiating it from other surfaces.

## Component cues
- **Ghost Navigation Link**: Navigation and secondary actions
- **Primary Filled Button**: Call to action
- **Secondary Filled Button**: Alternative call to action, less prominent than primary
- **Standard Content Card**: Group related content, statistics, or testimonials
- **Highlighted Content Card**: Feature specific content or testimonials with slight visual distinction

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
