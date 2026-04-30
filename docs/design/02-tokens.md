# 02. Design Tokens

> 모든 색·radius·shadow·spacing 수치의 단일 출처. 새 코드는 여기 정의된 토큰만 사용합니다.

토큰 계층은 [DESIGN.md 4.3.1](../../DESIGN.md)을 따릅니다:

```
Brand → Foundation → Semantic → Component
```

이 문서는 **Foundation + Semantic** 두 층을 정의합니다. Component 층은 [04-components.md](04-components.md)에서 다룹니다.

---

## 1. 색상 (OKLCH)

### 1.1 Foundation Color Scale

표준 그레이스케일. 모든 명도는 OKLCH의 L 값으로 일관 관리.

| 토큰 | OKLCH | 16진 근사 | 용도 |
|---|---|---|---|
| `--gray-0`   | `oklch(1 0 0)`     | `#ffffff` | 순백 (라이트 background) |
| `--gray-50`  | `oklch(0.985 0 0)` | `#fafafa` | 라이트 elevated bg, 다크 foreground |
| `--gray-100` | `oklch(0.97  0 0)` | `#f5f5f5` | 라이트 muted/secondary |
| `--gray-200` | `oklch(0.922 0 0)` | `#ebebeb` | 라이트 border/input |
| `--gray-300` | `oklch(0.708 0 0)` | `#b5b5b5` | 라이트 ring, 다크 muted-foreground |
| `--gray-400` | `oklch(0.556 0 0)` | `#8e8e8e` | 라이트 muted-foreground |
| `--gray-500` | `oklch(0.439 0 0)` | `#707070` | 다크 ring |
| `--gray-700` | `oklch(0.269 0 0)` | `#444444` | 다크 muted/secondary/border |
| `--gray-800` | `oklch(0.205 0 0)` | `#333333` | 라이트 primary/foreground, 다크 card |
| `--gray-900` | `oklch(0.145 0 0)` | `#252525` | 라이트 foreground, 다크 background |

### 1.2 Semantic Tokens — Light

| 토큰 | 값 | 의미 |
|---|---|---|
| `--background` | `oklch(1 0 0)` | 페이지 기본 배경 |
| `--foreground` | `oklch(0.145 0 0)` | 본문 텍스트 |
| `--card` | `oklch(1 0 0)` | 카드 배경 |
| `--card-foreground` | `oklch(0.145 0 0)` | 카드 위 텍스트 |
| `--popover` | `oklch(1 0 0)` | 팝오버/메뉴/툴팁 배경 |
| `--popover-foreground` | `oklch(0.145 0 0)` | 팝오버 위 텍스트 |
| `--primary` | `oklch(0.205 0 0)` | 기본 액션 (버튼) |
| `--primary-foreground` | `oklch(0.985 0 0)` | primary 위 텍스트 |
| `--secondary` | `oklch(0.97 0 0)` | 보조 액션 배경 |
| `--secondary-foreground` | `oklch(0.205 0 0)` | secondary 위 텍스트 |
| `--muted` | `oklch(0.97 0 0)` | 묻힌 영역 (skeleton, disabled) |
| `--muted-foreground` | `oklch(0.556 0 0)` | 묻힌 텍스트 (메타 정보) |
| `--accent` | `oklch(0.97 0 0)` | hover 강조 배경 |
| `--accent-foreground` | `oklch(0.205 0 0)` | accent 위 텍스트 |
| `--destructive` | `oklch(0.577 0.245 27.325)` | 위험·삭제 액션 |
| `--destructive-foreground` | `oklch(0.577 0.245 27.325)` | destructive 위 텍스트 (드물게) |
| `--border` | `oklch(0.922 0 0)` | 모든 1px 구획 |
| `--input` | `oklch(0.922 0 0)` | 입력 보더 |
| `--ring` | `oklch(0.708 0 0)` | 포커스 링 |

### 1.3 Semantic Tokens — Dark

라이트의 L값을 반전한 형태. hue/chroma는 보존.

| 토큰 | 값 |
|---|---|
| `--background` | `oklch(0.145 0 0)` |
| `--foreground` | `oklch(0.985 0 0)` |
| `--card` | `oklch(0.205 0 0)` |
| `--card-foreground` | `oklch(0.985 0 0)` |
| `--primary` | `oklch(0.985 0 0)` |
| `--primary-foreground` | `oklch(0.205 0 0)` |
| `--secondary` | `oklch(0.269 0 0)` |
| `--muted` | `oklch(0.269 0 0)` |
| `--muted-foreground` | `oklch(0.708 0 0)` |
| `--accent` | `oklch(0.269 0 0)` |
| `--destructive` | `oklch(0.637 0.237 25.331)` |
| `--destructive-foreground` | `oklch(0.985 0 0)` |
| `--border` | `oklch(0.269 0 0)` |
| `--input` | `oklch(0.269 0 0)` |
| `--ring` | `oklch(0.439 0 0)` |

### 1.4 Sidebar Tokens (운영 화면 전용)

운영자용 페이지에서 사이드바를 별도 컬러 슬롯으로 관리.

