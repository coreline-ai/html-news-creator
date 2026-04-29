# Coreline Agent Codex CLI OAuth Proxy 검토

작성 일시: `2026-04-27 KST`
대상 저장소: `https://github.com/coreline-ai/coreline-agent`
검토 commit: `0248fe148ba7cf17e0e0d8abe0802350bb9be058`

## 결론

`coreline-agent`는 Codex CLI OAuth 기반 프록시 연결에 사용할 수 있다.

핵심은 `codex-backend` provider가 Codex CLI 로그인으로 생성된 `~/.codex/auth.json` OAuth 토큰을 읽고, `coreline-agent-proxy`가 OpenAI 호환 엔드포인트를 제공하는 구조다. 이 경로는 `OPENAI_API_KEY`가 아니라 Codex CLI OAuth 파일을 사용한다.

```text
Codex CLI
  -> Coreline Agent Proxy
     base_url=http://127.0.0.1:4317/openai/v1
     endpoint=/responses
  -> provider router
  -> codex-backend
  -> ~/.codex/auth.json 또는 CODEX_AUTH_PATH
  -> https://chatgpt.com/backend-api/codex/responses
```

## 확인한 사실

### 1. provider 지원

`coreline-agent`는 다음 provider type을 포함한다.

- `codex-backend`: Codex CLI OAuth 파일을 직접 읽어 ChatGPT/Codex backend로 요청한다.
- `codex-cli`: 로컬 `codex exec`를 spawn하는 fallback이다.

Codex CLI에서 다시 프록시를 바라보는 구조라면 기본 경로는 `codex-backend`가 맞다. `codex-cli` fallback을 기본 provider로 두면 `Codex CLI -> proxy -> codex-cli -> Codex CLI` 형태의 재귀 루프 위험이 있다.

### 2. OAuth 파일 탐색 순서

`codex-backend`는 OAuth 토큰 파일을 다음 순서로 찾는다.

1. provider 설정의 `oauthFile`
2. `CODEX_AUTH_PATH`
3. `~/.codex/auth.json`
4. legacy proxy token path: `~/.chatgpt-codex-proxy/tokens.json`

현재 로컬 환경 확인 결과:

- Codex CLI: `codex-cli 0.118.0`
- `~/.codex/auth.json`: 존재
- 권한: `rw-------`
- `~/.codex/config.toml`: 존재

토큰 내용은 출력하지 않았다.

### 3. proxy endpoint

`coreline-agent-proxy`는 Codex CLI custom provider 연결에 필요한 Responses 호환 엔드포인트를 제공한다.

- `POST /openai/v1/responses`
- `POST /openai/v1/chat/completions`
- alias: `POST /v1/responses`
- alias: `POST /v1/chat/completions`

proxy 인증은 `--auth-token` 또는 `PROXY_AUTH_TOKEN`으로 설정할 수 있다. 설정하면 요청에 `Authorization: Bearer <token>` 또는 `x-api-key`가 필요하다.

### 4. Codex CLI 공식 설정과의 호환

OpenAI Codex 공식 문서 기준으로 custom model provider는 `~/.codex/config.toml` 또는 trusted project의 `.codex/config.toml`에서 설정한다.

Codex custom provider의 핵심 필드는 다음과 같다.

- `model_provider`
- `model_providers.<id>.base_url`
- `model_providers.<id>.env_key`
- `model_providers.<id>.wire_api = "responses"`

`wire_api`는 공식 문서상 `responses`만 지원하므로, Codex CLI 연결은 `/openai/v1/responses` 기준으로 검증해야 한다.

## 권장 설정

### 1. Coreline provider 설정

`~/.coreline-agent/providers.yml` 예시:

```yaml
default: chatgpt

providers:
  chatgpt:
    type: codex-backend
    model: gpt-5
    maxContextTokens: 200000
```

커스텀 OAuth 파일을 쓰는 경우:

```yaml
default: chatgpt

providers:
  chatgpt:
    type: codex-backend
    model: gpt-5
    oauthFile: /custom/path/to/auth.json
    maxContextTokens: 200000
```

