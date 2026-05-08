# xAI - Refero Design MD

- Source: https://styles.refero.design/style/3b83dfe4-2f53-4a4d-819d-e6045ca5f7dc
- Original site: https://x.ai
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Midnight Command Center: A dark, responsive interface with precise typographic hierarchy and subtle interactive cues.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Midnight | `#0c0c0b` | neutral | Neutral form states, badge text, and quiet UI feedback where color should stay understated. Do not promote it to the pr. |
| Faded Steel | `#1f2228` | neutral | Secondary background, subtle borders for ghost buttons and card outlines. Its slight tint keeps it from being pure black |
| Frost White | `#ffffff` | neutral | Primary text, interactive element text, button backgrounds, and subtle highlight shadows. Provides high contrast on dar. |
| Muted Ash | `#7d8187` | neutral | Secondary text for badges, navigation, and body copy. Offers readability without high contrast; Decorative footer backg. |
| Whisper Gray | `#474747` | neutral | Subtle button and navigation borders, creating a very soft outline |
| Electric Blue | `#2563eb` | accent | Violet state accent for badges, validation surfaces, and short status labels. Do not promote it to the primary CTA color |

```css
:root {
  --ref-deep-midnight: #0c0c0b;
  --ref-faded-steel: #1f2228;
  --ref-frost-white: #ffffff;
  --ref-muted-ash: #7d8187;
  --ref-whisper-gray: #474747;
  --ref-electric-blue: #2563eb;
}
```

## Typography direction
- Primary: **universalSans**; substitute `Inter`.
- Secondary/code: **GeistMono**; substitute `Space Mono`.

## Spacing / shape
- Section gap: `48px`
- Card padding: `16px`
- Element gap: `12px`
- Radius: `{'inputs': '24px', 'buttons': '9999px', 'calloutCards': '0px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
