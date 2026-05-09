# Langbase - Refero Design MD

- Source: https://styles.refero.design/style/ad48f4ad-42c0-4c91-a189-fa7a73a7a9e9
- Original site: https://langbase.com
- Theme: `dark`
- Industry: `ai`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Midnight Terminal, Pulsing Data

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Screen | `#000000` | neutral | Primary text or dark surface |
| Ghost Ink | `#232324` | neutral | Primary text or dark surface |
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Ash Gray | `#a1a1aa` | neutral | Border, muted text, or supporting surface |
| Slate Text | `#454546` | neutral | Border, muted text, or supporting surface |
| Smoke Border | `#5c5c61` | neutral | Border, muted text, or supporting surface |
| Subtle Cream | `#ebeced` | neutral | Page background or card surface |
| Deep Plum Gradient | `#f6d1ac` | accent | Action accent / signal color |
| Code Block Highlight | `#a1a1a1` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-screen: #000000;
  --ref-ghost-ink: #232324;
  --ref-canvas-white: #fafafa;
  --ref-ash-gray: #a1a1aa;
  --ref-slate-text: #454546;
  --ref-smoke-border: #5c5c61;
  --ref-subtle-cream: #ebeced;
  --ref-deep-plum-gradient: #f6d1ac;
}
```

## Typography direction
- **GeistSans**: 400, 500, 600, 700, 12px, 14px, 16px, 18px, 20px, 48px, 1.00, 1.17, 1.33, 1.40, 1.43, 1.50, 1.56, 1.71, 1.75; substitute `Inter`.
- **GeistMono**: 400, 500, 12px, 13px, 16px, 60px, 72px, 1.00, 1.30, 1.33, 1.50, 1.52; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `24px`
- Card Padding: `24px`
- Element Gap: `12px`
- Radius: `pills: 9999px, default: 4px, buttonsSmall: 12px, buttonsRounded: 100px`

## Component cues
- **Filled Primary Button**: Call to action button for primary actions.
- **Ghost Button**: Secondary action or navigational link button.
- **Subtle Tag Button**: Small, informational tags within a dark section.
- **Card Button**: Prominent interactive elements for larger sections, such as feature cards or navigation options.
- **Header Navigation Link**: Primary navigation links in the header.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
