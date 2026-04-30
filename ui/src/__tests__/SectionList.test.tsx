import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { SectionList } from "@/components/SectionList";
import { AllProviders } from "./test-utils";
import type { ReportSection } from "@/lib/api";

function makeSection(
  i: number,
  overrides: Partial<ReportSection> = {},
): ReportSection {
  return {
    id: `s-${i}`,
    section_order: i,
    title: `Section ${i + 1}`,
    fact_summary: `Summary ${i + 1}`,
    ...overrides,
  };
}

describe("SectionList (TC-4.1, TC-4.2)", () => {
  it("renders an empty state when there are no sections", () => {
    render(
      <AllProviders>
        <SectionList
          sections={[]}
          selectedSectionId={null}
          disabledSectionIds={{}}
          onSelect={vi.fn()}
          onToggle={vi.fn()}
          onReorder={vi.fn()}
        />
      </AllProviders>,
    );
    expect(screen.getByTestId("section-list-empty")).toBeInTheDocument();
  });

  it("renders all section rows with handles and toggles", () => {
    const sections = [makeSection(0), makeSection(1), makeSection(2)];
    render(
      <AllProviders>
        <SectionList
          sections={sections}
          selectedSectionId={null}
          disabledSectionIds={{}}
          onSelect={vi.fn()}
          onToggle={vi.fn()}
          onReorder={vi.fn()}
        />
      </AllProviders>,
    );

    expect(screen.getByTestId("section-list")).toBeInTheDocument();
    sections.forEach((s) => {
      expect(screen.getByTestId(`section-row-${s.id}`)).toBeInTheDocument();
      expect(screen.getByTestId(`section-handle-${s.id}`)).toBeInTheDocument();
      expect(screen.getByTestId(`section-toggle-${s.id}`)).toBeInTheDocument();
    });
    expect(screen.getByText("1. Section 1")).toBeInTheDocument();
  });

  it("calls onSelect when the body of a row is clicked", () => {
    const onSelect = vi.fn();
    const sections = [makeSection(0), makeSection(1)];
    render(
      <AllProviders>
        <SectionList
          sections={sections}
          selectedSectionId={null}
          disabledSectionIds={{}}
          onSelect={onSelect}
          onToggle={vi.fn()}
          onReorder={vi.fn()}
        />
      </AllProviders>,
    );

    fireEvent.click(screen.getByText("2. Section 2"));
    expect(onSelect).toHaveBeenCalledWith("s-1");
  });

  it("calls onToggle when the on/off checkbox flips (TC-4.2)", () => {
    const onToggle = vi.fn();
    const sections = [makeSection(0)];
    render(
      <AllProviders>
        <SectionList
          sections={sections}
          selectedSectionId={null}
          disabledSectionIds={{}}
          onSelect={vi.fn()}
          onToggle={onToggle}
          onReorder={vi.fn()}
        />
      </AllProviders>,
    );

    fireEvent.click(screen.getByTestId("section-toggle-s-0"));
    expect(onToggle).toHaveBeenCalledWith("s-0");
  });

  it("marks disabled sections with data-enabled=false (hatch styling)", () => {
    const sections = [makeSection(0), makeSection(1)];
    render(
      <AllProviders>
        <SectionList
          sections={sections}
          selectedSectionId={null}
          disabledSectionIds={{ "s-1": true }}
          onSelect={vi.fn()}
          onToggle={vi.fn()}
          onReorder={vi.fn()}
        />
      </AllProviders>,
    );

    expect(screen.getByTestId("section-row-s-0")).toHaveAttribute(
      "data-enabled",
      "true",
    );
    expect(screen.getByTestId("section-row-s-1")).toHaveAttribute(
      "data-enabled",
      "false",
    );
  });

  it("highlights the selected row with data-selected=true", () => {
    const sections = [makeSection(0), makeSection(1)];
    render(
      <AllProviders>
        <SectionList
          sections={sections}
          selectedSectionId={"s-1"}
          disabledSectionIds={{}}
          onSelect={vi.fn()}
          onToggle={vi.fn()}
          onReorder={vi.fn()}
        />
      </AllProviders>,
    );

    expect(screen.getByTestId("section-row-s-1")).toHaveAttribute(
      "data-selected",
      "true",
    );
    expect(screen.getByTestId("section-row-s-0")).toHaveAttribute(
      "data-selected",
      "false",
    );
  });
});