```css
/* light */
--sidebar:                    oklch(0.985 0 0);
--sidebar-foreground:         oklch(0.145 0 0);
--sidebar-primary:            oklch(0.205 0 0);
--sidebar-primary-foreground: oklch(0.985 0 0);
--sidebar-accent:             oklch(0.97 0 0);
--sidebar-accent-foreground:  oklch(0.205 0 0);
--sidebar-border:             oklch(0.922 0 0);
--sidebar-ring:               oklch(0.708 0 0);

/* dark */
--sidebar:                    oklch(0.145 0 0);
--sidebar-foreground:         oklch(0.985 0 0);
--sidebar-primary:            oklch(0.488 0.243 264.376);
--sidebar-primary-foreground: oklch(0.985 0 0);
--sidebar-accent:             oklch(0.269 0 0);
--sidebar-accent-foreground:  oklch(0.985 0 0);
--sidebar-border:             oklch(0.269 0 0);
--sidebar-ring:               oklch(0.439 0 0);
```

### 1.5 Chart Palette (데이터 시각화 전용)

UI 강조에 사용 금지. 차트·그래프·태그 색상에만 사용.

| 토큰 | Light | Dark |
|---|---|---|
| `--chart-1` | `oklch(0.646 0.222 41.116)` (오렌지) | `oklch(0.488 0.243 264.376)` (블루) |
| `--chart-2` | `oklch(0.6 0.118 184.704)` (티얼) | `oklch(0.696 0.17 162.48)` (그린) |
| `--chart-3` | `oklch(0.398 0.07 227.392)` (네이비) | `oklch(0.769 0.188 70.08)` (옐로우) |
| `--chart-4` | `oklch(0.828 0.189 84.429)` (옐로우) | `oklch(0.627 0.265 303.9)` (퍼플) |
| `--chart-5` | `oklch(0.769 0.188 70.08)` (옐로우-오렌지) | `oklch(0.645 0.246 16.439)` (핑크) |

---

## 2. Radius

```css
--radius-sm: 0.375rem;  /* 6px  — 입력, 작은 버튼 */
--radius-md: 0.5rem;    /* 8px  — 기본 버튼, 뱃지 */
--radius-lg: 0px;       /* 카드, 모달, 시트 — 의도적 0 */
--radius-xl: 0px;       /* 동일 */
```

**적용 가이드:**
- 카드(`<Card>`)·다이얼로그·시트는 **항상 0**
- 버튼·입력·뱃지는 **md**(0.5rem)
- 칩·작은 토큰·아이콘 박스는 **sm**(0.375rem)
- 12px 이상 radius 절대 금지

---

## 3. Shadow

```css
--shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px 0 rgb(0 0 0 / 0.06);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -1px rgb(0 0 0 / 0.06);
```

**적용 가이드:**
- 본문 카드: 그림자 없음. `border` 한 줄로만.
- outline 버튼: `shadow-xs`
- 팝오버/드롭다운/툴팁: `shadow-md`
- `shadow-lg` 이상 절대 금지

---

## 4. Spacing

Tailwind 기본 스케일을 그대로 따름. 주요 사용:

| 토큰 | 픽셀 | 주 사용처 |
|---|---|---|
| `--space-1` | 4px | 인라인 간격, 아이콘-텍스트 |
| `--space-2` | 8px | 작은 그룹 간격 |
| `--space-3` | 12px | 카드 내 항목 간격 |
| `--space-4` | 16px | 카드 패딩, 섹션 내부 |
| `--space-6` | 24px | 카드 간 간격 |
| `--space-8` | 32px | 섹션 간 간격 (운영 화면) |
| `--space-12` | 48px | 본문 섹션 간격 (리포트) |
| `--space-16` | 64px | 헤더/푸터 간격 |

---

## 5. Motion

```css
--duration-fast:    120ms;
--duration-base:    180ms;
--duration-slow:    280ms;

--ease-standard:    cubic-bezier(0.4, 0, 0.2, 1);
--ease-emphasized:  cubic-bezier(0.2, 0, 0, 1);
--ease-decelerate:  cubic-bezier(0, 0, 0.2, 1);
```

**적용 가이드:**
- hover/focus 색상 전환: `120ms ease-standard`
- 드롭다운/팝오버 등장: `180ms ease-decelerate`
- 모달/시트 전환: `280ms ease-emphasized`
- 페이지 전환은 fade만 (slide 금지)

---

## 6. Touch Target (모바일)

`@media (pointer: coarse)`에서 최소 크기 강제:

```css
button, [role="button"], input, select, textarea {
  min-height: 44px;
}
```

DESIGN.md 7.6의 "hit target ≥ 44px" 규칙을 그대로 반영.

---

## 7. 토큰 사용 규칙

### Do
- `var(--primary)` / `bg-primary` / `text-foreground` 만 사용
- 새 토큰이 필요하면 이 문서를 먼저 갱신
- 라이트/다크 양쪽 값을 항상 같이 정의

### Don't
- 컴포넌트에서 `oklch()` 직접 호출
- raw hex (`#000000`) 사용
- `--background` 외의 페이지 배경 만들기
- `border` 토큰 무시하고 임의 색 보더 적용

---

## 8. 토큰 추가 절차

1. 이 문서 표에 행 추가
2. [tokens.css](tokens.css)와 [tokens.json](tokens.json)에 라이트·다크 값 추가
3. PR description에 추가 사유 기록
4. 사용 첫 컴포넌트에서 [04-components.md](04-components.md)에 적용 사례 추가
