import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { ReportCalendar } from "@/components/ReportCalendar";
import type { ReportSummary } from "@/lib/api";
import { useAppStore } from "@/lib/store";
import { AllProviders } from "./test-utils";

// Capture navigate() calls without coupling to a real router transition.
const navigateMock = vi.fn();

vi.mock("react-router-dom", async () => {
  const actual =
    await vi.importActual<typeof import("react-router-dom")>(
      "react-router-dom",
    );
  return {
    ...actual,
    useNavigate: () => navigateMock,
  };
});

const PERSIST_KEY = "news-studio-options";

beforeEach(() => {
  navigateMock.mockReset();
  window.localStorage.clear();
  // Ensure a fresh tab default per test.
  useAppStore.setState({ calendarTab: "month" });
});

afterEach(() => {
  vi.restoreAllMocks();
});

const TODAY = "2026-04-30";

const reports: ReportSummary[] = [
  {
    id: "r-1",
    report_date: "2026-04-30",
    title: "Today",
    status: "published",
    created_at: "2026-04-30T00:00:00Z",
  },
  {
    id: "r-2",
    report_date: "2026-04-28",
    title: "Two days ago",
    status: "failed",
    created_at: "2026-04-28T00:00:00Z",
  },
];

describe("ReportCalendar — month view (TC-1)", () => {
  it("keeps month navigation positioned inside the calendar root", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    const calendar = screen
      .getByTestId("report-calendar-month-view")
      .querySelector(".rdp-root");
    expect(calendar?.className).toContain("relative");
  });

  it("moves to the previous month when the calendar previous button is clicked", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    const monthView = screen.getByTestId("report-calendar-month-view");
    expect(within(monthView).getByText("April 2026")).toBeInTheDocument();

    fireEvent.click(
      within(monthView).getByRole("button", {
        name: /go to the previous month/i,
      }),
    );

    expect(within(monthView).getByText("March 2026")).toBeInTheDocument();
  });

  it("renders the month view by default and tags published days with the success token", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    expect(
      screen.getByTestId("report-calendar-month-view"),
    ).toBeInTheDocument();

    // The 30th of April 2026 (todayIso) carries the `published` modifier
    // class so the after: dot pseudo-element is visible. Use the day-button
    // role (`button`) since "30" appears in multiple cells (outside days,
    // March/May spillover) and we want the in-month, current button.
    const monthView = screen.getByTestId("report-calendar-month-view");
    const dayButtons = within(monthView).getAllByRole("button", { name: /30/ });
    const inMonth = dayButtons.filter(
      (b) => !b.parentElement?.className.includes("day-outside"),
    );
    expect(inMonth.length).toBeGreaterThan(0);
    const dayCell = inMonth[0].parentElement!;
    expect(dayCell.className).toMatch(/after:bg-\[var\(--status-success\)\]/);
  });
});

describe("ReportCalendar — heatmap view (TC-2)", () => {
  beforeEach(() => {
    useAppStore.setState({ calendarTab: "heatmap" });
  });

  it("colors today's cell with the published token", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    const heatmap = screen.getByTestId("report-calendar-heatmap-view");
    const todayCell = within(heatmap).getByRole("gridcell", {
      name: new RegExp(`${TODAY} 발행`),
    });
    expect(todayCell.getAttribute("data-status")).toBe("published");
    expect(todayCell.className).toMatch(/bg-\[var\(--status-success\)\]/);
  });

  it("navigates to /reports/{ISO} when a heatmap cell is clicked (TC-3)", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    const heatmap = screen.getByTestId("report-calendar-heatmap-view");
    const cell = within(heatmap).getByRole("gridcell", {
      name: new RegExp(`${TODAY} 발행`),
    });
    fireEvent.click(cell);

    expect(navigateMock).toHaveBeenCalledWith(`/reports/${TODAY}`);
  });
});

describe("ReportCalendar — tab persistence (TC-4)", () => {
  it("writes calendarTab to localStorage when the tab is switched", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    const heatmapTrigger = screen.getByTestId("calendar-tab-heatmap");
    // Radix tabs activate on pointerdown + click; jsdom dispatches both via
    // mouseDown/mouseUp/click. Use the user-facing pointer sequence.
    fireEvent.mouseDown(heatmapTrigger);
    fireEvent.mouseUp(heatmapTrigger);
    fireEvent.click(heatmapTrigger);

    // Store update is the source of truth for "active tab" persistence.
    expect(useAppStore.getState().calendarTab).toBe("heatmap");

    const raw = window.localStorage.getItem(PERSIST_KEY);
    expect(raw).toBeTruthy();
    const parsed = JSON.parse(raw!) as {
      version: number;
      state: { calendarTab?: string };
    };
    expect(parsed.version).toBe(1);
    expect(parsed.state.calendarTab).toBe("heatmap");
  });

  it("rehydrates the previously persisted tab so the heatmap view mounts on first render", async () => {
    window.localStorage.setItem(
      PERSIST_KEY,
      JSON.stringify({
        version: 1,
        state: {
          calendarTab: "heatmap",
          runOptions: useAppStore.getState().runOptions,
          activeRun: null,
        },
      }),
    );
    await useAppStore.persist.rehydrate();

    render(
      <AllProviders>
        <ReportCalendar reports={reports} todayIso={TODAY} />
      </AllProviders>,
    );

    expect(
      screen.getByTestId("report-calendar-heatmap-view"),
    ).toBeInTheDocument();
    expect(useAppStore.getState().calendarTab).toBe("heatmap");
  });
});

describe("ReportCalendar — empty data (TC-E2)", () => {
  it("renders the month view footer count as 0 when there are zero reports", () => {
    render(
      <AllProviders>
        <ReportCalendar reports={[]} todayIso={TODAY} />
      </AllProviders>,
    );

    expect(
      screen.getByTestId("report-calendar-month-view"),
    ).toBeInTheDocument();
    expect(
      screen.getByTestId("report-calendar-month-count"),
    ).toHaveTextContent(/^0 \//);
  });

  it("renders all heatmap cells in the muted bucket when there are zero reports", () => {
    useAppStore.setState({ calendarTab: "heatmap" });
    render(
      <AllProviders>
        <ReportCalendar reports={[]} todayIso={TODAY} />
      </AllProviders>,
    );

    const heatmap = screen.getByTestId("report-calendar-heatmap-view");
    const cells = within(heatmap).getAllByRole("gridcell");
    const populated = cells.filter((c) => c.hasAttribute("data-date"));
    expect(populated.length).toBeGreaterThan(0);
    for (const c of populated) {
      expect(c.getAttribute("data-status")).toBe("none");
      expect(c.className).toMatch(/bg-muted/);
    }
  });
});
