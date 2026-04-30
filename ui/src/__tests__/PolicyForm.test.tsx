import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { PolicyForm } from "@/components/PolicyForm";
import { AddSourceDialog } from "@/components/AddSourceDialog";
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

describe("PolicyForm (TC-5.3)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
  });

  it("renders the volatile-override banner and 5 sections", async () => {
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

    expect(screen.getByTestId("policy-volatile-banner")).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: /^Source tiers$/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: /^Scoring weights$/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: /^Penalties$/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: /^Quotas$/i }),
    ).toBeInTheDocument();
    expect(
      screen.getByRole("heading", { name: /^Report selection$/i }),
    ).toBeInTheDocument();
  });

  it("changes target_sections via slider and saves with PUT /api/policy", async () => {
    const calls: { url: string; init?: RequestInit }[] = [];
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL, init?: RequestInit) => {
      const u = typeof url === "string" ? url : url.toString();
      calls.push({ url: u, init });
      if (u === "/api/policy" && (!init || !init.method || init.method === "GET")) {
        return jsonResponse({
          policy: {
            source_tiers: {
              official: { boost: 18, eligible_for_main: true },
            },
            report_selection: { target_sections: 10, max_sections: 10 },
          },
        });
      }
      if (u === "/api/policy" && init?.method === "PUT") {
        return jsonResponse({ policy: JSON.parse(String(init.body)).patch });
      }
      return new Response("nope", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders>
        <PolicyForm />
      </AllProviders>,
    );

    const slider = await screen.findByLabelText(/^Target sections$/);
    fireEvent.change(slider, { target: { value: "7" } });

    const saveBtn = screen.getByRole("button", { name: /save policy/i });
    expect(saveBtn).toBeEnabled();
    fireEvent.click(saveBtn);

    await waitFor(() => {
      const put = calls.find((c) => c.init?.method === "PUT");
      expect(put).toBeDefined();
      const body = JSON.parse(String(put!.init!.body));
      expect(body.patch.report_selection.target_sections).toBe(7);
    });
  });
});

describe("AddSourceDialog (TC-5.E1)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
  });

  it("blocks submit with a validation error when the URL has no scheme", async () => {
    const fetchSpy = vi.fn(async () =>
      jsonResponse({ source: { name: "x" } }),
    ) as unknown as typeof fetch;
    globalThis.fetch = fetchSpy;

    render(
      <AllProviders>
        <AddSourceDialog open onOpenChange={() => {}} />
      </AllProviders>,
    );

    const nameInput = await screen.findByLabelText(/^Name$/);
    fireEvent.change(nameInput, { target: { value: "Acme AI" } });
    const urlInput = screen.getByLabelText(/^URL$/);
    fireEvent.change(urlInput, { target: { value: "example.com/feed" } });

    const submit = screen.getByRole("button", { name: /add source/i });
    fireEvent.click(submit);

    await waitFor(() => {
      expect(
        screen.getByText(/URL must start with http:\/\/ or https:\/\//i),
      ).toBeInTheDocument();
    });

    // No POST should have fired.
    expect(
      (fetchSpy as unknown as ReturnType<typeof vi.fn>).mock.calls.find(
        (call: unknown[]) => {
          const init = call[1] as RequestInit | undefined;
          return init?.method === "POST";
        },
      ),
    ).toBeUndefined();
  });
});
