import { useEffect, useMemo, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { RunProgressToast } from "@/components/RunProgressToast";
import { useRunStream, type RunProgressEvent } from "@/hooks/useRunStream";
import { ApiError, apiFetch } from "@/lib/api";
import { useAppStore, type ActiveRun } from "@/lib/store";

interface RunSummary {
  run_id: string;
  status: "queued" | "running" | "completed" | "failed" | string;
  started_at?: string | null;
  completed_at?: string | null;
  return_code?: number | null;
  error?: string | null;
  trackable?: boolean;
}

interface RunStatusResponse {
  run: RunSummary;
}

type TerminalNotice = {
  status: "done" | "error";
  title?: string;
  error: string | null;
  run: ActiveRun;
};

const WAITING_EVENT: RunProgressEvent = {
  step: "preflight",
  progress: 0,
  message: "Resuming run stream",
};

function reportPathFor(run: ActiveRun | null): string | null {
  return run?.options?.date ? `/reports/${run.options.date}` : null;
}

function failedRunMessage(run: RunSummary): string {
  if (run.error) return run.error;
  if (typeof run.return_code === "number") {
    return `실행 실패 (exit ${run.return_code}).`;
  }
  return "실행에 실패했습니다.";
}

export function GlobalRunIndicator() {
  const activeRun = useAppStore((s) => s.activeRun);
  const setActiveRun = useAppStore((s) => s.setActiveRun);
  const navigate = useNavigate();
  const location = useLocation();

  const [streamRunId, setStreamRunId] = useState<string | null>(null);
  const [checkingRunId, setCheckingRunId] = useState<string | null>(null);
  const [terminalNotice, setTerminalNotice] = useState<TerminalNotice | null>(
    null,
  );

  const stream = useRunStream(streamRunId);

  useEffect(() => {
    let cancelled = false;

    setStreamRunId(null);
    setCheckingRunId(activeRun?.run_id ?? null);
    if (!activeRun) {
      return () => {
        cancelled = true;
      };
    }

    setTerminalNotice(null);

    const checkRun = async () => {
      try {
        const response = await apiFetch<RunStatusResponse>(
          `/api/runs/${encodeURIComponent(activeRun.run_id)}`,
        );
        if (cancelled) return;

        const status = response.run.status;
        if (status === "completed") {
          setTerminalNotice({ status: "done", error: null, run: activeRun });
          setActiveRun(null);
          setCheckingRunId(null);
          return;
        }
        if (status === "failed") {
          setTerminalNotice({
            status: "error",
            title: "실행 실패",
            error: failedRunMessage(response.run),
            run: activeRun,
          });
          setActiveRun(null);
          setCheckingRunId(null);
          return;
        }
        if (response.run.trackable === false) {
          // DB에는 남아 있지만 현재 서버 프로세스가 SSE stream을 이어갈 수
          // 없는 과거 run이다. 사용자에게 실패처럼 띄우지 말고 조용히 정리한다.
          setActiveRun(null);
          setCheckingRunId(null);
          return;
        }

        setCheckingRunId(null);
        setStreamRunId(activeRun.run_id);
    } catch (err) {
        if (cancelled) return;
        if (err instanceof ApiError && err.status === 404) {
          // localStorage에 남은 과거 activeRun 찌꺼기다. 새 실행 실패가
          // 아니므로 토스트를 띄우지 않고 조용히 제거한다.
          setTerminalNotice(null);
          setActiveRun(null);
          setCheckingRunId(null);
          return;
        }
        const msg =
          err instanceof Error
              ? `Run 상태 확인 실패: ${err.message}`
              : "Run 상태 확인 실패.";
        setTerminalNotice({
          status: "error",
        title: "상태 확인 실패",
          error: msg,
          run: activeRun,
        });
        setActiveRun(null);
        setCheckingRunId(null);
      }
    };

    void checkRun();

    return () => {
      cancelled = true;
    };
  }, [activeRun, setActiveRun]);

  useEffect(() => {
    if (!activeRun || streamRunId !== activeRun.run_id) return;

    if (stream.status === "done") {
      const finishedRun = activeRun;
      setTerminalNotice({ status: "done", error: null, run: finishedRun });
      setActiveRun(null);
      setStreamRunId(null);

      if (location.pathname === "/reports/new") {
        const path = reportPathFor(finishedRun);
        if (path) {
          queueMicrotask(() => navigate(path));
        }
      }
      return;
    }

    if (stream.status === "error") {
      setTerminalNotice({
        status: "error",
        title: "실행 실패",
        error: stream.error ?? "Run stream failed.",
        run: activeRun,
      });
      setActiveRun(null);
      setStreamRunId(null);
    }
  }, [activeRun, location.pathname, navigate, setActiveRun, stream, streamRunId]);

  const waitingForRun = Boolean(activeRun && checkingRunId === activeRun.run_id);
  const terminalReportPath = useMemo(
    () =>
      terminalNotice?.status === "done"
        ? reportPathFor(terminalNotice.run)
        : null,
    [terminalNotice],
  );

  if (activeRun && (stream.status !== "idle" || waitingForRun)) {
    const lastEvent = stream.lastEvent ?? (waitingForRun ? WAITING_EVENT : null);
    const events =
      stream.events.length > 0
        ? stream.events
        : waitingForRun
          ? [WAITING_EVENT]
          : [];
    return (
      <RunProgressToast
        status={waitingForRun ? "running" : stream.status}
        lastEvent={lastEvent}
        events={events}
        error={stream.error}
        onDismiss={() => {
          setActiveRun(null);
          setStreamRunId(null);
        }}
      />
    );
  }

  if (terminalNotice) {
    return (
      <RunProgressToast
        status={terminalNotice.status}
        title={terminalNotice.title}
        lastEvent={stream.lastEvent}
        events={stream.events}
        error={terminalNotice.error}
        onDismiss={() => setTerminalNotice(null)}
        actionLabel={terminalReportPath ? "결과 리포트 보기" : undefined}
        onAction={
          terminalReportPath
            ? () => {
                navigate(terminalReportPath);
                setTerminalNotice(null);
              }
            : undefined
        }
      />
    );
  }

  return null;
}

export default GlobalRunIndicator;
