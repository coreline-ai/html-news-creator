# Shares - Refero Design MD

- Source: https://styles.refero.design/style/cd293b92-71a3-4cc2-a56b-0fa60425b42a
- Original site: https://shares.io
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
White-canvas violet-accent structured finance

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#1f1f1f` | neutral | Primary text or dark surface |
| Carbon Gray | `#333333` | neutral | Primary text or dark surface |
| Cloud Gray | `#f6f6f6` | neutral | Page background or card surface |
| Steel Gray | `#888888` | neutral | Border, muted text, or supporting surface |
| Stone Gray | `#b0b0b0` | neutral | Border, muted text, or supporting surface |
| Silver Mist | `#e7e7e7` | neutral | Page background or card surface |
| Slate Gray | `#5d5d5d` | neutral | Border, muted text, or supporting surface |
| Shares Violet | `#594ff4` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-ink-black: #1f1f1f;
  --ref-carbon-gray: #333333;
  --ref-cloud-gray: #f6f6f6;
  --ref-steel-gray: #888888;
  --ref-stone-gray: #b0b0b0;
  --ref-silver-mist: #e7e7e7;
  --ref-slate-gray: #5d5d5d;
}
```

## Typography direction
- **Aeonik**: 500, 700, 14px, 15px, 16px, 17px, 18px, 20px, 26px, 36px, 56px, 72px, 1.00, 1.05, 1.10, 1.15, 1.18, 1.20, 1.33, 1.43, 1.50; substitute `Inter`.
- **Rubik**: 500, 14px, 1.50; substitute `Roboto`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `24px`
- Page Max Width: `1224px`
- Radius: `cards: 36px, small: 4px, inputs: 16px, buttons: 99px, largeFeatures: 60px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background, base layer.
- **Cloud Gray** `#f6f6f6`: Content cards, section backgrounds, subtle elevation from the canvas.

## Component cues
- **Primary Violet Button**: Main call to action button.
- **Light Ghost Button**: Secondary action or navigation item on light backgrounds.
- **Text Link Button**: Minimalist action trigger, often for 'learn more' or navigation.
- **Product Feature Card**: Showcasing distinct product features or information blocks.
- **FAQ Accordion Card**: Expandable content sections for frequently asked questions.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
