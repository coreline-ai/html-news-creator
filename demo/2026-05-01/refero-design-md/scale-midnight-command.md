# Scale - Refero Design MD

- Source: https://styles.refero.design/style/e81d4724-9615-4159-8678-cef35f986cab
- Original site: https://scale.com
- Theme: `dark`
- Recommended fit: **Admin operations / developer tooling**

## North star
Midnight Command Center: An expanse of polished dark surfaces, illuminated by precise white text and the occasional shimmer of an iridescent, almost holographic, light.

## Why this fits html-news-creator
Useful for pipeline monitor, run logs, source health, and operator review surfaces.

## Apply to
- Run progress and status systems
- Source ledger / diagnostics panels
- Compact technical cards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Deep Space | `#000000` | neutral | Primary page background, card backgrounds, creating a high-contrast canvas. |
| Ghost White | `#ffffff` | neutral | Primary text color for headlines and body text, accentuating information against the dark background. Also used for bor. |
| Iron Slate | `#a1a1a1` | neutral | Secondary text for less prominent information, active navigation links, and subtle borders. |
| Halo Pale | `#f4f0ff` | neutral | Subtle, near-white text for secondary links and body text in less prominent sections. This provides a very soft contras. |
| Shadow Tint | `#020202` | neutral | Subtle shadows and background for elements that need a touch more depth than pure black. |
| Subtle Gray | `#e5e5e5` | neutral | Text and icon color, for details that require slightly less prominence than Ghost White. |
| Iridescent Glow | `#bbdef2` | brand | Backgrounds of geometric abstract shapes, providing a luminous, futuristic visual accent. |
| Spectrum Flare | `#d1aad7` | brand | Used for the lighter parts of the iridescent gradient, giving it a soft, ethereal quality. |

```css
:root {
  --ref-deep-space: #000000;
  --ref-ghost-white: #ffffff;
  --ref-iron-slate: #a1a1a1;
  --ref-halo-pale: #f4f0ff;
  --ref-shadow-tint: #020202;
  --ref-subtle-gray: #e5e5e5;
  --ref-iridescent-glow: #bbdef2;
}
```

## Typography direction
- Primary: **Inter**; substitute `system-ui, sans-serif`.
- Secondary/code: **aeonik**; substitute `Montserrat, sans-serif`.

## Spacing / shape
- Section gap: `32px`
- Card padding: `24px`
- Element gap: `8px`
- Radius: `{'links': '16px', 'lists': '4px', 'default': '8px'}`

## Agent notes
- Treat this as reference material, not a direct template copy.
- Do not apply this wholesale to templates/report_newsstream.html.j2 unless the user explicitly asks for an HTML report migration.
- Preserve the project information hierarchy: title, why it matters, source evidence, confidence, image evidence.
