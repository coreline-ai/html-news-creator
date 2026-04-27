# 개발 문서 상세 검토 — 2026-04-27

대상 문서:

- `dev-plan/implement_20260427_221152.md` — AI Trend Report Engine 구현 계획
- `dev-plan/implement_20260427_215727.md` — multi-model-tui / Codex CLI / gpt-image-2 연동 계획
- `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md` — 통합 개발 참고 문서
- `docs/deep-research-report.md` — PRD/TRD 생성 보고서 스텁

검토 기준: 아키텍처 일관성, 구현 가능성, 범위 관리, 테스트 충분성, 보안/운영 리스크, 문서 참조 무결성.

## 결론

현재 문서들은 방향성은 좋지만, 바로 구현에 들어가기 전 반드시 정리해야 할 **차단급 문서 결함 5개**가 있다.

1. `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md`는 여러 파일을 한 문서에 붙인 상태인데, 구현 계획은 이를 실제 `.env.example`, `schema.sql`, `docker-compose.yml`, workflow 파일이 이미 존재하는 것처럼 가정한다.
2. `dev-plan/implement_20260427_221152.md`의 Phase 의존성이 논리적으로 충돌한다. Phase 2는 `verify_cluster(cluster)`를 요구하지만 cluster는 Phase 4에서 생성된다.
3. `dev-plan/implement_20260427_221152.md`의 dry-run 정책이 서로 모순된다. 어떤 곳은 DB write 없음, 어떤 곳은 `job_runs` 행 생성을 요구한다.
4. `dev-plan/implement_20260427_215727.md`는 현재 프로젝트 구조와 맞지 않는 `backend/src/ai/*` 경로를 사용한다. 기존 계획은 Python `app/` 패키지를 기준으로 한다.
5. `docs/deep-research-report.md`는 sandbox 다운로드 링크와 깨진 citation markup만 남아 있어 개발 참조 문서로 신뢰하기 어렵다.

권장 방향은 **문서 정규화 Phase를 먼저 추가**한 뒤, MVP를 `RSS-only → extract → classify → Jinja2 render`로 축소하여 한 번에 동작하는 vertical slice를 만드는 것이다.

## Step 0. Scope Challenge

### 이미 존재하는 것

| 하위 문제 | 이미 있는 문서/흐름 | 재사용 판단 |
|---|---|---|
| DB 스키마 | `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md` 내 `schema.sql` 블록 | 실제 `schema.sql`로 추출 필요 |
| 로컬 인프라 | 통합 문서 내 `docker-compose.yml` 블록 | 실제 파일로 추출 필요 |
| 일일 실행 workflow | 통합 문서 내 `github-actions-daily-report.yml` 블록 | `.github/workflows/daily-report.yml`로 추출 필요 |
| AI 파이프라인 | `dev-plan/implement_20260427_221152.md` | 의존성 순서 수정 필요 |
| OpenAI-compatible proxy | `dev-plan/implement_20260427_215727.md` | `app/` 구조에 맞춰 경로 수정 필요 |
| Codex 이미지 생성 | `dev-plan/implement_20260427_215727.md` Phase 6 | `gpt-image-2` 표준 결정은 적절 |

### 최소 변경으로 목표 달성하는 방법

1. 통합 문서에서 실제 파일을 먼저 추출한다.
2. Phase 2/4 의존성 충돌을 해소한다.
3. `app/ai/gateway_client.py` 또는 `app/clients/ai_gateway.py`로 AI Gateway 위치를 통일한다.
4. MVP는 RSS-only와 Jinja2 HTML 생성까지만 먼저 완성한다.
5. OCR, X/Twitter, 관리자 대시보드, 생성형 HTML은 후순위로 유지한다.

### 복잡도 판정

현재 주 구현 계획은 신규 파일 50개 이상, 외부 API 8개 이상, 배포/스토리지/OCR/LLM/관리자 API까지 포함한다. 전체 로드맵으로는 적절하지만, 첫 구현 단위로는 과대 범위다. 첫 PR/Phase는 8개 이하 파일을 목표로 축소하는 것이 안전하다.

## Architecture Review

### A1. Phase 의존성 충돌: Verification이 Cluster보다 먼저 정의됨

