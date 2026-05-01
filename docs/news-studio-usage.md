# News Studio 운영 가이드

운영자가 매일의 AI 트렌드 리포트를 웹에서 직접 생성·튜닝·검토·발행하기 위한 단일 사용자 도구 사용 가이드입니다. 본 문서는 React 19 + Vite SPA(`ui/`)와 FastAPI(`app/admin/api.py`)로 구성된 News Studio 웹앱의 운영자 매뉴얼입니다.

---

## 1. 개요

News Studio는 `scripts/run_daily.py` CLI를 그대로 호출하는 thin wrapper로, 운영자가 다음 작업을 GUI로 처리할 수 있게 합니다.

- 옵션 변경 → 라이브 미리보기 (DB 쓰기 없음)
- 파이프라인 9단계 진행률 SSE 스트리밍
- 섹션 단위 reorder · 편집 · 단일 재생성
- 37개 소스 토글 및 `editorial_policy.yaml` 런타임 오버라이드
- Netlify 배포 트리거 + 결과 URL 복사

정적 HTML 리포트(`templates/report_newsstream.html.j2`, `public/news/*.html`)는 본 웹앱의 자동 변경 대상이 아닙니다. 미리보기는 옵션 오버라이드 + 인메모리 렌더만 사용합니다.

---

## 2. 시작

### 운영 모드 (단일 진입점, :8000)

```bash
make ui-build   # ui/dist/ 산출
make serve      # uvicorn app.admin.api:app --port 8000
```

`make serve`는 `make ui-build`를 의존성으로 호출하므로 한 번에 실행됩니다. 브라우저에서 `http://localhost:8000` 접속 시 SPA + API가 같은 origin에서 동작합니다.

### 개발 모드 (HMR, :5173 + :8000)

```bash
# 터미널 1
cd ui && npm run dev

# 터미널 2
PYTHONPATH=. uv run uvicorn app.admin.api:app --reload --port 8000
```

Vite dev 서버(5173)가 `/api/*` 요청을 8000으로 프록시합니다. `app/admin/api.py`의 CORS 화이트리스트는 `localhost:5173`을 기본 포함합니다.

---

## 3. 4 화면 가이드

### 3.1 대시보드 (`/`)

오늘의 리포트 상태와 최근 실행 이력을 한 화면에서 확인합니다.

- **오늘 카드**: 가장 최근 `Report.report_date` 기준 status·섹션 수·summary 미리보기
- **Quick actions**: `[신규 생성]` `[검토]` `[소스 관리]` 3개 카드 — 각 라우트로 즉시 이동
- **최근 실행 테이블**: `JobRun` 최신 N건 — 행 클릭 시 `/reports/:date`로 진입
- API 다운/빈 DB 상태에서는 EmptyState 카드를 표시 (백지화 금지)

### 3.2 신규 리포트 (`/reports/new`)

옵션을 조정하며 라이브 미리보기로 결과를 확인하고, 만족하면 Run을 트리거합니다.

- **5그룹 옵션** (Accordion): A 실행 / B 편집 / C 소스 / D 출력 / E 발행
- **라이브 미리보기**: 옵션 변경 → 2초 디바운스 → `POST /api/preview` → iframe `srcdoc` 갱신. LLM 재호출 없이 캐시된 클러스터·섹션 재사용
- **뷰포트 토글**: `[💻][📱][🌙]` 버튼으로 데스크톱/모바일/다크 미리보기 전환
- **Run**: 옵션을 `POST /api/runs`로 전송 → SSE 진행률 토스트 → 완료 시 `/reports/:date`로 자동 이동
- `dry_run` 토글 ON 상태에서는 DB 쓰기 없이 시뮬레이션만 수행

### 3.3 검토 (`/reports/:date`)

생성 완료된 리포트의 섹션을 reorder · edit · publish 합니다.

- **SectionList**: `@dnd-kit/sortable` 드래그로 순서 변경 → `POST /api/reports/:date/reorder` 호출, 응답 후 미리보기 자동 갱신
- **on/off 토글**: 비활성화 섹션은 hatch 패턴으로 표시, 발행 시 자동 제외
- **SectionEditor**: 제목 / 요약(`fact_summary`) / 시사점(`inference_summary`) / 이미지 URL 편집 — `PATCH /api/sections/:id`
- **Regenerate**: 단일 섹션만 LLM 재생성 (`POST /api/sections/:id/regenerate`, 다른 섹션 영향 없음)
- **미리보기 모드 토글**: `live` (iframe) ↔ `section` (편집 폼) — store의 `previewMode`로 제어
- **PDF**: `[PDF]` 버튼 → `GET /api/reports/:date/pdf` → 현재 HTML을 A4 PDF로 다운로드 (`fresh=true`면 DB 재렌더)
- **Publish**: 확인 다이얼로그 → `POST /api/reports/:date/publish` (Netlify) → 결과 URL 토스트로 복사 가능

