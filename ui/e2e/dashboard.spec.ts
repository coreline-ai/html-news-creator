import { expect, test } from "@playwright/test";
import { mockApi, resetClientState } from "./fixtures";

/**
 * Scenario D — dark/light theme toggle is consistent across every route.
 * Plus a small dashboard sanity check (h1, sidebar nav, recent runs table).
 *
 * Theme is stored under localStorage["theme"] = "dark" | "light" and applied
 * to <html class="dark"> by `applyTheme()` in `ui/src/lib/store.ts`. We
 * verify the class survives reloads + navigation between routes.
 */

test.describe("Dashboard + theme toggle (Scenario D)", () => {
  test.beforeEach(async ({ page }) => {
    await mockApi(page, {
      reports: [
        {
          id: "r-1",
          report_date: "2026-04-29",
          title: "Yesterday's report",
          status: "ready",
          created_at: "2026-04-29T00:00:00Z",
        },
      ],
    });
    await page.goto("/");
    await resetClientState(page);
  });

  test("renders the dashboard with header and recent runs", async ({ page }) => {
    await page.goto("/");
    await expect(
      page.getByRole("heading", { name: "Dashboard", level: 1 }),
    ).toBeVisible();
    // Sidebar shows Home aria-current.
    const homeLink = page.getByRole("link", { name: "Home" });
    await expect(homeLink).toHaveAttribute("aria-current", "page");
    // Recent runs table renders the mocked report row.
    await expect(page.getByTestId("recent-runs-table")).toBeVisible();
    await expect(page.getByText("Yesterday's report")).toBeVisible();
  });

  test("theme toggle persists across reload + every route (Scenario D)", async ({
    page,
  }) => {
    await page.goto("/");
    // Default is dark — verify <html class="dark"> is applied.
    await expect(page.locator("html")).toHaveClass(/dark/);

    // Toggle to light via the header button.
    const themeBtn = page.getByRole("button", {
      name: /switch to (light|dark) theme/i,
    });
    await themeBtn.click();
    await expect(page.locator("html")).not.toHaveClass(/dark/);

    // Reload — light persists.
    await page.reload();
    await expect(page.locator("html")).not.toHaveClass(/dark/);

    // Navigate through every route. Light class must remain stable.
    for (const path of ["/reports/new", "/sources", "/settings", "/"]) {
      await page.goto(path);
      await expect(page.locator("html")).not.toHaveClass(/dark/);
    }

    // Toggle back to dark and verify it sticks across one navigation.
    await page.goto("/");
    await page
      .getByRole("button", { name: /switch to (light|dark) theme/i })
      .click();
    await expect(page.locator("html")).toHaveClass(/dark/);
    await page.goto("/sources");
    await expect(page.locator("html")).toHaveClass(/dark/);
  });

  test("forcing light via localStorage applies on first paint", async ({
    page,
  }) => {
    // The inline boot script in index.html honours localStorage["theme"].
    await page.goto("/");
    await page.evaluate(() => {
      window.localStorage.setItem("theme", "light");
    });
    await page.reload();
    await expect(page.locator("html")).not.toHaveClass(/dark/);
  });
});
