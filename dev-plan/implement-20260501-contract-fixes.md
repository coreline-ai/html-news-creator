# Implementation Plan: News Studio 운영 계약 정합성 복구

> Generated: 2026-05-01
> Source: `dev-plan/review-20260501-news-studio-gap-analysis.md`
> Project: html-news-creator
> Goal: "웹앱에서 한 일이 발행 결과물에 반영된다"는 기본 약속을 회복한다.

---

## 1. Context

### 1.1 Why
직전 리뷰에서 **5개 P0 + 4개 P1**의 계약 갭이 확정됐다. 계약을 고치지 않으면 운영자는 화면을 조작하고도 결과물이 바뀌지 않는 상황을 반복한다.

### 1.2 코드 검증으로 확정된 갭

| # | 갭 | 검증 결과 |
|---|---|---|
| P0-1 | `_build_argv`가 5개 옵션만 CLI 전달 | ✅ 확정 (`--date/--mode/--from-step/--to-step/--dry-run`) |
| P0-2 | SSE schema 불일치 + 실패 → 성공 처리 | ✅ BE는 `{stream,line,ts}`, FE는 `{step,progress}` 기대 |
| P0-3 | Review 수정이 발행 HTML에 반영 X | ✅ `publish.py`에 render 호출 0건 |
| P0-4 | `POST /api/sources` 부재 | ✅ GET/PUT만 존재, FE는 POST 호출 |
| P0-5 | `quotas`↔`section_quotas` schema 불일치 + Settings override 미전달 | ✅ FE `quotas`, yaml `section_quotas`, runtime override는 메모리만 |
| P1-1 | 이미지 URL 검증 없음 | ✅ `api_patch_section`에 검증 0 |
| P1-2 | `output_theme` UI에 있지만 적용 안 됨 | ✅ store/Panel만 존재, BE/template 미사용 |
| P1-3 | KST helper 3 곳 분산 | ✅ `store.ts:todayKstString`, `Dashboard:todayKst`, `Reports:DATE_FMT` |
| P1-4 | `sources_admin` write atomic 아님 | ✅ `path.open("w")` 직접 |

### 1.3 Scope
- **In**: 위 9개 갭의 코드 수정 + 단위 테스트.
- **Out**: 라우터 파일 대규모 재구조 (P2), 통합 테스트 (별도 작업).

---

## 2. Phase 분할 (4개)

```
Phase A: 계약 정리 (SSE + Run options)        ─┐
Phase B: Render → Publish 완성                  ├─ 병렬 가능 (영역 분리)
Phase C: Sources POST + Policy schema           │
Phase D: P1 안정화                             ─┘
```

각 Phase는 독립 영역에 작업하므로 충돌 없음.
공유 파일(`app/admin/api.py`)은 Phase별로 **새 router 파일을 만들고 api.py에 한 줄씩 include**해서 충돌 회피.

---

## 3. Phase A — 계약 정리 (SSE + Run options)
> Dependencies: 없음

### 3.1 Tasks
- [ ] `app/admin/sse.py` — `progress` 이벤트의 `data`를 구조화: `{step, progress, message, raw_line}`. BE에서 `line` 내부의 JSON을 파싱해 step/level/event를 뽑아 전달. 파싱 실패 시에도 raw_line은 포함.
- [ ] `app/admin/sse.py` — `done` 이벤트의 status 보존(이미 그렇게 동작). FE가 정확히 처리하도록 schema 명시.
- [ ] `ui/src/hooks/useRunStream.ts` — 새 schema 파싱. `done` 이벤트의 `status === "failed"` 시 hook status를 `"error"`로 전환 (현재 항상 `"done"`).
- [ ] `ui/src/pages/NewReport.tsx` — Run 완료 후 navigate 분기: 성공 시 `/reports/{date}`, 실패 시 navigate 금지 + 에러 토스트 유지.
- [ ] `app/admin/run_runner.py` — `_build_argv`를 **현재 CLI 지원 옵션으로 명시 제한**. 미지원 옵션은 warning 로그.
- [ ] `ui/src/components/RunOptionsPanel.tsx` — 미지원 옵션 그룹(D 출력의 `output_theme`/`format`, E 발행의 `deploy_target`/`slack_notify`/`publish_at`)에 "Preview only — not yet applied to actual run" 배지. 또는 disabled.
- [ ] 단위 테스트: `tests/unit/test_admin_sse_schema.py` (새 schema), `ui/src/__tests__/useRunStream.test.tsx`(실패 처리), `ui/src/__tests__/NewReport.failure.test.tsx`.

