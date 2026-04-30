import { useEffect, useRef, useState } from "react";

export interface RunProgressEvent {
  step: string;
  progress: number; // 0..1
  message?: string;
}

export type RunStreamStatus = "idle" | "running" | "done" | "error";

export interface UseRunStreamState {
  status: RunStreamStatus;
  events: RunProgressEvent[];
  lastEvent: RunProgressEvent | null;
  error: string | null;
}

const INITIAL: UseRunStreamState = {
  status: "idle",
  events: [],
  lastEvent: null,
  error: null,
};

/**
 * Subscribe to `/api/runs/{id}/stream` via EventSource. Listens for `progress`
 * events (default), and finalises on `done` / `error`. When `runId` is null,
 * the hook is inert.
 */
export function useRunStream(
  runId: string | null,
  endpoint?: (id: string) => string,
): UseRunStreamState {
  const [state, setState] = useState<UseRunStreamState>(INITIAL);
  const sourceRef = useRef<EventSource | null>(null);

  useEffect(() => {
    if (!runId) {
      setState(INITIAL);
      return;
    }

    const url = endpoint
      ? endpoint(runId)
      : `/api/runs/${encodeURIComponent(runId)}/stream`;

    if (typeof EventSource === "undefined") {
      setState({
        status: "error",
        events: [],
        lastEvent: null,
        error: "EventSource is not available in this environment.",
      });
      return;
    }

    const es = new EventSource(url);
    sourceRef.current = es;
    setState({ status: "running", events: [], lastEvent: null, error: null });

    const handleProgress = (e: MessageEvent) => {
      let parsed: RunProgressEvent | null = null;
      try {
        const data = JSON.parse(e.data) as Partial<RunProgressEvent>;
        if (typeof data.step === "string") {
          parsed = {
            step: data.step,
            progress:
              typeof data.progress === "number" ? data.progress : 0,
            message:
              typeof data.message === "string" ? data.message : undefined,
          };
        }
      } catch {
        parsed = null;
      }
      if (!parsed) return;
      setState((s) => ({
        status: s.status === "running" ? "running" : s.status,
        events: [...s.events, parsed!],
        lastEvent: parsed,
        error: s.error,
      }));
    };

    const handleDone = () => {
      setState((s) => ({ ...s, status: "done" }));
      es.close();
    };

    const handleError = (e: MessageEvent | Event) => {
      const msg =
        "data" in e && typeof (e as MessageEvent).data === "string"
          ? (e as MessageEvent).data
          : "Stream error";
      setState((s) => ({ ...s, status: "error", error: msg }));
      es.close();
    };

    es.addEventListener("progress", handleProgress as EventListener);
    es.addEventListener("done", handleDone as EventListener);
    es.addEventListener("error", handleError as EventListener);
    // Default unnamed message (some servers don't set event name).
    es.onmessage = handleProgress;

    return () => {
      es.removeEventListener("progress", handleProgress as EventListener);
      es.removeEventListener("done", handleDone as EventListener);
      es.removeEventListener("error", handleError as EventListener);
      es.close();
      sourceRef.current = null;
    };
  }, [runId, endpoint]);

  return state;
}
