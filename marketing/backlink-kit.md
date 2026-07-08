# Backlink Kit — StackFreeks Tools

> 만든 날: 2026-07-08. 아래 카피는 붙여넣기용. 등록은 계정이 필요해서 직접 진행.
> 완료하면 체크박스에 표시.

## 1. Product Hunt (효과 최대 — 화·수·목 발행 추천)

- [ ] https://www.producthunt.com/posts/new

**Name**: StackFreeks Tools
**Tagline** (60자 이내): `45 free browser-based tools for developers and sysadmins`
**Description**:

> A collection of 45 free tools for developers, sysadmins, and VPS users — cost
> calculators (VPS, game servers, object storage), config generators (nginx, SSH,
> Dockerfile, firewall rules), and everyday dev utilities. Everything runs 100%
> in your browser: no signup, no server, no data sent anywhere. Built as pure
> static HTML/CSS/JS, English + Korean.

**Topics**: Developer Tools, Web App, Productivity
**First comment** (maker comment):

> Hi PH! I built these because most "free online tools" are ad-stuffed and slow.
> Every tool here is a single static page — works offline once loaded, nothing
> leaves your browser. The niche ones I'm most proud of: a game server cost
> calculator (RAM by player count for Minecraft/Valheim/Rust), a Docker RAM
> calculator, and an object storage cost comparator. Feedback welcome — what
> tool is missing?

## 2. Hacker News — Show HN (사이트 전체 말고 니치 툴 하나로)

- [ ] https://news.ycombinator.com/submit

**Title**: `Show HN: Game server cost calculator – VPS cost by player count`
**URL**: `https://tools.stackfreeks.com/tools/game-server-cost-calculator/`
**First comment**:

> I run game servers for friends and always ended up guessing RAM. This
> calculates the VPS spec + monthly cost from game and player count
> (Minecraft, Valheim, Rust, ARK, CS2...). Estimates are community-sourced;
> corrections welcome. Pure static page, no backend.

실패해도 손해 없음. 몇 주 뒤 docker-ram-calculator로 한 번 더 가능.

## 3. dev.to 글 (가입만 하면 발행 가능, 트래픽+링크)

- [ ] https://dev.to/new

**Title**: `I built 45 free static dev tools with no backend — lessons learned`
**개요** (본문은 빌드 스토리로 4~6문단):

1. 왜: 광고범벅 툴 사이트에 지쳐서 / 정적 HTML이면 충분하다
2. 스택: 순수 HTML/CSS/JS + Cloudflare Pages — 빌드 없음, $0 호스팅
3. 배운 것: JSON-LD/FAQ 스키마, 크로스링크, i18n을 정적으로 처리한 방법
4. 니치 툴이 범용 툴보다 낫다는 깨달음 (경쟁 얘기)
5. 링크: 대표 툴 3~4개 + 사이트

## 4. 디렉터리 등록 (각 10분, 한 번만)

- [ ] **AlternativeTo** — https://alternativeto.net/manage-item/ — 주요 툴 5개 개별 등록
      (vps-cost-calculator, game-server-cost-calculator, docker-ram-calculator,
       cron-builder, subnet-calculator)
- [ ] **SaaSHub** — https://www.saashub.com/submit
- [ ] **Uneed** — https://www.uneed.best/submit-a-tool
- [ ] **Fazier** — https://fazier.com/submit

## 5. 레딧 플레이북 (룰: 답변으로 등장, 홍보 금지)

| 서브레딧 | 매칭 툴 | 노리는 스레드 유형 |
|---|---|---|
| r/admincraft | game-server-cost-calculator | "how much RAM for X players" |
| r/selfhosted | docker-ram-calculator, cron-builder | "VPS sizing", "docker memory" |
| r/homelab | linux-swap-calculator, subnet-calculator | 네트워크/메모리 질문 |
| r/webdev | og-meta-generator (가끔만) | OG 태그 질문 |

- 계정에 링크 없는 일반 답변 5~10개 먼저 쌓고 시작
- 링크는 답변 맥락에 자연스러울 때만, 월 몇 회 이내
- 같은 링크 반복 투척 금지 (밴 리스크)

## 블로그 → 툴 역링크 (stackfreeks.com 쪽 작업)

툴 → 블로그 링크는 완료(2026-07-08). 반대 방향은 WordPress 글에 넣어야 함.
기존 글에 아래 툴 링크 삽입 추천 (글 수정 또는 다음 리라이트 때):

| 블로그 글 | 삽입할 툴 링크 |
|---|---|
| vultr-pricing-2026 | /tools/vps-cost-calculator/ |
| best-cheap-vps-2026 | /tools/vps-cost-calculator/, /tools/vps-bandwidth-calculator/ |
| vultr-object-storage-2026 | /tools/object-storage-calculator/ |
| deploy-docker-vultr-vps | /tools/docker-ram-calculator/, /tools/dockerfile-generator/ |
| vultr-firewall-setup | /tools/firewall-rule-builder/, /tools/subnet-calculator/ |
| self-host-n8n-vultr | /tools/cron-builder/ |
| deploy-nodejs-vultr-vps | /tools/curl-command-generator/, /tools/jwt-decoder/ |
| deploy-wordpress-on-vultr-... | /tools/chmod-calculator/, /tools/htpasswd-generator/ |
| vultr-vs-hetzner-2026 | /tools/vps-cost-calculator/, /tools/server-spec-recommender/ |
| migrate-digitalocean-to-vultr | /tools/vps-migration-checklist/ |
