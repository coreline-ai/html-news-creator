# Twingate - Refero Design MD

- Source: https://styles.refero.design/style/0acef011-07da-4416-b874-ccdd675140f6
- Original site: https://twingate.com
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, Pulsing Neon. A dark, digital interface illuminated by precise, electric glows.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Carbon | `#0e0f11` | neutral | Primary text or dark surface |
| Basalt | `#141617` | neutral | Primary text or dark surface |
| Obsidian | `#1d2023` | neutral | Primary text or dark surface |
| Platinum | `#ffffff` | neutral | Page background or card surface |
| Graphite | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Ash | `#cfcfd3` | neutral | Border, muted text, or supporting surface |
| Spectral Violet | `#b6abff` | brand | Action accent / signal color |
| Electric Lime | `#eef35f` | brand | Action accent / signal color |
| System Teal | `#00cbaa` | accent | Action accent / signal color |
| Deep Violet | `#6350dd` | accent | Action accent / signal color |

```css
:root {
  --ref-carbon: #0e0f11;
  --ref-basalt: #141617;
  --ref-obsidian: #1d2023;
  --ref-platinum: #ffffff;
  --ref-graphite: #a1a1aa;
  --ref-ash: #cfcfd3;
  --ref-spectral-violet: #b6abff;
  --ref-electric-lime: #eef35f;
}
```

## Typography direction
- **TT Hoves Light**: 300, 400, 22px, 24px, 48px, 54px, 55px, 62px, 68px, 1.10, 1.20, 1.30, 1.50; substitute `Open Sans Light`.
- **TT Hoves Medium**: 400, 500, 11px, 12px, 13px, 14px, 15px, 16px, 17px, 20px, 32px, 1.04, 1.12, 1.13, 1.14, 1.20, 1.27, 1.29, 1.50; substitute `Open Sans Medium`.
- **TT Hoves Regular**: 400, 11px, 12px, 14px, 15px, 16px, 17px, 1.14, 1.20, 1.31, 1.50, 1.70; substitute `Open Sans Regular`.

## Spacing / shape
- Section Gap: `80px`
- Card Padding: `16px`
- Element Gap: `4px`
- Radius: `tags: 20px, cards: 12px, buttons: 50px, default: 8px`

## Component cues
- **Hero CTA Button Group**: Reference component style.
- **Feature Cards — Security, Performance, Simplicity**: Reference component style.
- **Testimonial Card with G2 Rating**: Reference component style.
- **Primary CTA Button**: Key interaction for conversions
- **Secondary CTA Button (Outlined)**: Alternative call to action, less prominent than primary

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
