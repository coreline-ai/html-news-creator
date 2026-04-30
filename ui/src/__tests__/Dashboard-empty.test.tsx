import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { Dashboard } from "@/pages/Dashboard";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

beforeEach(() => {
  document.documentElement.classList.add("dark");
  globalThis.fetch = vi.fn().mockResolvedValue(
    new Response(JSON.stringify({ reports: [] }), {
      status: 200,
      headers: { "content-type": "application/json" },
    }),
  ) as unknown as typeof fetch;
});

describe("Dashboard — empty DB UX polish", () => {
  it("renders the localized empty title when there are zero reports", async () => {
    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByText(/아직 리포트가 없습니다/)).toBeInTheDocument();
    });
  });

  it("renders the primary CTA linking to /reports/new", async () => {
    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    const cta = await screen.findByRole("link", {
      name: /오늘자 첫 리포트 생성/,
    });
    expect(cta).toHaveAttribute("href", "/reports/new");
  });

  it("renders the help/policy link to /settings", async () => {
    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    const help = await screen.findByRole("link", {
      name: /도움말/,
    });
    expect(help).toHaveAttribute("href", "/settings");
  });

  it("groups CTA + help link under a stable testid container", async () => {
    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(
        screen.getByTestId("dashboard-empty-actions"),
      ).toBeInTheDocument();
    });
  });
});
