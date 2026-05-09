# dope.security - Refero Design MD

- Source: https://styles.refero.design/style/e1f18a7e-5af1-46b3-8f89-bce6c78b80d4
- Original site: https://dope.security
- Theme: `dark`
- Industry: `saas`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Celestial command center

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Eclipse | `#090909` | neutral | Primary text or dark surface |
| Cloud Whisper | `#f7f9fa` | neutral | Page background or card surface |
| Code Ghost | `#f0f0f0` | neutral | Page background or card surface |
| Slate Hint | `#6b6b6b` | neutral | Border, muted text, or supporting surface |
| Steel Accent | `#475467` | neutral | Border, muted text, or supporting surface |
| Deep Violet | `#af50ff` | brand | Action accent / signal color |
| Cosmic Gradient A | `#6c4bd6` | accent | Action accent / signal color |
| Cosmic Gradient B | `#401860` | accent | Action accent / signal color |

```css
:root {
  --ref-midnight-eclipse: #090909;
  --ref-cloud-whisper: #f7f9fa;
  --ref-code-ghost: #f0f0f0;
  --ref-slate-hint: #6b6b6b;
  --ref-steel-accent: #475467;
  --ref-deep-violet: #af50ff;
  --ref-cosmic-gradient-a: #6c4bd6;
  --ref-cosmic-gradient-b: #401860;
}
```

## Typography direction
- **Whyte Inktrap**: 300, 400, 500, 700, 10px, 12px, 14px, 16px, 18px, 20px, 24px, 28px, 32px, 40px, 48px, 49px, 50px, 64px, 80px, 88px, 0.80, 0.90, 1.00, 1.11, 1.20, 1.25, 1.50, 1.56, 1.60; substitute `Montserrat, sans-serif`.
- **Whyte Inktrap Mono**: 400, 14px, 74px, 0.90, 1.50; substitute `Space Mono, monospace`.
- **GrandSlang**: 300, 400, 32px, 50px, 64px, 88px, 146px, 0.80, 1.20, 1.25, 1.50; substitute `Playfair Display, serif`.

## Spacing / shape
- Section Gap: `64px`
- Card Padding: `16px`
- Element Gap: `16px`
- Page Max Width: `1200px`
- Radius: `tags: 99px, cards: 19.2px, buttons: 8px, circular: 10000px, pillButtons: 1584px, smallWidgets: 10.8px`

## Surface cues
- **Deep Space Canvas** `#090909`: Primary page background, base for all content sections.
- **Frosted Pane** `#00000000`: Translucent elements within sections, often with backdrop blur, such as informational cards or content containers in headers.
- **Gradient Field** `#401860`: Layered backgrounds for feature cards or interactive modules, providing subtle color variation through gradients.

## Component cues
- **Primary Filled Button**: Call to action.
- **Ghost Button (Primary)**: Secondary call to action.
- **Pill Button**: Interactive filters or small, rounded CTAs.
- **Small Ghost Button**: Tertiary actions or compact navigation items.
- **Frosted Card (Large)**: Content segmentation and informational display, primarily in hero sections.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