### 2. proxy 실행

```bash
coreline-agent-proxy --port 4317 --default chatgpt
```

proxy bearer 인증을 켜는 경우:

```bash
coreline-agent-proxy --port 4317 --default chatgpt --auth-token local-dev-only
```

### 3. Codex CLI custom provider 설정

`~/.codex/config.toml` 또는 trusted project의 `.codex/config.toml`:

```toml
model = "gpt-5"
model_provider = "coreline_agent"

[model_providers.coreline_agent]
name = "Coreline Agent Proxy"
base_url = "http://127.0.0.1:4317/openai/v1"
env_key = "CORELINE_AGENT_PROXY_TOKEN"
wire_api = "responses"
request_max_retries = 2
stream_max_retries = 2
stream_idle_timeout_ms = 300000
```

proxy를 `--auth-token local-dev-only`로 실행했다면:

```bash
export CORELINE_AGENT_PROXY_TOKEN=local-dev-only
codex --profile coreline_agent
```

별도 proxy auth를 켜지 않는다면 `env_key`는 dummy bearer 용도로만 쓰일 수 있다. 운영/공유 환경에서는 proxy auth를 켜는 편이 안전하다.

## 검증 결과

`/tmp/coreline-agent`에서 의존성 설치 후 관련 테스트를 실행했다.

```bash
bun install
bun test tests/codex-auth.test.ts \
  tests/cloud-oauth-providers.test.ts \
  tests/proxy-server.test.ts \
  tests/proxy-mapper-openai-responses.test.ts
```

결과:

- 22 pass
- 0 fail
- Codex auth/config reader 테스트 통과
- `codex-backend` provider instantiation 테스트 통과
- OpenAI Responses mapper 테스트 통과
- proxy auth/route 테스트 통과

## 주의 사항

- `codex-backend`는 공식 OpenAI public API가 아니라 `https://chatgpt.com/backend-api/codex/responses` 계열 private backend에 의존한다.
- 장기 안정성, 약관, rate limit, quota 정책은 공식 OpenAI API와 다르게 관리해야 한다.
- 현재 로컬 Codex CLI는 `codex login` 명령을 제공한다. `coreline-agent` 문서에는 일부 `codex auth login` 표기가 있으나, 현재 설치된 `codex-cli 0.118.0` 기준으로는 `codex login`/`codex login status`가 맞다.
- Codex CLI에서 `coreline-agent-proxy`를 호출하고, proxy 기본 provider가 `codex-cli`이면 재귀 루프가 생길 수 있으므로 기본 provider는 `codex-backend`로 둔다.
- 토큰/API 키는 로그와 문서에 출력하지 않는다.

## 현재 개발 계획에 대한 판단

`multi_model_tui`와 비교했을 때 `coreline-agent`는 Codex OAuth proxy 용도에 더 직접적인 문서와 테스트를 갖고 있다.

권장 반영 방식:

- 기본 후보: `multi_model_tui` 유지
- 대안/검증 후보: `coreline-agent-proxy + codex-backend` 추가
- Codex CLI custom provider 검증은 둘 다 `wire_api = "responses"` 기준으로 수행
- `/embeddings`는 두 proxy 모두 핵심 경로가 아니므로 기존대로 `EMBEDDING_PROVIDER=local-hashing` fallback 유지

## 참조

- Coreline Agent GitHub: https://github.com/coreline-ai/coreline-agent
- OpenAI Codex config reference: https://developers.openai.com/codex/config-reference#configtoml
- 검토 소스 파일:
  - `/tmp/coreline-agent/docs/cloud-oauth-providers.md`
  - `/tmp/coreline-agent/docs/proxy-operations.md`
  - `/tmp/coreline-agent/README.md`
  - `/tmp/coreline-agent/src/providers/codex-auth.ts`
  - `/tmp/coreline-agent/src/providers/codex-backend.ts`
  - `/tmp/coreline-agent/src/proxy/server.ts`
