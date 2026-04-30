# 05. Layout Patterns

> 두 표면(일일 리포트 / 운영 웹앱)의 레이아웃 표준. paperclip의 Workspace 레이아웃을 운영 화면에 차용하고, 리포트는 에디토리얼 단일 컬럼.

---

## 1. 기본 그리드

### 1.1 페이지 골격

```
┌─────────────────────────────────────────┐
│         (운영) Sidebar │ Main          │
│         (리포트) Main 단일 컬럼         │
└─────────────────────────────────────────┘
```

### 1.2 Container 폭

| 표면 | 폭 | 비고 |
|---|---|---|
| 일일 리포트 본문 | `max-width: 820px` | 한국어 가독성 최적 (50~75자/줄) |
| 운영 메인 영역 | `max-width: 1440px` | 4 컬럼 그리드 가능 |
| 운영 좁은 화면 | `min-width: 320px` | 모바일 한계 |

### 1.3 Page Padding

- 모바일: `16px`
- 태블릿: `24px`
- 데스크탑: `32px`
- 와이드: `48px` (운영 화면 한정)

---

## 2. 일일 리포트 레이아웃 (현재)

### 2.1 구조

```
─────────────────────
header
  · 날짜
  · 메인 타이틀
  · 통계 (수집 N건 / 클러스터 M개)
─────────────────────
section[1]
  · 카테고리 라벨 (xs uppercase)
  · 제목 (xl semibold)
  · 팩트 요약 (base)
  · 이미지 (full-bleed within container)
  · 소셜 시그널
  · 출처 목록
  · 시사점
─────────────────────
section[2…N]
─────────────────────
footer
  · 메타 정보
  · 다음 리포트 안내
─────────────────────
```

### 2.2 섹션 간격

- 섹션 ↔ 섹션: `space-12` (48px) ~ `space-16` (64px)
- 섹션 내 요소: `space-4` (16px) ~ `space-6` (24px)

### 2.3 이미지 처리

- 폭: container 풀폭 (`width: 100%`)
- aspect-ratio: `16/9` 기본, `4/3` 허용
- border: `1px solid --border`
- border-radius: 0 (에디토리얼)
- 캡션: 이미지 아래 `text-xs text-muted-foreground` 정렬 left

### 2.4 다크모드 토글

```html
<button class="theme-toggle" aria-label="테마 전환">
  <svg class="icon-sun">…</svg>
  <svg class="icon-moon">…</svg>
</button>
```

```js
// localStorage + prefers-color-scheme 자동 감지
const stored = localStorage.getItem('theme');
const dark = stored
  ? stored === 'dark'
  : window.matchMedia('(prefers-color-scheme: dark)').matches;
document.documentElement.classList.toggle('dark', dark);
```

---

## 3. 운영 웹앱 레이아웃 (향후)

### 3.1 Workspace Shell (paperclip 패턴)

```
┌──────┬─────────────────────────┬──────────┐
│      │ Breadcrumb     Toolbar  │          │
│  Si  ├─────────────────────────┤  Right   │
│  de  │                         │  Panel   │
│  ba  │   Main Content          │  (선택)  │
│  r   │                         │          │
│ 240  │                         │   320    │
└──────┴─────────────────────────┴──────────┘
```

### 3.2 Sidebar (240px)

- 폭 고정 240px (CSS 변수 `--sidebar-width: 240px`)
- 모바일에서 sheet로 전환 (`@media (max-width: 768px)`)
- 섹션 헤더 + 항목 리스트 + 하단 계정 메뉴
- 항목당 32px 높이, 8px 패딩

### 3.3 Header Bar

```css
.header-bar {
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  border-bottom: 1px solid var(--border);
  background: var(--background);
  position: sticky;
  top: 0;
  z-index: 10;
}
```

좌: 브레드크럼 / 우: 검색·알림·계정 메뉴.

### 3.4 Right Panel (320px, 선택적)

상세 정보·코멘트·메타데이터 패널.

```css
.right-panel {
  width: 320px;
  border-left: 1px solid var(--border);
  background: var(--background);
  overflow-y: auto;
}
```

토글 가능. 모바일에서는 다이얼로그/시트.

### 3.5 Main Content Variants

| 패턴 | 사용처 | 그리드 |
|---|---|---|
| **List** | 소스/리포트 목록 | 단일 컬럼 행 |
| **Kanban** | 클러스터 검토 워크플로우 | 3~5 컬럼 |
| **Table** | 정밀 데이터 (큐타스/메트릭) | 풀폭 테이블 |
| **Detail** | 단일 항목 상세 | 본문 + 사이드 메타 |
| **Dashboard** | 메트릭 카드 그리드 | 12 컬럼 grid |

---

## 4. 정보 위계 표준

### 4.1 카드 그리드 (대시보드)

```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}
```

`auto-fit` + `minmax(280px, 1fr)`로 컬럼 수 자동 조정.

### 4.2 마스터-디테일

```
┌───────────────┬──────────────────────┐
│ List (320px)  │ Detail (남은 폭)     │
│  - item       │                      │
│  - item ✓     │  (선택된 item 상세)  │
│  - item       │                      │
└───────────────┴──────────────────────┘
```

리스트는 폭 고정, 디테일은 flex-grow.

