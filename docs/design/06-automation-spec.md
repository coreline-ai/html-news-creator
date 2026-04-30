# 06. Automation Spec

> 자동화 에이전트(LLM 코드젠, 빌드 스크립트, 디자인 도구)가 이 디자인 시스템을 기계적으로 적용할 수 있도록 만든 인터페이스 명세.

이 문서는 **사람이 아닌 도구가 읽는 것**이 목적입니다. 표·룰·예시는 의도적으로 단정적이고 좁게 적습니다.

> **범위 가드**
> 이 명세의 기본 적용 대상은 추가 개발될 웹앱입니다. 현재 정적 HTML 리포트(`templates/report_newsstream.html.j2`, `public/news/*.html`)는 참고 표면이며, 명시적인 마이그레이션 요청 없이는 이 명세를 적용하지 않습니다.

---

## 1. 시스템 메타데이터

```yaml
name: html-news-creator-design-system
version: 1.0.0
basis:
  - shadcn/ui new-york style (OKLCH monochrome convention)
  - DESIGN.md (project-internal standard)
license: MIT
color_space: oklch
font_primary: Pretendard
language_priority: [ko, en]
modes: [light, dark]
primary_target_surfaces:
  - operator_webapp        # 추가 개발될 운영/관리자/대시보드 웹앱
reference_surfaces:
  - daily_report_html      # 현재 정적 HTML 리포트. 기본 적용 대상 아님.
```

---

## 2. 코드젠 입력 컨트랙트

자동화 도구가 화면을 만들 때 받을 입력 형태:

```typescript
interface DesignRequest {
  surface: 'operator_webapp';
  reference_surface?: 'daily_report_html'; // 참고용. 명시적 마이그레이션 작업이 아니면 생성 대상 아님.
  pattern:
    | 'list' | 'detail' | 'kanban' | 'table' | 'dashboard'
    | 'empty_state' | 'form' | 'modal';
  density: 'comfortable' | 'compact';
  intent: string;          // 자연어 한 줄 — 화면이 무엇을 위한 것인가
  data?: Record<string, unknown>;  // 실제 데이터 (있으면 사용, 없으면 placeholder)
  variants?: string[];     // 선택적 variant 키
}
```

자동화 도구는 위 입력을 받아 다음 출력을 만듭니다:

```typescript
interface DesignArtifact {
  html: string;            // 웹앱 화면 마크업 (semantic, accessible). 정적 리포트 HTML 템플릿 아님.
  css?: string;            // 페이지 한정 추가 CSS (필요할 때만)
  tokens_imported: string[];  // 사용한 토큰 키 목록
  components_used: string[];  // 사용한 컴포넌트 이름 목록
  warnings: string[];      // 어긴 규칙·placeholder 사용 이력
}
```

---

## 3. 결정 트리 — 코드젠이 따르는 우선순위

```
1. surface가 operator_webapp?
   → workspace shell (sidebar 240 + main + right 320)
   → density compact (행 36~44px)
   → table/list/kanban 패턴 우선

2. surface가 daily_report_html로 요청되었나?
   → 기본 거부/경고. 현재 HTML 리포트는 이 명세의 기본 적용 대상이 아님.
   → 사용자가 "HTML 리포트 디자인 마이그레이션"을 명시한 경우에만 별도 계획 후 진행.

3. data가 비어 있나?
   → empty_state 패턴 적용
   → "지금 실행" 액션 버튼 1개만

4. 토큰 외 색·radius·shadow가 필요한가?
   → 거부. 기존 토큰으로 표현 가능한지 다시 검토.
   → 정말 필요하면 02-tokens.md에 먼저 추가 후 사용.

5. variant가 명시되었나?
   → 04-components.md의 variant 표 매핑.
   → 없는 variant 요청 시 가장 가까운 표준 variant로 fallback + warning.
```

---

## 4. CSS 변수 사용 강제

자동화 도구가 생성한 CSS에서 다음을 검사:

### Pass 조건
- 색: `var(--background)`, `var(--foreground)`, `bg-primary` 등 토큰만 사용
- radius: `var(--radius-sm/md/lg)`, `rounded-md` 등 토큰만 사용
- shadow: `var(--shadow-xs/sm/md)`, `shadow-xs` 등 토큰만 사용
- spacing: 8의 배수 (0, 4, 8, 12, 16, 24, 32, 48, 64) — `gap-3`, `p-4` 등

### Fail 조건 (warning에 추가)
- raw hex (`#1a1a1a`)
- raw rgb / rgba / hsl
- 직접 `oklch()` 호출
- `border-radius: 12px` 같은 magic number
- `box-shadow: 0 4px 20px rgba(...)` 같은 자유 그림자

