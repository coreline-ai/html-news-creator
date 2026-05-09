# Pika - Refero Design MD

- Source: https://styles.refero.design/style/9fe9f106-44d2-45fc-9873-10c6ddcfa59b
- Original site: https://pika.art
- Theme: `mixed`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Dual-pane studio and control room. One side warm, inviting; the other dark, efficient.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Buttermilk Base | `#ffedd2` | brand | Action accent / signal color |
| Inkwell Deep | `#0d0d0d` | neutral | Primary text or dark surface |
| Carbon Panel | `#1f1f1f` | neutral | Primary text or dark surface |
| Paper White | `#ffffff` | neutral | Page background or card surface |
| Chrome Edges | `#e5e7eb` | neutral | Page background or card surface |
| Facebook Blue | `#4267b2` | accent | Action accent / signal color |
| Discord Purple | `#5865f2` | accent | Action accent / signal color |
| Google Yellow | `#ffc107` | accent | Action accent / signal color |

```css
:root {
  --ref-buttermilk-base: #ffedd2;
  --ref-inkwell-deep: #0d0d0d;
  --ref-carbon-panel: #1f1f1f;
  --ref-paper-white: #ffffff;
  --ref-chrome-edges: #e5e7eb;
  --ref-facebook-blue: #4267b2;
  --ref-discord-purple: #5865f2;
  --ref-google-yellow: #ffc107;
}
```

## Typography direction
- **telka**: 300, 400, 450, 12px, 14px, 16px, 1.33, 1.43, 1.50; substitute `Inter`.
- **telkaExtended**: 900, 32px, 1.13; substitute `Inter Black`.

## Spacing / shape
- Section Gap: `56px`
- Element Gap: `8px`
- Radius: `buttons: 6px, videoPlayer: 10px`

## Component cues
- **Sign-in Panel**: Reference component style.
- **Feature Promo Card**: Reference component style.
- **Footer Links Bar**: Reference component style.
- **Primary Sign-in Button**: Main call to action for email sign-in.
- **Social Sign-in Button**: Alternative sign-in options via social platforms.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
