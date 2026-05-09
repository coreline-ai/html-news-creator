# zkPass - Refero Design MD

- Source: https://styles.refero.design/style/3a398f82-579e-4ec4-a442-9962bf007edf
- Original site: https://zkpass.org
- Theme: `dark`
- Industry: `crypto`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Digital-noir command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Silver Whisper | `#ffffff` | neutral | Page background or card surface |
| Lime Interface | `#c5ff4a` | brand | Action accent / signal color |
| Dark Grid | `#252525` | neutral | Primary text or dark surface |
| Mid-Gray Border | `#7a7a7a` | neutral | Border, muted text, or supporting surface |
| Faint Grid | `#3d3d3d` | neutral | Primary text or dark surface |
| Glow Green | `#597321` | accent | Action accent / signal color |
| Soft Lime | `#314013` | accent | Action accent / signal color |
| White Outlined Text | `#c5c5c5` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-midnight-ink: #000000;
  --ref-silver-whisper: #ffffff;
  --ref-lime-interface: #c5ff4a;
  --ref-dark-grid: #252525;
  --ref-mid-gray-border: #7a7a7a;
  --ref-faint-grid: #3d3d3d;
  --ref-glow-green: #597321;
  --ref-soft-lime: #314013;
}
```

## Typography direction
- **PT Serif**: 300, 400, 14px, 16px, 20px, 22px, 24px, 26px, 32px, 40px, 49px, 56px, 60px, 72px, 75px, 78px, 86px, 89px, 130px, 0.88, 0.90, 0.94, 0.95, 0.98, 1.00, 1.02, 1.04, 1.05, 1.06, 1.10, 1.15, 1.18, 1.20, 1.30, 1.55; substitute `Source Serif 4`.
- **Inter Tight**: 400, 500, 600, 9px, 10px, 11px, 12px, 13px, 14px, 16px, 20px, 28px, 1.08, 1.20, 1.30, 1.50, 1.55, 1.60, 1.70, 1.75, 1.90; substitute `Inter`.
- **ui-monospace**: 400, 9px, 11px, 12px, 1.20, 1.55; substitute `SF Mono`.

## Spacing / shape
- Section Gap: `28px`
- Card Padding: `22px`
- Element Gap: `10px`
- Radius: `none: 0px`

## Surface cues
- **Deep Space** `#000000`: Primary page background, foundational surface.
- **Subtle Panel** `#060606`: Slightly elevated panels or background sections, almost indistinguishable from the base.
- **Dark Card** `#1f1f1f`: Card backgrounds, slightly more prominent than general backgrounds.
- **Interactive Border** `#252525`: Borders for interactive elements, distinct containers, and form fields.
- **Elevated Accent** `#313131`: More pronounced borders and minor elevated elements.

## Component cues
- **Underlined Navigation Button**: Header navigation links and secondary actions where emphasis is achieved through a bottom border rather than a solid background.
- **Faint Border Button**: Subtle calls to action or secondary interactive elements within sections, providing a ghost-like presence.
- **Primary Action Button - Lime**: Hero call to action, main navigation launch button. High contrast and immediate visibility.
- **Text Link Button**: Inline textual links or buttons that blend into the surrounding content, often using arrow icons for interaction cues.
- **Section Divider**: Visually separates content blocks, often appearing as a thin horizontal line.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
