import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { PolicyForm } from "@/components/PolicyForm";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

function jsonResponse(body: unknown, init: ResponseInit = {}) {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { "content-type": "application/json" },
    ...init,
  });
}

afterEach(() => {
  globalThis.fetch = originalFetch;
  vi.restoreAllMocks();
});

describe("PolicyForm — Persist to yaml (Phase E)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
  });

  it("renders the [Persist to yaml] button in the footer", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(
      jsonResponse({
        policy: {
          source_tiers: { official: { boost: 18, eligible_for_main: true } },
          report_selection: { target_sections: 10, max_sections: 10 },
        },
      }),
    ) as unknown as typeof fetch;

    render(
      <AllProviders>
        <PolicyForm />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("policy-form")).toBeInTheDocument();
    });

    const persistBtn = screen.getByTestId("policy-persist-button");
    expect(persistBtn).toBeInTheDocument();
    expect(persistBtn).toHaveTextContent(/Persist to yaml/i);
  });

  it("opens the confirmation dialog and posts to /api/policy/persist on confirm", async () => {
    const calls: { url: string; init?: RequestInit }[] = [];
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL, init?: RequestInit) => {
      const u = typeof url === "string" ? url : url.toString();
      calls.push({ url: u, init });
      if (u === "/api/policy" && (!init || !init.method || init.method === "GET")) {
        return jsonResponse({
          policy: {
            source_tiers: { official: { boost: 18, eligible_for_main: true } },
            report_selection: { target_sections: 10, max_sections: 10 },
          },
        });
      }
      if (u === "/api/policy/persist" && init?.method === "POST") {
        return jsonResponse({
          persisted_to: "data/editorial_policy.yaml",
          backup: "data/editorial_policy.yaml.bak",
        });
      }
      return new Response("nope", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders>
        <PolicyForm />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("policy-form")).toBeInTheDocument();
    });

    // Open the dialog.
    fireEvent.click(screen.getByTestId("policy-persist-button"));
    await waitFor(() => {
      expect(screen.getByTestId("policy-persist-dialog")).toBeInTheDocument();
    });
    expect(
      screen.getByRole("heading", { name: /yaml 파일에 영구 저장/i }),
    ).toBeInTheDocument();

    // Confirm — fires the mutation.
    fireEvent.click(screen.getByTestId("policy-persist-confirm"));

    await waitFor(() => {
      const persist = calls.find(
        (c) => c.url === "/api/policy/persist" && c.init?.method === "POST",
      );
      expect(persist).toBeDefined();
    });
  });

  it("surfaces the success toast with persisted_to + backup paths", async () => {
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL, init?: RequestInit) => {
      const u = typeof url === "string" ? url : url.toString();
      if (u === "/api/policy" && (!init || !init.method || init.method === "GET")) {
        return jsonResponse({
          policy: { report_selection: { target_sections: 10, max_sections: 10 } },
        });
      }
      if (u === "/api/policy/persist" && init?.method === "POST") {
        return jsonResponse({
          persisted_to: "data/editorial_policy.yaml",
          backup: "data/editorial_policy.yaml.bak",
        });
      }
      return new Response("nope", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders>
        <PolicyForm />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("policy-form")).toBeInTheDocument();
    });

    fireEvent.click(screen.getByTestId("policy-persist-button"));
    await waitFor(() => {
      expect(screen.getByTestId("policy-persist-dialog")).toBeInTheDocument();
    });
    fireEvent.click(screen.getByTestId("policy-persist-confirm"));

    await waitFor(() => {
      expect(screen.getByTestId("policy-persist-toast")).toBeInTheDocument();
    });
    const toast = screen.getByTestId("policy-persist-toast");
    expect(toast).toHaveTextContent(/yaml에 저장됨/);
    expect(toast).toHaveTextContent(/data\/editorial_policy\.yaml/);
    expect(toast).toHaveTextContent(/data\/editorial_policy\.yaml\.bak/);
  });
});
