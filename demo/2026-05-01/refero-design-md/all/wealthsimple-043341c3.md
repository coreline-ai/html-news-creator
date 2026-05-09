# Wealthsimple - Refero Design MD

- Source: https://styles.refero.design/style/043341c3-cf82-4be1-9142-fa5e6a370ca9
- Original site: https://wealthsimple.com
- Theme: `light`
- Industry: `fintech`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Warm Minimalism on Linen. Imagine precise, intentional content laid out on a finely textured, off-white linen, framed by subtle, earthy tones.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Greyscale Black | `#32302f` | neutral | Primary text or dark surface |
| Linen White | `#fcfcfc` | neutral | Page background or card surface |
| Slate Border | `#e4e2e1` | neutral | Page background or card surface |
| Text Muted | `#686664` | neutral | Border, muted text, or supporting surface |
| Ash Canvas | `#f1f0f0` | neutral | Page background or card surface |
| Input Gray | `#eeece7` | neutral | Page background or card surface |
| Ocean Tint | `#d3e5f3` | brand | Action accent / signal color |
| Success Green | `#486635` | semantic | Action accent / signal color |
| Error Red | `#a43d12` | semantic | Action accent / signal color |
| Focus Outline | `#afaaa7` | accent | Action accent / signal color |

```css
:root {
  --ref-greyscale-black: #32302f;
  --ref-linen-white: #fcfcfc;
  --ref-slate-border: #e4e2e1;
  --ref-text-muted: #686664;
  --ref-ash-canvas: #f1f0f0;
  --ref-input-gray: #eeece7;
  --ref-ocean-tint: #d3e5f3;
  --ref-success-green: #486635;
}
```

## Typography direction
- **the-future**: 400, 500, 14px, 16px, 18px, 20px, 56px, 58px, 1.00, 1.16, 1.40; substitute `system-ui, sans-serif`.
- **wealthsimple-sans**: 400, 16px, 1.20; substitute `Inter, system-ui, sans-serif`.
- **tiempos**: 400, 500, 14px, 16px, 18px, 36px, 56px, 64px, 72px, 84px, 1.08, 1.16, 1.24; substitute `serif`.

## Spacing / shape
- Section Gap: `40-48px`
- Element Gap: `8px`
- Radius: `cards: 100px, minor: 2px, inputs: 100px, buttons: 1600px`

## Component cues
- **Button Group**: Reference component style.
- **Feature Cards Row**: Reference component style.
- **Product Feature Section**: Reference component style.
- **Secondary Outlined Button**: Secondary action, navigation
- **Small Utility Button**: Icon-only actions, small interactive elements

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
