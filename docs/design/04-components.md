# 04. Components

> 핵심 컴포넌트의 variant·size·상태를 한곳에 정의. shadcn/ui 표준 컴포넌트 패턴을 그대로 채택해 향후 React 도입 시 무축약 호환.

각 컴포넌트는 **HTML/CSS 명세** + **React/shadcn 매핑**을 함께 제공합니다. 자동화 코드젠은 이 표를 기준으로 마크업을 생성합니다.

---

## 1. Button

### 1.1 Variants

| variant | bg | fg | border | hover |
|---|---|---|---|---|
| `default` | `--primary` | `--primary-foreground` | — | `--primary/0.9` |
| `destructive` | `--destructive` | `#fff` | — | `--destructive/0.9` |
| `outline` | `--background` | `--foreground` | `1px solid --border` | bg `--accent`, fg `--accent-foreground` |
| `secondary` | `--secondary` | `--secondary-foreground` | — | `--secondary/0.8` |
| `ghost` | transparent | inherit | — | bg `--accent`, fg `--accent-foreground` |
| `link` | transparent | `--primary` | — | underline |

### 1.2 Sizes

| size | height | px / py | rounded | text |
|---|---|---|---|---|
| `xs` | 24px | 8 / 0 | `--radius-md` | `text-xs` |
| `sm` | 36px | 12 / 0 | `--radius-md` | `text-sm` |
| `default` | 40px | 16 / 8 | `--radius-md` | `text-sm` |
| `lg` | 40px | 24 / 0 | `--radius-md` | `text-sm` |
| `icon` | 40×40 | — | `--radius-md` | — |
| `icon-xs` | 24×24 | — | `--radius-md` | — |
| `icon-sm` | 36×36 | — | `--radius-md` | — |

### 1.3 상태

- **focus-visible**: `border-color: --ring; ring: 3px var(--ring) / 0.5`
- **disabled**: `pointer-events: none; opacity: 0.5`
- **aria-invalid**: `border-color: --destructive; ring: --destructive/0.2`

### 1.4 HTML 예시

```html
<button class="btn btn-default btn-md">
  <svg class="icon" aria-hidden="true">…</svg>
  저장
</button>
```

### 1.5 React (shadcn)

```tsx
<Button variant="default" size="default">저장</Button>
<Button variant="outline" size="sm"><Plus /> 추가</Button>
<Button variant="destructive">삭제</Button>
```

---

## 2. Card

### 2.1 구조

```
<Card>
  <CardHeader>
    <CardTitle />
    <CardDescription />
    <CardAction />          ← 우측 액션
  </CardHeader>
  <CardContent />
  <CardFooter />
</Card>
```

### 2.2 스타일

| 부분 | 토큰 |
|---|---|
| `Card` | `bg: --card; color: --card-foreground; border: 1px solid --border; border-radius: --radius-lg (=0)` |
| `CardHeader` | `padding: 24px; border-bottom: 1px solid --border` (선택) |
| `CardTitle` | `text-base font-semibold leading-snug` |
| `CardDescription` | `text-sm text-muted-foreground` |
| `CardContent` | `padding: 24px` |
| `CardFooter` | `padding: 16px 24px; border-top: 1px solid --border` (선택) |

### 2.3 변형

- **본문 카드**: 그림자 없음, 보더 한 줄. 디폴트.
- **interactive 카드**: hover 시 `bg-accent` 전환 + cursor pointer.
- **outlined 강조**: 보더 색만 `--ring`으로 변경 (focus 상태 표현).

### 2.4 사용 가이드

- 카드 안에 카드 중첩 금지 (radius 0 제약상 시각 위계가 모호해짐)
- 카드 폭은 최소 320px, 권장 360~480px
- 카드 내부 spacing은 `space-3`(12px) ~ `space-6`(24px) 범위

---

## 3. Input / Textarea

### 3.1 스타일