### 3.2 Success Criteria
- BE SSE에서 progress event 받을 때 `data.step`이 항상 string (collect/extract/.../notify), 알 수 없으면 `"unknown"`.
- 실패 run을 백엔드에서 simulate → FE 토스트 "Run failed" + Review 페이지 자동 이동 X.

---

## 4. Phase B — Render → Publish 완성
> Dependencies: 없음 (Phase A와 병렬 가능)

### 4.1 Tasks
- [ ] `app/admin/render.py` (신규) — `render_published(date_kst, db, disabled_section_ids) -> Path`:
  1. DB의 최신 `Report` + `ReportSection` 로드 (선택된 날짜)
  2. `disabled_section_ids` 제외
  3. `app/rendering/jinja_renderer.py`로 `report_newsstream.html.j2` 렌더
  4. `public/news/{date}-trend.html` 덮어쓰기
  5. `ReportArtifact` (artifact_type=html, storage_path) 기록
- [ ] `app/admin/publish.py` — `publish_report` 호출 흐름을 `render_published` → `NetlifyPublisher.deploy` 순서로 변경. 실패 시 명확한 에러.
- [ ] `app/admin/api.py` — 신규 `POST /api/reports/{date}/render` 라우트 (publish 없이 render만, 디버그용).
- [ ] `app/admin/api.py` — `api_publish_report`가 body에서 `disabled_section_ids: string[]`를 받음. publish 헬퍼에 전달.
- [ ] `ui/src/hooks/useSections.ts::usePublishReport()` — body에 `disabled_section_ids` 포함.
- [ ] `ui/src/pages/ReviewReport.tsx::handlePublishConfirm` — `useReviewStore.disabledSectionIds`의 key 배열을 mutation에 전달.
- [ ] 단위 테스트: `tests/unit/test_admin_render.py` (render_published mock with disabled), `tests/unit/test_admin_publish_disabled.py`.

### 4.2 Success Criteria
- `POST /api/reports/2026-05-01/publish` body=`{disabled_section_ids:["abc-123"]}` → 발행 HTML에서 해당 섹션 미포함.
- Review 화면에서 섹션 제목 수정 → Save → Publish → 발행 HTML 새 제목 반영.

---

## 5. Phase C — Sources POST + Policy 통일
> Dependencies: 없음

### 5.1 Tasks
- [ ] `app/admin/sources_admin.py` — `add_source(fields) -> dict`. 중복 name 검사, 필수 필드(name/source_type) 검증, atomic write (tempfile + os.replace).
- [ ] `app/admin/sources_admin.py::update_source` — atomic write 동일 적용.
- [ ] `app/admin/api.py` — `POST /api/sources` 라우트 추가 (호출만, 본문은 `add_source`로).
- [ ] `ui/src/components/PolicyForm.tsx` — `toPatch()`가 `quotas` 대신 **`section_quotas`** 키로 보냄. types도 `section_quotas`로 통일.
- [ ] `app/admin/policy_admin.py::set_policy_override` — runtime override를 임시 yaml 파일로 dump하는 헬퍼 추가 (`materialize_to(tmp_path)`).
- [ ] `app/admin/run_runner.py` — runtime override가 비어있지 않으면 임시 yaml로 dump → `EDITORIAL_POLICY_PATH=/tmp/...` 환경변수로 subprocess에 전달.
- [ ] `app/editorial/policy.py` — 환경변수 `EDITORIAL_POLICY_PATH` 우선 읽기 (없으면 `data/editorial_policy.yaml`).
- [ ] `scripts/run_daily.py` — `--policy-path` 옵션도 같이 추가 (env과 동치, 명시적 운영 편의).
- [ ] 단위 테스트: `test_admin_sources_post`, `test_policy_override_subprocess_pass_through`, `test_sources_admin_atomic`.

