import { Link } from "react-router-dom";
import { FileText, ExternalLink, RefreshCw, AlertCircle } from "lucide-react";
import { useReports } from "@/hooks/useReports";
import { EmptyState } from "@/components/EmptyState";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { formatKstDateTime } from "@/lib/kst";

const PAGE_LIMIT = 50;

function formatPublished(iso?: string | null): string {
  return formatKstDateTime(iso);
}

function StatusPill({ status }: { status: string | null | undefined }) {
  const tone =
    status === "published"
      ? "text-[var(--status-success)] bg-[color-mix(in_oklab,var(--status-success)_15%,transparent)]"
      : status === "failed"
        ? "text-destructive bg-[color-mix(in_oklab,var(--destructive)_15%,transparent)]"
        : "text-muted-foreground bg-muted";
  return (
    <span
      className={`inline-flex items-center rounded-md px-2 py-0.5 text-[11px] font-medium ${tone}`}
    >
      {status ?? "draft"}
    </span>
  );
}

export function Reports() {
  const { data, isLoading, isError, error, refetch } = useReports({
    limit: PAGE_LIMIT,
  });

  return (
    <div className="mx-auto max-w-[1200px] px-6 py-6">
      <header className="mb-4 flex items-end justify-between gap-3">
        <div>
          <h1 className="text-foreground text-xl font-semibold tracking-tight">
            Reports
          </h1>
          <p className="text-muted-foreground text-sm">
            발행됐거나 진행 중인 모든 일일 리포트.
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Button
            variant="outline"
            size="sm"
            onClick={() => void refetch()}
            disabled={isLoading}
          >
            <RefreshCw
              className={`size-4 ${isLoading ? "animate-spin" : ""}`}
              aria-hidden="true"
            />
            새로고침
          </Button>
          <Button asChild size="sm">
            <Link to="/reports/new">
              <FileText className="size-4" aria-hidden="true" />
              신규 생성
            </Link>
          </Button>
        </div>
      </header>

      {isLoading ? (
        <div className="flex flex-col gap-2">
          {Array.from({ length: 6 }).map((_, i) => (
            <Skeleton key={i} className="h-12 w-full" />
          ))}
        </div>
      ) : isError ? (
        <EmptyState
          icon={AlertCircle}
          title="리포트 목록을 불러오지 못했습니다"
          description={
            error instanceof Error ? error.message : "백엔드 응답 오류"
          }
          action={
            <Button size="sm" variant="outline" onClick={() => void refetch()}>
              다시 시도
            </Button>
          }
        />
      ) : !data || data.length === 0 ? (
        <EmptyState
          icon={FileText}
          title="아직 발행된 리포트가 없습니다"
          description="신규 생성에서 첫 리포트를 만들어 보세요."
          action={
            <Button asChild size="sm">
              <Link to="/reports/new">신규 생성</Link>
            </Button>
          }
        />
      ) : (
        <div
          className="border-border overflow-hidden rounded-md border"
          data-testid="reports-table"
        >
          <table className="w-full text-sm">
            <thead className="bg-muted/50 text-muted-foreground">
              <tr className="text-[11px] tracking-wide uppercase">
                <th className="px-3 py-2 text-left font-medium w-[120px]">
                  날짜
                </th>
                <th className="px-3 py-2 text-left font-medium">제목</th>
                <th className="px-3 py-2 text-left font-medium w-[100px]">
                  상태
                </th>
                <th className="px-3 py-2 text-left font-medium w-[180px] whitespace-nowrap">
                  발행 시각
                </th>
                <th className="px-3 py-2 text-right font-medium w-[80px]">
                </th>
              </tr>
            </thead>
            <tbody>
              {data.map((r) => {
                const dateStr = r.report_date;
                return (
                  <tr
                    key={r.id}
                    className="border-border hover:bg-accent/40 border-t transition-colors"
                    data-testid="reports-row"
                  >
                    <td className="px-3 py-2 font-mono">
                      {dateStr ? (
                        <Link
                          to={`/reports/${dateStr}`}
                          className="text-primary hover:underline"
                        >
                          {dateStr}
                        </Link>
                      ) : (
                        <span className="text-muted-foreground">—</span>
                      )}
                    </td>
                    <td className="px-3 py-2 text-foreground">
                      <span className="line-clamp-1">{r.title ?? "(제목 없음)"}</span>
                    </td>
                    <td className="px-3 py-2">
                      <StatusPill status={r.status} />
                    </td>
                    <td className="px-3 py-2 text-muted-foreground whitespace-nowrap">
                      {formatPublished(r.published_at ?? r.created_at)}
                    </td>
                    <td className="px-3 py-2 text-right">
                      {dateStr ? (
                        <a
                          href={`/api/reports/${dateStr}/html`}
                          target="_blank"
                          rel="noreferrer"
                          className="text-muted-foreground hover:text-foreground inline-flex items-center gap-1 text-xs"
                          aria-label="발행된 HTML 새 탭에서 열기"
                        >
                          <ExternalLink
                            className="size-3.5"
                            aria-hidden="true"
                          />
                        </a>
                      ) : null}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Reports;
