import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import { usePreview } from "@/hooks/usePreview";
import { DEFAULT_RUN_OPTIONS } from "@/lib/store";

const originalFetch = globalThis.fetch;

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.useRealTimers();
  vi.restoreAllMocks();
});

describe("usePreview", () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  it("debounces a single POST /api/preview after the delay (TC-3.2)", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValue(
        new Response("<html>preview</html>", {
          status: 200,
          headers: { "content-type": "text/html" },
        }),
      );
    globalThis.fetch = fetchMock as unknown as typeof fetch;

    const opts = { ...DEFAULT_RUN_OPTIONS, target_sections: 5 };
    const { result, rerender } = renderHook(
      ({ o }) => usePreview(o, { debounceMs: 2000 }),
      { initialProps: { o: opts } },
    );

    // No call yet because the debounce timer hasn't fired.
    expect(fetchMock).not.toHaveBeenCalled();
    expect(result.current.isLoading).toBe(true);

    // Change before debounce — should *not* fire either.
    rerender({ o: { ...opts, target_sections: 8 } });
    await act(async () => {
      vi.advanceTimersByTime(1000);
    });
    expect(fetchMock).not.toHaveBeenCalled();

    // Now let the debounce window elapse.
    await act(async () => {
      vi.advanceTimersByTime(2100);
    });
    // Allow the awaited microtasks inside the effect to drain.
    await vi.waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(1));

    const [, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(typeof init.body).toBe("string");
    const sentBody = JSON.parse(init.body as string) as {
      target_sections: number;
    };
    expect(sentBody.target_sections).toBe(8);
  });

  it("aborts the in-flight request when options change again (TC-3.E2)", async () => {
    const aborts: AbortSignal[] = [];
    const fetchMock = vi.fn((_url: string, init?: RequestInit) => {
      if (init?.signal) aborts.push(init.signal);
      return new Promise<Response>((resolve, reject) => {
        if (init?.signal) {
          init.signal.addEventListener("abort", () => {
            reject(new DOMException("Aborted", "AbortError"));
          });
        }
        // Never resolve until we tell it to (we expect the abort path here).
        setTimeout(() => {
          resolve(new Response("late", { status: 200 }));
        }, 100_000);
      });
    });
    globalThis.fetch = fetchMock as unknown as typeof fetch;

    const opts = { ...DEFAULT_RUN_OPTIONS };
    const { rerender } = renderHook(
      ({ o }) => usePreview(o, { debounceMs: 1000 }),
      { initialProps: { o: opts } },
    );

    // Fire first request.
    await act(async () => {
      vi.advanceTimersByTime(1100);
    });
    await vi.waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(1));
    expect(aborts[0]?.aborted).toBe(false);

    // Change options before the first resolves.
    rerender({ o: { ...opts, target_sections: 12 } });
    // Hook's cleanup runs synchronously and aborts the previous controller.
    expect(aborts[0]?.aborted).toBe(true);

    // Second request should fire after debounce.
    await act(async () => {
      vi.advanceTimersByTime(1100);
    });
    await vi.waitFor(() => expect(fetchMock).toHaveBeenCalledTimes(2));
  });

  it("captures an error message when the API returns 500 (TC-3.E1)", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValue(
        new Response("boom", { status: 500, statusText: "Server Error" }),
      );
    globalThis.fetch = fetchMock as unknown as typeof fetch;

    const { result } = renderHook(() =>
      usePreview(DEFAULT_RUN_OPTIONS, { debounceMs: 500 }),
    );

    await act(async () => {
      vi.advanceTimersByTime(600);
    });
    // Switch to real timers so waitFor's polling can drain pending microtasks.
    vi.useRealTimers();
    await waitFor(() => {
      expect(result.current.error).toMatch(/preview request failed/i);
    });
    expect(result.current.isLoading).toBe(false);
  });
});
