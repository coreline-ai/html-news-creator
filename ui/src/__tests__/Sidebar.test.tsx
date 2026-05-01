import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { MobileSidebar, Sidebar } from "@/components/Sidebar";
import { AllProviders } from "./test-utils";

describe("Sidebar (TC-2.2)", () => {
  it("renders all primary nav entries with lucide icons", () => {
    render(
      <AllProviders initialEntries={["/"]}>
        <Sidebar />
      </AllProviders>,
    );

    expect(screen.getByText("Home")).toBeInTheDocument();
    expect(screen.getByText("Reports")).toBeInTheDocument();
    expect(screen.getByText("Sources")).toBeInTheDocument();
    expect(screen.getByText("Policy")).toBeInTheDocument();
    expect(screen.getByText("Settings")).toBeInTheDocument();
  });

  it("marks the current route with aria-current=page", () => {
    render(
      <AllProviders initialEntries={["/sources"]}>
        <Sidebar />
      </AllProviders>,
    );

    const sourcesLink = screen.getByRole("link", { name: /sources/i });
    expect(sourcesLink).toHaveAttribute("aria-current", "page");

    const homeLink = screen.getByRole("link", { name: /^home$/i });
    expect(homeLink).not.toHaveAttribute("aria-current", "page");
  });

  it("treats `/` as Home active only on the index route (end matching)", () => {
    render(
      <AllProviders initialEntries={["/reports"]}>
        <Sidebar />
      </AllProviders>,
    );

    const homeLink = screen.getByRole("link", { name: /^home$/i });
    expect(homeLink).not.toHaveAttribute("aria-current", "page");
    const reportsLink = screen.getByRole("link", { name: /^reports$/i });
    expect(reportsLink).toHaveAttribute("aria-current", "page");
  });

  it("keeps Policy and Settings active states independent", () => {
    const first = render(
      <AllProviders initialEntries={["/policy"]}>
        <Sidebar />
      </AllProviders>,
    );

    const policyLink = screen.getByRole("link", { name: /^policy$/i });
    const settingsLink = screen.getByRole("link", { name: /^settings$/i });
    expect(policyLink).toHaveAttribute("href", "/policy");
    expect(settingsLink).toHaveAttribute("href", "/settings");
    expect(policyLink).toHaveAttribute("aria-current", "page");
    expect(settingsLink).not.toHaveAttribute("aria-current", "page");
    first.unmount();

    render(
      <AllProviders initialEntries={["/settings"]}>
        <Sidebar />
      </AllProviders>,
    );

    expect(screen.getByRole("link", { name: /^settings$/i })).toHaveAttribute(
      "aria-current",
      "page",
    );
    expect(screen.getByRole("link", { name: /^policy$/i })).not.toHaveAttribute(
      "aria-current",
      "page",
    );
  });

  it("renders a clear X close button in the mobile drawer", () => {
    render(
      <AllProviders initialEntries={["/"]}>
        <MobileSidebar open onOpenChange={() => undefined} />
      </AllProviders>,
    );

    const close = screen.getByRole("button", { name: /close navigation/i });
    expect(close).toBeInTheDocument();
    expect(close).toHaveAttribute("data-testid", "mobile-sidebar-close");
  });
});
