# Midjourney - Refero Design MD

- Source: https://styles.refero.design/style/225059ac-0450-49d3-b2b7-d0e98b7ae938
- Original site: https://midjourney.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep-ocean bioluminescent terminal. A pressurized darkness where intelligence visibly generates itself in ASCII streams, and controls appear as faintly glowing specimens.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cosmic Void | `#06051d` | brand | Action accent / signal color |
| Abyssal Blue | `#0f1c36` | brand | Action accent / signal color |
| Steel Navy | `#1d293d` | neutral | Primary text or dark surface |
| Deep Slate | `#314062` | neutral | Primary text or dark surface |
| Mist | `#cad5e2` | neutral | Border, muted text, or supporting surface |
| Fog | `#e5e7eb` | neutral | Page background or card surface |
| Ash | `#2e3038` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Ice Blue | `#ebf8ff` | neutral | Action accent / signal color |
| Portal Blue | `#63b3ed` | accent | Action accent / signal color |

```css
:root {
  --ref-cosmic-void: #06051d;
  --ref-abyssal-blue: #0f1c36;
  --ref-steel-navy: #1d293d;
  --ref-deep-slate: #314062;
  --ref-mist: #cad5e2;
  --ref-fog: #e5e7eb;
  --ref-ash: #2e3038;
  --ref-ghost-white: #ffffff;
}
```

## Typography direction
- **JetBrains Mono**: 400, 14px, 16px, 30px, 1.25–1.63; substitute `Fira Code, Source Code Pro`.
- **DM Sans**: 400, 500, 16px, 1.50; substitute `Inter, Outfit`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `32px`
- Element Gap: `8-16px`
- Page Max Width: `800px`
- Radius: `cards: 8px, images: 8px, inputs: 8px, buttons: 9999px`

## Surface cues
- **Cosmic Void** `#06051d`: Base page background — the deepest layer, the void all other surfaces float within
- **Deep Navy Gradient** `#061434`: Upper-hero gradient terminus, slightly lighter for atmospheric depth illusion
- **Abyssal Blue** `#0f1c36`: Button container backgrounds, secondary surface areas
- **Steel Navy** `#1d293d`: Navigation bar background, card container backgrounds
- **Deep Slate** `#314062`: Elevated or hover-state surfaces

## Component cues
- **Pill Button Group**: Reference component style.
- **Section Heading with Body — About**: Reference component style.
- **Projects Section with Image Grid**: Reference component style.
- **Sign Up Pill Button**: Primary registration CTA in navigation
- **Log In Pill Button**: Secondary auth action in navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
