import { act, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { GlobalRunIndicator } from "@/components/GlobalRunIndicator";
import { DEFAULT_RUN_OPTIONS, useAppStore, type ActiveRun } from "@/lib/store";
import { AllProviders } from "./test-utils";

type Listener = (event: MessageEvent | Event) => void;

class MockEventSource {
  url: string;
  readyState = 1;
  onmessage: Listener | null = null;
  closed = false;
  private listeners: Record<string, Listener[]> = {};

  constructor(url: string) {
    this.url = url;
    MockEventSource.instances.push(this);
  }

  addEventListener(type: string, fn: Listener): void {
    (this.listeners[type] ??= []).push(fn);
  }

  removeEventListener(type: string, fn: Listener): void {
    const arr = this.listeners[type];
    if (!arr) return;
    this.listeners[type] = arr.filter((x) => x !== fn);
  }

  close(): void {
    this.closed = true;
  }

  emit(type: string, data: unknown): void {
    const event = new MessageEvent(type, {
      data: typeof data === "string" ? data : JSON.stringify(data),
    });
    for (const listener of this.listeners[type] ?? []) listener(event);
    if (type === "message" && this.onmessage) this.onmessage(event);
  }

  static instances: MockEventSource[] = [];
}

const originalFetch = globalThis.fetch;
const originalEventSource = globalThis.EventSource;

function makeActiveRun(run_id = "run-1"): ActiveRun {
  return {
    run_id,
    started_at: "2026-05-01T00:00:00.000Z",
    options: { ...DEFAULT_RUN_OPTIONS, date: "2026-05-01" },
  };
}

beforeEach(() => {
  window.localStorage.clear();
  MockEventSource.instances = [];
  useAppStore.setState({
    runOptions: { ...DEFAULT_RUN_OPTIONS },
    activeRun: null,
  });
  (globalThis as unknown as { EventSource: typeof EventSource }).EventSource =
    MockEventSource as unknown as typeof EventSource;
});

afterEach(() => {
  globalThis.fetch = originalFetch;
  (globalThis as unknown as { EventSource: typeof EventSource }).EventSource =
    originalEventSource;
  vi.restoreAllMocks();
});

describe("GlobalRunIndicator", () => {
  it("preflights activeRun, subscribes once, and clears activeRun on done", async () => {
    const activeRun = makeActiveRun("run-live");
    useAppStore.getState().setActiveRun(activeRun);
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          run: {
            run_id: activeRun.run_id,
            status: "running",
            started_at: activeRun.started_at,
          },
        }),
        {
          status: 200,
          headers: { "content-type": "application/json" },
        },
      ),
    ) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/"]}>
        <GlobalRunIndicator />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(globalThis.fetch).toHaveBeenCalledWith(
        "/api/runs/run-live",
        expect.any(Object),
      );
    });
    await waitFor(() => {
      expect(MockEventSource.instances).toHaveLength(1);
    });
    expect(MockEventSource.instances[0].url).toBe("/api/runs/run-live/stream");

    act(() => {
      MockEventSource.instances[0].emit("progress", {
        step: "render",
        progress: 0.9,
        message: "rendering",
      });
    });

    await waitFor(() => {
      expect(screen.getByTestId("run-progress-toast")).toBeInTheDocument();
    });
    expect(screen.getByText("render")).toBeInTheDocument();
    expect(screen.getByText(/rendering/)).toBeInTheDocument();
    expect(
      screen.queryByRole("button", { name: /결과 리포트 보기/ }),
    ).not.toBeInTheDocument();

    act(() => {
      MockEventSource.instances[0].emit("done", {
        status: "completed",
        return_code: 0,
      });
    });

    await waitFor(() => {
      expect(useAppStore.getState().activeRun).toBeNull();
    });
    expect(screen.getByText(/리포트 생성 완료/)).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /결과 리포트 보기/ }),
    ).toBeInTheDocument();
  });

  it("silently clears stale activeRun when backend no longer knows the run_id", async () => {
    useAppStore.getState().setActiveRun(makeActiveRun("missing-run"));
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ detail: "unknown run_id" }), {
        status: 404,
        statusText: "Not Found",
        headers: { "content-type": "application/json" },
      }),
    ) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/sources"]}>
        <GlobalRunIndicator />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(useAppStore.getState().activeRun).toBeNull();
    });
    expect(MockEventSource.instances).toHaveLength(0);
    expect(
      screen.queryByTestId("run-progress-toast"),
    ).not.toBeInTheDocument();
  });

  it("silently clears DB-only running runs that are not stream-trackable", async () => {
    const activeRun = makeActiveRun("db-only-run");
    useAppStore.getState().setActiveRun(activeRun);
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          run: {
            run_id: activeRun.run_id,
            status: "running",
            started_at: activeRun.started_at,
            trackable: false,
            source: "db",
            error: "server_restart_or_memory_state_lost",
          },
        }),
        {
          status: 200,
          headers: { "content-type": "application/json" },
        },
      ),
    ) as unknown as typeof fetch;

    render(
      <AllProviders initialEntries={["/reports/new"]}>
        <GlobalRunIndicator />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(useAppStore.getState().activeRun).toBeNull();
    });
    expect(MockEventSource.instances).toHaveLength(0);
    expect(
      screen.queryByTestId("run-progress-toast"),
    ).not.toBeInTheDocument();
  });
});
