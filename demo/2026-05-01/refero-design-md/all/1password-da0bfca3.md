# 1Password - Refero Design MD

- Source: https://styles.refero.design/style/da0bfca3-df1d-49d9-ae25-61d8f348426f
- Original site: https://1password.com
- Theme: `mixed`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Secure Airlock Behind Glass. A system that moves from the protective dark of an airlock to the bright clarity of a control room.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Brand Blue | `#145fe4` | brand | Action accent / signal color |
| Hero Fade | `#145fe4` | brand | Action accent / signal color |
| White | `#ffffff` | neutral | Page background or card surface |
| Onyx | `#000000` | neutral | Primary text or dark surface |
| Deep Space | `#1d1d21` | neutral | Primary text or dark surface |
| Void | `#242529` | neutral | Primary text or dark surface |
| Graphite | `#303136` | neutral | Primary text or dark surface |
| Ash | `#d7d7db` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-brand-blue: #145fe4;
  --ref-hero-fade: #145fe4;
  --ref-white: #ffffff;
  --ref-onyx: #000000;
  --ref-deep-space: #1d1d21;
  --ref-void: #242529;
  --ref-graphite: #303136;
  --ref-ash: #d7d7db;
}
```

## Typography direction
- **agileSans**: 300, 350, 400, 500, 14px, 16px, 18px, 20px, 32px, 40px, 48px, 64px, 88px, 128px, 1.10, 1.20, 1.25, 1.43, 1.50, 1.60; substitute `Inter, Manrope`.
- **ui-sans-serif**: 400, 16px, 1.50; substitute `System UI`.

## Spacing / shape
- Section Gap: `80-120px`
- Card Padding: `24px`
- Element Gap: `8-16px`
- Page Max Width: `1200px`
- Radius: `cards: 16px, inputs: 8px, buttons: 9999px`

## Component cues
- **Button Group — Primary + Secondary CTAs**: Reference component style.
- **Business / Personal Toggle**: Reference component style.
- **Feature Cards — Discover, Secure, Audit**: Reference component style.
- **Primary CTA Button**: The main call-to-action.
- **Secondary CTA Button**: A secondary call-to-action, typically used on dark backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
