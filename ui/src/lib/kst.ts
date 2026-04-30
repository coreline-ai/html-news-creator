/**
 * KST (Asia/Seoul) date helpers — single source of truth.
 *
 * The Studio UI consistently treats "today" as the operator's KST calendar
 * day, regardless of the browser's local time zone. Multiple call sites
 * previously open-coded their own helpers with subtly different behavior
 * (notably `Date#getFullYear()` used the local tz, not Asia/Seoul). This
 * module centralizes that logic so the dashboard, store defaults, and the
 * Reports table all agree on the same string.
 *
 * - `todayKstISO()` — `YYYY-MM-DD` for **today in Asia/Seoul**.
 * - `formatKstDateTime(iso, opts?)` — `ko-KR` formatter pinned to
 *   Asia/Seoul. Pass `opts` to override fields; the time zone is always
 *   forced to Asia/Seoul.
 */

const ISO_FMT = new Intl.DateTimeFormat("en-CA", {
  timeZone: "Asia/Seoul",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
});

const DEFAULT_DATETIME_OPTS: Intl.DateTimeFormatOptions = {
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
};

/**
 * Returns today's calendar date **in Asia/Seoul** as `YYYY-MM-DD`.
 *
 * `en-CA` locale formats dates as ISO-style `YYYY-MM-DD`, which matches
 * what the backend expects on `/api/reports/{date}` paths.
 */
export function todayKstISO(): string {
  return ISO_FMT.format(new Date());
}

/**
 * Formats an ISO timestamp in `ko-KR` locale, time zone forced to
 * Asia/Seoul.
 *
 * Returns "—" for null/undefined/invalid inputs so call sites can drop
 * defensive ternaries.
 */
export function formatKstDateTime(
  iso: string | null | undefined,
  opts?: Intl.DateTimeFormatOptions,
): string {
  if (!iso) return "—";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return "—";
  const fmt = new Intl.DateTimeFormat("ko-KR", {
    ...DEFAULT_DATETIME_OPTS,
    ...opts,
    // Always pin to Asia/Seoul — opts cannot override.
    timeZone: "Asia/Seoul",
  });
  return fmt.format(d);
}
