import { defineConfig, devices } from "@playwright/test";

/**
 * Playwright configuration for News Studio E2E golden-path tests.
 *
 * Strategy:
 *  - Tests run against the FastAPI server on :8000 which serves both the
 *    built SPA bundle (`ui/dist/`) and the `/api/*` routes.
 *  - All `/api/*` calls are mocked via `page.route()` inside individual
 *    specs, so the actual DB / pipeline state never matters.
 *  - The `webServer` block boots `make serve` from the repo root if a
 *    server is not already listening on :8000 (CI-safe, idempotent locally).
 */
export default defineConfig({
  testDir: "./e2e",
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: process.env.CI ? "list" : "html",
  timeout: 30_000,
  expect: {
    timeout: 10_000,
  },
  use: {
    baseURL: "http://localhost:8000",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
  webServer: {
    // `make serve` builds the SPA bundle then runs uvicorn on :8000. If a
    // server is already up (common during local dev) Playwright will reuse
    // it via `reuseExistingServer`.
    command: "cd .. && make serve",
    url: "http://localhost:8000/health",
    timeout: 60_000,
    reuseExistingServer: true,
    stdout: "pipe",
    stderr: "pipe",
  },
});
