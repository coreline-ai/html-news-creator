# Implementation Plan: News Studio 웹앱

> 매일 생성되는 AI 트렌드 리포트를 운영자가 웹에서 직접 생성·튜닝·검토·발행할 수 있는 단일 사용자 도구.
> Generated: 2026-04-30
> Project: html-news-creator

---

## 1. Context (배경)

### 1.1 Why (왜 필요한가)
- 운영자는 현재 `scripts/run_daily.py` CLI로만 파이프라인을 다루고, 옵션은 `data/editorial_policy.yaml` 수정 후 재실행해야 반영된다.
- 옵션과 결과의 인과 관계가 한 화면에 보이지 않아, 작은 정책 변화에도 빌드를 새로 돌려 HTML을 열어 비교해야 한다.
- 운영 빈도가 늘면서 "특정 날짜 재생성", "섹션 1개 교체", "소스 일시 끄기" 같은 손작업이 잦다.

### 1.2 Current State (현재 상태)
- 백엔드 FastAPI 골격: `app/admin/` 디렉토리만 존재 (최소 헬스체크 수준).
- 디자인 시스템: `docs/design/` 완비 (shadcn/ui new-york, OKLCH 모노크롬, light/dark, `tokens.css`).
- 데이터 모델: 14개 테이블 (`Source`, `RawItem`, `Cluster`, `Report`, `ReportSection`, …).
- 파이프라인 진입점: `scripts/run_daily.py` (Click CLI, 9 단계).

### 1.3 Target State (목표 상태)
- `ui/` 디렉토리에 React 19 + Vite + TypeScript + shadcn/ui 기반 SPA.
- 4 화면: 대시보드 · 신규 생성 · 검토 · 설정.
- 라이브 미리보기 우선, 섹션 단위 검토 모드 전환 가능.
- **다크 테마 기본**, 라이트 토글, 아이콘 매핑 변경 가능 (`SIDEBAR_NAV_ICONS` 상수 1군데).
- FastAPI 측 `/api/*` 엔드포인트 8개 신규.
- 인증 없음 (개인용, 로컬 또는 신뢰 네트워크).
- 현재 정적 HTML 리포트(`templates/report_newsstream.html.j2`)는 자동 변경 대상 아님.

### 1.4 Scope Boundary (범위)
- **In scope**: 4 화면 SPA · API 확장 · SSE 진행률 · 라이브/섹션 미리보기 · Netlify 발행 트리거 · 기본 다크 + 라이트 + 아이콘 교체.
- **Out of scope**: 다중 사용자 인증·권한 · 모바일 우선 최적화(반응형 기본만) · LLM 모델 직접 변경 UI · 신규 소스 타입(rss/github/arxiv/website 외) 추가 · 정적 HTML 리포트 자체 마이그레이션.

---

## 2. Architecture Overview (아키텍처)

### 2.1 Design Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                        Browser (localhost:5173)                    │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  ui/  React SPA  (Vite dev → static build)                   │  │
│  │   ├── pages/Dashboard, NewReport, ReviewReport, Sources       │  │
│  │   ├── lib/api.ts  (TanStack Query)                            │  │
│  │   └── components/ui/  (shadcn new-york)                       │  │
│  └─────────────────┬──────────────────────────┬─────────────────┘  │
└─────────────────────┼──────────────────────────┼────────────────────┘
                      │ JSON / SSE              │ iframe srcdoc
                      ▼                          ▼
┌────────────────────────────────────────────────────────────────────┐
│               FastAPI  (app/admin/api.py 확장)                      │
│   /api/reports         /api/runs (POST + SSE stream)               │
│   /api/preview         /api/policy                                 │
│   /api/sources         /api/sections/{id}                          │
└─────────────────────┬──────────────────────────┬───────────────────┘
                      │                          │
                      ▼                          ▼
            scripts/run_daily.py         app/rendering/jinja_renderer.py
            (subprocess / asyncio)       (in-process render with overrides)
                      │                          │
                      ▼                          ▼
                PostgreSQL                 templates/report_newsstream.html.j2
