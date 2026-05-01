import { describe, it, expect, beforeEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ThemeToggle } from "@/components/ThemeToggle";
import { useAppStore } from "@/lib/store";

describe("ThemeToggle (TC-2.1, TC-2.4)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
    document.documentElement.classList.remove("light");
    window.localStorage.clear();
    useAppStore.setState({ theme: "dark" });
  });

  it("starts in dark mode (TC-2.1)", () => {
    render(<ThemeToggle />);
    expect(document.documentElement.classList.contains("dark")).toBe(true);
    expect(document.documentElement.classList.contains("light")).toBe(false);
    const btn = screen.getByRole("button");
    expect(btn).toHaveAttribute("aria-pressed", "true");
  });

  it("toggles dark class on <html> and writes localStorage (TC-2.4)", () => {
    render(<ThemeToggle />);

    const btn = screen.getByRole("button");
    fireEvent.click(btn);

    expect(document.documentElement.classList.contains("dark")).toBe(false);
    expect(document.documentElement.classList.contains("light")).toBe(true);
    expect(window.localStorage.getItem("theme")).toBe("light");
    expect(btn).toHaveAttribute("aria-pressed", "false");

    fireEvent.click(btn);
    expect(document.documentElement.classList.contains("dark")).toBe(true);
    expect(document.documentElement.classList.contains("light")).toBe(false);
    expect(window.localStorage.getItem("theme")).toBe("dark");
  });
});
