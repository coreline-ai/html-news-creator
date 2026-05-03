import { describe, it, expect, afterEach, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { Reports } from "@/pages/Reports";
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

describe("Reports downloads", () => {
  it("renders a published HTML download action beside report actions", async () => {
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      if (path.startsWith("/api/reports")) {
        return jsonResponse({
          reports: [
            {
              id: "r1",
              report_date: "2026-05-03",
              title: "AI Trend",
              status: "published",
              created_at: "2026-05-03T00:00:00Z",
            },
          ],
        });
      }
      return new Response("unexpected", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/reports"]}>
        <Reports />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("reports-table")).toBeInTheDocument();
    });

    const htmlDownload = screen.getByLabelText("발행된 HTML 다운로드");
    expect(htmlDownload).toHaveAttribute(
      "href",
      "/api/reports/2026-05-03/html/download",
    );
    expect(htmlDownload).toHaveAttribute("download", "2026-05-03-trend.html");
  });
});
