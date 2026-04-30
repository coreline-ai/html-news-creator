# 03. Typography

> 한국어 본문 가독성을 최우선. paperclip의 system-stack을 거부하고 **Pretendard**를 시스템 표준 폰트로 채택.

## 1. 폰트 스택

```css
--font-display: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont,
                "Apple SD Gothic Neo", "Malgun Gothic", "Noto Sans KR", sans-serif;
--font-body:    var(--font-display);
--font-mono:    "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
```

**근거:**
- Pretendard는 한글·영문·숫자가 메트릭상 잘 어울리며 weight 9단계 + variable axis 제공
- `templates/report_newsstream.html.j2`가 이미 Pretendard를 로드 중 — 호환성 유지
- system-ui는 OS별 가독성 차이가 심해 일일 리포트에 부적합

## 2. Type Scale

8단계 타입 램프. paperclip은 14·16·18·24가 주력이지만 우리는 한국어 본문 + 에디토리얼 포맷이라 한 단계씩 보정.

| 토큰 | px | rem | line-height | weight | 사용처 |
|---|---|---|---|---|---|
| `text-xs` | 12 | 0.75 | 1.5 | 500 | 메타 정보, 캡션, 카테고리 라벨 |
| `text-sm` | 14 | 0.875 | 1.5 | 400 | 보조 본문, 폼 라벨, 표 셀 |
| `text-base` | 16 | 1.0 | 1.6 | 400 | 기본 본문 |
| `text-lg` | 18 | 1.125 | 1.6 | 500 | 강조 본문, 섹션 도입 문장 |
| `text-xl` | 20 | 1.25 | 1.45 | 600 | 카드 제목, 작은 섹션 제목 |
| `text-2xl` | 24 | 1.5 | 1.35 | 600 | 페이지 제목, 큰 섹션 제목 |
| `text-3xl` | 30 | 1.875 | 1.25 | 700 | 리포트 메인 타이틀 |
| `text-4xl` | 36 | 2.25 | 1.2 | 700 | 히어로 영역 (선택) |

## 3. Font Weight

| 토큰 | 값 | 사용 |
|---|---|---|
| `font-normal` | 400 | 본문 기본 |
| `font-medium` | 500 | 강조, 폼 라벨, 작은 제목 |
| `font-semibold` | 600 | 카드/섹션 제목 |
| `font-bold` | 700 | 페이지 타이틀, 매우 강한 강조 |

> **금지**: `font-extrabold`(800), `font-black`(900) 사용 금지. 한국어에서 시각 잡음이 너무 큼.

## 4. Line Height & Letter Spacing

```css
--leading-tight:    1.2;   /* 큰 제목 */
--leading-snug:     1.35;  /* 중간 제목 */
--leading-normal:   1.5;   /* 보조 본문 */
--leading-relaxed:  1.6;   /* 본문 (기본) */
--leading-loose:    1.75;  /* 긴 글, 인용 */

--tracking-tight:   -0.01em;  /* 큰 제목 */
--tracking-normal:  0;        /* 본문 */
--tracking-wide:    0.02em;   /* uppercase 라벨 */
```

**기본값:**
- 본문: `leading-relaxed` (1.6) + `tracking-normal`
- 제목: `leading-tight` (1.2) + `tracking-tight` (-0.01em)
- 캡션·라벨: `leading-normal` (1.5)

## 5. Text Wrap & Balance

```css
h1, h2, h3 {
  text-wrap: balance;
}
p {
  text-wrap: pretty;
}
```

paperclip의 `text-wrap: balance` 패턴을 그대로 채택. 제목은 줄 길이가 균형있게, 본문은 끊김이 자연스럽게.

## 6. 인쇄·임베드 시 안전 폰트

리포트 HTML이 외부 메일/임베드로 갈 때 Pretendard가 로드 안 될 수 있음. **fallback 체인이 필수**:

```
Pretendard → Apple SD Gothic Neo → Malgun Gothic → Noto Sans KR → sans-serif
```

각 환경에서 다음 폰트로 fallback:
- macOS: Apple SD Gothic Neo
- Windows: Malgun Gothic
- Android/Linux: Noto Sans KR
- 기타: sans-serif

## 7. 두 표면별 사용 패턴

### A. 일일 리포트 (현재 출력 HTML)

| 요소 | 클래스/스타일 | 비고 |
|---|---|---|
| 메인 타이틀 | `text-3xl font-bold leading-tight` | "AI 트렌드 핵심 요약" |
| 섹션 제목 | `text-xl font-semibold leading-snug` | 클러스터 제목 |
| 본문 | `text-base font-normal leading-relaxed` | 팩트 요약 |
| 메타/소셜 | `text-sm text-muted-foreground` | 시그널, 시각, 출처 |
| 캡션 | `text-xs text-muted-foreground tracking-wide uppercase` | 카테고리 라벨 |

### B. 운영 웹앱 (향후)

paperclip 패턴 — 더 작고 조밀하게.

| 요소 | 클래스 |
|---|---|
| 페이지 제목 | `text-2xl font-semibold` |
| 카드 제목 | `text-base font-medium` |
| 표 헤더 | `text-xs font-medium uppercase tracking-wide text-muted-foreground` |
| 표 셀 | `text-sm font-normal` |
| 보조 정보 | `text-xs text-muted-foreground` |
| 빈 상태 | `text-sm text-muted-foreground italic` |

## 8. Code & Mono

코드/JSON/CLI 출력은 monospace.

```css
code, pre, kbd {
  font-family: var(--font-mono);
  font-size: 0.9em;  /* 본문 대비 살짝 작게 */
}
pre {
  background: var(--muted);
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-md);
  overflow-x: auto;
  line-height: 1.5;
}
code {
  background: var(--muted);
  padding: 0.125em 0.375em;
  border-radius: var(--radius-sm);
}
```

## 9. 접근성

- 본문 16px 미만 사용 금지 (메타·캡션 제외)
- 본문 컬러 contrast ratio ≥ 4.5:1 (`--foreground` on `--background`는 ~14:1로 충분)
- 폰트 weight를 색 대신 강조에 우선 사용 (저시력 사용자 대응)

## 10. 운영 규칙

- 화면 하나에 type scale 단계는 **3개 이하**
- 한 컴포넌트 안에서 weight 변화는 **2개 이하**
- 정렬은 `text-left` 기본, `text-center`는 빈 상태·히어로에만
