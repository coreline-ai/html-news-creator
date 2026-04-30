import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { SectionEditor } from "@/components/SectionEditor";
import { AllProviders } from "./test-utils";
import type { ReportSection } from "@/lib/api";

function makeSection(overrides: Partial<ReportSection> = {}): ReportSection {
  return {
    id: "sec-1",
    section_order: 0,
    title: "Original title",
    fact_summary: "Original summary",
    inference_summary: "Original implication",
    image_evidence_json: [{ url: "https://cdn.example/old.png" }],
    ...overrides,
  };
}

describe("SectionEditor (TC-4.3, TC-4.E1)", () => {
  it("renders the empty placeholder when no section is selected", () => {
    render(
      <AllProviders>
        <SectionEditor
          section={null}
          onSave={vi.fn()}
          onRegenerate={vi.fn()}
        />
      </AllProviders>,
    );
    expect(screen.getByTestId("section-editor-empty")).toBeInTheDocument();
  });

  it("hydrates form fields from the selected section", () => {
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={vi.fn()}
          onRegenerate={vi.fn()}
        />
      </AllProviders>,
    );
    expect(screen.getByTestId("section-editor-title")).toHaveValue(
      "Original title",
    );
    expect(screen.getByTestId("section-editor-summary")).toHaveValue(
      "Original summary",
    );
    expect(screen.getByTestId("section-editor-implication")).toHaveValue(
      "Original implication",
    );
    expect(screen.getByTestId("section-editor-image")).toHaveValue(
      "https://cdn.example/old.png",
    );
  });

  it("calls onSave with only the changed fields (TC-4.3)", async () => {
    const onSave = vi.fn().mockResolvedValue(undefined);
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={onSave}
          onRegenerate={vi.fn()}
        />
      </AllProviders>,
    );

    fireEvent.change(screen.getByTestId("section-editor-title"), {
      target: { value: "Updated title" },
    });
    fireEvent.click(screen.getByTestId("section-editor-save"));

    await waitFor(() => {
      expect(onSave).toHaveBeenCalledTimes(1);
    });
    expect(onSave).toHaveBeenCalledWith({ title: "Updated title" });
  });

  it("does not call onSave when nothing has changed", async () => {
    const onSave = vi.fn().mockResolvedValue(undefined);
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={onSave}
          onRegenerate={vi.fn()}
        />
      </AllProviders>,
    );
    fireEvent.click(screen.getByTestId("section-editor-save"));
    // form submit goes through but no fields differ → no call
    await new Promise((r) => setTimeout(r, 0));
    expect(onSave).not.toHaveBeenCalled();
  });

  it("calls onRegenerate when the regenerate button is pressed", () => {
    const onRegenerate = vi.fn().mockResolvedValue(undefined);
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={vi.fn()}
          onRegenerate={onRegenerate}
        />
      </AllProviders>,
    );
    fireEvent.click(screen.getByTestId("section-editor-regenerate"));
    expect(onRegenerate).toHaveBeenCalledTimes(1);
  });

  it("renders an inline error when regenerate fails (TC-4.E1)", () => {
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={vi.fn()}
          onRegenerate={vi.fn()}
          error="Regenerate failed: 500"
        />
      </AllProviders>,
    );
    expect(screen.getByTestId("section-editor-error")).toHaveTextContent(
      "Regenerate failed: 500",
    );
  });

  it("disables inputs while saving and shows the saving label", () => {
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={vi.fn()}
          onRegenerate={vi.fn()}
          saving
        />
      </AllProviders>,
    );
    expect(screen.getByTestId("section-editor-title")).toBeDisabled();
    expect(screen.getByTestId("section-editor-save")).toHaveTextContent(
      /saving/i,
    );
  });

  it("renames the manual-toggle button when toggled", () => {
    render(
      <AllProviders>
        <SectionEditor
          section={makeSection()}
          onSave={vi.fn()}
          onRegenerate={vi.fn()}
        />
      </AllProviders>,
    );
    const btn = screen.getByTestId("section-editor-manual-toggle");
    expect(btn).toHaveTextContent(/manual edit/i);
    fireEvent.click(btn);
    expect(btn).toHaveTextContent(/auto/i);
  });
});
