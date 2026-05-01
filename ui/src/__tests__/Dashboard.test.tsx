import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { Dashboard } from "@/pages/Dashboard";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

describe("Dashboard (TC-2.E1)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
  });

  it("renders an EmptyState (no white screen) when the API errors", async () => {
    globalThis.fetch = vi
      .fn()
      .mockResolvedValue(
        new Response("boom", { status: 500, statusText: "Server Error" }),
      ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByText(/could not load reports/i)).toBeInTheDocument();
    });
    expect(screen.getByRole("button", { name: /retry/i })).toBeInTheDocument();
  });

  it("renders the empty list state when /api/reports returns no rows", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ reports: [] }), {
        status: 200,
        headers: { "content-type": "application/json" },
      }),
    ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByText(/아직 리포트가 없습니다/)).toBeInTheDocument();
    });
    expect(screen.getByTestId("dashboard-header-new-report")).toHaveAttribute(
      "href",
      "/reports/new",
    );
  });

  it("renders the recent runs table when /api/reports returns rows", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          reports: [
            {
              id: "1",
              report_date: "2026-04-29",
              title: "AI Trend — Yesterday",
              status: "published",
              created_at: "2026-04-29T08:00:00Z",
            },
          ],
        }),
        {
          status: 200,
          headers: { "content-type": "application/json" },
        },
      ),
    ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("recent-runs-table")).toBeInTheDocument();
    });
    expect(screen.getByText("AI Trend — Yesterday")).toBeInTheDocument();
    const viewAll = screen.getByTestId("dashboard-view-all-link");
    const table = screen.getByTestId("recent-runs-table");
    expect(viewAll).toHaveAttribute("href", "/reports");
    expect(
      Boolean(
        viewAll.compareDocumentPosition(table) &
          Node.DOCUMENT_POSITION_FOLLOWING,
      ),
    ).toBe(true);
    const dateLink = screen.getByRole("link", { name: "2026-04-29" });
    expect(dateLink).toHaveAttribute("href", "/reports/2026-04-29");
  });

  it("links Schedule run to the Policy page", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ reports: [] }), {
        status: 200,
        headers: { "content-type": "application/json" },
      }),
    ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    const scheduleRun = await screen.findByRole("link", {
      name: /schedule run/i,
    });
    expect(scheduleRun).toHaveAttribute("href", "/policy");
  });

  it("visually highlights the New report quick action", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ reports: [] }), {
        status: 200,
        headers: { "content-type": "application/json" },
      }),
    ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    const newReport = await screen.findByTestId("dashboard-new-report-card");
    expect(newReport).toHaveAttribute("href", "/reports/new");
    expect(newReport.className).toContain("bg-primary/10");
    expect(newReport.className).toContain("border-primary/40");
  });
});
