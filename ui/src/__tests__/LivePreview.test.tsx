import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { LivePreview } from "@/components/LivePreview";

describe("LivePreview (TC-3.4)", () => {
  it("renders an iframe with sandbox=allow-same-origin and srcDoc", () => {
    render(<LivePreview html="<p>hi</p>" />);
    const iframe = screen.getByTestId("preview-iframe") as HTMLIFrameElement;
    expect(iframe).toBeInTheDocument();
    expect(iframe.getAttribute("sandbox")).toBe("allow-same-origin");
    // React renders srcDoc as the `srcdoc` attribute on the DOM node.
    expect(iframe.getAttribute("srcdoc")).toContain("<p>hi</p>");
  });

  it("toggles desktop → mobile viewport (1280 → 375)", () => {
    render(<LivePreview html="<p>hi</p>" />);
    const container = screen.getByTestId("preview-frame-container");
    expect(container.getAttribute("style")).toContain("width: 1280px");

    fireEvent.click(screen.getByTestId("vp-mobile"));
    expect(container.getAttribute("style")).toContain("width: 375px");

    const root = screen.getByTestId("live-preview");
    expect(root.getAttribute("data-viewport")).toBe("mobile");
  });

  it("toggles tablet viewport to 768px", () => {
    render(<LivePreview html="<p>hi</p>" />);
    fireEvent.click(screen.getByTestId("vp-tablet"));
    const container = screen.getByTestId("preview-frame-container");
    expect(container.getAttribute("style")).toContain("width: 768px");
  });

  it("falls back to placeholder document when html is null", () => {
    render(<LivePreview html={null} />);
    const iframe = screen.getByTestId("preview-iframe") as HTMLIFrameElement;
    expect(iframe.getAttribute("srcdoc")).toContain("No preview yet");
  });

  it("shows the error string when error is provided", () => {
    render(<LivePreview html={null} error="boom" />);
    expect(screen.getByText("boom")).toBeInTheDocument();
  });

  it("surfaces a loading indicator when isLoading is true", () => {
    render(<LivePreview html={null} isLoading />);
    expect(screen.getByText(/rendering preview/i)).toBeInTheDocument();
  });
});