- 위치: `dev-plan/implement_20260427_221152.md:190-214`, `738-750`, `860-862`
- 문제: Phase 2는 `SourceVerifier.verify_cluster(cluster)`를 구현하라고 하지만, cluster 생성은 Phase 4다. 반면 파이프라인 순서는 `cluster → verify`로 되어 있어 문서 내부가 충돌한다.
- 영향: 구현자가 Phase 2에서 아직 존재하지 않는 `Cluster` 모델/데이터를 필요로 하게 된다.
- 권장 수정:
  - Phase 2를 `SourceTrustRegistry + item/source-level verification`으로 축소한다.
  - Phase 4에서 clustering 후 `ClusterVerifier`를 실행하도록 이동한다.
  - 파이프라인 순서는 `collect → extract → classify → embed → cluster → verify → generate`로 명확히 한다.

### A2. 통합 문서가 실제 파일처럼 취급됨

- 위치: `dev-plan/implement_20260427_221152.md:14-20`, `352`, `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md:7`, `2346`, `2388`, `2467`
- 문제: `.env.example`, `docker-compose.yml`, `schema.sql`, GitHub Actions가 실제 파일로 존재하는 것처럼 표현되어 있지만 실제 repo에는 통합 MD 안의 코드 블록만 있다.
- 영향: `make dev`, `psql -f schema.sql`, `npm ci`, Actions 실행이 바로 실패한다.
- 권장 수정: Phase 0 앞에 `Phase 0A: 문서 패키지 실제 파일 추출`을 추가한다.

### A3. multi-model-tui 연동 계획의 경로가 프로젝트 구조와 다름

- 위치: `dev-plan/implement_20260427_215727.md:199`, `428`
- 문제: 기존 엔진 계획은 Python `app/` 구조인데, 새 연동 계획은 `backend/src/ai/*`를 전제로 한다.
- 영향: 구현 시 AI Gateway 위치가 갈라지고 중복 abstraction이 생긴다.
- 권장 수정: `backend/src/ai/*`를 `app/ai/*` 또는 `app/clients/*`로 변경한다.

### A4. OpenAI-compatible 범위가 충분히 계층화되지 않음

- 위치: `dev-plan/implement_20260427_215727.md:53-60`, `285-314`, `435-440`
- 확인: `/tmp/multi_model_tui` 기준 build/test는 통과했지만, capabilities 상 hosted tools/citations/caching은 미지원 또는 unverified이며 structured output/state도 부분 검증 상태다.
- 영향: “OpenAI API 호환”을 너무 넓게 해석하면 SDK는 붙지만 고급 Responses 기능에서 실패할 수 있다.
- 권장 수정: 호환성 등급을 명시한다.
  - L0: health/model route
  - L1: non-stream text Responses
  - L2: stream SSE
  - L3: JSON schema
  - L4: tool call
  - L5: previous_response_id / files / hosted tools

### A5. 배포 대상이 문서마다 다름

- 위치: `dev-plan/implement_20260427_221152.md:45`, `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md:107`, `132`, `1083`, `1452-1453`
- 문제: 주 계획은 Vercel을 out of scope로 두지만 통합 문서는 Netlify/Vercel/GitHub Pages를 반복 언급한다.
- 권장 수정: MVP는 Netlify만, Vercel/GitHub Pages는 Appendix 또는 Phase 8 후보로 분리한다.

## Code Quality / 문서 품질 Review

### Q1. 참조 링크 깨짐

- 위치: `dev-plan/implement_20260427_215727.md:42`
- 문제: `../docs/impl-plan-ai-trend-report-engine.md`는 존재하지 않는다. 현재 대응 문서는 `dev-plan/implement_20260427_221152.md`다.
- 권장 수정: 링크를 `./implement_20260427_221152.md`로 변경한다.

### Q2. `docs/deep-research-report.md`는 개발 참조로 부적합

- 위치: `docs/deep-research-report.md:7-17`
- 문제: `sandbox:/mnt/data/...` 다운로드 링크와 `cite...` citation 토큰이 남아 있다.
- 영향: repo 외부 임시 파일을 참조하므로 재현성과 신뢰성이 없다.
- 권장 수정: 삭제하거나 실제 `PRD.md`, `TRD.md`를 repo에 추가하고 이 문서는 색인으로만 유지한다.

### Q3. DB 테이블명이 문서 내에서 불일치

