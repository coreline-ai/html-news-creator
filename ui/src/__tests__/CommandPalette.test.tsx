import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { Routes, Route, useLocation } from "react-router-dom";
import { CommandPalette } from "@/components/CommandPalette";
import { AllProviders } from "./test-utils";

function LocationProbe() {
  const location = useLocation();
  return <div data-testid="probe-pathname">{location.pathname}</div>;
}

function renderPalette({
  open = true,
  onOpenChange = () => {},
  onRerunLast,
  onPublishCurrent,
}: {
  open?: boolean;
  onOpenChange?: (o: boolean) => void;
  onRerunLast?: () => void;
  onPublishCurrent?: () => void;
} = {}) {
  return render(
    <AllProviders initialEntries={["/"]}>
      <Routes>
        <Route
          path="*"
          element={
            <>
              <LocationProbe />
              <CommandPalette
                open={open}
                onOpenChange={onOpenChange}
                onRerunLast={onRerunLast}
                onPublishCurrent={onPublishCurrent}
              />
            </>
          }
        />
      </Routes>
    </AllProviders>,
  );
}

describe("CommandPalette (TC-6.1)", () => {
  it("renders all 7 commands when open", () => {
    renderPalette({ open: true });
    expect(screen.getByTestId("command-palette")).toBeInTheDocument();
    expect(screen.getByText("Go to Dashboard")).toBeInTheDocument();
    expect(screen.getByText("New report")).toBeInTheDocument();
    expect(screen.getByText("Sources")).toBeInTheDocument();
    expect(screen.getByText("Editorial Policy")).toBeInTheDocument();
    expect(screen.getByText("Settings")).toBeInTheDocument();
    expect(screen.getByText("Re-run last")).toBeInTheDocument();
    expect(screen.getByText("Publish current")).toBeInTheDocument();
  });

  it("does not render content when closed", () => {
    renderPalette({ open: false });
    expect(screen.queryByTestId("command-palette")).not.toBeInTheDocument();
  });

  it("filters commands by typed query", async () => {
    renderPalette({ open: true });
    const input = screen.getByTestId("command-palette-input");
    fireEvent.change(input, { target: { value: "Sources" } });
    await waitFor(() => {
      expect(screen.getByText("Sources")).toBeInTheDocument();
    });
    // Items that don't match should drop out of the list.
    expect(screen.queryByText("Re-run last")).not.toBeInTheDocument();
  });

  it("invokes onRerunLast when 'Re-run last' is selected", () => {
    const onRerunLast = vi.fn();
    const onOpenChange = vi.fn();
    renderPalette({ open: true, onRerunLast, onOpenChange });
    fireEvent.click(screen.getByTestId("command-item-rerun-last"));
    expect(onRerunLast).toHaveBeenCalledTimes(1);
    expect(onOpenChange).toHaveBeenCalledWith(false);
  });

  it("invokes onPublishCurrent when 'Publish current' is selected", () => {
    const onPublishCurrent = vi.fn();
    const onOpenChange = vi.fn();
    renderPalette({ open: true, onPublishCurrent, onOpenChange });
    fireEvent.click(screen.getByTestId("command-item-publish-current"));
    expect(onPublishCurrent).toHaveBeenCalledTimes(1);
    expect(onOpenChange).toHaveBeenCalledWith(false);
  });

  it("navigates to /sources when nav command is selected", async () => {
    const onOpenChange = vi.fn();
    renderPalette({ open: true, onOpenChange });
    fireEvent.click(screen.getByTestId("command-item-go-sources"));
    await waitFor(() =>
      expect(screen.getByTestId("probe-pathname")).toHaveTextContent("/sources"),
    );
    expect(onOpenChange).toHaveBeenCalledWith(false);
  });

  it("navigates to /policy when Editorial Policy command is selected", async () => {
    const onOpenChange = vi.fn();
    renderPalette({ open: true, onOpenChange });
    fireEvent.click(screen.getByTestId("command-item-go-policy"));
    await waitFor(() =>
      expect(screen.getByTestId("probe-pathname")).toHaveTextContent("/policy"),
    );
    expect(onOpenChange).toHaveBeenCalledWith(false);
  });
});