### 3.4 소스 / 설정 (`/sources`, `/settings`)

37개 활성 소스 관리와 `editorial_policy.yaml` 런타임 오버라이드.

- **Sources**: 등급별 5개 그룹 (official / mainstream / developer_signal / research / community) 헤더 + 행 (이름·tier·type·last_run·item_count·toggle)
- 토글 → `PUT /api/sources/:name`, `data/sources_registry.yaml` 즉시 갱신, 다음 run에 반영
- **AddSourceDialog**: 신규 소스 폼 (name/url/source_type/tier) — 잘못된 url 스키마는 검증 차단
- **PolicyForm** (`/settings`): `source_tiers / scoring_weights / penalties / quotas / report_selection` 5섹션 슬라이더
- 정책 저장 → `PUT /api/policy`, **런타임 오버라이드만 적용** (yaml 미수정, 재시작 시 휘발). 화면 상단에 휘발성 배너 노출
- **Persist to yaml** 버튼 → `POST /api/policy/persist`, 런타임 오버라이드를 `data/editorial_policy.yaml`에 영구 저장 (백업 `*.yaml.bak` 자동 생성, 서버 재시작 후에도 유지)

---

## 3.5 Policy precedence

PolicyForm이 변경하는 값은 3개의 레이어 중 하나에 들어갑니다. 우선순위는 **per-run options > runtime override > yaml** 입니다 (오른쪽이 더 약함).

| Layer | 변경 위치 | 영속성 | 적용 범위 |
|---|---|---|---|
| **yaml (영구)** | `data/editorial_policy.yaml` 직접 편집 또는 `[Persist to yaml]` 버튼 | 디스크에 보존, 재시작 시 유지 | 이후 모든 Run의 baseline |
| **runtime override** | `/settings` PolicyForm `[Save]` (= `PUT /api/policy`) | 메모리(휘발), 서버 재시작 시 소실 | 이후 모든 Run에 누적 적용 |
| **per-run options** | `/reports/new`의 옵션 패널 (RunOptionsPanel) | 단일 Run 한정 | 해당 Run만 |

세 시나리오:

1. **실험만** — PolicyForm `[Save]` → 메모리 오버라이드만 적용. 만족스러우면 `[Persist to yaml]`, 아니면 서버 재시작으로 폐기.
2. **운영 영구 변경** — PolicyForm에서 값 조정 → `[Save]` → 다음 Run 결과로 검증 → `[Persist to yaml]` 클릭 → yaml 저장 + `.bak` 백업.
3. **단일 Run 한정** — runtime override에 손대지 않고 `/reports/new`의 RunOptionsPanel에서 `target_sections` 등을 일시적으로 바꿔 Run.

`[Persist to yaml]`은 현재 메모리에 살아있는 runtime override만 yaml에 머지합니다. 오버라이드가 비어있으면 (`Save`가 한 번도 일어나지 않았거나 빈 값으로 초기화한 상태) 400을 반환합니다.

---

## 4. 단축키

| 단축키 | 동작 | 비고 |
|---|---|---|
| `⌘K` / `Ctrl+K` | 명령 팔레트 토글 | 모든 화면에서 검색·이동·실행 |
| `R` | 마지막 옵션으로 재실행 | ReviewReport에선 해당 날짜로 스코프 |
| `P` | 현재 리포트 발행 | ReviewReport에서만 동작 |
| 테마 토글 | 다크 ↔ 라이트 | HeaderBar 우측 버튼, `localStorage('theme')` 영속 |

입력 필드(`<input>`, `<textarea>`, `contenteditable`) 포커스 중에는 `R`/`P` 단축키가 무시됩니다. 명령 팔레트가 열린 상태에서도 단축키 충돌을 피하기 위해 무시됩니다.

---

## 5. API 엔드포인트

`app/admin/api.py`에 정의된 12개 News Studio 라우트입니다. (legacy `/api/v1/*`은 별도 유지)

