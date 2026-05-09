# Freelance frontend UI developer and designer, Rou Hun Fan - Refero Design MD

- Source: https://styles.refero.design/style/ffb945f9-2d70-45e8-9024-492900318fa8
- Original site: https://flowen.me
- Theme: `dark`
- Industry: `design`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
retro arcade glow

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Charcoal | `#161b1b` | neutral | Primary text or dark surface |
| Ghost White | `#ffffff` | neutral | Page background or card surface |
| Vermilion Red | `#ff0000` | brand | Action accent / signal color |
| Electric Pink | `#e82f5c` | accent | Action accent / signal color |
| Neon Yellow | `#f0f26a` | accent | Action accent / signal color |
| Bubblegum Pink | `#ffa8a8` | accent | Action accent / signal color |
| Aqua Glow | `#00ffff` | accent | Action accent / signal color |
| Muted Gray | `#b3aba4` | neutral | Border, muted text, or supporting surface |
| Violet Streak | `#b333b3` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-charcoal: #161b1b;
  --ref-ghost-white: #ffffff;
  --ref-vermilion-red: #ff0000;
  --ref-electric-pink: #e82f5c;
  --ref-neon-yellow: #f0f26a;
  --ref-bubblegum-pink: #ffa8a8;
  --ref-aqua-glow: #00ffff;
  --ref-muted-gray: #b3aba4;
}
```

## Typography direction
- **Azeret Mono**: 400, 700, 100px, 1.20; substitute `IBM Plex Mono`.
- **Ephidona**: 400, 100px, 108px, 1.20; substitute `DM Serif Display`.

## Spacing / shape
- Section Gap: `40-80px`
- Card Padding: `24px`
- Element Gap: `9px`
- Page Max Width: `1100px`
- Radius: `default: 0px`

## Surface cues
- **Midnight Charcoal Canvas** `#161b1b`: The foundational page background for most content, offering a deep, dark base.
- **Vermilion Red Accent Surface** `#ff0000`: Used for prominent content blocks or interactive regions, creating a high-energy contrast against the charcoal background.
- **Aqua Glow Accent Surface** `#00ffff`: Secondary accent surface for key features or showcase content, providing a cool, vibrant counterpoint to the Vermilion Red.

## Component cues
- **Primary Navigation Link**: Top-level navigation items.
- **Hero Headline Block**: Main page title or section headline.
- **Accent Content Box (Aqua Glow)**: Highlighting a key message or interactive area.
- **Accent Content Box (Vermilion Red)**: Highlighting high-impact calls to action or interactive features.
- **Decorative Section Title**: Stylized section headings.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
