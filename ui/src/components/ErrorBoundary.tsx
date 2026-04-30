import { Component, type ErrorInfo, type ReactNode } from "react";
import { AlertCircle, RotateCw } from "lucide-react";
import { Button } from "@/components/ui/button";

interface ErrorBoundaryProps {
  children: ReactNode;
  /** Optional custom fallback render. If provided, replaces the default UI. */
  fallback?: (error: Error, reset: () => void) => ReactNode;
}

interface ErrorBoundaryState {
  error: Error | null;
}

/**
 * App-level error boundary. Wraps the workspace `<Outlet />` so a thrown render
 * error in any page does not blank the entire shell.
 *
 * - Production: minimal message + retry button.
 * - Development: includes stack trace for debugging.
 */
export class ErrorBoundary extends Component<
  ErrorBoundaryProps,
  ErrorBoundaryState
> {
  state: ErrorBoundaryState = { error: null };

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { error };
  }

  componentDidCatch(error: Error, info: ErrorInfo): void {
    // Surface for devs; intentionally console-only — no telemetry coupling.
    if (import.meta.env?.DEV) {
      // eslint-disable-next-line no-console
      console.error("ErrorBoundary caught:", error, info.componentStack);
    }
  }

  reset = (): void => {
    this.setState({ error: null });
  };

  render(): ReactNode {
    const { error } = this.state;
    if (!error) return this.props.children;

    if (this.props.fallback) {
      return this.props.fallback(error, this.reset);
    }

    const isDev = !!import.meta.env?.DEV;
    return (
      <div
        role="alert"
        data-testid="error-boundary"
        className="mx-auto flex max-w-[680px] flex-col items-center gap-4 px-6 py-16 text-center"
      >
        <AlertCircle
          className="text-destructive size-8"
          strokeWidth={1.5}
          aria-hidden="true"
        />
        <div className="text-foreground text-base font-medium">
          Something went wrong
        </div>
        <p className="text-muted-foreground max-w-md text-sm">
          {isDev
            ? error.message || "An unexpected error occurred."
            : "An unexpected error occurred. Please retry."}
        </p>
        {isDev && error.stack ? (
          <pre className="bg-muted text-muted-foreground max-h-48 w-full overflow-auto rounded-md p-3 text-left font-mono text-[11px] whitespace-pre-wrap">
            {error.stack}
          </pre>
        ) : null}
        <Button
          type="button"
          variant="default"
          size="sm"
          onClick={this.reset}
          data-testid="error-boundary-retry"
        >
          <RotateCw className="size-4" aria-hidden="true" />
          Retry
        </Button>
      </div>
    );
  }
}

export default ErrorBoundary;
