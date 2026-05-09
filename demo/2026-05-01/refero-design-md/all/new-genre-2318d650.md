# New Genre - Refero Design MD

- Source: https://styles.refero.design/style/2318d650-b229-4be0-9adc-9f17cecfd253
- Original site: https://newgenre.studio
- Theme: `light`
- Industry: `design`
- Recommended fit: **Editorial report / executive brief**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Shifting Gradual Horizon — a continuous, subtle color transition across surfaces, like watching a sunrise or sunset unfold.

## Apply to
- Long-form AI report reading experience
- Executive brief layouts and narrative summaries
- Article cards with strong typography hierarchy

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Ebon Depth | `#000000` | neutral | Primary text or dark surface |
| Whisper White | `#ffffff` | neutral | Page background or card surface |
| Midnight Oil Stain | `#1e1310` | neutral | Primary text or dark surface |
| Onyx Shadow | `#0c1018` | neutral | Primary text or dark surface |
| Mist Gray | `#9e9fa3` | neutral | Border, muted text, or supporting surface |
| Steel Glimmer | `#6d7074` | neutral | Border, muted text, or supporting surface |
| Sky Gradient | `#280e01` | brand | Action accent / signal color |
| Amber Glow | `#ffe600` | accent | Action accent / signal color |
| Sunset Gradient | `#f7f3f0` | brand | Action accent / signal color |
| Earthfire Gradient | `#1e1310` | brand | Action accent / signal color |

```css
:root {
  --ref-ebon-depth: #000000;
  --ref-whisper-white: #ffffff;
  --ref-midnight-oil-stain: #1e1310;
  --ref-onyx-shadow: #0c1018;
  --ref-mist-gray: #9e9fa3;
  --ref-steel-glimmer: #6d7074;
  --ref-sky-gradient: #280e01;
  --ref-amber-glow: #ffe600;
}
```

## Typography direction
- **Serrif Condensed Regular**: 400, 64px, 72px, 1.05; substitute `IBM Plex Serif`.
- **Saans Variable**: 300, 400, 500, 12px, 14px, 16px, 20px, 24px, 32px, 1.00, 1.10, 1.15, 1.40; substitute `Inter Variable`.
- **Saans Medium**: 400, 570, 16px, 1.00; substitute `Inter Medium`.

## Spacing / shape
- Section Gap: `48-52px`
- Card Padding: `16-32px`
- Element Gap: `6-24px`
- Radius: `buttons: 50px, default: 8px, components: 16px, pillButtons: 90px`

## Component cues
- **Cookie Consent Banner**: Reference component style.
- **Process Step Cards**: Reference component style.
- **Subtle Accent Button Group**: Reference component style.
- **Navigation Link**: Interactive text link
- **Subtle Accent Button**: Ghost button with subtle background

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