### 4.3 분할 비율

- 좌 사이드(메뉴): 240px 고정
- 좌 리스트(데이터): 320~360px 고정
- 우 패널(메타): 280~320px 고정
- 메인 영역: 나머지 flex (최소 480px)

---

## 5. 반응형 단계

DESIGN.md 4.3.1의 "반응형은 밀도 변화로" 원칙 적용.

### 5.1 Breakpoint

| 이름 | min-width | 용도 |
|---|---|---|
| `sm` | 640px | 큰 모바일 / 작은 태블릿 |
| `md` | 768px | 태블릿 |
| `lg` | 1024px | 작은 데스크탑 |
| `xl` | 1280px | 데스크탑 |
| `2xl` | 1536px | 와이드 |

### 5.2 변환 규칙

| 데스크탑 패턴 | 모바일 변환 |
|---|---|
| Sidebar (240px) | Sheet (드로어) |
| Right Panel (320px) | Dialog (모달) |
| Master-Detail | 풀스크린 화면 전환 |
| 멀티 컬럼 카드 그리드 | 단일 컬럼 |
| Table | 카드 변환 (각 행 = 카드) |
| Toolbar 가로 | 하단 고정 ActionBar |

### 5.3 모바일 전용 컴포넌트

- `MobileBottomNav` — 하단 고정 5개 이내 메인 네비게이션 (paperclip 패턴)
- `SwipeToArchive` — 스와이프 액션
- `BottomSheet` — 모바일 시트

---

## 6. 스크롤 정책

### 6.1 페이지 스크롤

- 운영 화면은 `body { overflow: hidden }` + 메인 영역만 스크롤 (paperclip 패턴)
- 리포트는 정상적인 `body` 스크롤

### 6.2 스크롤바

```css
/* paperclip 패턴 — 다크모드 전용 커스텀 */
.dark *::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.dark *::-webkit-scrollbar-track {
  background: oklch(0.205 0 0);
}
.dark *::-webkit-scrollbar-thumb {
  background: oklch(0.4 0 0);
  border-radius: 4px;
}

/* auto-hide: 공간은 reserve, 호버 시만 보임 */
.scrollbar-auto-hide::-webkit-scrollbar { width: 8px; background: transparent; }
.scrollbar-auto-hide::-webkit-scrollbar-thumb { background: transparent; }
.scrollbar-auto-hide:hover::-webkit-scrollbar-thumb { background: var(--muted-foreground); }
```

---

## 7. 빈 공간(Whitespace) 규칙

### 7.1 Vertical Rhythm

- 같은 그룹 내: `space-2` (8px) ~ `space-3` (12px)
- 섹션 내: `space-4` (16px) ~ `space-6` (24px)
- 섹션 간: `space-8` (32px) ~ `space-12` (48px)
- 페이지 시작/끝: `space-16` (64px)

### 7.2 Horizontal Rhythm

- inline 요소: `space-1` (4px) ~ `space-2` (8px)
- 카드 내 패딩: `space-4` (16px) ~ `space-6` (24px)
- 컬럼 간격(grid gap): `space-4` (16px) ~ `space-8` (32px)

### 7.3 빈 공간 부풀리기 금지

DESIGN.md 4.2 원칙 3 — 화면이 비어 보이면 spacing이 아닌 콘텐츠 위계를 다시 봅니다. `padding: 96px` 같은 과도한 패딩 금지.

---

## 8. Z-Index 스케일

```css
--z-base:       0;     /* 일반 요소 */
--z-sticky:     10;    /* sticky header, table thead */
--z-dropdown:   20;    /* 드롭다운, 툴팁 */
--z-popover:    30;    /* 팝오버, 컨텍스트 메뉴 */
--z-overlay:    50;    /* dialog overlay */
--z-modal:      51;    /* dialog content */
--z-toast:      60;    /* toast / snackbar */
```

토큰을 벗어나는 z-index 사용 금지.

---

## 9. 적용 예시

### 9.1 일일 리포트 컨테이너

```html
<body class="bg-background text-foreground">
  <main class="report-container">
    <header class="report-header">…</header>
    <article class="report-section">…</article>
    <article class="report-section">…</article>
    <footer class="report-footer">…</footer>
  </main>
</body>
```

```css
.report-container {
  max-width: 820px;
  margin: 0 auto;
  padding: 32px 16px;
}
.report-section + .report-section {
  margin-top: 64px;
  padding-top: 48px;
  border-top: 1px solid var(--border);
}
```

### 9.2 운영 워크스페이스 셸

```html
<body class="workspace">
  <aside class="sidebar">…</aside>
  <div class="workspace-main">
    <header class="header-bar">…</header>
    <div class="content-area">
      <section class="content-main">…</section>
      <aside class="right-panel">…</aside>
    </div>
  </div>
</body>
```

```css
.workspace {
  display: grid;
  grid-template-columns: 240px 1fr;
  height: 100vh;
  overflow: hidden;
}
.workspace-main {
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.content-area {
  display: grid;
  grid-template-columns: 1fr 320px;
  overflow: hidden;
}
.content-main {
  overflow-y: auto;
  padding: 24px;
}
.right-panel {
  overflow-y: auto;
  border-left: 1px solid var(--border);
}
```
