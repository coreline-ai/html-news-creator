# Implementation Plan: Dashboard "Run history & Calendar" 카드

> Run history와 발행 달력을 한 카드 안에서 좌우 분할(`1fr 280px`)로 통합. 탭으로 월별 ↔ 90일 추세 전환.
> Generated: 2026-05-01
> Project: html-news-creator
> Source 시안: 사용자 컨펌 — `Run history (좌, flex) | divider | Calendar (우, 280px)` 단일 카드

---

## 1. Context

### 1.1 Why
- Dashboard에서 운영자는 "최근 실행 내역"과 "발행 추세"를 동시에 보고 싶다.
- 별도 우측 패널은 시각 잡음 + 화면 폭 차지.
- 한 카드 안에서 vertical divider로 분할하면 동선이 짧고 시선이 한 곳에 모인다.

### 1.2 Current State
- `ui/src/pages/Dashboard.tsx`에 "Recent runs" 표가 단일 컬럼으로 풀폭.
- 달력은 어디에도 없음.
- shadcn Tabs는 Phase 0에서 설치됨 (`ui/src/components/ui/tabs.tsx`).
- shadcn Calendar는 미설치 (react-day-picker 의존).

### 1.3 Target State
- Dashboard "Run history" 자리에 신규 카드 — 좌측 표 + 우측 280px 달력 패널.
- 우측 패널 상단 탭: `월별 달력` / `90일 추세`. 활성 탭은 localStorage에 영속.
- 두 view 모두 cell 클릭 → `/reports/{date}` 이동.
- 모바일(<768px)에서 좌우를 위/아래로 stack.

### 1.4 Scope
- **In**: `ReportCalendar` 컴포넌트 신규, Dashboard 카드 grid 변경, shadcn `calendar` install, KST helper 활용, 단위 테스트.
- **Out**: 페이지/라우트 추가, 백엔드 변경, 데이터 모델 변경, 다른 화면(Reports/Sources/Settings) 변경.

---

## 2. Architecture

### 2.1 Card 내부 구조

```
┌── Card (border 1px var(--border), rounded-none) ──────────────────────┐
│ Header  px-6 py-3 border-b                                            │
│   "Run history & Calendar"                              [Today]       │
├──────────────────────────────────┬────────────────────────────────────┤
│ Left pane                        │ Right pane                         │
│   flex: 1, overflow-y: auto       │   w-[280px] border-l shrink-0      │
│   Run history 표                  │   Tabs (월별 / 90일 추세)         │
│   ─ DATE / STATUS / SEC / TIME    │   selected TabContent             │
│   ─ row click → /reports/{date}   │     · MonthView (shadcn Calendar) │
│                                   │     · HeatmapView (자체 grid)     │
└──────────────────────────────────┴────────────────────────────────────┘
```

### 2.2 데이터 흐름

```
useReports({ limit: 90 })
  → reports[]
  → useMemo: statusByDate: Map<"YYYY-MM-DD", "published"|"draft"|"failed">
  ├─→ Run history 표 (latest 7~10건)
  └─→ ReportCalendar 두 view 모두 같은 Map 활용
```

### 2.3 신규 파일

| 파일 | 용도 |
|---|---|
| `ui/src/components/ReportCalendar.tsx` | Tabs + 두 view 래퍼 (~120 LOC) |
| `ui/src/components/ReportCalendar.MonthView.tsx` | shadcn Calendar 래퍼 + status modifier (~80 LOC) |
| `ui/src/components/ReportCalendar.HeatmapView.tsx` | 자체 div grid heatmap (~100 LOC) |
| `ui/src/components/ui/calendar.tsx` | shadcn Calendar primitive (new-york 표준 구현) |
| `ui/src/__tests__/ReportCalendar.test.tsx` | vitest — Tabs 전환 / status mapping / cell click |

### 2.4 수정 파일

| 파일 | 변경 |
|---|---|
| `ui/src/pages/Dashboard.tsx` | Run history 카드를 `1fr 280px` grid로 변경 + 우측 pane에 `<ReportCalendar />` 마운트 + 모바일 stack |
| `ui/src/lib/store.ts` | persist slice에 `calendarTab: "month" \| "heatmap"` 추가 |
| `ui/package.json` | `react-day-picker` (>=9), `date-fns` (>=3) 추가 |

---

## 3. Tasks

