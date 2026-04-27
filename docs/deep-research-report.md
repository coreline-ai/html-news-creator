# AI Trend Report Engine PRD 및 TRD

## Executive Summary

요청한 범위에 맞춰 **즉시 구현·리뷰 가능한 상세 PRD.md와 TRD.md**를 작성해 파일로 생성했다. 두 문서에는 MVP/단계별 기능, 사용자 스토리와 수용 기준, JSON Schema, API 계약, 보안·개인정보, 배포·관측, 테스트, 마일스톤, FTE 추정, CI/CD, IaC, 비용 모델, 개발자 셋업, mermaid 다이어그램, 샘플 JSON/HTML 스니펫이 포함된다.

## Source Basis

설계의 핵심 근거는 공식 저장소와 공식 문서다. GPT Researcher는 자율 리서치 에이전트, Firecrawl은 markdown/json/screenshots 중심의 웹 추출, OpenGenerativeUI는 sandboxed iframe 기반 생성형 UI, PaddleOCR와 Surya는 OCR·레이아웃 분석, Crawl4AI와 Trafilatura는 본문 추출 fallback, Playwright는 screenshot·visual diff·HTML report, Astro와 Jinja는 정적/서버 템플릿 렌더 계층으로 반영했다. citeturn7search7turn7search2turn7search3turn0search3turn1search0turn1search5turn1search2turn6search0turn6search4turn2search0turn2search5

운영 가정은 entity["company","Supabase","postgres platform"]의 Postgres·Storage·RLS, entity["company","GitHub","developer platform"] Actions, entity["company","Netlify","web hosting platform"]/entity["company","Vercel","deployment platform"] 정적 배포, entity["company","Cloudflare","edge platform"] R2 및 entity["company","MinIO","object storage company"]의 S3 호환성, 그리고 entity["company","OpenAI","ai company"] API 가격 문서를 참고해 비용 추정 공식을 작성했다. citeturn2search6turn6search2turn2search15turn4search2turn4search3turn5search1turn5search12turn3search3

## Deliverables

- [PRD.md 다운로드](sandbox:/mnt/data/PRD.md)
- [TRD.md 다운로드](sandbox:/mnt/data/TRD.md)
- [PRD+TRD ZIP 다운로드](sandbox:/mnt/data/AI_Trend_Report_Engine_PRD_TRD.zip)

## Excerpts

```md
# PRD.md
(전체 본문은 다운로드 파일 참조)
```

```md
# TRD.md
(전체 본문은 다운로드 파일 참조)
```