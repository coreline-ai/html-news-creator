# Dash Digital Studio - Refero Design MD

- Source: https://styles.refero.design/style/6036b661-3886-4f76-a5e6-bb8960eb7db5
- Original site: https://dashdigital.studio
- Theme: `light`
- Industry: `agency`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Architectural blueprints on concrete

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Storm Canvas | `#f0f0f0` | neutral | Page background or card surface |
| Carbon Text | `#2a2a2a` | neutral | Primary text or dark surface |
| Midnight Ink | `#000000` | neutral | Primary text or dark surface |
| Cloud Gray | `#fafafa` | neutral | Page background or card surface |
| Slate Divider | `#d6d6d6` | neutral | Border, muted text, or supporting surface |

```css
:root {
  --ref-storm-canvas: #f0f0f0;
  --ref-carbon-text: #2a2a2a;
  --ref-midnight-ink: #000000;
  --ref-cloud-gray: #fafafa;
  --ref-slate-divider: #d6d6d6;
}
```

## Typography direction
- **Founders Grotesk**: 300, 400, 12px, 14px, 16px, 17px, 22px, 40px, 70px, 101px, 0.80, 0.88, 0.90, 1.00, 1.17, 1.20; substitute `Inter`.
- **Editorial Neue**: 400, 16px, 0.90; substitute `Playfair Display`.

## Spacing / shape
- Section Gap: `115px`
- Card Padding: `14px`
- Element Gap: `4px`
- Page Max Width: `1200px`
- Radius: `pill: 999px, default: 0px`

## Surface cues
- **Storm Canvas** `#f0f0f0`: Primary page background
- **Cloud Gray** `#fafafa`: Elevated card surface, subtle content blocks
- **Slate Divider** `#d6d6d6`: Background for less prominent areas or subtle separation

## Component cues
- **Ghost Nav Link**: Navigation item and secondary calls to action
- **Text Accent Button**: Outlined textual action prompts, typically for 'View Case Study' or 'More +' links
- **Project Card**: Displays individual portfolio projects or featured content.
- **Information Block Card**: Structured content blocks, such as client testimonials or service descriptions.
- **Pill Badge**: Small, descriptive labels or navigational markers.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