```css
.input {
  height: 40px;          /* default */
  padding: 8px 12px;
  border: 1px solid var(--input);
  border-radius: var(--radius-md);
  background: var(--background);
  color: var(--foreground);
  font-size: 14px;
  transition: border-color var(--duration-fast), box-shadow var(--duration-fast);
}
.input:focus-visible {
  border-color: var(--ring);
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--ring) 50%, transparent);
  outline: none;
}
.input[aria-invalid="true"] {
  border-color: var(--destructive);
}
.input::placeholder {
  color: var(--muted-foreground);
}
```

### 3.2 Sizes

- `sm`: 36px high, 12/8 padding, text-xs
- `default`: 40px high, 12/8 padding, text-sm
- `lg`: 44px high, 16/10 padding, text-sm (모바일 권장)

### 3.3 Textarea

기본 동작 동일. 추가:
```css
textarea {
  min-height: 80px;
  resize: vertical;
  line-height: 1.6;
}
```

---

## 4. Badge

### 4.1 Variants

| variant | bg | fg | border |
|---|---|---|---|
| `default` | `--primary` | `--primary-foreground` | — |
| `secondary` | `--secondary` | `--secondary-foreground` | — |
| `outline` | transparent | `--foreground` | `1px solid --border` |
| `destructive` | `--destructive` | `#fff` | — |

### 4.2 스타일

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  height: 22px;
  padding: 0 8px;
  border-radius: var(--radius-md);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.02em;
  white-space: nowrap;
}
```

### 4.3 사용

- 카테고리 라벨, 상태 표시, 태그
- 카드 우측 상단 또는 제목 inline
- 아이콘은 `size-3` (12px)

---

## 5. Status Badge (도메인 특화)

뉴스레터 도메인에서 자주 쓰는 상태 변형. 운영 워크스페이스의 status pill 패턴을 차용.

| 상태 | 색 | 비고 |
|---|---|---|
| `success` | `oklch(0.65 0.15 145)` (그린) | 추출 성공, 검증 완료 |
| `warning` | `oklch(0.75 0.15 75)` (앰버) | 부분 실패, 낮은 신뢰도 |
| `error` | `--destructive` | 실패, 차단됨 |
| `info` | `oklch(0.55 0.15 240)` (블루) | 정보, 진행 중 |
| `neutral` | `--muted` / `--muted-foreground` | 대기, 미분류 |

```html
<span class="status-badge status-success">
  <span class="dot"></span> 성공
</span>
```

도트(8px 원)는 텍스트 없이 줄 단위로 상태만 표시할 때도 사용.

---

## 6. Sidebar Navigation

### 6.1 구조

```
<aside class="sidebar">
  <SidebarSection label="메인">
    <SidebarNavItem icon="Home" href="/">대시보드</SidebarNavItem>
    <SidebarNavItem icon="FileText" href="/reports" active>리포트</SidebarNavItem>
  </SidebarSection>
  <SidebarSection label="관리">
    <SidebarNavItem icon="Database" href="/sources">소스</SidebarNavItem>
    <SidebarNavItem icon="Settings" href="/policy">편집 정책</SidebarNavItem>
  </SidebarSection>
  <SidebarAccountMenu />
</aside>
```

### 6.2 스타일

```css
.sidebar {
  width: 240px;
  background: var(--sidebar);
  color: var(--sidebar-foreground);
  border-right: 1px solid var(--sidebar-border);
  padding: 16px 12px;
}
.sidebar-section-label {
  font-size: 11px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--muted-foreground);
  padding: 12px 8px 4px;
}
.sidebar-nav-item {
  display: flex;
  align-items: center;
  gap: 8px;
  height: 32px;
  padding: 0 8px;
  border-radius: var(--radius-md);
  font-size: 13px;
  color: var(--sidebar-foreground);
  transition: background var(--duration-fast);
}
.sidebar-nav-item:hover {
  background: var(--sidebar-accent);
  color: var(--sidebar-accent-foreground);
}
.sidebar-nav-item[aria-current="page"] {
  background: var(--sidebar-primary);
  color: var(--sidebar-primary-foreground);
}
.sidebar-nav-item .icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}
```

---

## 7. Breadcrumb

```html
<nav class="breadcrumb" aria-label="Breadcrumb">
  <a href="/">홈</a>
  <span class="separator">/</span>
  <a href="/reports">리포트</a>
  <span class="separator">/</span>
  <span class="current">2026-04-30</span>
