# Nile Postgres - Refero Design MD

- Source: https://styles.refero.design/style/7671d0fc-b9fc-462e-9c74-38511264aabd
- Original site: https://www.thenile.dev
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight console, glowing accents

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#0e0e0e` | neutral | Primary text or dark surface |
| Carbon Panel | `#1c1c1c` | neutral | Primary text or dark surface |
| Ash Gray | `#3f3f3f` | neutral | Primary text or dark surface |
| Steel Gray | `#2f3336` | neutral | Primary text or dark surface |
| Smoke | `#2b2b2b` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Silver Muted | `#d3d3d3` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Cyber Cyan | `#6fe2ff` | brand | Action accent / signal color |
| Amber Glow | `#ffba6a` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-ink: #0e0e0e;
  --ref-carbon-panel: #1c1c1c;
  --ref-ash-gray: #3f3f3f;
  --ref-steel-gray: #2f3336;
  --ref-smoke: #2b2b2b;
  --ref-ghost-white: #ffffff;
  --ref-silver-muted: #d3d3d3;
  --ref-slate-text: #a1a1aa;
}
```

## Typography direction
- **aeonik**: 400, 600, 700, 12px, 14px, 15px, 16px, 18px, 20px, 24px, 32px, 40px, 42px, 48px, 64px, 96px, 1.00, 1.08, 1.10, 1.18, 1.20, 1.25, 1.43, 1.50, 1.56, 1.60; substitute `system-ui`.
- **aeonik**: 500, 16px, 20px, 24px, 96px, 1.00, 1.20, 1.25, 1.50; substitute `system-ui`.
- **ui-monospace**: 400, 14px, 1.14, 1.18, 1.50; substitute `monospace`.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Page Max Width: `1280px`
- Radius: `tags: 10px, cards: 16px, buttons: 9999px, hero-cards: 20px, large-elements: 100px`

## Component cues
- **Primary Action Button**: Main call-to-action button for initiating key actions.
- **Ghost Action Button**: Secondary action or navigational button within the dark theme.
- **Tertiary Ghost Button**: Subtle interactive button, often for 'View on X' or less prominent actions.
- **Testimonial Card**: Displaying short quotes or testimonials.
- **Hero Feature Card**: Highlights key features with distinct background colors.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
