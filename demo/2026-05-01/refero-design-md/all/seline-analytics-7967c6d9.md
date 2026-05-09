# Seline Analytics - Refero Design MD

- Source: https://styles.refero.design/style/7967c6d9-e50c-42b5-b4d1-74003ba41781
- Original site: https://seline.so
- Theme: `light`
- Industry: `saas`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Crisp Data Canvas

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Cloud White | `#ffffff` | neutral | Page background or card surface |
| Canvas Fog | `#fafaf9` | neutral | Page background or card surface |
| Slate Text | `#0c0a09` | neutral | Primary text or dark surface |
| Ash Gray | `#78716c` | neutral | Border, muted text, or supporting surface |
| Stone Border | `#e5e7eb` | neutral | Page background or card surface |
| Platinum Outline | `#d6d3d1` | neutral | Border, muted text, or supporting surface |
| Steel Gray | `#a8a29e` | neutral | Border, muted text, or supporting surface |
| Hover Stone | `#c9c5c2` | neutral | Border, muted text, or supporting surface |
| Ghost Ink | `#1c1917` | neutral | Primary text or dark surface |
| Chartwell Blue | `#3ba6f1` | brand | Action accent / signal color |

```css
:root {
  --ref-cloud-white: #ffffff;
  --ref-canvas-fog: #fafaf9;
  --ref-slate-text: #0c0a09;
  --ref-ash-gray: #78716c;
  --ref-stone-border: #e5e7eb;
  --ref-platinum-outline: #d6d3d1;
  --ref-steel-gray: #a8a29e;
  --ref-hover-stone: #c9c5c2;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 12px, 13px, 14px, 15px, 16px, 18px, 1.00, 1.29, 1.33, 1.43, 1.50, 1.53, 1.54, 1.56, 1.64, 1.67, 1.69, 1.77, 1.92; substitute `system-ui`.
- **roobert**: 400, 500, 16px, 18px, 20px, 32px, 52px, 1.00, 1.12, 1.20, 1.22, 1.25, 1.69; substitute `sans-serif`.

## Spacing / shape
- Section Gap: `48px`
- Card Padding: `24px`
- Element Gap: `8px`
- Radius: `tags: 9999px, cards: 10px, inputs: 4px, buttons: 9999px, largeCard: 16px`

## Surface cues
- **Canvas Fog** `#fafaf9`: Base page background. Provides a warm achromatic canvas for content.
- **Cloud White** `#ffffff`: Primary content surface for cards, modals, and primary UI elements. Sits directly above Canvas Fog.

## Component cues
- **Primary Filled Button**: Call to action.
- **Ghost Button - Light**: Secondary actions or navigation items.
- **Ghost Button - Dark Text**: Secondary actions with higher text prominence.
- **Subtle Ghost Button**: Tertiary actions, tabs, or selections within confined spaces.
- **Dashboard Card**: Container for data visualizations and content blocks.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
