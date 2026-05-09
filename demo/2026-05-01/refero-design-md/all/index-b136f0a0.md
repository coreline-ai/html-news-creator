# Index - Refero Design MD

- Source: https://styles.refero.design/style/b136f0a0-8064-4978-a18e-db54b9362c24
- Original site: https://index.inc
- Theme: `dark`
- Industry: `productivity`
- Recommended fit: **Admin console / run monitor / developer tooling**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
Deep space command console.

## Apply to
- Admin run monitor and review states
- Compact evidence cards and source inspection panels
- Dark-mode operational dashboards

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Void Black | `#02030b` | neutral | Primary text or dark surface |
| Eclipse Gray | `#04061c` | neutral | Primary text or dark surface |
| Twilight Violet | `#0c0a2b` | neutral | Action accent / signal color |
| Ash Slate | `#11132b` | neutral | Primary text or dark surface |
| Slate Blue | `#152e58` | neutral | Action accent / signal color |
| Gunmetal Gray | `#202333` | neutral | Primary text or dark surface |
| Dark Star | `#242444` | neutral | Primary text or dark surface |
| Lunar Violet | `#292a4d` | neutral | Action accent / signal color |
| Nebula Blue | `#2c2b52` | neutral | Action accent / signal color |
| Graphite Border | `#353545` | neutral | Primary text or dark surface |

```css
:root {
  --ref-void-black: #02030b;
  --ref-eclipse-gray: #04061c;
  --ref-twilight-violet: #0c0a2b;
  --ref-ash-slate: #11132b;
  --ref-slate-blue: #152e58;
  --ref-gunmetal-gray: #202333;
  --ref-dark-star: #242444;
  --ref-lunar-violet: #292a4d;
}
```

## Typography direction
- **Inter**: 400, 500, 600, 11px, 13px, 14px, 15px, 16px, 17px, 18px, 24px, 1.50, 1.60; substitute `system-ui`.
- **Index**: 400, 500, 600, 12px, 13px, 14px, 15px, 16px, 17px, 18px, 20px, 22px, 23px, 32px, 42px, 56px, 72px, 1.20, 1.30, 1.50, 1.60; substitute `system-ui`.
- **-apple-system**: 500, 600, 13px, 15px, 1.6.

## Spacing / shape
- Section Gap: `60px`
- Card Padding: `12px`
- Element Gap: `8px`
- Radius: `lg: 20px, md: 12px, sm: 6px, xl: 24px, none: 0px, pill: 30px, round: 50px`

## Surface cues
- **Eclipse Gray Canvas** `#04061c`: Primary page background, base layer.
- **Twilight Violet Surface** `#0c0a2b`: Secondary backgrounds, default card level for content blocks.
- **Deep Space Panel** `#02030b`: Elevated card surfaces, product UI elements, embedded applications.

## Component cues
- **Navigation Link (Ghost)**: Top navigation items, secondary actions within complex UIs.
- **Primary Action Button (Filled)**: Main call to action for the site and product onboarding.
- **Subtle Action Button (Pill)**: Informational prompts or secondary, less urgent actions.
- **Feature Card (Subdued)**: Container for features, testimonials, or content blocks.
- **Data Row Card**: Items within a table or list view, emphasizing content over visual flourish.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
