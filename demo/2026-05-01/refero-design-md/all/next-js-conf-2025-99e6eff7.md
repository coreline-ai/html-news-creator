# Next.js Conf 2025 - Refero Design MD

- Source: https://styles.refero.design/style/99e6eff7-871d-4018-bb81-d2ea235f4f91
- Original site: https://nextjs.org/conf
- Theme: `light`
- Industry: `devtools`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Pragmatic developer canvas: sharp type on white, pixel grid accents.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#fafafa` | neutral | Page background or card surface |
| Text Primary | `#171717` | neutral | Primary text or dark surface |
| Text Secondary | `#4d4d4d` | neutral | Border, muted text, or supporting surface |
| Text Tertiary | `#8f8f8f` | neutral | Border, muted text, or supporting surface |
| Border Light | `#e6e6e6` | neutral | Page background or card surface |
| Info Background | `#e9f4ff` | semantic | Action accent / signal color |
| Function Blue | `#0057ff` | brand | Action accent / signal color |
| Accent Blue | `#005ff2` | accent | Action accent / signal color |
| Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-canvas-white: #fafafa;
  --ref-text-primary: #171717;
  --ref-text-secondary: #4d4d4d;
  --ref-text-tertiary: #8f8f8f;
  --ref-border-light: #e6e6e6;
  --ref-info-background: #e9f4ff;
  --ref-function-blue: #0057ff;
  --ref-accent-blue: #005ff2;
}
```

## Typography direction
- **Geist**: 400, 500, 600, 12px, 14px, 16px, 32px, 48px, 72px, 1.00, 1.43, 1.50; substitute `Inter`.
- **Geist Mono**: 400, 13px, 14px, 16px, 18px, 20px, 1.00, 1.11, 1.50; substitute `JetBrains Mono`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `20px`
- Element Gap: `24px`
- Radius: `cards: 8px, links: 8px, badges: 9999px, images: 8px, buttons: 100px`

## Surface cues
- **Base Canvas** `#fafafa`: Dominant background for the entire application, providing a clean, bright foundation.
- **Info Surface** `#e9f4ff`: Used as a subtle background for informational badges, hinting at interactivity or newness.
- **Card Surface** `#e6e6e6`: Background for certain card-like content areas or partner blocks, providing a very subtle visual separation without shadow.

## Component cues
- **Primary Filled Button**: Main call-to-action button for initiating key actions.
- **Ghost Button**: Secondary action or navigation buttons that should not draw primary attention.
- **Conference Card**: Containers for content blocks like session details or speaker information.
- **New Feature Badge**: Highlights new or important informational elements, often associated with updates.
- **Navigation Link**: Top-level navigation items, directing users to main sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
