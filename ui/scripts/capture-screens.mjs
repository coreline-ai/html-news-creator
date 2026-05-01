// ui/scripts/capture-screens.mjs
// One-off helper to capture News Studio screens for README.
// Run: cd ui && node scripts/capture-screens.mjs
// Requires server on http://127.0.0.1:8000 with at least one report in DB.

import { chromium } from "playwright";
import { mkdir } from "node:fs/promises";
import { resolve } from "node:path";

const BASE = process.env.NS_BASE || "http://127.0.0.1:8000";
const OUT = resolve(import.meta.dirname, "..", "..", "docs", "screenshots");

const SCREENS = [
  { name: "01-dashboard", path: "/" },
  { name: "02-reports", path: "/reports" },
  { name: "03-review", path: "/reports/2026-05-01" },
  { name: "04-sources", path: "/sources" },
  { name: "05-policy", path: "/policy" },
];

async function main() {
  await mkdir(OUT, { recursive: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 2,
    colorScheme: "dark",
  });

  for (const { name, path } of SCREENS) {
    const page = await ctx.newPage();
    await page.goto(`${BASE}${path}`, { waitUntil: "networkidle" });
    // Brief settle so React skeleton state finishes
    await page.waitForTimeout(800);
    const out = resolve(OUT, `news-studio-${name}.png`);
    await page.screenshot({ path: out, fullPage: false });
    console.log(`✓ ${path}  →  ${out}`);
    await page.close();
  }

  await browser.close();
}

main().catch((err) => {
  console.error("capture failed:", err);
  process.exit(1);
});
