import { describe, it, expect, afterEach, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { Route, Routes } from "react-router-dom";
import { ReviewReport } from "@/pages/ReviewReport";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

function jsonResponse(body: unknown, init: ResponseInit = {}) {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { "content-type": "application/json" },
    ...init,
  });
}

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

describe("ReviewReport downloads", () => {
  it("renders HTML download next to PDF download", async () => {
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      if (path === "/api/reports/2026-05-03") {
        return jsonResponse({
          id: "r1",
          report_date: "2026-05-03",
          title: "AI Trend",
          status: "published",
          sections: [
            {
              id: "s1",
              section_order: 0,
              title: "Section",
              fact_summary: "Summary",
              importance_score: 0.9,
            },
          ],
        });
      }
      return new Response("unexpected", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/reports/2026-05-03"]}>
        <Routes>
          <Route path="/reports/:date" element={<ReviewReport />} />
        </Routes>
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("html-download-button")).toBeInTheDocument();
    });

    expect(screen.getByTestId("html-download-button")).toHaveAttribute(
      "href",
      "/api/reports/2026-05-03/html/download",
    );
    expect(screen.getByTestId("html-download-button")).toHaveAttribute(
      "download",
      "2026-05-03-trend.html",
    );
    expect(screen.getByTestId("pdf-download-button")).toHaveAttribute(
      "href",
      "/api/reports/2026-05-03/pdf",
    );
  });

  it("turns a missing report 404 into a create-for-date state", async () => {
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      if (path === "/api/reports/2026-05-10") {
        return jsonResponse({ detail: "report not found" }, { status: 404 });
      }
      return new Response("unexpected", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/reports/2026-05-10"]}>
        <Routes>
          <Route path="/reports/:date" element={<ReviewReport />} />
        </Routes>
      </AllProviders>,
    );

    expect(
      await screen.findByText("아직 생성되지 않은 리포트입니다"),
    ).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "이 날짜로 뉴스 생성하기" }))
      .toHaveAttribute("href", "/reports/new?date=2026-05-10");
  });

  it("surfaces static-only empty reports as recreate candidates", async () => {
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      if (path === "/api/reports/2026-04-27") {
        return jsonResponse({
          id: "static-only-2026-04-27",
          report_date: "2026-04-27",
          title: "Static report",
          status: "static_only",
          stats_json: {
            static_only: true,
            content_quality: "empty_placeholder",
          },
          sections: [],
        });
      }
      return new Response("unexpected", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/reports/2026-04-27"]}>
        <Routes>
          <Route path="/reports/:date" element={<ReviewReport />} />
        </Routes>
      </AllProviders>,
    );

    expect(
      await screen.findByText("구조화된 리포트 데이터가 없습니다"),
    ).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "기존 HTML 보기" }))
      .toHaveAttribute("href", "/api/reports/2026-04-27/html");
    expect(screen.getByRole("link", { name: "이 날짜로 다시 생성하기" }))
      .toHaveAttribute("href", "/reports/new?date=2026-04-27");
  });
});