자동 검사 정규식 (`scripts/lint_design_tokens.py`로 구현됨, `make lint-design`):

```python
FORBIDDEN_PATTERNS = [
    r'#[0-9a-fA-F]{3,8}\b',                        # hex
    r'rgb[a]?\([^)]+\)',                            # rgb/rgba
    r'hsl[a]?\([^)]+\)',                            # hsl/hsla
    r'oklch\([^)]+\)(?!\s*var\()',                 # oklch outside var
    r'border-radius:\s*(?!0|var\()\d+',            # raw radius
    r'box-shadow:\s*(?!none|var\()',               # raw shadow
]
```

---

## 5. 컴포넌트 → HTML 매핑 표

자동화 도구가 컴포넌트 이름을 받았을 때 생성할 정확한 HTML.

### Button (default + default size)
```html
<button class="btn btn-default" data-variant="default" data-size="default">
  {label}
</button>
```

### Card
```html
<article class="card">
  <header class="card-header">
    <h3 class="card-title">{title}</h3>
    <p class="card-description">{description}</p>
  </header>
  <div class="card-content">
    {children}
  </div>
</article>
```

### Input
```html
<label class="field">
  <span class="field-label">{label}</span>
  <input class="input" type="{type}" placeholder="{placeholder}" />
</label>
```

### Status Badge
```html
<span class="status-badge status-{status}">
  <span class="dot" aria-hidden="true"></span>
  <span class="label">{label}</span>
</span>
```

### Empty State
```html
<div class="empty-state">
  <svg class="icon-large" aria-hidden="true">{icon}</svg>
  <h3 class="empty-title">{title}</h3>
  <p class="empty-desc">{description}</p>
  <button class="btn btn-default">{action}</button>
</div>
```

전체 매핑 표는 [04-components.md](04-components.md)에 있습니다.

---

## 6. 토큰 → Tailwind 클래스 매핑

향후 Tailwind 도입 시 자동화 도구가 사용할 매핑.

| Token | Tailwind utility |
|---|---|
| `var(--background)` | `bg-background` |
| `var(--foreground)` | `text-foreground` |
| `var(--primary)` | `bg-primary` / `text-primary` |
| `var(--primary-foreground)` | `text-primary-foreground` |
| `var(--muted)` | `bg-muted` |
| `var(--muted-foreground)` | `text-muted-foreground` |
| `var(--border)` | `border-border` |
| `var(--ring)` | `ring-ring` |
| `var(--radius-sm)` | `rounded-sm` |
| `var(--radius-md)` | `rounded-md` |
| `var(--radius-lg)` | `rounded-lg` (=0) |
| `var(--shadow-xs)` | `shadow-xs` |

shadcn/ui 표준이므로 [tokens.css](tokens.css)의 `@theme inline` 블록만 import하면 자동으로 활성화됩니다.

---

## 7. 콘텐츠 슬롯 매핑

도메인 데이터 → 화면 슬롯 매핑.

### 일일 리포트 섹션 (참고 전용)

현재 HTML 리포트 데이터 구조를 웹앱에서 미리보기/상세 화면으로 다룰 때 참고합니다. 이 매핑만으로 HTML 리포트 템플릿을 수정하지 않습니다.
```yaml
section:
  category_label:    # 11px uppercase, --muted-foreground
    source: cluster.topic_type
    fallback: "기타"
  title:             # text-xl semibold
    source: cluster.title_ko
    required: true
  fact_summary:      # text-base
    source: cluster.summary_ko
  hero_image:        # 16/9 aspect, border 1px
    source: cluster.image_url
    fallback: app.utils.generated_images
  social_signal:     # status-badge row
    source: cluster.metrics
  source_list:       # text-sm muted-foreground
    source: cluster.sources[]
  implication:       # text-base, italic optional
    source: cluster.implication_ko
```

### 운영 — 리포트 리스트
```yaml
row:
  date:              # text-sm font-medium
    source: report.date_kst
  status:            # status-badge
    source: report.status
    map:
      success: "발행 완료"
      partial: "부분 완료"
      failed: "실패"
  section_count:     # text-sm muted
    source: report.section_count
  generated_at:      # text-xs muted, relative time
    source: report.generated_at
  actions:           # button-icon-sm
    - { type: 'view', icon: 'Eye' }
    - { type: 'rerun', icon: 'RotateCcw' }
```

---

## 8. 자동화 도구 호출 인터페이스

