# Tableland - Refero Design MD

- Source: https://styles.refero.design/style/573fe0d5-8f0b-4c59-bae3-3f2e67cc63f0
- Original site: https://tableland.xyz
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight data oasis

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#101e1e` | neutral | Primary text or dark surface |
| Shadow Realm | `#162929` | neutral | Primary text or dark surface |
| Graphite | `#3b4949` | neutral | Border, muted text, or supporting surface |
| Code Block | `#1a1a1a` | neutral | Primary text or dark surface |
| Mist | `#e5e7eb` | neutral | Page background or card surface |
| Porcelain | `#ffffff` | neutral | Page background or card surface |
| Teal Accent | `#75b6b5` | accent | Action accent / signal color |
| Emerald Spark | `#0be291` | brand | Action accent / signal color |
| Lavender Haze | `#e4cbf2` | brand | Action accent / signal color |
| Cardinal Red | `#f4706b` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #101e1e;
  --ref-shadow-realm: #162929;
  --ref-graphite: #3b4949;
  --ref-code-block: #1a1a1a;
  --ref-mist: #e5e7eb;
  --ref-porcelain: #ffffff;
  --ref-teal-accent: #75b6b5;
  --ref-emerald-spark: #0be291;
}
```

## Typography direction
- **Poppins**: 300, 400, 500, 700, 12px, 14px, 16px, 18px, 22px, 24px, 30px, 48px, 1.00, 1.20, 1.33, 1.43, 1.45, 1.50, 1.56, 1.78; substitute `system-ui, sans-serif`.
- **monospace**: 300, 12px, 1.33; substitute `SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `24px`
- Element Gap: `16px`
- Page Max Width: `1280px`
- Radius: `tags: 9999px, cards: 8px, inputs: 4px, buttons: 16px, navigation: 12px`

## Surface cues
- **Deep Space Canvas** `#101e1`: The foundational page background for most sections, creating a dark, immersive base layer.
- **Shadow Realm Substrate** `#162929`: A slightly elevated surface used for subtle content blocks or as a border for ghost elements, providing minimal visual separation.
- **Graphite Card Surface** `#3b4949`: Used for distinct cards and active interactive elements like filled buttons, providing a clear visual lift from the base canvas.

## Component cues
- **Primary Filled Button**: Action button
- **Secondary Ghost Button**: Secondary action button
- **Navigation Link Button**: Navigation and secondary calls to action
- **Social Proof Card**: Content container for testimonials/social feeds
- **Feature Card**: Information display for features or benefits

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
