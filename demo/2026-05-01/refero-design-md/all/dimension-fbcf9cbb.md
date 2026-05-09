# Dimension - Refero Design MD

- Source: https://styles.refero.design/style/fbcf9cbb-7c6b-449d-862a-bce521a8ab1d
- Original site: https://www.dimension.dev
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-space command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Base | `#0a0a0a` | neutral | Primary text or dark surface |
| Storm Gray | `#161616` | neutral | Primary text or dark surface |
| Gunmetal | `#282828` | neutral | Primary text or dark surface |
| Slate Text | `#686868` | neutral | Border, muted text, or supporting surface |
| Ash Text | `#b2b2b2` | neutral | Border, muted text, or supporting surface |
| Silver Whisper | `#c2c2c2` | neutral | Border, muted text, or supporting surface |
| Ghost White | `#e5e5e5` | neutral | Page background or card surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Gradient Aura | `#4867af` | accent | Action accent / signal color |
| Interactive Glow | `#6b62f2` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-base: #0a0a0a;
  --ref-storm-gray: #161616;
  --ref-gunmetal: #282828;
  --ref-slate-text: #686868;
  --ref-ash-text: #b2b2b2;
  --ref-silver-whisper: #c2c2c2;
  --ref-ghost-white: #e5e5e5;
  --ref-canvas-white: #ffffff;
}
```

## Typography direction
- **DM Sans**: 400, 500, 700, 14px, 15px, 16px, 18px, 40px, 72px, 1.00, 1.11, 1.20, 1.25, 1.43, 1.50, 1.56; substitute `Inter`.
- **Geist**: 400, 500, 600, 14px, 16px, 18px, 24px, 32px, 36px, 48px, 1.00, 1.11, 1.14, 1.33, 1.43, 1.50, 1.71; substitute `system-ui`.
- **system-ui**: 400, 500, 18px, 1.5.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `16px`
- Element Gap: `8px`
- Radius: `cards: 24px, buttons: 9999px, callouts: 10px, app-icons-ui: 10px, hero-sections: 40px`

## Surface cues
- **Midnight Base** `#0a0a0a`: Dominant page and main container background.
- **Translucent Accent** `#00000033`: Soft, translucent cards that overlay the base, allowing background gradients to show through, often paired with a backdrop blur.
- **Semi-Transparent Overlay** `#d4d4d41a`: Subtle, ghost-like cards or containers with minimal visual presence.

## Component cues
- **Ghost Button**: Secondary action button
- **Navigation Link Button**: Navigation items within a menu
- **Pill Button**: Primary action button, tags, or small interactive elements
- **Floating Pill Bar Button**: Buttons within the floating navigation/action bar
- **Translucent Spotlight Card**: Displaying featured content or application icons

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