### 8.1 LLM 프롬프트 컨텍스트 (권장 형태)

```
당신은 html-news-creator의 추가 웹앱 화면 코드를 생성합니다. 다음 디자인 시스템을 따릅니다.
현재 정적 HTML 리포트 템플릿은 생성/수정 대상이 아닙니다:

1. 토큰: tokens.css (이 파일을 import한다고 가정)
2. 컴포넌트 매핑: 04-components.md의 표 그대로
3. 레이아웃: 05-layout-patterns.md의 패턴 카탈로그
4. 거부 패턴: 01-philosophy.md의 anti-patterns 섹션

생성 시 다음을 검사:
- 토큰 외 색·radius·shadow 사용 금지
- 카드 radius는 항상 0
- 한 화면에 강조색 1개만
- Pretendard 폰트
- 라이트/다크 양쪽에서 동작

요청: {DesignRequest as YAML}
```

### 8.2 코드젠 후 검증

생성된 웹앱 화면 코드를 다음 순서로 검사:

1. `scripts/lint_design_tokens.py {file}` — 토큰 위반 검사
2. HTML validator — semantic 마크업 확인
3. axe-core / pa11y — 접근성 검사
4. 시각 회귀 테스트 (선택) — Storybook + Chromatic 또는 Playwright snapshot

---

## 9. HTML 리포트 마이그레이션 가드

기존 `templates/report_newsstream.html.j2`는 이 디자인 시스템의 기본 적용 대상이 아닙니다. 아래 절차는 사용자가 명시적으로 HTML 리포트 디자인 마이그레이션을 요청한 경우에만 사용합니다.

### Phase 1. 토큰 임포트
- `<style>` 블록 상단에 `tokens.css` 내용 삽입
- 기존 변수와 충돌 시 새 토큰을 우선

### Phase 2. 컬러 치환
- `color: #FFFFFF` → `color: var(--foreground)`
- `background: #0E0E10` → `background: var(--background)`
- 매뉴얼 다크모드 셀렉터를 `.dark` 토글로 통합

### Phase 3. Radius/Shadow 치환
- `border-radius: 12px` → `var(--radius-md)` 또는 0
- `box-shadow: ...` → `var(--shadow-xs)` 또는 제거

### Phase 4. 폰트 검토
- Pretendard 유지 확인
- size 단계가 type scale에 맞는지 검증
- 잘못된 weight(800/900) 사용 제거

### Phase 5. 컴포넌트 추출
- 반복되는 카드/뱃지 마크업을 04-components.md 표준으로 통일

각 phase는 시각 회귀가 거의 없어야 합니다. 시각 차이가 크면 phase를 더 잘게 쪼갭니다.

---

## 10. 빌드 파이프라인 통합

### 10.1 토큰 빌드

```bash
# tokens.json → tokens.css 생성 (구현됨)
python3 scripts/build_tokens.py
# CI 드리프트 검사:
python3 scripts/build_tokens.py --check
```

### 10.2 린트

```bash
# CI에서 실행
python scripts/lint_design_tokens.py app/ docs/design/
```

### 10.3 PR 자동화

PR에 다음 파일이 변경되면 자동 검사:
- `docs/design/**` → 토큰 빌드 + 린트 자동 실행
- 웹앱 UI 파일 → 린트 자동 실행
- `templates/**.j2`, `public/news/**` → 기본 제외. 명시적 HTML 리포트 마이그레이션 PR에서만 별도 린트
- 새 컴포넌트 추가 시 → 04-components.md 갱신 확인

---

## 11. 버전·호환성

- 이 디자인 시스템 버전: `1.0.0`
- 의존하는 외부 표준:
  - shadcn/ui new-york style (OKLCH monochrome convention, snapshot 2026-04-30)
  - Tailwind CSS v4 (호환은 yes, 강제는 아님)
- breaking change 정책: token 키 삭제·rename은 minor↑ (`1.x → 2.0`)
- 토큰 값 변경(라이트/다크 OKLCH 수정)은 patch↑

---

## 12. 자동화가 어기지 말아야 할 5가지

1. **token outside this guide is invented** — 새 토큰을 만들지 말 것
2. **a card cannot have radius > 0** — 카드는 항상 각진 모서리
3. **only one accent color per screen** — 한 화면에 강조색 1개
4. **content must drive layout** — 빈 공간을 채우려 콘텐츠를 지어내지 말 것
5. **light/dark must mirror in L only** — 다크모드는 L값만 반전, hue/chroma 유지

이 5가지가 깨지면 자동화 도구는 사용자에게 명시적 확인을 받아야 합니다.
