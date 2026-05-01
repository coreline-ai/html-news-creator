import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import type { CalendarStatus } from "./ReportCalendar";

export interface ReportCalendarHeatmapViewProps {
  statusByDate: Map<string, CalendarStatus>;
  todayIso: string;
}

const WEEKS = 13; // 13 weeks × 7 days = 91 days
const DAYS = 7;
const ROW_LABELS = ["월", "화", "수", "목", "금", "토", "일"];
// Map JS Date.getDay() (0=Sun..6=Sat) → row index where 0=Mon..6=Sun.
const DAY_TO_ROW = [6, 0, 1, 2, 3, 4, 5];

interface Cell {
  iso: string | null;
  status: CalendarStatus | null;
  isToday: boolean;
}

function isoFromDate(d: Date): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

function statusToClass(status: CalendarStatus | null): string {
  switch (status) {
    case "published":
      return "bg-[var(--status-success)]";
    case "draft":
      return "bg-[var(--status-warning)]";
    case "failed":
      return "bg-[var(--status-error)]";
    default:
      return "bg-muted";
  }
}

function statusToLabel(status: CalendarStatus | null): string {
  switch (status) {
    case "published":
      return "발행";
    case "draft":
      return "부분";
    case "failed":
      return "실패";
    default:
      return "없음";
  }
}

export function ReportCalendarHeatmapView({
  statusByDate,
  todayIso,
}: ReportCalendarHeatmapViewProps) {
  const navigate = useNavigate();

  /**
   * Build 7 × WEEKS grid where the *last* column ends on todayIso, and the
   * top row is Monday. Out-of-range cells (before today − 90d) get null.
   */
  const grid = useMemo<Cell[][]>(() => {
    const today = new Date(todayIso + "T00:00:00");
    const todayRow = DAY_TO_ROW[today.getDay()];
    // Anchor: the bottom-right column shows the column containing today.
    // Earliest day in the grid = today − ((WEEKS - 1) * 7 + todayRow) days.
    const start = new Date(today);
    start.setDate(start.getDate() - ((WEEKS - 1) * 7 + todayRow));

    const rows: Cell[][] = Array.from({ length: DAYS }, () => []);
    for (let col = 0; col < WEEKS; col += 1) {
      for (let row = 0; row < DAYS; row += 1) {
        const cur = new Date(start);
        cur.setDate(start.getDate() + col * DAYS + row);
        // Anything past today is shown as empty (no future placeholder).
        if (cur > today) {
          rows[row].push({ iso: null, status: null, isToday: false });
          continue;
        }
        const iso = isoFromDate(cur);
        rows[row].push({
          iso,
          status: statusByDate.get(iso) ?? null,
          isToday: iso === todayIso,
        });
      }
    }
    return rows;
  }, [statusByDate, todayIso]);

  return (
    <div
      className="flex flex-col gap-3 px-3 pb-3"
      data-testid="report-calendar-heatmap-view"
    >
      <div className="text-muted-foreground text-[11px]">90일 추세</div>

      <div className="flex gap-2">
        {/* Row labels (Mon..Sun) */}
        <div className="text-muted-foreground flex flex-col gap-0.5 pt-0.5 text-[10px] font-medium tracking-wide uppercase">
          {ROW_LABELS.map((label, idx) => (
            <span
              key={label}
              className="flex h-4 items-center"
              // Show every other label so the column doesn't crowd at 280px.
              style={{ visibility: idx % 2 === 0 ? "visible" : "hidden" }}
            >
              {label}
            </span>
          ))}
        </div>

        {/* The grid itself: 7 rows × WEEKS columns */}
        <div
          role="grid"
          aria-label="최근 90일 발행 히트맵"
          className="flex flex-col gap-0.5"
        >
          {grid.map((row, rowIdx) => (
            <div key={rowIdx} role="row" className="flex gap-0.5">
              {row.map((cell, colIdx) => {
                if (!cell.iso) {
                  return (
                    <span
                      key={`${rowIdx}-${colIdx}`}
                      role="gridcell"
                      aria-hidden="true"
                      className="size-4"
                    />
                  );
                }
                return (
                  <button
                    key={`${rowIdx}-${colIdx}`}
                    type="button"
                    role="gridcell"
                    data-date={cell.iso}
                    data-status={cell.status ?? "none"}
                    title={`${cell.iso} · ${statusToLabel(cell.status)}`}
                    aria-label={`${cell.iso} ${statusToLabel(cell.status)}`}
                    onClick={() => navigate(`/reports/${cell.iso}`)}
                    className={`size-4 cursor-pointer rounded-sm transition-colors hover:ring-1 hover:ring-ring focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring ${statusToClass(
                      cell.status,
                    )} ${cell.isToday ? "ring-1 ring-ring" : ""}`}
                  />
                );
              })}
            </div>
          ))}
        </div>
      </div>

      {/* Legend */}
      <div className="text-muted-foreground flex flex-wrap items-center gap-x-3 gap-y-1 text-[11px]">
        <LegendChip dotClass="bg-[var(--status-success)]" label="발행" />
        <LegendChip dotClass="bg-[var(--status-warning)]" label="부분" />
        <LegendChip dotClass="bg-[var(--status-error)]" label="실패" />
        <LegendChip dotClass="bg-muted" label="없음" />
      </div>
    </div>
  );
}

function LegendChip({ dotClass, label }: { dotClass: string; label: string }) {
  return (
    <span className="flex items-center gap-1">
      <span className={`size-2 rounded-sm ${dotClass}`} aria-hidden="true" />
      <span>{label}</span>
    </span>
  );
}

export default ReportCalendarHeatmapView;
