# Runway - Refero Design MD

- Source: https://styles.refero.design/style/8f623d19-51f6-4da2-bc45-05573cc98283
- Original site: https://runwayml.com
- Theme: `light`
- Industry: `ai`
- Recommended fit: **Research brief / AI trend page**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Precision-engineered black glass. Every element is deliberately placed like components in a high-performance machine, with a single bright light indicating activity.

## Apply to
- Research section pages and model-release briefs
- Lab-note style cards
- AI product/research trend summaries

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Gray | `#6b7280` | neutral | Border, muted text, or supporting surface |
| Runway Midnight | `#2b22fa` | brand | Action accent / signal color |
| Cloud Burst | `#e5e7eb` | neutral | Page background or card surface |
| Graphite | `#404040` | neutral | Border, muted text, or supporting surface |
| Pure White | `#ffffff` | neutral | Page background or card surface |
| Deep Shadow | `#0c0c0c` | neutral | Primary text or dark surface |
| Silver Mist | `#cccccc` | neutral | Border, muted text, or supporting surface |
| Obsidian | `#2a2a2a` | neutral | Primary text or dark surface |
| Ash Gray | `#999999` | neutral | Border, muted text, or supporting surface |
| Pitch Black | `#000000` | neutral | Primary text or dark surface |

```css
:root {
  --ref-storm-gray: #6b7280;
  --ref-runway-midnight: #2b22fa;
  --ref-cloud-burst: #e5e7eb;
  --ref-graphite: #404040;
  --ref-pure-white: #ffffff;
  --ref-deep-shadow: #0c0c0c;
  --ref-silver-mist: #cccccc;
  --ref-obsidian: #2a2a2a;
}
```

## Typography direction
- **abcNormal**: 400, 450, 500, 600, 11px, 13px, 14px, 16px, 20px, 24px, 36px, 40px, 48px, 1.00, 1.10, 1.25, 1.30, 1.43, 1.50; substitute `Inter, Arial`.

## Spacing / shape
- Section Gap: `48-80px`
- Card Padding: `16-24px`
- Element Gap: `4px`
- Radius: `cards: 8px, buttons: 6px, default: 4px`

## Component cues
- **Announcement Banner**: Reference component style.
- **Research & Product Cards**: Reference component style.
- **Feature Detail Block**: Reference component style.
- **Primary Dark Button**: Call to action buttons
- **Ghost Button**: Secondary actions, tertiary navigation

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