```

### 2.2 Key Design Decisions

| 결정 사항 | 선택 | 근거 |
|---|---|---|
| 프런트 위치 | `ui/` 별도 디렉토리 | 백엔드와 분리, 정적 빌드 산출물만 배포 |
| 빌드 도구 | Vite 6 + TS 5.7 | React 19 호환 + 빠른 HMR |
| UI | shadcn/ui new-york + Tailwind v4 | `docs/design/` 시스템과 100% 정합 |
| 상태 | TanStack Query + Zustand | 서버 상태 / 로컬 옵션 상태 분리 |
| 라이브 미리보기 | iframe + `srcdoc` | 보안·격리 + 옵션 변경 시 디바운스 재렌더 |
| 진행률 | SSE | 단방향 push, FastAPI 표준 지원 |
| 실행 트리거 | FastAPI → asyncio subprocess | 기존 `run_daily.py` 그대로 호출 |
| 기본 테마 | dark (사용자 요청) | `<html class="dark">` 초기값 |
| 아이콘 | `lucide-react` + 매핑 상수 | `SIDEBAR_NAV_ICONS` 한 곳에서 변경 |
| 인증 | 없음 | 개인용 / 로컬 |

### 2.3 New Files (신규 파일)

| 파일 경로 | 용도 |
|---|---|
| `ui/package.json` | npm 의존성 + 스크립트 |
| `ui/vite.config.ts` | Vite 설정 + `/api` 프록시 |
| `ui/tsconfig.json` | TypeScript 설정 |
| `ui/components.json` | shadcn/ui 설정 (new-york, neutral) |
| `ui/index.html` | 진입점 |
| `ui/src/main.tsx` | React entry |
| `ui/src/App.tsx` | 라우팅 + 셸 |
| `ui/src/index.css` | tokens.css import + Tailwind |
| `ui/src/lib/api.ts` | API 호출 hooks |
| `ui/src/lib/utils.ts` | `cn()` 헬퍼 |
| `ui/src/lib/store.ts` | Zustand: 옵션·테마·아이콘 매핑 |
| `ui/src/lib/icons.ts` | `SIDEBAR_NAV_ICONS` 매핑 + lucide re-export |
| `ui/src/components/Sidebar.tsx` | 좌측 사이드바 |
| `ui/src/components/HeaderBar.tsx` | 상단 브레드크럼 + 액션 |
| `ui/src/components/RunOptionsPanel.tsx` | 5그룹 옵션 컨트롤 |
| `ui/src/components/LivePreview.tsx` | iframe 미리보기 (디바운스) |
| `ui/src/components/SectionList.tsx` | dnd-kit 섹션 리스트 |
| `ui/src/components/SectionEditor.tsx` | 섹션 단위 편집 폼 |
| `ui/src/components/ThemeToggle.tsx` | 다크/라이트 토글 |
| `ui/src/components/ui/*` | shadcn primitives (button, card, input, …) |
| `ui/src/pages/Dashboard.tsx` | Screen 1 |
| `ui/src/pages/NewReport.tsx` | Screen 2 |
| `ui/src/pages/ReviewReport.tsx` | Screen 3 |
| `ui/src/pages/Sources.tsx` | Screen 4 |
| `ui/src/hooks/useReports.ts` | 리포트 목록·상세 |
| `ui/src/hooks/useRunStream.ts` | SSE 진행률 |
| `ui/src/hooks/usePreview.ts` | 미리보기 HTML fetch (debounce) |
| `app/admin/api.py` | (확장) `/api/*` 신규 8 엔드포인트 |
| `app/admin/preview.py` | 옵션 오버라이드로 인메모리 렌더 |
| `app/admin/run_runner.py` | asyncio 기반 백그라운드 러너 |
| `app/admin/sse.py` | EventSourceResponse 헬퍼 |
| `tests/unit/test_admin_api.py` | API 단위 테스트 |
| `tests/unit/test_preview_renderer.py` | 인메모리 렌더 테스트 |
| `ui/src/__tests__/RunOptionsPanel.test.tsx` | vitest 컴포넌트 테스트 |

### 2.4 Modified Files (수정 파일)

| 파일 경로 | 변경 내용 |
|---|---|
| `app/admin/__init__.py` | router include 추가 |
| `app/config.py` | `ui_dist_path`, `ui_dev_origin` 설정 추가 |
| `requirements.txt` | `sse-starlette` 추가 |
| `Makefile` | `ui-dev`, `ui-build`, `serve` 타겟 추가 |
| `.gitignore` | `ui/node_modules`, `ui/dist` 무시 |

---

## 3. Phase Dependencies (페이즈 의존성)

```
Phase 0 (Foundation)
    │
    ├──► Phase 1 (Backend API)        ◄┐
    │                                  │
    ├──► Phase 2 (Shell + Dashboard) ──┤   ← API 응답 필요
    │                                  │
    ├──► Phase 3 (NewReport)        ───┤   ← Preview/Run API 필요
    │                                  │
    ├──► Phase 4 (Review)           ───┤   ← Section API 필요
    │                                  │
    └──► Phase 5 (Sources & Policy) ───┘   ← Policy/Sources API 필요

Phase 6 (Polish) ─ 모든 페이즈 후
```

Phase 1은 다른 모든 UI 페이즈의 데이터 의존성. Phase 2는 셸이므로 3·4·5의 부모. **2 → 3·4·5는 병렬 가능** (서로 다른 라우트).

---

## 4. Implementation Phases (구현 페이즈)

### Phase 0: Foundation Setup (기반 설정)
> 모든 페이즈의 전제 조건 — 빌드·디자인 토큰·라우팅 골격
> Dependencies: 없음

#### Tasks
- [x] [ui/package.json](ui/package.json) 생성: `react@19`, `react-dom@19`, `react-router-dom@7`, `@tanstack/react-query@5`, `zustand@5`, `lucide-react`, `clsx`, `tailwind-merge`, `class-variance-authority`, devDeps `vite@6`, `typescript@5.7`, `@vitejs/plugin-react`, `tailwindcss@4`, `@tailwindcss/vite`, `vitest`, `@testing-library/react`
- [x] [ui/vite.config.ts](ui/vite.config.ts): React 플러그인 + `@tailwindcss/vite` + `/api` → `http://localhost:8000` 프록시
- [x] [ui/tsconfig.json](ui/tsconfig.json), [ui/index.html](ui/index.html), [ui/src/main.tsx](ui/src/main.tsx), [ui/src/App.tsx](ui/src/App.tsx) 골격
- [x] [ui/src/index.css](ui/src/index.css): `@import "tailwindcss"` + `@import "../../docs/design/tokens.css"` + `<html class="dark">` 초기화 스크립트
- [x] [ui/components.json](ui/components.json): `style: new-york`, `baseColor: neutral`, `cssVariables: true`
- [x] shadcn 기본 12개 설치: `button card input label badge dialog dropdown-menu tabs separator scroll-area tooltip skeleton`
- [x] [Makefile](Makefile)에 `ui-dev`, `ui-build`, `ui-test` 타겟 추가

#### Success Criteria
- `cd ui && npm install && npm run dev` → 빈 페이지가 `localhost:5173`에서 다크 배경으로 렌더링
- `npm run typecheck` → 0 에러
- shadcn `<Button>`이 `tokens.css`의 `--primary`를 사용한다 (devtools에서 `oklch(0.985 0 0)` 다크 primary 확인)

#### Test Cases
- [x] TC-0.1: dev 서버 부팅 시 콘솔 에러 0건
- [x] TC-0.2: `<html>` 요소에 `class="dark"`가 기본 적용됨
- [x] TC-0.3: `<Button>` 렌더 시 background에 `--primary` 토큰이 적용됨
- [x] TC-0.E1: 잘못된 토큰 변수(`var(--unknown)`) 사용 시 fallback 색이 적용되어도 빌드는 통과

#### Testing Instructions
```bash
cd ui
npm install
npm run dev &        # http://localhost:5173
npm run typecheck
```

---

### Phase 1: Backend API (FastAPI 확장)
> 4 화면이 사용할 8개 엔드포인트
> Dependencies: 없음 (Phase 0과 병렬 가능)

#### Tasks
- [x] [app/admin/api.py](app/admin/api.py): `GET /api/reports?limit=20`, `GET /api/reports/{date_kst}` 구현 (DB의 `Report` + `ReportSection` 조회)
- [x] [app/admin/preview.py](app/admin/preview.py): `render_preview(options: dict) -> str` — `app/editorial/policy.py`에 옵션 오버라이드 주입 후 `app/rendering/jinja_renderer.render_report()` 호출, **DB 쓰기 없이** 렌더 결과 HTML 반환
- [x] [app/admin/api.py](app/admin/api.py): `POST /api/preview` — 위 함수 노출 (debounce는 클라이언트 책임)
- [x] [app/admin/run_runner.py](app/admin/run_runner.py): `start_run(options) -> run_id` (asyncio.create_subprocess_exec로 `scripts/run_daily.py` 호출, stdout 라인을 큐에 push)
- [x] [app/admin/sse.py](app/admin/sse.py): `stream_run(run_id) -> EventSourceResponse` — `sse-starlette` 사용, 단계별 progress event 전송
- [x] [app/admin/api.py](app/admin/api.py): `GET /api/policy` (현재 yaml 반환), `PUT /api/policy` (런타임 오버라이드 저장 — 재시작 시 휘발)
- [x] [app/admin/api.py](app/admin/api.py): `GET /api/sources`, `PUT /api/sources/{name}` (enable/disable 토글, yaml에 즉시 반영)

#### Success Criteria
- `curl http://localhost:8000/api/reports` → JSON 배열 반환, 200
- `curl -X POST http://localhost:8000/api/preview -d '{"target_sections":5}'` → HTML 문자열 반환 (5 섹션)
- `curl http://localhost:8000/api/runs/{id}/stream` → `data: {"step":"collect","progress":0.1}` 형태 SSE 라인 흐름
- DB에 새 레코드 생성 0 (preview는 read-only)

#### Test Cases
- [x] TC-1.1: `GET /api/reports` 빈 DB → `{"reports": []}` 반환
- [x] TC-1.2: `GET /api/reports/2026-04-30` 존재 시 14개 필드 (status, sections, generated_at 포함)
- [x] TC-1.3: `POST /api/preview {"target_sections":5}` → HTML에 `<article class="report-section">` 5개 포함
- [x] TC-1.4: `POST /api/runs` → 200 + `run_id` 반환, 백그라운드 프로세스 시작됨
- [x] TC-1.5: SSE stream → 9개 step 이벤트 모두 도착 + `done` 이벤트로 종료
- [x] TC-1.6: `PUT /api/sources/openai-blog {"enabled":false}` → `data/sources_registry.yaml` 갱신 + 200
- [x] TC-1.E1: 존재하지 않는 날짜 `GET /api/reports/2099-01-01` → 404
- [x] TC-1.E2: 잘못된 옵션 `POST /api/preview {"target_sections":-5}` → 400 + 메시지

#### Testing Instructions
```bash
PYTHONPATH=. uv run pytest tests/unit/test_admin_api.py tests/unit/test_preview_renderer.py -v --tb=short
PYTHONPATH=. uv run uvicorn app.admin.api:app --reload --port 8000 &
curl -s http://localhost:8000/api/reports | jq .
```

**테스트 실패 시 워크플로우:**
1. 에러 출력 분석 → 근본 원인 식별
2. 원인 수정 → 재테스트
3. **모든 테스트가 통과할 때까지 다음 Phase 진행 금지**

---

### Phase 2: Shell + Dashboard (Screen 1)
> 모든 화면이 공유하는 셸 + 첫 화면
> Dependencies: Phase 0 (UI 골격), Phase 1 (`/api/reports`)

#### Tasks
- [x] [ui/src/lib/icons.ts](ui/src/lib/icons.ts): `SIDEBAR_NAV_ICONS = { home: Home, reports: FileText, sources: Database, policy: SlidersHorizontal, schedule: Calendar }` — **사용자가 변경할 단일 지점**
- [x] [ui/src/components/Sidebar.tsx](ui/src/components/Sidebar.tsx): 240px 고정폭, `--sidebar-*` 토큰 사용, NavLink 5개 + 최근 실행 5건 + 하단 설정 버튼
- [x] [ui/src/components/HeaderBar.tsx](ui/src/components/HeaderBar.tsx): 48px, 좌측 브레드크럼 / 우측 ⌘K · ThemeToggle · 계정 아이콘
- [x] [ui/src/components/ThemeToggle.tsx](ui/src/components/ThemeToggle.tsx): `localStorage('theme')` + `documentElement.classList.toggle('dark')`, 기본 dark
- [x] [ui/src/lib/api.ts](ui/src/lib/api.ts) + [ui/src/hooks/useReports.ts](ui/src/hooks/useReports.ts): `useReports()`, `useReport(date)` TanStack Query hooks
- [x] [ui/src/pages/Dashboard.tsx](ui/src/pages/Dashboard.tsx): "오늘" 카드 + Quick actions 3개 카드 + 최근 실행 테이블

#### Success Criteria
- `localhost:5173/` → 다크 테마, 사이드바 + 헤더 + 콘텐츠 영역 정확히 240/48/나머지 그리드
- 사이드바 항목 5개가 lucide 아이콘과 함께 표시
- 최근 실행 행을 클릭하면 `/reports/:date` 라우트로 이동
- Theme toggle 누르면 `<html>`에서 `dark` 클래스 토글, localStorage에 저장

#### Test Cases
- [x] TC-2.1: 초기 로드 시 다크 테마 활성 (background `oklch(0.145 0 0)`)
- [x] TC-2.2: 사이드바 NavLink가 현재 경로일 때 `--sidebar-primary` 배경
- [x] TC-2.3: 최근 실행 행 클릭 → `/reports/2026-04-30`로 이동
- [x] TC-2.4: Theme toggle 클릭 → `dark` 클래스 제거 + localStorage `theme=light`
- [x] TC-2.E1: API 에러 시 dashboard에 EmptyState 또는 에러 카드 표시 (백지화 금지)

#### Testing Instructions
```bash
cd ui && npm run test -- src/__tests__/Sidebar.test.tsx src/__tests__/Dashboard.test.tsx
cd ui && npm run dev   # 시각 확인
```

---

### Phase 3: NewReport — 라이브 미리보기 (Screen 2)
> 옵션 패널 + iframe 미리보기 + Run 트리거
> Dependencies: Phase 2 (셸), Phase 1 (`/api/preview`, `/api/runs`)

#### Tasks
- [x] [ui/src/lib/store.ts](ui/src/lib/store.ts): Zustand store — `runOptions`, `setOption(key, value)`, `previewMode: 'live' | 'section'`
- [x] [ui/src/components/RunOptionsPanel.tsx](ui/src/components/RunOptionsPanel.tsx): Accordion 5그룹 (A 실행 / B 편집 / C 소스 / D 출력 / E 발행), 각 그룹에 옵션 컨트롤 + tooltip으로 `editorial_policy.yaml` 디폴트 표시
- [x] [ui/src/hooks/usePreview.ts](ui/src/hooks/usePreview.ts): `runOptions` 변경 → 2초 디바운스 → `POST /api/preview` → HTML 반환
- [x] [ui/src/components/LivePreview.tsx](ui/src/components/LivePreview.tsx): iframe `srcdoc=html` + 우상단 `[💻][📱][🌙]` 뷰포트/테마 토글
- [x] [ui/src/hooks/useRunStream.ts](ui/src/hooks/useRunStream.ts): EventSource로 SSE 구독, step별 진행률 state
- [x] [ui/src/pages/NewReport.tsx](ui/src/pages/NewReport.tsx): 좌(40%) RunOptionsPanel / 우(60%) LivePreview, 하단 sticky `[Save draft] [Run]` 액션바
- [x] [Run] 클릭 시: 옵션을 `POST /api/runs`로 전송, 진행률 토스트, 완료 시 `ReviewReport` 페이지로 이동

#### Success Criteria
- 슬라이더 변경 → 2초 후 iframe이 새 HTML로 갱신 (네트워크 1회)
- Run 클릭 → 9개 단계 progress 이벤트가 화면 하단 토스트에 표시
- 완료 후 `/reports/{new_date}` 자동 이동
- 옵션 패널 5그룹 모두 펼쳤을 때 28개 컨트롤 표시 (Section 1 옵션 카탈로그 기준)

#### Test Cases
- [x] TC-3.1: 옵션 패널이 5개 Accordion 그룹을 렌더 (A~E)
- [x] TC-3.2: `target_sections` 슬라이더 5→8 변경 → 2초 후 iframe 내 `<article class="report-section">` 8개
- [x] TC-3.3: Run 클릭 → 9 progress 이벤트 수신, 마지막 `done` 이벤트 후 redirect
- [x] TC-3.4: 미리보기 뷰포트 토글 `📱` → iframe 폭 `375px`로 축소
- [x] TC-3.5: dry-run 토글 ON 상태에서 Run → API 응답에 `dry_run: true` 포함
- [x] TC-3.E1: API 500 시 에러 토스트 표시 + Run 버튼 다시 활성화
- [x] TC-3.E2: 디바운스 중 두 번째 변경 → 첫 요청 abort, 두 번째만 수행

#### Testing Instructions
```bash
cd ui && npm run test -- src/__tests__/RunOptionsPanel.test.tsx src/__tests__/LivePreview.test.tsx
cd ui && npm run dev   # 시각 확인 + 옵션 변경 → preview 갱신
```

---

### Phase 4: Review — 섹션 단위 검토 (Screen 3)
> 생성 완료된 리포트의 섹션 reorder · edit · 발행
> Dependencies: Phase 2 (셸), Phase 1 (`/api/reports/{date}`, `/api/sections/{id}`)

#### Tasks
- [x] [app/admin/api.py](app/admin/api.py) 추가: `PATCH /api/sections/{id}` (title/summary/implication 수정), `POST /api/sections/{id}/regenerate`, `POST /api/reports/{date}/reorder`, `POST /api/reports/{date}/publish`
- [x] [ui/src/components/SectionList.tsx](ui/src/components/SectionList.tsx): `@dnd-kit/sortable`로 행 드래그, 행 좌측 핸들, 우측 on/off 토글, 클릭 시 SectionEditor 활성
- [x] [ui/src/components/SectionEditor.tsx](ui/src/components/SectionEditor.tsx): 제목/이미지/요약/시사점 폼 + `[Regenerate] [Manual edit]` 버튼
- [x] [ui/src/pages/ReviewReport.tsx](ui/src/pages/ReviewReport.tsx): 좌(40%) SectionList / 우(60%) SectionEditor or LivePreview (모드 토글)
- [x] 미리보기 모드 토글: `live` 모드는 Phase 3와 동일 iframe / `section` 모드는 SectionEditor 폼 — store의 `previewMode`로 제어
- [x] [Publish] 버튼: 확인 다이얼로그 → `POST /api/reports/{date}/publish` (Netlify 배포 트리거) → URL 복사
- [x] 비활성화된 섹션(off)은 hatch 패턴으로 표시, 발행 시 자동 제외

#### Success Criteria
- 섹션 드래그로 순서 변경 → `reorder` API 호출 → 응답 후 미리보기 자동 갱신
- 섹션 off 토글 → 즉시 미리보기에서 사라짐
- Regenerate 클릭 → 단일 섹션만 LLM 재생성, 화면 갱신
- Publish 성공 → "https://ai-news-5min-kr.netlify.app/2026-04-30-trend.html" 복사 가능

#### Test Cases
- [x] TC-4.1: SectionList 드래그 → onDragEnd 핸들러가 reorder API 호출
- [x] TC-4.2: 섹션 off 토글 → SectionList state + 미리보기에서 해당 섹션 제거
- [x] TC-4.3: SectionEditor에서 제목 변경 후 Save → PATCH 호출 + 미리보기 갱신
- [x] TC-4.4: previewMode 토글 'live' ↔ 'section' → 우측 컴포넌트 전환
- [x] TC-4.5: Publish 다이얼로그 → 확인 후 API 호출 + 토스트로 URL 표시
- [x] TC-4.E1: 단일 섹션 regenerate 도중 에러 → 다른 섹션 영향 없음, 해당 섹션만 에러 상태

#### Testing Instructions
```bash
cd ui && npm run test -- src/__tests__/SectionList.test.tsx src/__tests__/SectionEditor.test.tsx
PYTHONPATH=. uv run pytest tests/unit/test_admin_api.py::test_section_patch -v
```

---

### Phase 5: Sources & Policy (Screen 4)
> 37개 소스 관리 + 정책 폼
> Dependencies: Phase 2 (셸), Phase 1 (`/api/sources`, `/api/policy`)

#### Tasks
- [x] [ui/src/pages/Sources.tsx](ui/src/pages/Sources.tsx): 등급별 5개 그룹 헤더 + 행 (이름·tier·type·last_run·item_count·toggle·...)
- [x] [ui/src/components/AddSourceDialog.tsx](ui/src/components/AddSourceDialog.tsx): 신규 소스 폼 (name/url/source_type/tier), 제출 시 `POST /api/sources`
- [x] [ui/src/components/PolicyForm.tsx](ui/src/components/PolicyForm.tsx): `editorial_policy.yaml` 5섹션 (source_tiers / scoring_weights / penalties / quotas / report_selection), 슬라이더 + 숫자 입력
- [x] 정책 저장: `PUT /api/policy` → 런타임 오버라이드 (yaml 미수정), 화면에 "변경 사항 (재시작 시 휘발)" 배너
- [x] 소스 enable/disable 시 즉시 `data/sources_registry.yaml` 갱신, 다음 run에 반영
- [x] [Settings] 라우트(`/settings`)는 PolicyForm을 마운트, 사이드바 하단 ⚙ 버튼에서 진입

#### Success Criteria
- 소스 행 토글 → yaml에 반영, 페이지 새로고침해도 상태 유지
- 정책 슬라이더 변경 + 저장 → 다음 `POST /api/preview` 응답에 반영
- 신규 소스 추가 → 목록에 새 행, 다음 run에 수집 시도

#### Test Cases
- [x] TC-5.1: Sources 페이지 첫 진입 시 37행, 5그룹 헤더
- [x] TC-5.2: openai-blog 토글 off → yaml 파일에서 `enabled: false` 확인
- [x] TC-5.3: PolicyForm `target_sections` 10→7 변경 + 저장 → preview API 응답이 7 섹션
- [x] TC-5.4: AddSourceDialog 제출 → `/api/sources` 200 + 새 행 표시
- [x] TC-5.E1: 잘못된 url(스키마 없음) → 폼 검증 에러, 제출 차단

#### Testing Instructions
```bash
cd ui && npm run test -- src/__tests__/Sources.test.tsx src/__tests__/PolicyForm.test.tsx
PYTHONPATH=. uv run pytest tests/unit/test_admin_api.py -k "sources or policy" -v
```

---

### Phase 6: Polish & Build
> 단축키 · 반응형 · 에러 상태 · 정적 빌드
> Dependencies: Phase 2~5 완료

#### Tasks
- [x] `cmdk` 설치 + [ui/src/components/CommandPalette.tsx](ui/src/components/CommandPalette.tsx): ⌘K로 열고 검색·실행·이동
- [x] [ui/src/App.tsx](ui/src/App.tsx)에 글로벌 단축키 등록: `R`(re-run last) `P`(publish current)
- [x] 모바일 반응형: `@media (max-width: 768px)`에서 사이드바 → Sheet 변환 (`05-layout-patterns.md` 5.2)
- [x] 모든 페이지에 EmptyState/ErrorBoundary 적용
- [x] [ui/Makefile](Makefile) 또는 root `Makefile`: `make ui-build` → `ui/dist/` 산출, `make serve` → FastAPI가 `ui/dist`를 정적 서빙
- [x] [app/admin/api.py](app/admin/api.py): `app.mount("/", StaticFiles(directory="ui/dist", html=True))` 단일 진입점

#### Success Criteria
- ⌘K 누르면 명령 팔레트 표시, 화살표로 항목 이동, Enter로 실행
- 모바일(375px)에서 사이드바가 숨고 햄버거 → 시트로 표시
- `make ui-build && make serve` → `localhost:8000`에서 SPA 작동, 새로고침해도 라우트 유지
- 빌드 산출물 `ui/dist/`이 git에서 무시됨

#### Test Cases
- [x] TC-6.1: ⌘K → 검색창 표시, "오늘" 입력 → Dashboard로 이동 옵션
- [x] TC-6.2: viewport 375px → 사이드바 hidden, ☰ 버튼 표시
- [x] TC-6.3: API 다운(`pkill uvicorn`) → 페이지가 ErrorBoundary 메시지 + 재시도 버튼
- [x] TC-6.4: `make ui-build` 빌드 성공 + dist 폴더 생성
- [x] TC-6.5: `make serve` 후 `localhost:8000/sources` 새로고침 → 같은 페이지 유지 (404 아님)

#### Testing Instructions
```bash
cd ui && npm run build
make serve
curl -s http://localhost:8000/ | grep "<div id=\"root\"></div>"
```

---

## 5. Integration & Verification

### 5.1 Integration Test Plan (전 단계 통합)
- [x] **시나리오 A**: Dashboard → "신규 생성" → 옵션 변경 → 라이브 미리보기 갱신 → Run → 진행률 토스트 → ReviewReport로 이동 → 섹션 1개 off → Publish → URL 복사
- [x] **시나리오 B**: Sources에서 소스 1개 disable → NewReport 진입 → preview에 해당 소스의 섹션이 사라짐
- [x] **시나리오 C**: Settings에서 `target_sections` 5로 저장 → NewReport preview에 5 섹션
- [x] **시나리오 D**: 다크 → 라이트 토글 → 모든 페이지에서 토큰이 라이트 값으로 전환

### 5.2 Manual Verification Steps
1. `make serve`로 단일 진입점 부팅, `localhost:8000/` 접속
2. 4 화면을 좌측 사이드바로 순회, 콘솔 에러 0건 확인
3. ⌘K로 명령 팔레트, 모든 라우트 이동
4. 모바일 viewport(375)에서 핵심 화면 3개 사용 가능 확인
5. iframe 미리보기가 라이트/다크/`newsroom-white` 3 테마 모두 표시

### 5.3 Rollback Strategy
- UI는 `ui/` 디렉토리만 영향 → `git rm -rf ui/` + `Makefile`에서 ui 타겟 제거로 즉시 롤백
- API 변경은 `app/admin/api.py`의 새 라우트만 주석 처리하면 비활성
- `data/sources_registry.yaml` / `editorial_policy.yaml` 수정은 git revert로 복구

---

## 6. Edge Cases & Risks

| 위험 요소 | 영향도 | 완화 방안 |
|---|---|---|
| 라이브 미리보기 비용(LLM 호출 반복) | **높음** | preview는 캐시된 클러스터·섹션 재사용, generate 단계 skip. LLM은 재생성 명시 시만 호출 |
| SSE 연결 끊김 | 중간 | 클라이언트가 자동 재연결 + 마지막 progress 복원 |
| asyncio subprocess 좀비 | 중간 | `process.terminate()` on cancel, run 시작 시 기존 동일 날짜 프로세스 정리 |
| dnd-kit 모바일 터치 충돌 | 낮음 | 모바일에선 reorder를 화살표 버튼으로 대체 |
| 정책 런타임 오버라이드 휘발 | 중간 | 화면 상단 배너 + "yaml에 영구 저장" 별도 버튼 (Phase 6 옵션) |
| 정적 HTML 리포트 자동 변경 | **차단 대상** | preview 렌더링 시 `templates/report_newsstream.html.j2` 수정 금지, 옵션 오버라이드만 적용 |
| Tailwind v4 + shadcn new-york 호환 | 낮음 | 첫 컴포넌트로 검증 후 진행 |
| 인증 없음 → 의도치 않은 외부 노출 | 중간 | FastAPI를 `127.0.0.1` 바인드 기본, deploy 시 명시적 호스트 지정 |

---

## 7. Execution Rules

1. **독립 모듈**: 각 Phase는 분리 가능, Phase 2~5는 셸 완료 후 병렬 진행 가능.
2. **완료 조건**: 모든 태스크 체크박스 체크 + 모든 테스트 통과.
3. **테스트 실패 워크플로우**: 에러 분석 → 근본 원인 수정 → 재테스트 → 통과 후에만 다음 Phase 진행.
4. **Phase 완료 기록**: 체크박스를 직접 체크해 진행 상황을 이 문서에 반영.
5. **No-Modification Zone**: `templates/report_newsstream.html.j2`, `public/news/*.html`은 어떠한 Phase에서도 직접 변경하지 않음. preview는 옵션 오버라이드 + 인메모리 렌더만 사용.
6. **단일 출처**: 색·radius·shadow·spacing은 모두 `docs/design/tokens.css`에서 가져옴. 새 토큰 필요 시 `docs/design/02-tokens.md` 먼저 갱신.
7. **아이콘 변경**: `ui/src/lib/icons.ts`의 `SIDEBAR_NAV_ICONS`만 수정. 다른 곳에서 lucide 직접 import 금지.

---

## 8. Estimated Scope

| 항목 | 추정 |
|---|---|
| 신규 파일 | ~32개 (UI 25 + API 4 + 테스트 3) |
| 수정 파일 | ~5개 |
| 신규 LOC | ~3,500 (UI 2,800 + API 700) |
| 단계별 시간 (1인 기준) | Phase 0: 0.5일 / 1: 1일 / 2: 1일 / 3: 1.5일 / 4: 1.5일 / 5: 1일 / 6: 0.5일 → 총 7일 |
| 외부 신규 의존성 | `sse-starlette`(BE) + `cmdk`·`@dnd-kit/*`·`zustand`·`@tanstack/react-query`·shadcn(FE) |
