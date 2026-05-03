import { AlertTriangle, CheckCircle2, RefreshCw, ServerCrash } from "lucide-react";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { useRecoverProxy, useSystemStatus } from "@/hooks/useSystemStatus";
import { cn } from "@/lib/utils";

interface SystemStatusBannerProps {
  className?: string;
  compactReady?: boolean;
}

export function SystemStatusBanner({
  className,
  compactReady = false,
}: SystemStatusBannerProps) {
  const { data, error, isError, isFetching, isLoading, refetch } =
    useSystemStatus();
  const recoverProxy = useRecoverProxy();
  const [manualChecking, setManualChecking] = useState(false);
  const [manualError, setManualError] = useState<string | null>(null);

  if (!data?.llm && !isLoading && !isError) return null;

  const llm = data?.llm;
  const blocked = data?.can_generate === false;
  const ready = data?.can_generate === true;
  const statusText = llm?.status ?? (isLoading ? "checking" : "unknown");
  const message =
    llm?.message ??
    (isError
      ? error?.message || "시스템 상태를 확인할 수 없습니다."
      : "생성 가능 상태를 확인 중입니다.");
  const startCommand = llm?.start_command;
  const canRecover = blocked && llm?.recovery_supported === true;
  const checking = manualChecking || isLoading;
  const spinning = manualChecking || isFetching || recoverProxy.isPending;
  const recoveryMessage =
    recoverProxy.data?.message ??
    (recoverProxy.error instanceof Error ? recoverProxy.error.message : null);

  const handleRefresh = async () => {
    setManualError(null);
    setManualChecking(true);
    try {
      await refetch({ cancelRefetch: false });
    } catch (err) {
      setManualError(
        err instanceof Error ? err.message : "시스템 상태 재확인에 실패했습니다.",
      );
    } finally {
      setManualChecking(false);
    }
  };

  const handleRecover = async () => {
    setManualError(null);
    try {
      await recoverProxy.mutateAsync();
      await refetch({ cancelRefetch: false });
    } catch (err) {
      setManualError(
        err instanceof Error ? err.message : "프록시 복구 요청에 실패했습니다.",
      );
    }
  };

  const tone = blocked
    ? "border-destructive/40 bg-destructive/10 text-foreground"
    : isError
      ? "border-border bg-muted/50 text-foreground"
      : "border-border bg-card text-card-foreground";
  const icon = blocked ? (
    <ServerCrash className="text-destructive size-4" aria-hidden="true" />
  ) : ready ? (
    <CheckCircle2 className="text-primary size-4" aria-hidden="true" />
  ) : (
    <AlertTriangle className="text-muted-foreground size-4" aria-hidden="true" />
  );

  if (ready && compactReady) {
    return (
      <div
        role="status"
        data-testid="system-status-banner"
        className={cn(
          "border-border bg-card text-muted-foreground flex items-center justify-between border px-3 py-2 text-xs",
          className,
        )}
      >
        <div className="flex min-w-0 items-center gap-2">
          {icon}
          <span className="truncate">LLM 프록시 정상 · 생성 가능</span>
        </div>
        <Badge variant="outline">{statusText}</Badge>
      </div>
    );
  }

  return (
    <div
      role={blocked || isError ? "alert" : "status"}
      data-testid="system-status-banner"
      className={cn(
        "flex items-start justify-between gap-3 border px-4 py-3 text-sm",
        tone,
        className,
      )}
    >
      <div className="flex min-w-0 gap-3">
        <div className="mt-0.5 shrink-0">{icon}</div>
        <div className="min-w-0 space-y-1">
          <div className="flex flex-wrap items-center gap-2">
            <span className="font-medium">
              {blocked
                ? "생성 불가: LLM 프록시 미응답"
                : ready
                  ? "생성 가능: LLM 프록시 정상"
                  : "생성 가능 상태 확인 중"}
            </span>
            <Badge variant={blocked ? "destructive" : "outline"}>
              {statusText}
            </Badge>
          </div>
          <p className="text-muted-foreground leading-5">{message}</p>
          {blocked && startCommand ? (
            <p className="text-muted-foreground leading-5">
              터미널에서 <code className="bg-muted text-foreground rounded px-1 py-0.5 font-mono text-xs">{startCommand}</code> 실행 후 다시 확인하세요.
            </p>
          ) : null}
          {recoveryMessage || manualError ? (
            <p
              className={cn(
                "leading-5",
                manualError || recoverProxy.isError
                  ? "text-destructive"
                  : "text-muted-foreground",
              )}
              data-testid="system-status-action-message"
            >
              {manualError ?? recoveryMessage}
            </p>
          ) : null}
        </div>
      </div>
      <div className="flex shrink-0 flex-wrap justify-end gap-2">
        {canRecover ? (
          <Button
            type="button"
            size="sm"
            onClick={() => {
              void handleRecover();
            }}
            disabled={recoverProxy.isPending}
            data-testid="system-status-recover-button"
          >
            <ServerCrash className="size-3.5" aria-hidden="true" />
            {recoverProxy.isPending ? "복구 중" : "프록시 복구"}
          </Button>
        ) : null}
        <Button
          type="button"
          size="sm"
          variant="outline"
          onClick={() => {
            void handleRefresh();
          }}
          disabled={manualChecking}
          data-testid="system-status-refresh-button"
        >
          <RefreshCw className={cn("size-3.5", spinning && "animate-spin")} />
          {checking ? "확인 중" : "다시 확인"}
        </Button>
      </div>
    </div>
  );
}
