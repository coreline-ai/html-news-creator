import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import { useRunStream } from "@/hooks/useRunStream";

/**
 * Phase A — when the SSE `done` event arrives with `{status: "failed"}` the
 * hook must surface `status: "error"` (and pull the runner's `error` string
 * into `state.error`) so the page can suppress its post-run navigation.
 *
 * We stub `EventSource` because jsdom doesn't implement it.
 */

type Listener = (e: MessageEvent | Event) => void;

class MockEventSource {
  url: string;
  readyState = 1;
  onmessage: Listener | null = null;
  onerror: Listener | null = null;
  onopen: Listener | null = null;
  closed = false;
  private listeners: Record<string, Listener[]> = {};

  constructor(url: string) {
    this.url = url;
    MockEventSource.lastInstance = this;
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

  /** Test helper — fire a named SSE event with stringified data. */
  emit(type: string, data: unknown): void {
    const event = new MessageEvent(type, {
      data: typeof data === "string" ? data : JSON.stringify(data),
    });
    for (const fn of this.listeners[type] ?? []) fn(event);
    if (type === "message" && this.onmessage) this.onmessage(event);
  }

  static lastInstance: MockEventSource | null = null;
}

const originalEventSource = globalThis.EventSource;

beforeEach(() => {
  MockEventSource.lastInstance = null;
  (globalThis as unknown as { EventSource: typeof EventSource }).EventSource =
    MockEventSource as unknown as typeof EventSource;
});

afterEach(() => {
  (globalThis as unknown as { EventSource: typeof EventSource }).EventSource =
    originalEventSource;
  vi.restoreAllMocks();
});

describe("useRunStream — failed run handling (Phase A)", () => {
  it("flips status to 'error' when done payload has status='failed'", async () => {
    const { result } = renderHook(() => useRunStream("run-xyz"));

    // Wait for the EventSource to be created and the hook to enter "running".
    await waitFor(() => {
      expect(MockEventSource.lastInstance).not.toBeNull();
      expect(result.current.status).toBe("running");
    });

    const es = MockEventSource.lastInstance!;
    act(() => {
      es.emit("done", {
        status: "failed",
        return_code: 2,
        error: "max_runtime_exceeded: 300s",
      });
    });

    await waitFor(() => {
      expect(result.current.status).toBe("error");
    });
    expect(result.current.error).toBe("max_runtime_exceeded: 300s");
    expect(es.closed).toBe(true);
  });

  it("falls back to a generic message when 'failed' done event omits error", async () => {
    const { result } = renderHook(() => useRunStream("run-fallback"));
    await waitFor(() => {
      expect(MockEventSource.lastInstance).not.toBeNull();
    });
    const es = MockEventSource.lastInstance!;

    act(() => {
      es.emit("done", { status: "failed", return_code: 1 });
    });

    await waitFor(() => {
      expect(result.current.status).toBe("error");
    });
    expect(result.current.error).toMatch(/exit 1/);
  });

  it("treats status='completed' as a successful run", async () => {
    const { result } = renderHook(() => useRunStream("run-ok"));
    await waitFor(() => {
      expect(MockEventSource.lastInstance).not.toBeNull();
    });
    const es = MockEventSource.lastInstance!;

    act(() => {
      es.emit("done", { status: "completed", return_code: 0 });
    });

    await waitFor(() => {
      expect(result.current.status).toBe("done");
    });
    expect(result.current.error).toBeNull();
  });

  it("parses the new four-key progress payload (Phase A schema)", async () => {
    const { result } = renderHook(() => useRunStream("run-progress"));
    await waitFor(() => {
      expect(MockEventSource.lastInstance).not.toBeNull();
    });
    const es = MockEventSource.lastInstance!;

    act(() => {
      es.emit("progress", {
        step: "collect",
        progress: 0.11,
        message: "github_anonymous_fallback",
        raw_line: '{"step":"collect","event":"github_anonymous_fallback"}',
      });
    });

    await waitFor(() => {
      expect(result.current.lastEvent).not.toBeNull();
    });
    expect(result.current.lastEvent?.step).toBe("collect");
    expect(result.current.lastEvent?.progress).toBeCloseTo(0.11, 5);
    expect(result.current.lastEvent?.message).toBe(
      "github_anonymous_fallback",
    );
    expect(result.current.lastEvent?.raw_line).toContain("github_anonymous");
  });
});
