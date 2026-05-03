import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { NewReport } from "@/pages/NewReport";
import { DEFAULT_RUN_OPTIONS, useAppStore } from "@/lib/store";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

function jsonResponse(body: unknown, init: ResponseInit = {}) {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { "content-type": "application/json" },
    ...init,
  });
}

function unavailableStatus() {
  return {
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
      recovery_supported: true,
      recovery_endpoint: "/api/system/proxy/recover",
      last_error: "connect failed",
      health_payload: null,
    },
  };
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
      recovery_supported: true,
      recovery_endpoint: "/api/system/proxy/recover",
    },
  };
}

beforeEach(() => {
  document.documentElement.classList.add("dark");
  useAppStore.setState({
    runOptions: { ...DEFAULT_RUN_OPTIONS },
    activeRun: null,
  });
});

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

describe("NewReport — runtime status guard", () => {
  it("shows proxy outage and disables Run before starting a pipeline", async () => {
    const calls: string[] = [];
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      calls.push(path);
      if (path === "/api/system/status") return jsonResponse(unavailableStatus());
      if (path === "/api/preview") return jsonResponse({ html: "" });
      return new Response("unexpected", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders>
        <NewReport />
      </AllProviders>,
    );

    await waitFor(() => {
      const banner = screen.getByTestId("system-status-banner");
      expect(banner).toHaveTextContent("생성 불가");
      expect(banner).toHaveTextContent("make proxy");
    });

    const runButton = screen.getByTestId("run-button");
    await waitFor(() => expect(runButton).toBeDisabled());
    expect(runButton).toHaveTextContent(/proxy required/i);
    expect(calls).toContain("/api/system/status");
  });

  it("manual refresh re-checks proxy status and updates the banner", async () => {
    const calls: string[] = [];
    let statusCalls = 0;
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL) => {
      const path = typeof url === "string" ? url : url.toString();
      calls.push(path);
      if (path === "/api/system/status") {
        statusCalls += 1;
        return jsonResponse(statusCalls === 1 ? unavailableStatus() : readyStatus());
      }
      if (path === "/api/preview") return jsonResponse({ html: "" });
      return new Response("unexpected", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders>
        <NewReport />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("system-status-banner")).toHaveTextContent(
        "생성 불가",
      );
    });

    fireEvent.click(screen.getByTestId("system-status-refresh-button"));

    await waitFor(() => {
      expect(screen.getByTestId("system-status-banner")).toHaveTextContent(
        "생성 가능",
      );
    });
    expect(calls.filter((path) => path === "/api/system/status").length).toBeGreaterThanOrEqual(2);
  });

  it("proxy recovery button calls the recovery endpoint then refreshes status", async () => {
    const calls: string[] = [];
    let statusCalls = 0;
    globalThis.fetch = vi.fn(
      async (url: RequestInfo | URL, init?: RequestInit) => {
        const path = typeof url === "string" ? url : url.toString();
        calls.push(`${init?.method ?? "GET"} ${path}`);
        if (path === "/api/system/status") {
          statusCalls += 1;
          return jsonResponse(
            statusCalls === 1 ? unavailableStatus() : readyStatus(),
          );
        }
        if (path === "/api/system/proxy/recover") {
          return jsonResponse({
            status: "ready",
            action: "started",
            started: true,
            pid: 12345,
            message: "LLM 프록시 복구가 완료되었습니다.",
            system_status: readyStatus(),
          });
        }
        if (path === "/api/preview") return jsonResponse({ html: "" });
        return new Response("unexpected", { status: 404 });
      },
    ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <NewReport />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("system-status-recover-button")).toBeEnabled();
    });

    fireEvent.click(screen.getByTestId("system-status-recover-button"));

    await waitFor(() => {
      expect(calls).toContain("POST /api/system/proxy/recover");
      expect(screen.getByTestId("system-status-banner")).toHaveTextContent(
        "생성 가능",
      );
    });
  });
});
