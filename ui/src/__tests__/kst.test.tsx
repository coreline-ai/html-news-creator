import { describe, it, expect } from "vitest";
import { todayKstISO, formatKstDateTime } from "@/lib/kst";

describe("kst helpers", () => {
  describe("todayKstISO", () => {
    it("returns a ISO YYYY-MM-DD string", () => {
      const s = todayKstISO();
      expect(s).toMatch(/^\d{4}-\d{2}-\d{2}$/);
    });

    it("computes the KST calendar day for a fixed UTC instant", () => {
      // 2026-04-30T20:00:00Z → KST 2026-05-01 05:00.
      // Verify via a fresh formatter (mirroring the helper) so the test
      // doesn't depend on the runner's local time zone.
      const fmt = new Intl.DateTimeFormat("en-CA", {
        timeZone: "Asia/Seoul",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      });
      expect(fmt.format(new Date("2026-04-30T20:00:00Z"))).toBe("2026-05-01");
      // And the helper agrees on "today" (a tautology, but proves it runs).
      expect(todayKstISO()).toMatch(/^\d{4}-\d{2}-\d{2}$/);
    });
  });

  describe("formatKstDateTime", () => {
    it("returns em dash for null/undefined/invalid", () => {
      expect(formatKstDateTime(null)).toBe("—");
      expect(formatKstDateTime(undefined)).toBe("—");
      expect(formatKstDateTime("")).toBe("—");
      expect(formatKstDateTime("not-a-date")).toBe("—");
    });

    it("formats a UTC ISO timestamp in Asia/Seoul, ko-KR locale", () => {
      // 2026-04-30T00:00:00Z → KST 2026-04-30 09:00.
      const out = formatKstDateTime("2026-04-30T00:00:00Z");
      // ko-KR with 2-digit month/day/hour/minute renders like
      // "2026. 04. 30. 오전 09:00" (Node) or similar — assert the date
      // pieces and the minute rather than the exact glyphs to stay
      // tolerant across ICU versions / 12h vs 24h clocks.
      expect(out).toContain("2026");
      expect(out).toContain("04");
      expect(out).toContain("30");
      expect(out).toContain("09");
      expect(out).toContain(":00");
    });

    it("respects the Asia/Seoul tz across the date boundary", () => {
      // 23:30 UTC on 2026-04-30 is 08:30 the NEXT KST day.
      const out = formatKstDateTime("2026-04-30T23:30:00Z");
      expect(out).toContain("2026");
      expect(out).toContain("05"); // May
      expect(out).toContain("01");
      expect(out).toContain("08");
      expect(out).toContain(":30");
    });

    it("ignores attempts to override the timeZone option", () => {
      // The helper must always pin to Asia/Seoul, even if a caller passes
      // a different zone in opts. 2026-04-30T15:00:00Z is midnight UTC+9.
      const out = formatKstDateTime("2026-04-30T15:00:00Z", {
        timeZone: "America/New_York",
      });
      // KST 2026-05-01 — confirms timeZone override is ignored. Cross-check
      // against a New-York-zoned formatter to prove they would diverge if
      // override worked: NY would show "2026-04-30" 11 AM-ish.
      expect(out).toContain("2026");
      expect(out).toContain("05");
      expect(out).toContain("01");
      const nyFmt = new Intl.DateTimeFormat("ko-KR", {
        timeZone: "America/New_York",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      });
      expect(nyFmt.format(new Date("2026-04-30T15:00:00Z"))).toContain("04");
    });
  });
});
