import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import {
  fireEvent,
  render,
  screen,
  waitFor,
  within,
} from "@testing-library/react";
import { Sources } from "@/pages/Sources";
import { AllProviders } from "./test-utils";

const originalFetch = globalThis.fetch;

interface MockSource {
  name: string;
  source_type?: string;
  source_tier?: string;
  url?: string;
  enabled?: boolean;
}

/** Build 37 sources spread across 5 tiers (8/8/8/8/5). */
function build37(): MockSource[] {
  const tiers: { tier: string; count: number }[] = [
    { tier: "official", count: 8 },
    { tier: "mainstream", count: 8 },
    { tier: "developer_signal", count: 8 },
    { tier: "research", count: 8 },
    { tier: "community", count: 5 },
  ];
  const sources: MockSource[] = [];
  for (const t of tiers) {
    for (let i = 0; i < t.count; i++) {
      sources.push({
        name: `${t.tier}-${i}`,
        source_type: i % 2 === 0 ? "rss" : "website",
        source_tier: t.tier,
        url: `https://example.com/${t.tier}-${i}`,
        enabled: true,
      });
    }
  }
  return sources;
}

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

describe("Sources page (TC-5.1, TC-5.2)", () => {
  beforeEach(() => {
    document.documentElement.classList.add("dark");
  });

  it("renders 37 source rows in 5 tier groups (TC-5.1)", async () => {
    const sources = build37();
    expect(sources).toHaveLength(37);

    globalThis.fetch = vi
      .fn()
      .mockResolvedValue(jsonResponse({ sources })) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Sources />
      </AllProviders>,
    );

    await waitFor(() => {
      expect(screen.getByTestId("sources-groups")).toBeInTheDocument();
    });

    expect(screen.getByTestId("source-group-official")).toBeInTheDocument();
    expect(screen.getByTestId("source-group-mainstream")).toBeInTheDocument();
    expect(
      screen.getByTestId("source-group-developer_signal"),
    ).toBeInTheDocument();
    expect(screen.getByTestId("source-group-research")).toBeInTheDocument();
    expect(screen.getByTestId("source-group-community")).toBeInTheDocument();

    const headerCount = screen.getByText(/37 sources grouped by tier/i);
    expect(headerCount).toBeInTheDocument();

    const officialTable = screen.getByTestId("source-table-official");
    expect(within(officialTable).getAllByTestId(/source-row-/)).toHaveLength(8);
    const communityTable = screen.getByTestId("source-table-community");
    expect(within(communityTable).getAllByTestId(/source-row-/)).toHaveLength(
      5,
    );
  });

  it("toggles a source via PUT /api/sources/{name} with optimistic update (TC-5.2)", async () => {
    let serverEnabled = true;
    const calls: { url: string; init?: RequestInit }[] = [];
    globalThis.fetch = vi.fn(async (url: RequestInfo | URL, init?: RequestInit) => {
      const u = typeof url === "string" ? url : url.toString();
      calls.push({ url: u, init });
      if (u === "/api/sources" && (!init || !init.method || init.method === "GET")) {
        return jsonResponse({
          sources: [
            {
              name: "openai-blog",
              source_type: "rss",
              source_tier: "official",
              url: "https://openai.com/news/rss.xml",
              enabled: serverEnabled,
            },
          ],
        });
      }
      if (u === "/api/sources/openai-blog" && init?.method === "PUT") {
        const body = JSON.parse(String(init.body)) as { enabled?: boolean };
        if (typeof body.enabled === "boolean") serverEnabled = body.enabled;
        return jsonResponse({
          source: {
            name: "openai-blog",
            source_type: "rss",
            source_tier: "official",
            url: "https://openai.com/news/rss.xml",
            enabled: serverEnabled,
          },
        });
      }
      return new Response("nope", { status: 404 });
    }) as unknown as typeof fetch;

    render(
      <AllProviders>
        <Sources />
      </AllProviders>,
    );

    const toggle = await screen.findByTestId("source-toggle-openai-blog");
    expect(toggle).toBeChecked();

    fireEvent.click(toggle);

    // Optimistic update flips the checkbox immediately.
    await waitFor(() => {
      expect(
        screen.getByTestId("source-toggle-openai-blog"),
      ).not.toBeChecked();
    });

    await waitFor(() => {
      const put = calls.find((c) => c.init?.method === "PUT");
      expect(put).toBeDefined();
      expect(put!.url).toBe("/api/sources/openai-blog");
      expect(JSON.parse(String(put!.init!.body))).toEqual({ enabled: false });
    });
  });
});
