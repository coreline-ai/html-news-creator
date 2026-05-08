# Hyperstudio - Refero Design MD

- Source: https://styles.refero.design/style/8eb9c53e-d69c-497a-b640-610856cf3a60
- Original site: https://hyperstudio.org
- Theme: `dark`
- Recommended fit: **Terminal Ops / Source Ledger**
- Priority: **Supporting**

## Why this fits html-news-creator
Strong operations reference for logs and verification: near-black monochrome base with amber and status-green accents only.

## Apply to
- Terminal Ops variant
- Source health and status badges
- Pipeline logs and structured event panels

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Midnight Void | `#101010` | neutral | Primary page background, deepest dark surface. |
| Deep Space | `#080808` | neutral | Secondary background, slightly darker than Midnight Void, used for subtle depth. |
| Polar White | `#F3F3F3` | neutral | Primary text color, hero headlines, clear contrast against dark backgrounds. |
| Absolute Zero | `#FFFFFF` | neutral | Accent text and background for interactive elements like buttons, header text. |
| Ash Gray | `#949494` | neutral | Secondary text, subtle borders, slightly toned down from main text. |
| Dark Carbon | `#333333` | neutral | Border colors, muted backgrounds for secondary elements. |
| Slate | `#C1C1C1` | neutral | Subtle borders, outlines, dividers. |
| Light Gradients | `#B5B5B5` | neutral | Subtle background gradient for UI elements, providing a soft, almost imperceptible texture. |

```css
:root {
  --ref-midnight-void: #101010;
  --ref-deep-space: #080808;
  --ref-polar-white: #F3F3F3;
  --ref-absolute-zero: #FFFFFF;
  --ref-ash-gray: #949494;
  --ref-dark-carbon: #333333;
  --ref-slate: #C1C1C1;
}
```

## Typography direction
- Primary: **Aeonik**; substitute `Inter`.
- Secondary/code: **Input**; substitute `IBM Plex Mono`.

## Spacing / shape
- Section gap: `64px`
- Card padding: `24px`
- Element gap: `10px`
- Radius: `{'tags': '20px', 'buttons': '8px', 'default': '8px', 'statusIcons': '99px'}`

## Agent notes
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- Keep the project content hierarchy first: section title, why it matters, source evidence, confidence, and image evidence.
