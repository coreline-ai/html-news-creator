import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { useState } from "react";
import { ErrorBoundary } from "@/components/ErrorBoundary";

function Boom({ shouldThrow }: { shouldThrow: boolean }) {
  if (shouldThrow) {
    throw new Error("kaboom");
  }
  return <div data-testid="ok-child">child rendered</div>;
}

describe("ErrorBoundary (TC-6.3)", () => {
  // Suppress noisy console.error from React's boundary report path.
  let errorSpy: ReturnType<typeof vi.spyOn>;
  beforeEach(() => {
    errorSpy = vi.spyOn(console, "error").mockImplementation(() => {});
  });
  afterEach(() => {
    errorSpy.mockRestore();
  });

  it("renders children when no error is thrown", () => {
    render(
      <ErrorBoundary>
        <Boom shouldThrow={false} />
      </ErrorBoundary>,
    );
    expect(screen.getByTestId("ok-child")).toBeInTheDocument();
  });

  it("renders fallback with retry button when child throws", () => {
    render(
      <ErrorBoundary>
        <Boom shouldThrow />
      </ErrorBoundary>,
    );
    expect(screen.getByTestId("error-boundary")).toBeInTheDocument();
    expect(screen.getByText(/Something went wrong/i)).toBeInTheDocument();
    expect(screen.getByTestId("error-boundary-retry")).toBeInTheDocument();
  });

  it("retry button clears the error and re-renders children", () => {
    function Harness() {
      const [shouldThrow, setShouldThrow] = useState(true);
      return (
        <div>
          <button
            type="button"
            data-testid="fix-bug"
            onClick={() => setShouldThrow(false)}
          >
            fix
          </button>
          <ErrorBoundary>
            <Boom shouldThrow={shouldThrow} />
          </ErrorBoundary>
        </div>
      );
    }

    render(<Harness />);
    expect(screen.getByTestId("error-boundary")).toBeInTheDocument();

    // First "fix" the underlying bug, then click retry.
    fireEvent.click(screen.getByTestId("fix-bug"));
    fireEvent.click(screen.getByTestId("error-boundary-retry"));

    expect(screen.getByTestId("ok-child")).toBeInTheDocument();
    expect(screen.queryByTestId("error-boundary")).not.toBeInTheDocument();
  });

  it("uses the custom fallback render prop when provided", () => {
    render(
      <ErrorBoundary
        fallback={(err, reset) => (
          <div>
            <span data-testid="custom-fallback">custom: {err.message}</span>
            <button type="button" onClick={reset}>
              reset
            </button>
          </div>
        )}
      >
        <Boom shouldThrow />
      </ErrorBoundary>,
    );
    expect(screen.getByTestId("custom-fallback")).toHaveTextContent(
      "custom: kaboom",
    );
  });
});
