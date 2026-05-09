# aave.com - Refero Design MD

- Source: https://styles.refero.design/style/e352ec32-830a-4650-b7c2-d32a5f559f7e
- Original site: https://aave.com
- Theme: `mixed`
- Industry: `fintech`
- Recommended fit: **Source ledger / evidence dashboard**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep Slate Precision

## Apply to
- Source ledger, ranking, and verification screens
- Cluster evidence dashboards
- Dense data tables with clear hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background or card surface |
| Ink Black | `#221d1d` | neutral | Primary text or dark surface |
| Pewter | `#636161` | neutral | Border, muted text, or supporting surface |
| Misty Gray | `#8f8e8e` | neutral | Border, muted text, or supporting surface |
| Obsidian | `#0f0f10` | neutral | Primary text or dark surface |
| Light Alabaster | `#f6f7f4` | neutral | Page background or card surface |
| Slate Dust | `#858387` | neutral | Border, muted text, or supporting surface |
| Cosmic Violet | `#998eff` | brand | Action accent / signal color |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-ink-black: #221d1d;
  --ref-pewter: #636161;
  --ref-misty-gray: #8f8e8e;
  --ref-obsidian: #0f0f10;
  --ref-light-alabaster: #f6f7f4;
  --ref-slate-dust: #858387;
  --ref-cosmic-violet: #998eff;
}
```

## Typography direction
- **Aave Repro**: 400, 450, 500, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 24px, 32px, 40px, 72px, 1.00.
- **Inter**: 400, 700, 10px, 14px, 1.50.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `cards: 24px, input: 20px, pills: 1584px, buttons: 20px, navItems: 50px`

## Surface cues
- **Slate Dust** `#858387`: Base background for most content sections, providing a dark canvas.
- **Light Alabaster** `#f6f7f4`: Secondary background for cards and distinct content blocks, especially in lighter sections.
- **White Canvas** `#ffffff`: Primary background for hero sections and elevated elements, creating contrast and visual emphasis.

## Component cues
- **Primary Call to Action Button**: Filled button indicating primary interaction.
- **Ghost Button (Dark)**: Lightweight, secondary action on dark backgrounds.
- **Ghost Button (Light)**: Lightweight, secondary action on light backgrounds.
- **Navigation Link Button**: Header navigation items that act as buttons.
- **Card (White Canvas Background)**: Content container for features or data on white backgrounds.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
