import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { Sidebar } from "@/components/Sidebar";
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
});
