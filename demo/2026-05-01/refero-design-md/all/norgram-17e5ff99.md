# Norgram - Refero Design MD

- Source: https://styles.refero.design/style/17e5ff99-38c1-4ad6-8910-648f5798b3a5
- Original site: https://www.norgram.co
- Theme: `mixed`
- Industry: `design`
- Recommended fit: **Design reference / webapp exploration**
- Status: generated local summary; existing curated IDs are not overwritten

## Why this fits html-news-creator
monochromatic architectural blueprint

## Apply to
- General webapp UI exploration
- Demo cards and catalog surfaces
- Future admin/subscriber UI references

## Core tokens to borrow

| Name | Hex | Group | Suggested role |
|---|---:|---|---|
| Obsidian | `#000000` | neutral | Primary text or dark surface |
| Canvas White | `#ffffff` | neutral | Page background or card surface |
| Deep Graphite | `#141414` | neutral | Primary text or dark surface |
| Powder Gray | `#efefef` | neutral | Page background or card surface |
| Ash Mist | `#777777` | neutral | Border, muted text, or supporting surface |
| Soft Stone | `#cecece` | neutral | Border, muted text, or supporting surface |
| Whisper Gray | `#b2b2b2` | neutral | Border, muted text, or supporting surface |
| Smoked Glass | `#3f3f3f` | neutral | Primary text or dark surface |

```css
:root {
  --ref-obsidian: #000000;
  --ref-canvas-white: #ffffff;
  --ref-deep-graphite: #141414;
  --ref-powder-gray: #efefef;
  --ref-ash-mist: #777777;
  --ref-soft-stone: #cecece;
  --ref-whisper-gray: #b2b2b2;
  --ref-smoked-glass: #3f3f3f;
}
```

## Typography direction
- **Helvetica Now Display**: 400, 500, 10px, 12px, 36px, 87px, 1.00, 1.10, 1.17, 1.67; substitute `Inter`.
- **Times**: 400, 14px, 16px, 1.43, 1.50; substitute `Times New Roman`.
- **Helvetica Now Display**: use as primary family; substitute `Inter`.

## Spacing / shape
- Section Gap: `68px`
- Card Padding: `0px`
- Element Gap: `8px`
- Radius: `cards: 4.0678px, forms: 10px, links: 26px, buttons: 7px`

## Surface cues
- **Canvas White** `#ffffff`: Primary page background and default content areas.
- **Powder Gray** `#efefef`: Slightly elevated backgrounds, subtle containers, or section dividers.
- **Deep Graphite** `#141414`: Darker card surfaces and distinct content blocks within a lighter theme.
- **Obsidian** `#000000`: Dominant background for full-bleed dark sections, showcasing high-contrast content.
- **Smoked Glass** `#3f3f3f`: Transparent overlay for interactive elements like toast notifications, providing context without obscuring.

## Component cues
- **Ghost Player Button**: Interactive control for media playback or navigation within content blocks.
- **Toast Notification Button**: Close button for ephemeral notifications or alerts.
- **Basic Content Card**: Container for showcasing work, images, or small content snippets.
- **Interactive Link Button**: Actionable text links in notifications or informational areas.
- **Image Player Controls**: Controls for navigating through image galleries or project details.

## Agent notes
- Do not apply this wholesale to `templates/report_newsstream.html.j2` unless the user explicitly asks for an HTML report migration.
- Use this as a direction brief for demo variants, admin webapp screens, or a planned report redesign.
- This document links back to the Refero source page instead of mirroring media assets.