### 5.2 Success Criteria
- AddSourceDialog 제출 → 200 + 새 소스 목록 갱신.
- Settings에서 `target_sections=5` 저장 → `make run`(또는 `/api/runs`) 실행 결과 섹션 수가 5.

---

## 6. Phase D — P1 안정화
> Dependencies: 없음

### 6.1 Tasks
- [ ] `app/admin/api.py::api_patch_section` — `image_url` 입력 시 URL 검증 (`http(s)://` 스키마, host 존재). 부적합하면 400.
- [ ] `ui/src/lib/kst.ts` (신규) — `todayKstISO()`, `formatKstDateTime(iso)` 두 helper. `Asia/Seoul`을 `Intl.DateTimeFormat`의 `timeZone` 옵션으로 명시.
- [ ] `ui/src/lib/store.ts`, `ui/src/pages/Dashboard.tsx`, `ui/src/pages/Reports.tsx` — 각자 정의한 KST 함수를 `@/lib/kst`로 교체.
- [ ] `templates/report_newsstream.html.j2` — `{{ output_theme | default("dark") }}`을 `<html data-theme>` 또는 `class="dark"` 초기값에 반영.
- [ ] `app/rendering/jinja_renderer.py` — render 호출 시 `output_theme`을 컨텍스트에 주입 (Phase B의 render도 같은 경로).
- [ ] `ui/src/__tests__/kst.test.tsx`, `tests/unit/test_section_image_url_validation.py`.

### 6.2 Success Criteria
- 부적합한 image_url 제출 → 400.
- 화면 3 곳의 KST 표기가 시스템 시간대와 무관하게 동일.
- `output_theme=dark` 옵션으로 publish → 발행 HTML 첫 렌더가 `class="dark"`.

---

## 7. 검증 (모든 Phase 후)

```bash
PYTHONPATH=. uv run pytest tests/unit/ -m "not integration" -q
make lint-design
cd ui && npm run typecheck && npm run build && npm run test -- --run
make e2e
```

전체 통과 + 라이브 smoke:
- `POST /api/runs` → SSE에서 `{step}`이 보이고 실패는 error
- AddSourceDialog 제출 200
- ReviewReport 수정 → Publish → 발행 HTML 반영

---

## 8. 실행 룰 (병합 안전)

1. **No-Modification Zone**: `templates/report_newsstream.html.j2`는 Phase D의 한 줄 변경(theme initial value) 외 직접 수정 금지.
2. **api.py 충돌 회피**: 각 Phase가 라우트 추가 시 `app/admin/{render,publish_api,sources_api}.py` 같은 새 모듈에 함수 정의 → api.py에는 한 줄씩 라우트만.
3. **단일 출처**: 새 헬퍼는 자기 모듈에. lib/store/api 같은 공유 파일은 명확한 영역만.
4. **commit 스타일**: 각 Phase 1 commit, push는 메인 세션이 일괄.

---

## 9. 추정

| Phase | 신규 파일 | 수정 파일 | 추정 LOC | 시간 (1인 기준) |
|---|---|---|---|---|
| A | 1 | 4 | ~280 | 0.5일 |
| B | 1 | 4 | ~320 | 1일 |
| C | 1 | 6 | ~360 | 1일 |
| D | 1 | 6 | ~240 | 0.5일 |
| E | 0 | 4 | ~120 | 0.5일 |
| **총계** | **4** | **24** | **~1,320** | **3.5일** |

병렬 4 에이전트로 A~D ~6시간, Phase E는 단독 추가.

---

## 10. Phase E — Policy Persistence 명시화
> Source: `dev-plan/review-20260501-policy-persistence-deepdive.md`
> Dependencies: Phase C 머지 후 (이미 main)
> Phase A~D와 별개 후속 작업.

