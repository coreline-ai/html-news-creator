import { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import { Calendar } from "@/components/ui/calendar";
import type { CalendarStatus } from "./ReportCalendar";

export interface ReportCalendarMonthViewProps {
  statusByDate: Map<string, CalendarStatus>;
  todayIso: string;
}

/**
 * Convert a `Date` produced by react-day-picker into a KST `YYYY-MM-DD` string.
 *
 * react-day-picker hands us local-time `Date` objects (year/month/day fields
 * the user clicked on). Since the operator UI treats KST as the canonical
 * calendar, and the input is already a calendar-day intent (no time-of-day
 * component), we format the *date fields* directly rather than running them
 * through `Intl` (which would re-interpret the day in the host timezone and
 * possibly slip back/forward across midnight).
 */
function isoFromDate(d: Date): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}

const DOT_BASE =
  "after:absolute after:bottom-1 after:left-1/2 after:-translate-x-1/2 after:size-1.5 after:rounded-full after:content-['']";

export function ReportCalendarMonthView({
  statusByDate,
  todayIso,
}: ReportCalendarMonthViewProps) {
  const navigate = useNavigate();

  const modifiers = useMemo(
    () => ({
      published: (d: Date) => statusByDate.get(isoFromDate(d)) === "published",
      draft: (d: Date) => statusByDate.get(isoFromDate(d)) === "draft",
      failed: (d: Date) => statusByDate.get(isoFromDate(d)) === "failed",
    }),
    [statusByDate],
  );

  // Counts for the small footer "1 / 31 발행" line.
  const { publishedCount, monthDayCount } = useMemo(() => {
    const today = new Date(todayIso + "T00:00:00");
    const year = today.getFullYear();
    const month = today.getMonth();
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    let count = 0;
    for (let d = 1; d <= daysInMonth; d += 1) {
      const iso = `${year}-${String(month + 1).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
      if (statusByDate.get(iso) === "published") count += 1;
    }
    return { publishedCount: count, monthDayCount: daysInMonth };
  }, [statusByDate, todayIso]);

  return (
    <div
      className="flex flex-col gap-3"
      data-testid="report-calendar-month-view"
    >
      <Calendar
        mode="single"
        defaultMonth={new Date(todayIso + "T00:00:00")}
        modifiers={modifiers}
        modifiersClassNames={{
          published: `${DOT_BASE} after:bg-[var(--status-success)]`,
          draft: `${DOT_BASE} after:bg-[var(--status-warning)]`,
          failed: `${DOT_BASE} after:bg-[var(--status-error)]`,
        }}
        onDayClick={(d) => {
          navigate(`/reports/${isoFromDate(d)}`);
        }}
      />

      {/* Legend + footer count */}
      <div className="text-muted-foreground flex flex-col gap-2 px-3 pb-3 text-[11px]">
        <div className="flex flex-wrap items-center gap-x-3 gap-y-1">
          <LegendDot dotClass="bg-[var(--status-success)]" label="발행" />
          <LegendDot dotClass="bg-[var(--status-warning)]" label="부분" />
          <LegendDot dotClass="bg-[var(--status-error)]" label="실패" />
          <LegendDot dotClass="bg-muted" label="없음" />
        </div>
        <div data-testid="report-calendar-month-count">
          {publishedCount} / {monthDayCount} 발행
        </div>
      </div>
    </div>
  );
}

function LegendDot({ dotClass, label }: { dotClass: string; label: string }) {
  return (
    <span className="flex items-center gap-1">
      <span
        className={`size-1.5 rounded-full ${dotClass}`}
        aria-hidden="true"
      />
      <span>{label}</span>
    </span>
  );
}

export default ReportCalendarMonthView;
