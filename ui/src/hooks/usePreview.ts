import { useEffect, useRef, useState } from "react";
import type { RunOptions } from "@/lib/store";

export interface UsePreviewState {
  html: string | null;
  isLoading: boolean;
  error: string | null;
}

export interface UsePreviewOptions {
  /** Debounce window in ms. Plan §3 calls for 2000. */
  debounceMs?: number;
  /** Path to POST. Override in tests. */
  endpoint?: string;
}

/**
 * Subscribe to `runOptions` and POST `/api/preview` after a debounce window.
 * Each new options change cancels the in-flight request via AbortController
 * (TC-3.E2). The request also short-circuits if the component unmounts.
 */
export function usePreview(
  runOptions: RunOptions,
  opts: UsePreviewOptions = {},
): UsePreviewState {
  const debounceMs = opts.debounceMs ?? 2000;
  const endpoint = opts.endpoint ?? "/api/preview";

  const [state, setState] = useState<UsePreviewState>({
    html: null,
    isLoading: false,
    error: null,
  });

  const abortRef = useRef<AbortController | null>(null);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const optionsKey = JSON.stringify(runOptions);

  useEffect(() => {
    // Cancel any pending timer + in-flight request.
    if (timerRef.current) clearTimeout(timerRef.current);
    if (abortRef.current) abortRef.current.abort();

    const ctrl = new AbortController();
    abortRef.current = ctrl;

    setState((s) => ({ ...s, isLoading: true, error: null }));

    timerRef.current = setTimeout(() => {
      void (async () => {
        try {
          const res = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: optionsKey,
            signal: ctrl.signal,
          });
          if (!res.ok) {
            const text = await res.text().catch(() => "");
            throw new Error(
              `Preview request failed: ${res.status} ${res.statusText}${
                text ? ` — ${text}` : ""
              }`,
            );
          }
          const ct = res.headers.get("content-type") ?? "";
          let html: string;
          if (ct.includes("application/json")) {
            const data = (await res.json()) as { html?: string };
            html = typeof data?.html === "string" ? data.html : "";
          } else {
            html = await res.text();
          }
          if (ctrl.signal.aborted) return;
          setState({ html, isLoading: false, error: null });
        } catch (err) {
          if (ctrl.signal.aborted) return;
          const msg =
            err instanceof Error ? err.message : "Unknown preview error";
          setState((s) => ({
            html: s.html,
            isLoading: false,
            error: msg,
          }));
        }
      })();
    }, debounceMs);

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
      ctrl.abort();
    };
    // optionsKey already serialises every relevant option change.
  }, [optionsKey, debounceMs, endpoint]);

  return state;
}