### 10.1 Why
Phase C로 runtime override가 subprocess까지 전달되지만, 운영자에게는:
- "Settings 변경 = `data/editorial_policy.yaml`이 수정됐다"고 오해할 여지가 있고
- 영구 보존하려면 ssh로 yaml 직접 수정해야 하는 운영 UX 결함이 있다.

### 10.2 Tasks
- [ ] **R1** [`ui/src/components/PolicyForm.tsx`](ui/src/components/PolicyForm.tsx) — dirty/saved 배너 카피 강화:
  - dirty: "변경 중 — 저장 시 다음 Run부터 반영 (서버 재시작 시 유실)"
  - saved: "다음 Run에 반영됩니다 · `data/editorial_policy.yaml`은 수정되지 않습니다"
  - 상단에 작은 ⓘ 헬프: "정책 우선순위: yaml < runtime override < per-run options"
- [ ] **R2-BE** [`app/admin/policy_admin.py`](app/admin/policy_admin.py) — `persist_runtime_override_to_yaml() -> Path` 헬퍼: 현재 `_RUNTIME_OVERRIDE`를 yaml과 머지해 atomic write (`tempfile + os.replace`), 기존 파일은 `*.yaml.bak`로 백업.
- [ ] **R2-API** [`app/admin/api.py`](app/admin/api.py) — `POST /api/policy/persist` 라우트. 성공 시 `{persisted_to: "data/editorial_policy.yaml", backup: "data/editorial_policy.yaml.bak"}` 반환. override가 비어있으면 400.
- [ ] **R2-FE** [`ui/src/components/PolicyForm.tsx`](ui/src/components/PolicyForm.tsx) — 푸터에 `[Persist to yaml]` 버튼 + 확인 다이얼로그 ("이 작업은 디스크의 yaml 파일을 덮어씁니다. 백업이 함께 생성됩니다.").
- [ ] **R2-Hook** [`ui/src/hooks/usePolicy.ts`](ui/src/hooks/usePolicy.ts) — `usePersistPolicy` mutation 추가.
- [ ] **R3** [`docs/news-studio-usage.md`](docs/news-studio-usage.md) — "Policy precedence" 섹션 신규: 우선순위 표 + 시나리오 3건 (Preview / Per-run / Permanent).
- [ ] 단위 테스트: `tests/unit/test_policy_persist.py` (override → yaml dump + backup), `ui/src/__tests__/PolicyForm.persist.test.tsx`.

### 10.3 Success Criteria
- Settings에서 `target_sections=7` 변경 → `[Persist to yaml]` 클릭 → 확인 → `data/editorial_policy.yaml`의 해당 키가 7로 변경됨 + `*.yaml.bak`에 이전 값 보존.
- 서버 재시작 후 `GET /api/policy` 응답이 7로 유지.
- 운영자가 dirty 상태에서 "재시작 시 유실"이라는 안내를 명확히 본다.

### 10.4 Test Cases
- [ ] TC-E.1: `_RUNTIME_OVERRIDE = {"section_quotas": {"product": 6}}` → `persist_runtime_override_to_yaml()` → yaml 파일에 `section_quotas.product: 6` 반영, 백업 파일 생성.
- [ ] TC-E.2: override가 빈 dict → `persist` API → 400 + "no override to persist".
- [ ] TC-E.3: persist 도중 yaml dump 실패 → 원본 무손상 (atomic write 검증).
- [ ] TC-E.4: PolicyForm dirty 배너 → "재시작 시 유실" 문자열 포함.
- [ ] TC-E.5: persist 다이얼로그 확인 → API 호출 + 토스트 + 배너 → "all changes saved (persisted)".

### 10.5 Testing Instructions
```bash
PYTHONPATH=. uv run pytest tests/unit/test_policy_persist.py tests/unit/test_admin_api.py -v --tb=short
cd ui && npm run typecheck && npm run build && npm run test -- --run src/__tests__/PolicyForm.persist.test.tsx
```

**테스트 실패 시 워크플로우:**
1. 에러 출력 분석 → 근본 원인 식별
2. 원인 수정 → 재테스트
3. 모든 테스트가 통과할 때까지 main push 보류