- 위치: `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md:192-193`, `210`, `520`
- 문제: 다이어그램/백로그는 `raw_sources`, `source_media`, `source_verifications`를 쓰지만 실제 schema는 `raw_items`, `media_assets`, `verifications`다.
- 권장 수정: 모든 명칭을 schema 기준으로 통일한다.

### Q4. dry-run 의미가 충돌

- 위치: `dev-plan/implement_20260427_221152.md:634`, `637`, `651`, `1210`
- 문제: `--dry-run`은 DB write 없음이라고 하면서, success criteria/test는 `job_runs.status="completed"` 생성을 요구한다.
- 권장 수정: dry-run도 `job_runs`/`job_logs`만 기록하고 domain table write와 파일 생성은 하지 않는 정책으로 명시한다.

### Q5. report status 전이가 충돌

- 위치: `dev-plan/implement_20260427_221152.md:907`, `919`, `927-928`, `1163`
- 문제: assemble은 `draft`, high severity는 `review`, high 없음은 `review→published`, publish API는 `draft→published`로 서로 다르다.
- 권장 수정: 상태 전이를 다음처럼 고정한다.

```text
draft -> review_required -> approved -> published
      -> failed
      -> archived
```

MVP에서는 `publish=true`일 때만 `published`로 전환한다.

### Q6. Node/npm 전략이 없음

- 위치: `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md:2094`, `2427`, `dev-plan/implement_20260427_221152.md:1083-1088`
- 문제: repo에는 `package.json`이 없는데 문서는 `npm install`, `npm ci`, `npx netlify`를 요구한다.
- 권장 수정: 둘 중 하나를 선택한다.
  - Python Playwright만 사용할 경우 `npm ci` 제거, Netlify는 `npx --yes netlify-cli`로 실행.
  - Node 툴을 고정하려면 `package.json`과 lockfile 추가.

## Test Review

### 신규 데이터 흐름 / 테스트 매핑

```text
[Sources]
  -> collect
     tests: RSS/GitHub/arXiv mock, timeout, rate-limit
  -> extract
     tests: Firecrawl failover, SSRF, low quality, manual queue
  -> classify/entities
     tests: JSON schema, malformed LLM, score threshold
  -> embed/cluster
     tests: empty input, small N, noise, deterministic seed
  -> verify
     tests: item-level source trust, cluster-level evidence, unverified fallback
  -> generate report
     tests: fact/social/inference separation, factcheck high severity
  -> render/sanitize
     tests: XSS, javascript URL, class allowlist, fallback renderer
  -> publish
     tests: artifact existence, deploy failure, rollback path
```

### 테스트 갭

1. LLM eval이 부족하다. mock 응답 테스트만으로는 “출처 없는 fact 금지”를 보장하기 어렵다.
2. SSRF 테스트가 `169.254.169.254` 단일 케이스에 치우쳐 있다. IPv6, DNS rebinding, redirect, encoded IP, localhost alias가 필요하다.
3. dry-run 테스트 정책이 모순되어 있다.
4. visual regression은 threshold만 있고 baseline lifecycle이 없다.
5. `multi-model-tui` 연동은 SDK smoke test는 있으나 capability별 negative test가 부족하다.
6. 이미지 생성은 최소 1개 sample smoke가 있지만 이미지 파일 크기/비율/참조 경로 검증이 빠져 있다.

## Performance / 운영 Review

### P1. full pipeline 60분 목표와 GitHub Actions 90분 제한은 여유가 작음

- 위치: `dev-plan/implement_20260427_221152.md:1205`, `1244`
- 문제: OCR, Playwright, LLM 검증, embedding이 모두 들어오면 60분 목표가 흔들릴 수 있다.
- 권장 수정: 일일 실행은 source count, image count, LLM call budget을 환경변수로 강제한다.

### P2. Redis queue 역할이 불명확

- 위치: `dev-plan/implement_20260427_221152.md:109`, `522`, `647`
- 문제: Redis가 cache/rate-limit/manual_queue/job 상태를 모두 담당하지만 TTL/키 구조/장애 시 동작이 없다.
- 권장 수정: Redis key namespace와 TTL 정책을 문서화한다.

### P3. OpenAI 비용 통제가 부족함