### Phase 0 — 의존성 + shadcn primitive
- [ ] `cd ui && npm i react-day-picker date-fns`
- [ ] `ui/src/components/ui/calendar.tsx` 신규 — shadcn new-york 표준 Calendar (DayPicker 기반). 디자인 토큰만 사용, 카드 radius 0, 셀 hover `bg-accent`, today 강조 `ring-1 ring-ring`.

### Phase 1 — Calendar 컴포넌트
- [ ] `ui/src/components/ReportCalendar.tsx` — Card + Tabs 래퍼. `useReports({limit: 90})` 한 번 호출, `statusByDate` Map 계산, 두 view에 prop 전달.
- [ ] `ReportCalendar.MonthView.tsx` — `<Calendar>` + `modifiers` 3개 (`published`/`draft`/`failed`). `modifiersClassNames`로 status 토큰 적용 (`after:` pseudo-element 점). `onDayClick` → `navigate(/reports/{ISO})`.
- [ ] `ReportCalendar.HeatmapView.tsx` — 7행 × 13~14열 div grid. 각 셀 `data-date`, hover 시 툴팁(`title`), click → 라우트.
- [ ] 색상: `--status-success` / `--status-warning` / `--status-error` / `--muted`. 직접 hex/oklch 사용 0건.

### Phase 2 — Dashboard 통합
- [ ] `Dashboard.tsx`에서 기존 "Recent runs" 카드를 `<RunHistoryAndCalendarCard>` (또는 인라인)로 교체.
- [ ] 카드 내부: `grid grid-cols-1 md:grid-cols-[1fr_280px]`. 모바일에서 위/아래 stack.
- [ ] Left pane: 기존 Run history 표 그대로. Right pane: `<ReportCalendar />`.

### Phase 3 — Persist + KST 정합
- [ ] `lib/store.ts`에 `calendarTab` slice 추가 (기존 persist 패턴 차용, version=1).
- [ ] 모든 날짜 변환은 `@/lib/kst::todayKstISO`, `formatKstDateTime` 활용. `react-day-picker`의 Date 객체 ↔ ISO 변환 헬퍼 한 군데에 (`isoFromDate(d)`, `dateFromIso(s)`).

### Phase 4 — 테스트
- [ ] `__tests__/ReportCalendar.test.tsx` 5 케이스:
  - 초기 렌더 — 월별 탭 활성 (default)
  - 탭 클릭 → 90일 view 전환 + localStorage `calendarTab` 갱신
  - status Map 적용 — 발행된 날짜에 `data-published`/색상 modifier
  - 셀 클릭 → `navigate(/reports/{date})` 호출
  - 빈 데이터 — 모든 날짜가 "없음" 상태로 렌더, 에러 0
- [ ] 기존 `Dashboard.test.tsx` 회귀 0건 — 새 카드 grid에 적응.

---

## 4. Success Criteria

- 카드 헤더 "Run history & Calendar" 단일 카드 안에서 좌우 280px 분할 노출.
- 월별 탭에서 발행된 날짜에 status 토큰 색 점, 미발행은 muted.
- 90일 탭에서 7×13 grid, 어제까지 90일 표시.
- 두 view에서 동일 셀 클릭 시 `/reports/{ISO}` 정확 이동.
- 페이지 새로고침 후 직전에 본 탭 자동 복원.
- design-token lint clean (raw color 0건).
- 모바일 width 375px에서 좌우가 위/아래로 stack, 가로 스크롤 0.

---

## 5. Test Cases (TC)

- [ ] TC-1: 월별 탭에서 5/1자가 발행 상태 dot로 표시
- [ ] TC-2: 90일 탭에서 5/1자 셀이 `█` (published) 색상
- [ ] TC-3: ⌘ 클릭 또는 Enter 키로 셀 활성 시 `/reports/2026-05-01` 이동
- [ ] TC-4: 새로고침 후 active tab이 직전 선택 그대로 (`calendarTab` localStorage)
- [ ] TC-E1: API 에러 시 카드 본문에 "달력을 불러오지 못했습니다" + 재시도 버튼 (좌측 표는 자체 에러 처리)
- [ ] TC-E2: 빈 reports — 두 view 모두 깨지지 않고 모두 muted dot

---

## 6. Testing Instructions

