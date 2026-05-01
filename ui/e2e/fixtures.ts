import type { Page, Route } from "@playwright/test";

/**
 * Shared mock fixtures + `page.route()` helpers for News Studio E2E tests.
 *
 * Every spec calls `mockApi(page, ...)` from a `beforeEach` hook so each
 * test is fully isolated from the live DB. The router responds with stable
 * canned shapes that match `app/admin/api.py`.
 */

export interface MockSource {
  name: string;
  source_type: string;
  url: string;
  trust_level?: string | null;
  source_tier?: string | null;
  category?: string | null;
  priority?: number | null;
  max_items?: number | null;
  enabled?: boolean;
  last_run?: string | null;
  item_count?: number | null;
}

export interface MockSection {
  id: string;
  section_order: number;
  title: string;
  fact_summary?: string;
  inference_summary?: string;
}

export interface MockReport {
  id: string;
  report_date: string;
  title: string;
  status: string;
  summary_ko?: string | null;
  stats_json?: Record<string, unknown> | null;
  created_at?: string;
  updated_at?: string;
  published_at?: string | null;
}

export interface MockApiOptions {
  /** Reports list returned by GET /api/reports. */
  reports?: MockReport[];
  /** Single-report detail returned by GET /api/reports/{date}. */
  reportDetail?: { sections: MockSection[]; title?: string; status?: string };
  /** Sources returned by GET /api/sources. */
  sources?: MockSource[];
  /** Static policy returned by GET /api/policy. */
  policy?: Record<string, unknown>;
  /**
   * If true, the /api/runs/{id}/stream SSE response immediately emits one
   * progress event then a `done` event. If false, SSE is skipped entirely.
   */
  emitDoneStream?: boolean;
}

/** A small fixture set of 37 mock sources, mirroring the prod yaml shape. */
export function defaultSources(): MockSource[] {
  const out: MockSource[] = [];
  const tiers = [
    "official",
    "mainstream",
    "developer_signal",
    "research",
    "community",
  ];
  for (let i = 0; i < 37; i++) {
    const tier = tiers[i % tiers.length];
    out.push({
      name: `source_${String(i + 1).padStart(2, "0")}`,
      source_type: "rss",
      url: `https://example.com/feed/${i + 1}`,
      trust_level: tier,
      source_tier: tier,
      category: "ai",
      priority: 1,
      max_items: 20,
      enabled: true,
      last_run: "2026-04-29T00:00:00Z",
      item_count: 12,
    });
  }
  return out;
}

/** Build a tiny valid HTML preview with `n` <article> elements. */
export function buildPreviewHtml(n: number): string {
  const articles = Array.from({ length: n })
    .map(
      (_, i) =>
        `<article data-testid="preview-article" data-section-index="${i}"><h2>Section ${i + 1}</h2></article>`,
    )
    .join("");
  return `<!doctype html><html><body><main>${articles}</main></body></html>`;
}

/** Default policy payload used for /api/policy mocks. */
export function defaultPolicy(targetSections = 10): Record<string, unknown> {
  return {
    source_tiers: {
      official: { boost: 18, eligible_for_main: true },
      mainstream: { boost: 12, eligible_for_main: true },
      research: { boost: 4, eligible_for_main: false },
      developer_signal: { boost: 14, eligible_for_main: true },
      community: { boost: -4, eligible_for_main: false },
      unknown: { boost: -18, eligible_for_main: false },
    },
    scoring_weights: {
      base_score: 50,
      source_tier: 1.0,
      official_source_boost: 10,
      mainstream_source_boost: 6,
      product_signal: 8,
      research_signal: 3,
      main_image_signal: 8,
      metrics_signal: 0.25,
      cluster_size_boost_per_item: 5,
      cluster_size_boost_max: 20,
    },
    penalties: {
      obscure_research_penalty: 22,
      arxiv_only_main_penalty: 100,
      community_penalty: 8,
      missing_url_penalty: 40,
      missing_title_penalty: 30,
    },
    quotas: { product: 4, tooling: 4, research: 1, industry: 1, policy: 1 },
    report_selection: {
      max_sections: 10,
      target_sections: targetSections,
      min_section_score: 35,
      max_arxiv_only_sections: 1,
      max_community_sections: 1,
      max_same_source_name: 2,
      prefer_mainstream_first: true,
      backfill_require_image: false,
    },
  };
}

