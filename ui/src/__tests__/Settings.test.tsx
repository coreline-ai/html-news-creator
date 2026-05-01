import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import Settings from "@/pages/Settings";
import { DEFAULT_RUN_OPTIONS, useAppStore } from "@/lib/store";
import { AllProviders } from "./test-utils";

beforeEach(() => {
  document.documentElement.classList.add("dark");
  document.documentElement.classList.remove("light");
  window.localStorage.clear();
  useAppStore.setState({
    theme: "dark",
    runOptions: { ...DEFAULT_RUN_OPTIONS, output_theme: "newsroom-white" },
  });
});

function renderSettings() {
  return render(
    <AllProviders>
      <Settings />
    </AllProviders>,
  );
}

describe("Settings page", () => {
  it("separates app settings from editorial policy", () => {
    renderSettings();

    expect(screen.getByRole("heading", { name: /^settings$/i })).toBeInTheDocument();
    expect(screen.getByText("Editorial Policy")).toBeInTheDocument();
    expect(screen.getByRole("link", { name: /open policy/i })).toHaveAttribute(
      "href",
      "/policy",
    );
    expect(screen.getByTestId("settings-output-theme-newsroom-white")).toHaveAttribute(
      "aria-pressed",
      "true",
    );
    expect(screen.queryByTestId("policy-form")).not.toBeInTheDocument();
  });

  it("updates editable app and report defaults", () => {
    renderSettings();

    fireEvent.click(screen.getByTestId("settings-theme-light"));
    expect(useAppStore.getState().theme).toBe("light");
    expect(document.documentElement.classList.contains("light")).toBe(true);

    fireEvent.click(screen.getByTestId("settings-output-theme-dark"));
    expect(useAppStore.getState().runOptions.output_theme).toBe("dark");

    fireEvent.change(screen.getByTestId("settings-language"), {
      target: { value: "en" },
    });
    expect(useAppStore.getState().runOptions.language).toBe("en");

    fireEvent.change(screen.getByTestId("settings-format"), {
      target: { value: "markdown" },
    });
    expect(useAppStore.getState().runOptions.format).toBe("markdown");

    fireEvent.change(screen.getByTestId("settings-target-sections"), {
      target: { value: "8" },
    });
    expect(useAppStore.getState().runOptions.target_sections).toBe(8);

    fireEvent.click(screen.getByTestId("settings-deploy-local-only"));
    expect(useAppStore.getState().runOptions.deploy_target).toBe("local-only");

    fireEvent.click(screen.getByTestId("settings-slack-disabled"));
    expect(useAppStore.getState().runOptions.slack_notify).toBe(false);
  });

  it("resets report defaults without changing the app theme", () => {
    renderSettings();

    fireEvent.click(screen.getByTestId("settings-theme-light"));
    fireEvent.click(screen.getByTestId("settings-output-theme-dark"));
    fireEvent.change(screen.getByTestId("settings-target-sections"), {
      target: { value: "6" },
    });

    fireEvent.click(screen.getByTestId("settings-reset-run-defaults"));

    expect(useAppStore.getState().theme).toBe("light");
    expect(useAppStore.getState().runOptions.output_theme).toBe(
      DEFAULT_RUN_OPTIONS.output_theme,
    );
    expect(useAppStore.getState().runOptions.target_sections).toBe(
      DEFAULT_RUN_OPTIONS.target_sections,
    );
  });
});