- 위치: `dev-plan/implement_20260427_221152.md:1237`, `1264`
- 문제: mock 우선 원칙은 좋지만 실제 daily run의 max LLM calls, max tokens, retry budget이 없다.
- 권장 수정: `MAX_LLM_CALLS_PER_RUN`, `MAX_LLM_COST_USD_PER_RUN`, `LLM_TIMEOUT_MS`를 추가한다.

## Security Review

### S1. SSRF 방어가 부족함

현재 문서는 private CIDR 차단을 언급하지만, 실제 구현 기준은 더 구체적이어야 한다.

필수 보완:

- DNS resolve 후 private/link-local/loopback/multicast 차단
- redirect마다 재검증
- IPv6 `::1`, `fc00::/7`, `fe80::/10` 차단
- integer/hex/octal IP 표현 차단
- content-length와 streaming body size 제한
- image download도 동일 정책 적용

### S2. 관리자 API 인증 스펙이 미정

- 위치: `docs/AI_Trend_Report_Engine_Additional_Dev_Docs_COMBINED.md:809`, `dev-plan/implement_20260427_221152.md:1190`
- 문제: admin token/Supabase Auth를 언급하지만 실제 auth scheme, header, env var가 없다.
- 권장 수정: MVP는 `ADMIN_API_TOKEN` + `Authorization: Bearer`로 단순화하고, Supabase Auth는 후순위로 둔다.

### S3. HTML sanitizer class allowlist가 실제 코드 수준으로 명시되지 않음

- 위치: `dev-plan/implement_20260427_221152.md:953-973`
- 문제: `* : ["class"]`는 모든 class를 허용한다. 주석의 “allowlist class만 허용”과 구현 초안이 다르다.
- 권장 수정: allowed class prefix 또는 exact allowlist를 별도 상수로 둔다.

## NOT in scope 권장

- X/Twitter 수집: 약관/비용/품질 리스크가 크므로 MVP 이후.
- 관리자 대시보드 UI: backend pipeline 동작 전에는 과함.
- 생성형 HTML 전체 레이아웃: Jinja2 안정화 후 섹션 단위 opt-in.
- OCR/비전 전체 도입: 이미지가 리포트 품질에 실제로 기여하는지 확인 후.
- Vercel/GitHub Pages 동시 지원: Netlify 하나로 고정.
- native transparent image fallback: `gpt-image-2` 기준 chroma-key 후처리만 유지.

## 우선순위별 수정 권고

### P0 — 구현 전 반드시 수정

1. 통합 문서의 내장 파일들을 실제 파일로 추출하는 Phase 0A 추가.
2. Phase 2/4 검증·클러스터링 순서 재설계.
3. dry-run 정책 통일.
4. report status state machine 통일.
5. `backend/src/ai/*` 경로를 `app/ai/*` 또는 `app/clients/*`로 수정.
6. 깨진 참조 링크와 `deep-research-report.md` 정리.

### P1 — 첫 구현과 함께 수정

1. SSRF 상세 방어 기준 추가.
2. Admin auth scheme 확정.
3. LLM output JSON schema와 eval 케이스 추가.
4. Node/npm 전략 확정.
5. Redis key/TTL 정책 추가.

### P2 — MVP 이후

1. OCR/비전 batch budget.
2. X/Twitter policy review.
3. 생성형 HTML visual regression baseline 관리.
4. multi-model-tui advanced capabilities matrix.

## 권장 다음 액션

가장 좋은 다음 단계는 리뷰 결과를 반영해 기존 계획을 바로 고치는 것이다.

권장 수정 순서:

1. `dev-plan/implement_20260427_221152.md`에 `Phase 0A: 문서 파일 추출` 추가.
2. Phase 2를 `source trust registry`로 축소하고, cluster verification을 Phase 4 이후로 이동.
3. `dev-plan/implement_20260427_215727.md`의 참조 링크와 `backend/src/ai/*` 경로 수정.
4. `docs/deep-research-report.md`를 삭제 또는 실제 PRD/TRD 색인으로 교체.
5. dry-run/report status 정책을 표로 고정.

## 검증 메모

- `/tmp/multi_model_tui`에서 `npm install`, `npm run build`, `npm test`를 실행했다.
- 결과: build 성공, test 39개 통과.
- 참고: `npm install` 결과 external dependency audit에서 moderate 1건, high 1건이 보고되었다. 프로젝트에 vendoring하지 않는 한 즉시 차단 요소는 아니지만, vendoring/submodule 도입 시 별도 검토가 필요하다.
