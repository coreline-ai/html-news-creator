import { useEffect, useRef, useState } from "react";

export interface RunProgressEvent {
  step: string;
  progress: number; // 0..1
  message?: string;
  raw_line?: string;
}

/**
 * Shape of the `done` SSE event emitted by `app/admin/sse.py`. The runner puts
 * this on the queue from `_supervise` once the subprocess exits.
 */
interface RunDoneEvent {
  event?: "done";
  status?: "completed" | "failed" | string;
  return_code?: number | null;
  error?: string | null;
}

export type RunStreamStatus = "idle" | "running" | "done" | "error" | "stalled";

export interface UseRunStreamState {
  status: RunStreamStatus;
  events: RunProgressEvent[];
  lastEvent: RunProgressEvent | null;
  error: string | null;
  /** Milliseconds since the last activity (event or heartbeat). null when idle. */
  msSinceLastActivity: number | null;
}

const INITIAL: UseRunStreamState = {
  status: "idle",
  events: [],
  lastEvent: null,
  error: null,
  msSinceLastActivity: null,
};

/**
 * If the server doesn't emit any event (progress, heartbeat, or done) for
 * this long, the hook flips to status="stalled" so the UI can warn the user.
 * The backend SSE emits heartbeats at a much shorter interval, so this is
 * a generous safety net.
 */
const STALL_THRESHOLD_MS = 30_000;
const TICK_MS = 2_000;

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
        msSinceLastActivity: null,
      });
      return;
    }

    const es = new EventSource(url);
    sourceRef.current = es;
    setState({
      status: "running",
      events: [],
      lastEvent: null,
      error: null,
      msSinceLastActivity: 0,
    });

    let lastActivity = Date.now();
    const markActivity = () => {
      lastActivity = Date.now();
    };

    const handleProgress = (e: MessageEvent) => {
      markActivity();
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
            raw_line:
              typeof data.raw_line === "string" ? data.raw_line : undefined,
          };
        }
      } catch {
        parsed = null;
      }
      if (!parsed) return;
      setState((s) => ({
        status: s.status === "stalled" ? "running" : s.status,
        events: [...s.events, parsed!],
        lastEvent: parsed,
        error: s.error,
        msSinceLastActivity: 0,
      }));
    };

    const handleHeartbeat = () => {
      markActivity();
      setState((s) =>
        s.status === "stalled"
          ? { ...s, status: "running", msSinceLastActivity: 0 }
          : { ...s, msSinceLastActivity: 0 },
      );
    };

    const handleDone = (e: MessageEvent) => {
      let payload: RunDoneEvent = {};
      try {
        const obj = JSON.parse(e.data) as RunDoneEvent;
        if (obj && typeof obj === "object") {
          payload = obj;
        }
      } catch {
        // Body wasn't JSON — treat as success because the server emits done
        // only after the process exits; older deployments may have empty body.
        payload = {};
      }
      if (payload.status === "failed") {
        setState((s) => ({
          ...s,
          status: "error",
          error:
            (typeof payload.error === "string" && payload.error) ||
            (typeof payload.return_code === "number"
              ? `실행 실패 (exit ${payload.return_code})`
              : "실행에 실패했습니다."),
        }));
      } else {
        setState((s) => ({ ...s, status: "done" }));
      }
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
    es.addEventListener("heartbeat", handleHeartbeat as EventListener);
    es.addEventListener("done", handleDone as EventListener);
    es.addEventListener("error", handleError as EventListener);
    // Default unnamed message (some servers don't set event name).
    es.onmessage = handleProgress;

    // Stall watchdog: tick every TICK_MS, flip to "stalled" if no activity
    // arrived for STALL_THRESHOLD_MS. Reset back to "running" on next event.
    const tick = window.setInterval(() => {
      const elapsed = Date.now() - lastActivity;
      setState((s) => {
        if (s.status !== "running" && s.status !== "stalled") return s;
        if (elapsed >= STALL_THRESHOLD_MS && s.status !== "stalled") {
          return { ...s, status: "stalled", msSinceLastActivity: elapsed };
        }
        return { ...s, msSinceLastActivity: elapsed };
      });
    }, TICK_MS);

    return () => {
      window.clearInterval(tick);
      es.removeEventListener("progress", handleProgress as EventListener);
      es.removeEventListener("heartbeat", handleHeartbeat as EventListener);
      es.removeEventListener("done", handleDone as EventListener);
      es.removeEventListener("error", handleError as EventListener);
      es.close();
      sourceRef.current = null;
    };
  }, [runId, endpoint]);

  return state;
}
