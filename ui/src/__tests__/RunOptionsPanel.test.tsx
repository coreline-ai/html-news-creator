import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { RunOptionsPanel } from "@/components/RunOptionsPanel";
import { useAppStore, DEFAULT_RUN_OPTIONS } from "@/lib/store";
import { AllProviders } from "./test-utils";

beforeEach(() => {
  useAppStore.setState({
    runOptions: { ...DEFAULT_RUN_OPTIONS },
    previewMode: "live",
  });
});

describe("RunOptionsPanel (TC-3.1)", () => {
  it("renders five accordion groups (A..E)", () => {
    render(
      <AllProviders>
        <RunOptionsPanel />
      </AllProviders>,
    );
    expect(screen.getByTestId("group-A")).toBeInTheDocument();
    expect(screen.getByTestId("group-B")).toBeInTheDocument();
    expect(screen.getByTestId("group-C")).toBeInTheDocument();
    expect(screen.getByTestId("group-D")).toBeInTheDocument();
    expect(screen.getByTestId("group-E")).toBeInTheDocument();
  });

  it("starts with Execution + Editorial open by default", () => {
    render(
      <AllProviders>
        <RunOptionsPanel />
      </AllProviders>,
    );
    const a = screen.getByTestId("group-A");
    const b = screen.getByTestId("group-B");
    const c = screen.getByTestId("group-C");
    expect(within(a).getByLabelText(/^date \(KST\)$/i)).toBeInTheDocument();
    expect(within(b).getByLabelText(/target sections/i)).toBeInTheDocument();
    // Group C is closed → its button exists but content does not.
    expect(within(c).queryByText(/37 sources active/i)).toBeNull();
  });

  it("expands Sources group when its trigger is clicked", () => {
    render(
      <AllProviders>
        <RunOptionsPanel />
      </AllProviders>,
    );
    const c = screen.getByTestId("group-C");
    const trigger = within(c).getByRole("button", { expanded: false });
    fireEvent.click(trigger);
    expect(within(c).getByText(/37 sources active/i)).toBeInTheDocument();
  });

  it("updates the store when target_sections slider changes", () => {
    render(
      <AllProviders>
        <RunOptionsPanel />
      </AllProviders>,
    );
    const slider = screen.getByLabelText(/target sections/i) as HTMLInputElement;
    fireEvent.change(slider, { target: { value: "8" } });
    expect(useAppStore.getState().runOptions.target_sections).toBe(8);
  });

  it("toggles dry-run via the switch", () => {
    render(
      <AllProviders>
        <RunOptionsPanel />
      </AllProviders>,
    );
    const sw = screen.getByRole("switch", { name: /dry run/i });
    expect(sw).toHaveAttribute("aria-checked", "false");
    fireEvent.click(sw);
    expect(useAppStore.getState().runOptions.dry_run).toBe(true);
    expect(sw).toHaveAttribute("aria-checked", "true");
  });

  it("resets options back to defaults", () => {
    useAppStore.setState({
      runOptions: { ...DEFAULT_RUN_OPTIONS, target_sections: 3, dry_run: true },
    });
    render(
      <AllProviders>
        <RunOptionsPanel />
      </AllProviders>,
    );
    const reset = screen.getByRole("button", { name: /reset/i });
    fireEvent.click(reset);
    expect(useAppStore.getState().runOptions.target_sections).toBe(
      DEFAULT_RUN_OPTIONS.target_sections,
    );
    expect(useAppStore.getState().runOptions.dry_run).toBe(false);
  });
});