| # | Method | Path | 용도 |
|---|---|---|---|
| 1 | GET | `/api/reports` | 최근 리포트 요약 목록 (limit ≤ 100) |
| 2 | GET | `/api/reports/{date_kst}` | 단일 리포트 + 섹션 전체 |
| 3 | POST | `/api/preview` | 옵션 오버라이드 인메모리 렌더 (DB 쓰기 없음) |
| 4 | POST | `/api/runs` | `run_daily.py` 백그라운드 실행 시작 |
| 5 | GET | `/api/runs/{run_id}/stream` | 9단계 진행률 SSE |
| 6 | GET | `/api/policy` | yaml + 런타임 오버라이드 병합 정책 |
| 7 | PUT | `/api/policy` | 런타임 오버라이드 저장 (휘발) |
| 7b | POST | `/api/policy/persist` | 런타임 오버라이드를 yaml에 영구 저장 (`.bak` 백업) |
| 8a | GET | `/api/sources` | 레지스트리(yaml) 기반 소스 목록 |
| 8b | PUT | `/api/sources/{name}` | enabled/priority/max_items 등 패치 |
| 9 | PATCH | `/api/sections/{id}` | 단일 섹션 title/summary/implication/image_url 수정 |
| 10 | POST | `/api/sections/{id}/regenerate` | 단일 섹션 재생성 (현재 stub, 큐잉만) |
| 11 | POST | `/api/reports/{date}/reorder` | 섹션 `section_order` 일괄 갱신 |
| 12 | POST | `/api/reports/{date}/publish` | Netlify 배포 트리거 + 상태 갱신 |

`/health`, `/api/v1/*` (runs/reports/stats/sources)는 기존 호환성을 위해 유지됩니다.

---

## 6. 트러블슈팅

| 증상 | 원인 / 확인 | 조치 |
|---|---|---|
| `make serve` 후 `/`에서 흰 화면 | `ui/dist/`가 비어 있음 | `make ui-build` 재실행. 로그에 `ui_dist_not_found` 가 보이면 빌드 누락 |
| `/api/*` 호출 CORS 에러 | dev origin이 8000과 다름 | `app/config.py`의 `ui_dev_origin` 또는 `.env`의 동명 변수 확인 |
| 미리보기가 갱신되지 않음 | 디바운스 2초 대기 중이거나 옵션 검증 400 | DevTools Network에서 `POST /api/preview` 응답 확인. `target_sections` < 1 등 음수/범위 외 값은 400 |
| Run 진행률이 멈춤 | SSE 연결 끊김 또는 subprocess 좀비 | 페이지 새로고침 → 자동 재연결. 동일 날짜 재실행 시 이전 프로세스 정리 필요하면 `pkill -f run_daily.py` |
| 정책 변경이 다음 run에 반영 안됨 | 런타임 오버라이드는 휘발 (재시작 시 소실) | `/settings`의 `[Persist to yaml]` 버튼으로 영구 저장 (또는 `data/editorial_policy.yaml` 직접 편집 후 재시작) |
| Publish 실패 | Netlify CLI/토큰 누락 | `.env`의 `NETLIFY_AUTH_TOKEN`, `NETLIFY_SITE_ID` 확인. dry_run 옵션으로 URL만 검증 가능 |

---

## 7. 향후 작업 / 알려진 제한

회귀 테스트 시 참고할 현재 구현의 stub 및 제한 사항입니다.

- **단일 섹션 regenerate (`POST /api/sections/:id/regenerate`)**: 현재 큐잉 응답만 반환하는 stub. 실제 LLM 재호출은 `app/generation/` 와의 통합 작업이 필요합니다.
- **정책 오버라이드 영속화**: `PUT /api/policy`는 메모리에만 머물며 프로세스 재시작 시 소실됩니다. 영구 저장은 `/settings`의 `[Persist to yaml]` 버튼(`POST /api/policy/persist`)으로 처리하며, 기존 yaml은 `.bak`으로 자동 백업됩니다.
- **인증/권한**: 단일 사용자 가정으로 인증 없음. 기본은 `127.0.0.1` 바인드. 외부 호스트에 노출 시 별도 reverse proxy + 인증 필수.
- **소스 신규 타입**: rss / github / arxiv / website 외 타입은 UI에서 추가 불가 (Out of scope).
- **모바일 검토 화면**: `dnd-kit` 터치 충돌 가능성 — 모바일에서는 화살표 버튼 fallback 사용.
- **정적 HTML 리포트 마이그레이션**: 본 웹앱은 `templates/report_newsstream.html.j2`를 변경하지 않음. 디자인 시스템 적용은 별도 요청 시에만 진행.

상세 설계 의도와 결정 근거는 `dev-plan/implement-20260430-news-studio-webapp.md`, 디자인 토큰·컴포넌트 명세는 [`docs/design/`](design/)을 참고하세요.
