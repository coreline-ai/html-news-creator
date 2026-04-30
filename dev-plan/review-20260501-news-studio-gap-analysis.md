# Review: News Studio 웹앱 — 운영 계약 갭 분석

> Generated: 2026-05-01
> Scope: main 브랜치 전체 (웹앱 + 파이프라인 경계)
> Status: 정리(triage) 완료. 후속 구현 PR로 분리 예정.

---

## 1. 한 줄 요약

UI/테스트/빌드 수준은 양호하지만, **"웹앱에서 조작한 옵션이 실제 자동 파이프라인 결과에 반영된다"는 핵심 계약이 다섯 군데에서 끊겨 있다**. 겉모습은 완성됐지만 운영 플로우에서 사용자 의도가 결과물까지 도달하지 못한다.

---

## 2. 현재 상태 스냅샷

| 영역 | 상태 |
|---|---|
| 브랜치 | `main` |
| Backend Admin | `app/admin/*` 9개 파일 |
| Frontend UI | `ui/src/*` 63개 파일 |
| E2E | `ui/e2e/*` 5개 spec |
| 빌드 산출물 | `ui/dist`, `ui/node_modules` `.gitignore` 처리 |
| 실행 경계 | UI → FastAPI → subprocess → `scripts/run_daily.py` (방향 OK) |

### 검증 결과 (실행 기준 모두 통과)

| 검사 | 결과 |
|---|---|
| Python unit | **188 passed** |
| Ruff lint | 통과 |
| UI typecheck | 통과 |
| UI unit | **61 passed** |
| UI build | 통과 |
| Playwright E2E | **9 passed** |
| Design-token lint | clean — 38 files |

> ⚠️ E2E는 `/api/*` 대부분을 mock하므로 **실제 `run_daily.py`, 실제 SSE 로그, 실제 DB/HTML publish 계약까지는 검증하지 않는다**.

---

## 3. 잘 된 부분 (보존)

- 웹앱과 CLI 파이프라인 **경계 분리**(internal step 직접 import 안 함, subprocess CLI 호출).
- FastAPI **SPA fallback이 `/api/*`와 충돌 없음** (`api/*` 우선, 나머지 index.html).
- **Preview는 DB write 0** (read-only 시뮬레이션).
- UI 구조 `pages / components / hooks / lib` 분리, 유지보수성 양호.
- `docs/design/tokens.css` import + design-token lint 통과.

---

## 4. 치명적 이슈 (P0~P1) ─ 5건

### 4.1 Run Options UI ↔ 실제 파이프라인 계약 불일치 (P0)

**현상**

- UI 옵션: `source_types`, `target_sections`, `min_section_score`, `quotas`, `image_required`, `arxiv_max`, `community_max`, `output_theme`, `deploy_target`, `slack_notify`, `publish_at` 등 다수.
- `app/admin/run_runner.py::_build_argv()`가 실제로 CLI에 넘기는 인자: `--date`, `--mode`, `--from-step`, `--to-step`, `--dry-run` 만.
- `scripts/run_daily.py`도 위 5개만 지원.

**결과**

웹앱에서 `target_sections=10`, `newsroom-white`, `slack_notify=false` 등을 바꿔도 **실제 오늘자 리포트 생성에 반영 안 됨**.

**권장 수정 (양자택일)**

| 길 | 작업 |
|---|---|
| **A. 안전 정리** | 반영 안 되는 옵션은 UI에서 숨기거나 "Preview only" 라벨. `/api/runs` 본문도 CLI 지원 필드로 제한. |
| **B. 정식 구현** | `RunOptions → 임시 policy/env/json 파일 → run_daily.py`로 전달. CLI에 `--policy-override-json`, `--source-types`, `--output-theme`, `--deploy-target` 추가. |

---

### 4.2 SSE 진행 이벤트 계약 불일치 + 실패 run을 성공처럼 표시 (P0)

**현상**

- BE가 SSE에 보내는 형태:
  ```json
  {"stream": "stdout", "line": "...", "ts": "..."}
  ```
- FE `useRunStream.ts`가 기대하는 형태:
  ```ts
  { step: string; progress: number; message?: string }
  ```
- E2E mock은 `{step, progress}`라 통과하지만 **실제 서버와 다름**.
- 더 큰 문제: `done` 이벤트에 BE는 `status: "failed"`도 넣지만, FE는 어떤 `done`이든 `status: "done"`으로 처리 → **실패 run도 UI는 성공으로 표시 + Review 화면으로 이동**.

**권장 수정**

1. BE SSE를 구조화: `event: progress` + `data: {step, progress, message, raw_line}`. 또는 FE에서 `line` 내부 JSON을 파싱.
2. `done` 이벤트에 `status === "failed"` → FE `status: "error"`로 전환.
3. 실패 시 `/reports/{date}` 자동 이동 금지.

---

### 4.3 Review 화면 수정이 최종 HTML에 반영 안 됨 (P0)

**현상**

| Review 액션 | 현재 반영 위치 | 최종 HTML 반영 |
|---|---|---|
| 섹션 제목/요약/시사점 수정 | DB `ReportSection` | ❌ |
| 순서 변경 | DB `section_order` | ❌ |
| 섹션 Off 토글 | 브라우저 `localStorage` | ❌ (BE 미전달) |
| Publish | 기존 `public/` deploy | ⚠️ 수정사항 반영 보장 없음 |

**결과**

Review에서 수정 후 Publish해도 **이미 렌더된 오래된 `public/news/{date}-trend.html`이 그대로 배포될 수 있다**.