```bash
cd ui
npm install         # react-day-picker / date-fns 추가
npm run typecheck
npm run build
npm run test -- --run src/__tests__/ReportCalendar.test.tsx src/__tests__/Dashboard.test.tsx
make lint-design    # 새 컴포넌트가 토큰만 쓰는지 확인
```

라이브 smoke (사용자 직접):
```bash
make ui-build && make serve   # 8000
open http://127.0.0.1:8000/
# 1) 첫 진입 시 월별 탭. 5/1에 dot 확인.
# 2) 90일 추세 탭 클릭 → 셀 grid 표시. 새로고침 후에도 그 탭 유지.
# 3) 임의 셀 클릭 → ReviewReport로 이동.
```

**테스트 실패 시 워크플로우**: 에러 분석 → 근본 원인 수정 → 재테스트 → 모든 테스트 통과 후 push.

---

## 7. Edge Cases & Risks

| 위험 | 완화 |
|---|---|
| `react-day-picker` v9의 className API 변경 | shadcn 표준 `calendar.tsx` 그대로 차용 (toolkit-tested) |
| 90일 grid가 280px에 안 들어감 | 셀 폭 16px 고정, gap 2px로 13~14열 보장. 큰 폰트(접근성 모드)에서는 셀 폭 동일 + 가로 스크롤 허용 |
| 셀 hover 시 정보량 부족 | `title=` 또는 shadcn `Tooltip` (이미 설치됨)로 날짜·상태·섹션 수 노출 |
| 시간대 혼동 (UTC vs KST) | 모든 변환 `@/lib/kst` 단일 출처 |
| 빈 reports → "1년 내내 미발행"으로 보이는 시각 오해 | 상단에 "데이터 90일치 기준" 한 줄 노출 |

---

## 8. Execution Rules

1. **단일 출처 토큰**: 새 컴포넌트가 만든 색·radius·shadow 0건. 모두 `var(--*)` 또는 `bg-*` 토큰 클래스.
2. **No-Modification Zone**: `templates/`, `app/`, `data/` 직접 수정 금지. 데이터는 기존 `useReports` hook으로만.
3. **react-day-picker 표준**: shadcn 가이드의 setup 그대로. 자체 fork 금지.
4. **모바일 우선 grid**: `grid-cols-1 md:grid-cols-[1fr_280px]` — 데스크톱이 미디어쿼리로 추가.
5. **commit 단일**: phase 4건이지만 logical 변경 한 묶음이라 1 commit으로 OK.

---

## 9. 추정

| 항목 | 추정 |
|---|---|
| 신규 파일 | 5 (`ReportCalendar*.tsx` 3 + shadcn `calendar.tsx` + 테스트 1) |
| 수정 파일 | 3 (`Dashboard.tsx`, `lib/store.ts`, `package.json`) |
| 신규 LOC | ~480 |
| 신규 deps | `react-day-picker@^9`, `date-fns@^3` |
| 시간 (단독 에이전트) | ~50분 |

---

## 10. 시안 (참조)

```
┌── Run history & Calendar                                   [Today] ──┐
├──────────────────────────────────┬──────────────────────────────────┤
│ DATE      STATUS  SEC  TIME      │ ┌──────┬─────────────┐           │
│ 05-01     ✓       6   07:54     │ │▸월별 │ 90일 추세    │           │
│ 04-30     ✓      10   20:58     │ └──────┴─────────────┘           │
│ 04-29     ✓      10   19:25     │                                   │
│ 04-28     !       7   22:38     │ 2026 May        ◀ Apr ▶          │
│ 04-27     ✓      10   23:34     │ ───────────────────              │
│ 04-26     ✓       9   23:30     │  일 월 화 수 목 금 토              │
│ 04-25     ✓      10   23:35     │              ●1                  │
│ ...                              │  2  3  4  5  6  7  8             │
│                                  │  ·  ·  ·  ·  ·  ·  ·             │
│                                  │  ...                              │
│                                  │ ●발행  ⚠부분  ✗실패  · 없음       │
│                                  │       1 / 31 발행                │
└──────────────────────────────────┴──────────────────────────────────┘
```

---

## 11. 후속 후보 (out of scope, 별도 계획)

- 셀에 섹션 수 강도(0~10) 4단계 색 (현재는 이진).
- 우측 pane 폭을 사용자가 드래그로 조정 (`react-resizable-panels`).
- 달력에서 멀티-셀 선택 → 일괄 re-publish 액션.
