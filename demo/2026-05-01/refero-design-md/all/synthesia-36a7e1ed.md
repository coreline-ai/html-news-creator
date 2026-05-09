# Synthesia - Refero Design MD

- Source: https://styles.refero.design/style/36a7e1ed-8d14-456b-b828-ff4f47797a74
- Original site: https://www.synthesia.io
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Indigo-accented data canvas

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Subtle Ash | `#e6eaf4` | neutral | Page background or card surface |
| Ghost Fog | `#f5f8ff` | neutral | Page background or card surface |
| Slate Text | `#333b52` | neutral | Primary text or dark surface |
| Midnight Indigo | `#0d0f2c` | brand | Action accent / signal color |
| Muted Gray | `#656c86` | neutral | Border, muted text, or supporting surface |
| Input Border | `#d1d6e5` | neutral | Border, muted text, or supporting surface |
| Action Indigo | `#3e57da` | brand | Action accent / signal color |
| Sky Veil | `#c6d7fe` | accent | Action accent / signal color |
| Deep Accent Indigo | `#1f235b` | brand | Action accent / signal color |

```css
:root {
  --ref-canvas-white: #ffffff;
  --ref-subtle-ash: #e6eaf4;
  --ref-ghost-fog: #f5f8ff;
  --ref-slate-text: #333b52;
  --ref-midnight-indigo: #0d0f2c;
  --ref-muted-gray: #656c86;
  --ref-input-border: #d1d6e5;
  --ref-action-indigo: #3e57da;
}
```

## Typography direction
- **Basiersquare Webfont**: 400, 500, 12px, 14px, 15px, 16px, 18px, 20px, 28px, 40px, 56px, 88px, 1.00, 1.04, 1.10, 1.20, 1.21, 1.40, 1.43, 1.44, 1.50, 1.57, 1.60.

## Spacing / shape
- Section Gap: `40px`
- Card Padding: `32px`
- Element Gap: `24px`
- Page Max Width: `1200px`
- Radius: `cards: 24px, badges: 999px, inputs: 12px, buttons: 12px, smallComponents: 16px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and base for most content sections.
- **Ghost Fog** `#f5f8ff`: Slightly elevated background for cards and secondary panels, offering subtle differentiation from the main canvas.
- **Canvas White Elevated** `#ffffff`: Card surfaces and modal backgrounds that receive a distinct shadow for elevation.

## Component cues
- **Primary Filled Button**: Main call-to-action button, signaling key interactions.
- **Secondary Outlined Button**: Subtle alternative actions, often paired with a primary button.
- **Ghost Link Button**: Discreet, text-based actions found in navigation or inline.
- **Elevated Card**: Content container that gently floats above the page background, drawing attention.
- **Subtle Background Card**: Content container with a soft background, used for grouping related information.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
