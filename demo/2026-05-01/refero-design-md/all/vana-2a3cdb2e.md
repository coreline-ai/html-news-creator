# Vana - Refero Design MD

- Source: https://styles.refero.design/style/2a3cdb2e-effe-406b-932e-37e4dc88ab1d
- Original site: https://www.vana.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal Interface

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#161616` | neutral | Primary text or dark surface |
| Void Black | `#000000` | neutral | Primary text or dark surface |
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Slate Gray | `#3b3b3b` | neutral | Primary text or dark surface |
| Ash Gray | `#eaeaea` | neutral | Page background or card surface |
| Subtle Ash | `#b8ad97` | neutral | Border, muted text, or supporting surface |
| Ultraviolet Blue | `#0000ff` | brand | Action accent / signal color |
| Neon Violet | `#4141fc` | accent | Action accent / signal color |
| Lavender Glow | `#8b8bfe` | accent | Action accent / signal color |
| Status Mint | `#7fd579` | accent | Action accent / signal color |

```css
:root {
  --ref-deep-space: #161616;
  --ref-void-black: #000000;
  --ref-cloud-white: #ffffff;
  --ref-slate-gray: #3b3b3b;
  --ref-ash-gray: #eaeaea;
  --ref-subtle-ash: #b8ad97;
  --ref-ultraviolet-blue: #0000ff;
  --ref-neon-violet: #4141fc;
}
```

## Typography direction
- **Cofo Sans**: 400, 700, 13px, 14px, 16px, 24px, 64px, 1.00, 1.10, 1.15, 1.25; substitute `system-ui, sans-serif`.
- **Cofo Sans Pixel**: 400, 10px, 13px, 14px, 1.00, 1.10, 1.25; substitute `monospace, sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1440px`
- Radius: `pill: 1440px, cards: 2px, buttons: 2px`

## Surface cues
- **Deep Space Canvas** `#161616`: Primary page background and base surface for most sections.
- **Slate Gray Card** `#3b3b3b`: Background for feature cards, providing a distinct, slightly elevated surface.
- **Ultraviolet Interactive** `#0000ff`: Background for primary action buttons, signifying the highest level of interaction.

## Component cues
- **Primary Filled Button**: Call-to-action button, conveying primary interaction.
- **Secondary Outlined Button**: Secondary action button, providing a less prominent alternative to filled buttons.
- **Ghost Circular Button**: Decorative or tertiary action, often embedded in navigation or for subtle interaction.
- **Navigation Link**: Top-level navigation items.
- **Feature Card**: Container for distinct conceptual features or points of interest.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
