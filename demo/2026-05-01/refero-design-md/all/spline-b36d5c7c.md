# Spline - Refero Design MD

- Source: https://styles.refero.design/style/b36d5c7c-9b28-4c99-b5a8-69ce03621410
- Original site: https://spline.design
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Glowing Forms in the Void

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Panel Sheen | `#ffffff` | neutral | Page background or card surface |
| Button Sheen | `#ffffff` | neutral | Page background or card surface |
| Bright White | `#ffffff` | neutral | Page background or card surface |
| Cloud | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Silver | `#999999` | neutral | Border, muted text, or supporting surface |
| Text Dim | `#ffffff` | neutral | Page background or card surface |
| Nav Background | `#191a1d` | neutral | Primary text or dark surface |
| Spline Blue | `#0062ff` | brand | Action accent / signal color |
| Neon Pink | `#ff5cab` | accent | Action accent / signal color |

```css
:root {
  --ref-void-black: #000000;
  --ref-panel-sheen: #ffffff;
  --ref-button-sheen: #ffffff;
  --ref-bright-white: #ffffff;
  --ref-cloud: #cccccc;
  --ref-silver: #999999;
  --ref-text-dim: #ffffff;
  --ref-nav-background: #191a1d;
}
```

## Typography direction
- **Spline Sans**: 400, 500, 12px, 13px, 14px, 16px, 18px, 20px, 24px, 36px, 40px, 58px, 1.15, 1.22, 1.24, 1.25, 1.33, 1.35, 1.38, 1.43, 1.50, 1.56, 1.71; substitute `Inter`.
- **Spline Sans Mono**: 400, 14px, 1.50; substitute `IBM Plex Mono`.

## Spacing / shape
- Section Gap: `96px`
- Card Padding: `40px`
- Page Max Width: `1280px`
- Radius: `cards: 24px, pills: 99px, buttons: 12px, smallPanels: 16px`

## Surface cues
- **Void** `#000000`: Global page background
- **Panel** `#ffffff14`: Base card and large container surfaces
- **Interactive** `#ffffff26`: Secondary buttons and interactive surfaces

## Component cues
- **CTA Button Group**: Reference component style.
- **Community Showcase Cards**: Reference component style.
- **Announcement Banner + Feature Card**: Reference component style.
- **Primary CTA Button**: The main user call-to-action.
- **Secondary Button**: Secondary actions, like 'Log in' or alternate CTAs.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
