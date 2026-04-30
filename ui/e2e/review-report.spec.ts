import { expect, test } from "@playwright/test";
import { makeSections, mockApi, resetClientState } from "./fixtures";

/**
 * Scenario A back half — on the ReviewReport screen we toggle a section
 * off, then publish in dry-run mode. Verifies:
 *   1. Section disabled count updates in the header.
 *   2. Publish dialog opens, dispatches POST /api/reports/{date}/publish.
 *   3. Toast surfaces the deploy URL returned by the mock.
 */

test.describe("ReviewReport flow (Scenario A back half)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
    await resetClientState(page);
  });

  test("toggle a section off then publish (dry-run)", async ({ page }) => {
    const sections = makeSections(3);
    const state = await mockApi(page, {
      reportDetail: {
        sections,
        title: "Daily report — 2026-04-29",
        status: "ready",
      },
    });

    await page.goto("/reports/2026-04-29");
    await expect(
      page.getByRole("heading", { name: /Review/, level: 1 }),
    ).toBeVisible();

    // Header announces "3/3 sections active" before any toggle.
    await expect(
      page.getByText(/3\/3 sections active/),
    ).toBeVisible();

    // Toggle the second section off.
    const sectionToggle = page.getByTestId(`section-toggle-${sections[1].id}`);
    await expect(sectionToggle).toBeVisible();
    await sectionToggle.click();
    await expect(
      page.getByText(/2\/3 sections active/),
    ).toBeVisible();

    // Click Publish — dialog opens.
    await page.getByTestId("publish-button").click();
    await expect(page.getByTestId("publish-dialog")).toBeVisible();

    // Confirm — dispatches POST. The mock fixture returns dry-run regardless
    // of the request body, so we just assert at least one publish call landed.
    await page.getByTestId("publish-confirm").click();

    await expect.poll(() => state.publishCalls.length, { timeout: 5_000 })
      .toBeGreaterThan(0);
    const last = state.publishCalls[state.publishCalls.length - 1];
    expect(last.date).toBe("2026-04-29");

    // Toast shows the deploy URL the mock fabricated.
    const toasts = page.getByTestId("review-toasts");
    await expect(toasts).toContainText(/Published/);
    await expect(toasts).toContainText("news-studio-mock.netlify.app");
  });

  test("ReviewReport renders SectionList with all section rows", async ({
    page,
  }) => {
    const sections = makeSections(4);
    await mockApi(page, {
      reportDetail: { sections },
    });

    await page.goto("/reports/2026-04-30");
    await expect(page.getByTestId("section-list")).toBeVisible();
    for (const s of sections) {
      await expect(page.getByTestId(`section-row-${s.id}`)).toBeVisible();
    }
  });
});
