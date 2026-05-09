# Deezer - Refero Design MD

- Source: https://styles.refero.design/style/502af24a-b765-44b2-828f-dd610f27a125
- Original site: https://deezer.com
- Theme: `dark`
- Industry: `media`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Electric Violet Nightclub – a bold, high-contrast digital space pulsates with vibrant purple against a deep, dark backdrop.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#0f0d13` | neutral | Primary text or dark surface |
| Ghost White | `#fdfcfe` | neutral | Page background or card surface |
| Slate Echo | `#555257` | neutral | Border, muted text, or supporting surface |
| Ash Whisper | `#a9a6aa` | neutral | Border, muted text, or supporting surface |
| Deep Violet | `#a238ff` | brand | Action accent / signal color |
| Lavender Haze | `#d09aff` | brand | Action accent / signal color |

```css
:root {
  --ref-midnight-void: #0f0d13;
  --ref-ghost-white: #fdfcfe;
  --ref-slate-echo: #555257;
  --ref-ash-whisper: #a9a6aa;
  --ref-deep-violet: #a238ff;
  --ref-lavender-haze: #d09aff;
}
```

## Typography direction
- **Deezer Brand**: 700, 800, 18px, 19px, 24px, 35px, 46px, 56px, 120px, 140px, 0.71, 0.90, 1.00, 1.04, 1.20; substitute `Montserrat Black`.
- **Inter**: 400, 500, 600, 700, 12px, 14px, 16px, 20px, 1.00, 1.20, 1.33, 1.38, 1.50, 1.56, 1.75, 1.79; substitute `Inter`.

## Spacing / shape
- Section Gap: `90-140px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 8px, badges: 9px / 75%, buttons: 12px, general: 8px`

## Component cues
- **Pricing Card — Premium 1 Month Free**: Reference component style.
- **FAQ Accordion**: Reference component style.
- **CTA Banner — Live the Music with Deezer**: Reference component style.
- **Secondary Ghost Button**: Action
- **Tertiary Dark Button**: Action

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
