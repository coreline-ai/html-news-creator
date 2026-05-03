import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { Dashboard } from "@/pages/Dashboard";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

function jsonResponse(body: unknown, init: ResponseInit = {}) {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { "content-type": "application/json" },
    ...init,
  });
}

function readyStatus() {
  return {
    can_generate: true,
    llm: {
      openai_base_url: "http://127.0.0.1:4317/openai/v1",
      openai_model: "gpt-5.5",
      proxy_required: true,
      proxy_health_url: "http://127.0.0.1:4317/api/v1/health",
      proxy_reachable: true,
      status: "ready",
      message: "LLM 프록시가 정상 응답 중입니다.",
      start_command: "make proxy",
    },
  };
}

function mockDashboardFetch(reportsBody: unknown, statusBody = readyStatus()) {
  globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
    const path = typeof url === "string" ? url : url.toString();
    if (path === "/api/system/status") return jsonResponse(statusBody);
    if (path.startsWith("/api/reports")) return jsonResponse(reportsBody);
    return new Response("unexpected", { status: 404 });
  }) as unknown as typeof fetch;
}

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

describe("Dashboard (TC-2.E1)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
  });

  it("renders an LLM proxy outage banner before quick actions", async () => {
    mockDashboardFetch(
      { reports: [] },
      {
        can_generate: false,
        llm: {
          openai_base_url: "http://127.0.0.1:4317/openai/v1",
          openai_model: "gpt-5.5",
          proxy_required: true,
          proxy_health_url: "http://127.0.0.1:4317/api/v1/health",
          proxy_reachable: false,
          status: "unavailable",
          message: "LLM 프록시가 꺼져 있어 뉴스 생성 실행을 시작할 수 없습니다.",
          start_command: "make proxy",
        },
      },
    );

    render(
      <AllProviders>
        <Dashboard />
      </AllProviders>,
    );

    await waitFor(() => {
      const banner = screen.getByTestId("system-status-banner");
      expect(banner).toHaveTextContent("생성 불가");
      expect(banner).toHaveTextContent("make proxy");
    });
  });

  it("renders an EmptyState (no white screen) when the API errors", async () => {
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      if (path === "/api/system/status") return jsonResponse(readyStatus());
      return new Response("boom", { status: 500, statusText: "Server Error" });
    }) as unknown as typeof fetch;

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
    mockDashboardFetch({ reports: [] });

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
    mockDashboardFetch({
      reports: [
        {
          id: "1",
          report_date: "2026-04-29",
          title: "AI Trend — Yesterday",
          status: "published",
          created_at: "2026-04-29T08:00:00Z",
        },
      ],
    });

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
    mockDashboardFetch({ reports: [] });

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
    mockDashboardFetch({ reports: [] });

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
