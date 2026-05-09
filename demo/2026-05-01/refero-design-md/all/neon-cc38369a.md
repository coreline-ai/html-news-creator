# Neon - Refero Design MD

- Source: https://styles.refero.design/style/cc38369a-41e3-4bcd-b619-230ccffe7e8e
- Original site: https://neon.tech
- Theme: `dark`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Server Room After Dark. A deep black environment where data and interactions are the only sources of light.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Neon Glow | `#34d59a` | brand | Action accent / signal color |
| Neon Muted | `#285d49` | brand | Action accent / signal color |
| Scanline Fade | `#39a57d` | brand | Action accent / signal color |
| System Warning | `#ff3621` | accent | Action accent / signal color |
| Whiteout | `#ffffff` | neutral | Page background or card surface |
| Ash | `#797d86` | neutral | Border, muted text, or supporting surface |
| Cloud | `#c9cbcf` | neutral | Border, muted text, or supporting surface |
| Graphite Light | `#303236` | neutral | Primary text or dark surface |
| Graphite | `#242628` | neutral | Primary text or dark surface |
| Graphite Deep | `#151617` | neutral | Primary text or dark surface |

```css
:root {
  --ref-neon-glow: #34d59a;
  --ref-neon-muted: #285d49;
  --ref-scanline-fade: #39a57d;
  --ref-system-warning: #ff3621;
  --ref-whiteout: #ffffff;
  --ref-ash: #797d86;
  --ref-cloud: #c9cbcf;
  --ref-graphite-light: #303236;
}
```

## Typography direction
- **Inter**: 400, 500, 10px, 12px, 13px, 14px, 15px, 16px, 18px, 20px, 24px, 28px, 32px, 40px, 44px, 48px, 60px, 80px, 1.00, 1.13, 1.25, 1.38, 1.50; substitute `Inter`.
- **GeistMono**: 400, 500, 600, 12px, 14px, 16px, 18px, 20px, 1.00, 1.13, 1.38, 1.50, 1.65; substitute `Fira Code, Source Code Pro`.

## Spacing / shape
- Section Gap: `96-128px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `cards: 4px, inputs: 4px, buttons: 9999px, containers: 4px`

## Component cues
- **CTA Button Group**: Reference component style.
- **Terminal Code Block**: Reference component style.
- **Feature Navigation List**: Reference component style.
- **Primary Pill Button**: The main call-to-action, e.g., 'Get started', 'Sign up'.
- **Ghost Pill Button**: Secondary actions, e.g., 'Read the docs', 'Log in'.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