**권장 수정**

- 신규 라우트 `POST /api/reports/{date}/render` 또는 publish 내부에서 자동으로:
  ```
  DB 최신 Report/Sections
   → disabled section 제외
   → Jinja render
   → public/news/{date}-trend.html 재생성
   → StaticPublisher index 업데이트
   → ReportArtifact 기록
   → Netlify deploy
  ```
- 즉 publish는 항상 **fresh render** 위에서 수행.

---

### 4.4 Add Source UI는 있는데 BE POST가 없음 (P0)

**현상**

- FE: `AddSourceDialog`, `useAddSource()`가 `POST /api/sources`를 호출.
- BE: `GET /api/sources`, `PUT /api/sources/{name}`만 존재.
- → **Add Source 버튼 누르면 실패**.

**권장 수정 (양자택일)**

- `POST /api/sources` 구현 (yaml 안전 갱신).
- 또는 미지원 구간은 Add Source 버튼 숨김/비활성.

---

### 4.5 정책 schema 불일치 + Settings override 전달 안 됨 (P1, P0 경계)

**현상**

- `data/editorial_policy.yaml`: `section_quotas`
- `PolicyForm.toPatch()`: `quotas`
- 파이프라인 selection: `section_quotas` 읽음
- → **Settings에서 quota 바꿔도 실제 selection 미반영 가능**.
- 또한 Settings runtime override는 FastAPI 프로세스 메모리에만 존재. 파이프라인은 새 subprocess라 yaml을 다시 읽음 → **override 전달 안 됨**.

**권장 수정**

- `quotas → section_quotas` 키 통일 (FE 또는 BE 한쪽).
- runtime override를 subprocess에 전달:
  - 임시 yaml 파일로 dump → `--policy-override-yaml` CLI 인자
  - 또는 환경변수 prefix `POLICY_OVERRIDE_*`

---

## 5. 우선순위 표

| 순위 | 이슈 | 위치 |
|---|---|---|
| **P0** | 실패 run도 성공처럼 처리 | `useRunStream.ts`, `NewReport.tsx` |
| **P0** | Review 수정 후 HTML 재렌더 없음 | `ReviewReport.tsx`, `app/admin/publish.py` |
| **P0** | Disabled section이 publish에 전달 안 됨 | `useReviewStore.ts`, `usePublishReport()` |
| **P0** | Add Source POST 백엔드 없음 | `useSources.ts`, `app/admin/api.py` |
| **P0** | Run Options 대부분 실제 run 미반영 | `_build_argv()`, `run_daily.py` CLI |
| **P1** | 이미지 URL 수동 입력 검증 없음 | `api_patch_section()` |
| **P1** | Publish helper가 CLI publish와 다름 | `app/admin/publish.py`, `run_daily.py` |
| **P1** | `output_theme`이 실제 HTML 초기 테마에 반영 안 됨 | `RunOptionsPanel`, `JinjaRenderer`, template |
| **P1** | KST 날짜 계산이 실제 KST 고정 아님 | `store.ts`, `Dashboard.tsx` |
| **P2** | `app/admin/api.py`가 라우터 단위로 커짐 | `app/admin/api.py` |
| **P2** | source registry write가 atomic 아님 | `sources_admin.py` |

---

## 6. 권장 개발 순서

### 1단계: 계약 정리 (P0)
1. `/api/runs`가 실제 지원하는 옵션만 명확히 제한.
2. 미지원 옵션은 UI에서 숨김 또는 "preview-only" 표시.
3. SSE 이벤트 schema를 BE/FE에서 통일.
4. 실패 run을 정확히 error로 표시 + 자동 이동 금지.

### 2단계: Review → Render → Publish 완성
5. `POST /api/reports/{date}/render` 추가 (또는 publish 내부에서 자동 fresh render).
6. Review 저장/정렬/비활성을 렌더 입력에 반영 (BE에 disabled list 전달).
7. Publish 전에 항상 최신 DB 기준 HTML 재생성.
8. `ReportArtifact`, index 업데이트 로직을 CLI publish와 공유.

### 3단계: Source / Policy 완성
9. `POST /api/sources` 구현 or UI 비활성화.
10. `quotas → section_quotas` schema 통일.
11. Settings runtime override를 subprocess에 전달.

### 4단계: 안정화
12. 이미지 URL 검증 강화.
13. `app/admin/api.py` 라우터 분리.
14. source registry atomic write.
15. KST 날짜 helper 통일 (`Asia/Seoul` 명시).
16. 실제 FastAPI + 실제 SSE 통합 테스트 추가.

---

## 7. 가장 먼저 고칠 3가지

1. **SSE 실패/성공 판정 수정** — 0.5일.
2. **Run Options가 실제 run에 반영되는 범위 정리** — 0.5~1일 (안전 정리), 2~3일 (정식 구현).
3. **Review 수정사항을 HTML 재렌더 후 publish하도록 변경** — 1~2일.

이 3건이 끝나면 "웹앱에서 한 일이 결과물에 진짜로 반영된다"는 기본 약속이 회복된다.

---

## 8. 최종 평가

현재 상태는 **"웹앱 UI 프로토타입 + 일부 실제 API 연결"** 단계.
겉보기 품질은 좋지만, 운영 관점에서는 다음 세 계약을 먼저 고쳐야 한다:

- 파이프라인 실행 계약
- 리뷰 후 발행 계약
- 정책 반영 계약

위 3개 계약이 깔끔해진 뒤에야 일반 사용자에게 "신뢰 가능한 운영 도구"라고 부를 수 있다.