</nav>
```

```css
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
}
.breadcrumb a {
  color: var(--muted-foreground);
  text-decoration: none;
}
.breadcrumb a:hover {
  color: var(--foreground);
}
.breadcrumb .separator {
  color: var(--muted-foreground);
  user-select: none;
}
.breadcrumb .current {
  color: var(--foreground);
  font-weight: 500;
}
```

---

## 8. Empty State

빈 화면을 칠 때. 텍스트 + 보조 액션만, 일러스트 금지.

```html
<div class="empty-state">
  <svg class="icon-large" aria-hidden="true">…</svg>
  <h3 class="empty-title">아직 리포트가 없습니다</h3>
  <p class="empty-desc">파이프라인을 실행하면 일일 리포트가 생성됩니다.</p>
  <button class="btn btn-default">지금 실행</button>
</div>
```

```css
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 64px 24px;
  gap: 12px;
}
.empty-state .icon-large {
  width: 32px;
  height: 32px;
  color: var(--muted-foreground);
  margin-bottom: 8px;
}
.empty-state .empty-title {
  font-size: 16px;
  font-weight: 500;
  color: var(--foreground);
}
.empty-state .empty-desc {
  font-size: 14px;
  color: var(--muted-foreground);
  max-width: 360px;
  margin-bottom: 16px;
}
```

---

## 9. Skeleton (로딩)

```css
.skeleton {
  background: var(--muted);
  border-radius: var(--radius-md);
  animation: pulse 1.5s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}
```

너비/높이는 콘텐츠 자리만큼 inline 또는 클래스로 지정.

---

## 10. Dialog / Modal

shadcn 표준 `Sheet`/`Dialog` 패턴.

```css
.dialog-overlay {
  position: fixed;
  inset: 0;
  background: oklch(0 0 0 / 0.5);
  backdrop-filter: blur(2px);
  z-index: 50;
}
.dialog {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(560px, calc(100% - 32px));
  max-height: calc(100vh - 64px);
  background: var(--background);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);  /* = 0 */
  box-shadow: var(--shadow-md);
  z-index: 51;
  display: flex;
  flex-direction: column;
}
.dialog-header {
  padding: 24px 24px 16px;
  border-bottom: 1px solid var(--border);
}
.dialog-content {
  padding: 24px;
  overflow-y: auto;
}
.dialog-footer {
  padding: 16px 24px;
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
```

---

## 11. Table

운영 화면 핵심 컴포넌트.

```css
.table {
  width: 100%;
  font-size: 14px;
  border-collapse: collapse;
}
.table thead th {
  padding: 8px 12px;
  text-align: left;
  font-size: 11px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--muted-foreground);
  border-bottom: 1px solid var(--border);
  background: var(--background);
  position: sticky;
  top: 0;
}
.table tbody td {
  padding: 12px;
  border-bottom: 1px solid var(--border);
}
.table tbody tr {
  transition: background var(--duration-fast);
}
.table tbody tr:hover {
  background: var(--muted);
}
.table tbody tr[data-selected="true"] {
  background: var(--accent);
}
```

행 높이: 36~44px (워크스페이스 표준 밀도).

---

## 12. 컴포넌트 작성 체크리스트

새 컴포넌트를 만들 때 다음을 모두 확인:

- [ ] 토큰 외 raw 색·radius·shadow 사용 안 함
- [ ] 라이트/다크 양쪽에서 같은 위계 유지
- [ ] focus-visible 스타일 정의
- [ ] disabled 상태 정의 (`opacity: 0.5; pointer-events: none`)
- [ ] 모바일 hit target ≥ 44px
- [ ] semantic HTML(`button`/`nav`/`aside`) 사용
- [ ] aria 속성: `aria-label`, `aria-current`, `aria-invalid` 등
- [ ] keyboard 접근: Tab/Shift+Tab/Enter/Space/Escape