export function makeSections(n: number): MockSection[] {
  return Array.from({ length: n }).map((_, i) => ({
    id: `sec-${i + 1}`,
    section_order: i,
    title: `Section ${i + 1} title`,
    fact_summary: `Fact summary for section ${i + 1}.`,
    inference_summary: `Implication for section ${i + 1}.`,
  }));
}

/**
 * Install API route mocks. The function returns a `state` object so tests
 * can inspect call counts (e.g. assert that POST /api/preview was sent).
 */
export async function mockApi(
  page: Page,
  options: MockApiOptions = {},
): Promise<{
  previewCalls: Array<Record<string, unknown>>;
  publishCalls: Array<Record<string, unknown>>;
  policyPuts: Array<Record<string, unknown>>;
  sourcePuts: Array<{ name: string; body: Record<string, unknown> }>;
}> {
  const reports = options.reports ?? [];
  const sources = options.sources ?? defaultSources();
  const policy = options.policy ?? defaultPolicy();
  const emitDoneStream = options.emitDoneStream ?? true;

  const previewCalls: Array<Record<string, unknown>> = [];
  const publishCalls: Array<Record<string, unknown>> = [];
  const policyPuts: Array<Record<string, unknown>> = [];
  const sourcePuts: Array<{ name: string; body: Record<string, unknown> }> = [];
  let latestRunId = "test-run-1";
  let runStarted = false;

  // GET /api/reports
  await page.route(/\/api\/reports(?:\?.*)?$/, async (route: Route) => {
    if (route.request().method() === "GET") {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ reports }),
      });
      return;
    }
    await route.continue();
  });

  // GET /api/reports/{date} or POST /api/reports/{date}/publish or reorder
  await page.route(/\/api\/reports\/[^/]+(\/(publish|reorder))?$/, async (route: Route) => {
    const url = new URL(route.request().url());
    const path = url.pathname;
    const method = route.request().method();
    const publishMatch = path.match(/\/api\/reports\/([^/]+)\/publish$/);
    const reorderMatch = path.match(/\/api\/reports\/([^/]+)\/reorder$/);
    const detailMatch = path.match(/\/api\/reports\/([^/]+)$/);

    if (publishMatch && method === "POST") {
      const date = decodeURIComponent(publishMatch[1]);
      let body: Record<string, unknown> = {};
      try {
        body = JSON.parse(route.request().postData() ?? "{}");
      } catch {
        /* ignore */
      }
      publishCalls.push({ date, ...body });
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({
          status: body.dry_run ? "dry-run" : "ok",
          deployed_url: `https://news-studio-mock.netlify.app/${date}/`,
          report_date: date,
          details: { dry_run: Boolean(body.dry_run) },
        }),
      });
      return;
    }

    if (reorderMatch && method === "POST") {
      const date = decodeURIComponent(reorderMatch[1]);
      const sections = options.reportDetail?.sections ?? [];
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ report_date: date, sections }),
      });
      return;
    }

    if (detailMatch && method === "GET") {
      const date = decodeURIComponent(detailMatch[1]);
      const sections = options.reportDetail?.sections ?? makeSections(3);
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({
          id: "report-mock",
          report_date: date,
          title: options.reportDetail?.title ?? `Daily report — ${date}`,
          status: options.reportDetail?.status ?? "ready",
          summary_ko: null,
          stats_json: null,
          method_json: null,
          created_at: "2026-04-30T00:00:00Z",
          updated_at: "2026-04-30T00:00:00Z",
          published_at: null,
          sections,
        }),
      });
      return;
    }

    await route.continue();
  });

  // POST /api/preview
  await page.route(/\/api\/preview$/, async (route: Route) => {
    if (route.request().method() !== "POST") {
      await route.continue();
      return;
    }
    let body: Record<string, unknown> = {};
    try {
      body = JSON.parse(route.request().postData() ?? "{}");
    } catch {
      /* ignore */
    }
    previewCalls.push(body);
    const target =
      typeof body.target_sections === "number" ? body.target_sections : 10;
    const html = buildPreviewHtml(target);
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({ html, length: html.length }),
    });
  });

  // GET/POST /api/runs (no /stream suffix)
  await page.route(/\/api\/runs$/, async (route: Route) => {
    const method = route.request().method();
    if (method === "GET") {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({
          runs: runStarted
            ? [
                {
                  run_id: latestRunId,
                  status: "running",
                  started_at: "2026-05-01T00:00:00Z",
                  options: {},
                  trackable: true,
                  source: "memory",
                },
              ]
            : [],
        }),
      });
      return;
    }
    if (method !== "POST") {
      await route.continue();
      return;
    }
    runStarted = true;
    latestRunId = "test-run-1";
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        run_id: latestRunId,
        status: "running",
        options: {},
      }),
    });
  });

  // GET /api/runs/{id} — activeRun preflight before SSE subscription.
  await page.route(/\/api\/runs\/[^/]+$/, async (route: Route) => {
    if (route.request().method() !== "GET") {
      await route.continue();
      return;
    }
    const url = new URL(route.request().url());
    const runId = decodeURIComponent(url.pathname.split("/").pop() ?? "");
    if (!runStarted || runId !== latestRunId) {
      await route.fulfill({
        status: 404,
        contentType: "application/json",
        body: JSON.stringify({ detail: `unknown run_id: ${runId}` }),
      });
      return;
    }
    await route.fulfill({
      status: 200,
      contentType: "application/json",
      body: JSON.stringify({
        run: {
          run_id: runId,
          status: "running",
          started_at: "2026-05-01T00:00:00Z",
          options: {},
          trackable: true,
          source: "memory",
        },
      }),
    });
  });

  // GET /api/runs/{id}/stream — lightweight SSE simulate.
  await page.route(/\/api\/runs\/[^/]+\/stream$/, async (route: Route) => {
    if (!emitDoneStream) {
      await route.continue();
      return;
    }
    // Two events: one progress, one done. EventSource will close on done.
    const body =
      "event: progress\n" +
      `data: {"step": "render", "progress": 0.95, "message": "rendering"}\n\n` +
      "event: done\n" +
      `data: {}\n\n`;
    await route.fulfill({
      status: 200,
      headers: {
        "content-type": "text/event-stream",
        "cache-control": "no-cache",
      },
      body,
    });
  });

  // GET /api/policy + PUT /api/policy
  await page.route(/\/api\/policy$/, async (route: Route) => {
    const method = route.request().method();
    if (method === "GET") {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ policy }),
      });
      return;
    }
    if (method === "PUT") {
      let body: Record<string, unknown> = {};
      try {
        body = JSON.parse(route.request().postData() ?? "{}");
      } catch {
        /* ignore */
      }
      policyPuts.push(body);
      const patch =
        body && typeof body === "object" && body.patch && typeof body.patch === "object"
          ? (body.patch as Record<string, unknown>)
          : {};
      const merged = { ...policy, ...patch };
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ policy: merged }),
      });
      return;
    }
    await route.continue();
  });

  // GET /api/sources, PUT /api/sources/{name}
  await page.route(/\/api\/sources(\/[^/]+)?$/, async (route: Route) => {
    const method = route.request().method();
    const url = new URL(route.request().url());
    const m = url.pathname.match(/\/api\/sources\/([^/]+)$/);
    if (m && method === "PUT") {
      const name = decodeURIComponent(m[1]);
      let body: Record<string, unknown> = {};
      try {
        body = JSON.parse(route.request().postData() ?? "{}");
      } catch {
        /* ignore */
      }
      sourcePuts.push({ name, body });
      const target = sources.find((s) => s.name === name);
      const updated = { ...(target ?? { name }), ...body };
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ source: updated }),
      });
      return;
    }
    if (method === "GET" && url.pathname === "/api/sources") {
      await route.fulfill({
        status: 200,
        contentType: "application/json",
        body: JSON.stringify({ sources }),
      });
      return;
    }
    await route.continue();
  });

  return { previewCalls, publishCalls, policyPuts, sourcePuts };
}

/** Clear cookies + localStorage so each test starts fresh. */
export async function resetClientState(page: Page): Promise<void> {
  await page.context().clearCookies();
  // localStorage clear must happen after a navigation so window exists.
  // Callers typically run this before navigating, so we wrap in a try.
  try {
    await page.evaluate(() => {
      try {
        window.localStorage.clear();
        window.sessionStorage.clear();
      } catch {
        /* ignore */
      }
    });
  } catch {
    /* page may not be on an HTTP origin yet */
  }
}
