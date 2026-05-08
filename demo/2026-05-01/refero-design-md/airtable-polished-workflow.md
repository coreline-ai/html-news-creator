# Airtable - Refero Design MD

- Source: https://styles.refero.design/style/f4ef80f4-f6e5-4aea-8045-f99efaf208b8
- Original site: https://airtable.com
- Theme: `light`
- Recommended fit: **Admin operations / developer tooling**

## North star
Polished Workflow, Vibrant Efficiency - like a perfectly organized, brightly lit command center.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| White Canvas | `#ffffff` | neutral | Page background, primary surface color for cards and major sections. |
| Cloud Whisper | `#f8fafc` | neutral | Secondary background, subtle visual break for content cards and sections. |
| Warm Parchment | `#faf5e8` | neutral | Dominant canvas color, offers a slight warmth compared to pure white, establishing the overall page tone. |
| Slate Ink | `#181d26` | neutral | Primary heading color, strong body text, and background for primary action buttons. The core dark neutral. |
| Deep Graphite | `#333333` | neutral | General text color, provides strong contrast against light backgrounds. |
| Soft Steel | `#333840` | neutral | Default body text, slightly softer than Deep Graphite for secondary text information. |
| Silver Mist | `#e0e2e6` | neutral | Subtle borders, dividers, and disabled button backgrounds. |
| Muted Stone | `#41454d` | neutral | Less prominent body text, link text in paragraphs. |

```css
:root {
  --ref-white-canvas: #ffffff;
  --ref-cloud-whisper: #f8fafc;
  --ref-warm-parchment: #faf5e8;
  --ref-slate-ink: #181d26;
  --ref-deep-graphite: #333333;
  --ref-soft-steel: #333840;
  --ref-silver-mist: #e0e2e6;
}
```

## Typography direction
- Primary: **Haas Groot Disp**; substitute `IBM Plex Sans`.
- Secondary/code: **Haas**; substitute `Inter`.

## Spacing / shape
- Section gap: `40-80px`
- Card padding: `24-48px`
- Element gap: `16px`
- Radius: `{'nav': '12px', 'cards': '16px', 'links': '12px', 'buttons': '12px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
