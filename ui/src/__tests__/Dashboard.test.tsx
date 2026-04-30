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
      expect(screen.getByText(/no reports yet/i)).toBeInTheDocument();
    });
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
    const dateLink = screen.getByRole("link", { name: "2026-04-29" });
    expect(dateLink).toHaveAttribute("href", "/reports/2026-04-29");
  });
});
