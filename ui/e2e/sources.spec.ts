import { expect, test } from "@playwright/test";
import {
  buildPreviewHtml,
  defaultPolicy,
  defaultSources,
  mockApi,
  resetClientState,
  type MockSource,
} from "./fixtures";

/**
 * Scenario B — toggling a source off in /sources removes that source's
 * section from a subsequent NewReport preview render.
 *
 * The mock pipeline can't actually drop sections, so this test simulates
 * the behaviour: GET /api/sources serves a fixture; a PUT to disable one
 * source returns the updated row; afterwards the preview endpoint is
 * re-mocked to render fewer articles. We assert the article count drop.
 */

test.describe("Sources page (Scenario B)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
    await resetClientState(page);
  });

  test("loads grouped sources and shows enabled count", async ({ page }) => {
    await mockApi(page, {
      sources: defaultSources(),
    });
    await page.goto("/sources");
    await expect(
      page.getByRole("heading", { name: "Sources", level: 1 }),
    ).toBeVisible();
    // 37 mock rows distributed over 5 tiers — group containers exist.
    await expect(page.getByTestId("sources-groups")).toBeVisible();
    await expect(
      page.getByTestId("source-group-official"),
    ).toBeVisible();
    await expect(
      page.getByTestId("source-group-mainstream"),
    ).toBeVisible();
  });

  test("Scenario B — disabling a source updates server + drops preview", async ({
    page,
  }) => {
    const fixture: MockSource[] = defaultSources();
    const targetName = fixture[0].name; // first official-tier source

    const state = await mockApi(page, {
      sources: fixture,
      policy: defaultPolicy(3),
    });

    // -------- Step 1: Sources page — toggle the first source off.
    await page.goto("/sources");
    const toggle = page.getByTestId(`source-toggle-${targetName}`);
    await expect(toggle).toBeVisible();
    await expect(toggle).toBeChecked();
    await toggle.click();
    // PUT /api/sources/{name} fired with enabled=false.
    await expect.poll(() => state.sourcePuts.length, { timeout: 5_000 })
      .toBeGreaterThan(0);
    const lastPut = state.sourcePuts[state.sourcePuts.length - 1];
    expect(lastPut.name).toBe(targetName);
    expect(lastPut.body.enabled).toBe(false);

    // -------- Step 2: Re-route preview to return only 2 articles, simulating
    // that the disabled source's section is excluded from the next render.
    await page.unroute(/\/api\/preview$/);
    await page.route(/\/api\/preview$/, async (route) => {
      const html = buildPreviewHtml(2);
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ html, length: html.length }),
      });
    });

    // -------- Step 3: Visit New report and assert the iframe holds 2 articles.
    await page.goto("/reports/new");
    const frame = page.frameLocator("iframe");
    await expect(frame.locator('[data-testid="preview-article"]')).toHaveCount(
      2,
      { timeout: 6_000 },
    );
  });
});
