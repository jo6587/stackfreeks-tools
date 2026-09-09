# Backlink Kit — StackFreeks Tools

> 만든 날: 2026-07-08. 아래 카피는 붙여넣기용. 등록은 계정이 필요해서 직접 진행.
> 완료하면 체크박스에 표시.

## 1. Product Hunt (효과 최대 — 화·수·목 발행 추천)

- [x] 예약 완료: **2026-07-09 (목) 12:01 AM PDT** = 한국시간 목요일 오후 4:01
- [x] maker comment 등록 완료
- [ ] 발행 당일 댓글 답변 (목 저녁 / 금 오전 확인)

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

- [x] 제출 완료 (2026-07-20) — game-server-cost-calculator, 킷의 제목/URL/첫 댓글 그대로 사용
      → 몇 시간~하루 안에 코멘트/투표 반응 있으면 답변 챙길 것. 반응 저조해도 정상(Show HN 대부분 그럼).
      몇 주 뒤 docker-ram-calculator 또는 mysql-backup-script-generator로 한 번 더 시도 가능.

**Title**: `Show HN: Game server cost calculator – VPS cost by player count`
**URL**: `https://tools.stackfreeks.com/tools/game-server-cost-calculator/`
**First comment**:

> I run game servers for friends and always ended up guessing RAM. This
> calculates the VPS spec + monthly cost from game and player count
> (Minecraft, Valheim, Rust, ARK, CS2...). Estimates are community-sourced;
> corrections welcome. Pure static page, no backend.

실패해도 손해 없음. 몇 주 뒤 docker-ram-calculator로 한 번 더 가능.

## 3. dev.to 글 (가입만 하면 발행 가능, 트래픽+링크)

- [x] 발행 완료 (2026-07-11) — 초안: `marketing/devto-draft.md`
      → 댓글 달리면 답장 챙길 것. 댓글로 들어온 툴 아이디어는 tool-picker 입력으로 활용

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
       cron-builder, subnet-calculator) — 7일 제한 해제됨(7/15 이후), 등록 진행 중
      각 툴 등록 시 사용할 카피(Full description + Tags)는 아래 참조.

**Full description (복사용):**

| 툴 | Full description |
|---|---|
| vps-cost-calculator | A free browser-based calculator that compares monthly VPS hosting costs across Vultr, Hetzner, and DigitalOcean. Enter your specs — RAM, CPU, storage, bandwidth — and get an instant side-by-side price breakdown, so you can pick the cheapest provider for your workload without opening five pricing pages. No signup, no account, runs entirely in your browser. Part of StackFreeks Tools, a collection of free static developer and sysadmin utilities. |
| game-server-cost-calculator | A free tool that estimates VPS hosting costs for game servers by player count. Pick your game (Minecraft, Valheim, Rust, ARK, CS2, and more), enter the number of players, and get a recommended VPS spec plus monthly cost across major providers — no more guessing RAM or over/under-provisioning your server. No signup, no account, runs entirely in your browser. Part of StackFreeks Tools, a collection of free static developer and sysadmin utilities. |
| docker-ram-calculator | A free browser-based calculator that helps you size Docker container memory limits before picking a VPS plan. Enter your VPS RAM and container count (app, database, proxy, etc.), and it calculates a sensible `--memory` allocation for each one — so you avoid OOM kills without wasting RAM on oversized limits. No signup, no account, runs entirely in your browser. Part of StackFreeks Tools, a collection of free static developer and sysadmin utilities. |
| cron-builder | A free visual builder for cron expressions. Pick a schedule using dropdowns or presets (every 5 minutes, daily at 2am, every Sunday, etc.) and get the correct cron syntax instantly, plus a human-readable explanation and a preview of the next run times — no more counting asterisks or double-checking syntax against a cheat sheet. No signup, no account, runs entirely in your browser. Part of StackFreeks Tools, a collection of free static developer and sysadmin utilities. |
| subnet-calculator | A free subnet calculator for IPv4 networks. Enter an IP address and CIDR notation (or subnet mask) and instantly get the network address, broadcast address, usable host range, and total host count — useful for firewall rules, VPC configuration, and general network planning. No signup, no account, runs entirely in your browser. Part of StackFreeks Tools, a collection of free static developer and sysadmin utilities. |

**Tags (쉼표 구분, 복사용):**

| 툴 | Tags |
|---|---|
| vps-cost-calculator | vps, hosting, cloud hosting, pricing calculator, cost calculator, vultr, hetzner, digitalocean, server, sysadmin |
| game-server-cost-calculator | game server, minecraft, hosting, vps, cost calculator, gaming |
| docker-ram-calculator | docker, containers, devops, memory, sysadmin, vps |
| cron-builder | cron, scheduling, linux, sysadmin, devops, developer tools |
| subnet-calculator | networking, ip address, subnet, sysadmin, cidr, devops |
- [x] **SaaSHub** — 등록·검증 완료 (2026-07-12, ACTIVE). 분기마다 재검증 필요 —
      다음 검증: 2026년 10월경 (Manage → Verify 클릭만 하면 됨)
- [x] **Uneed** — 제출 완료 (2026-07-08). 무료 큐 대기 — **2026년 12월경 게시 예정**.
      유료 스킵 있지만 불필요, 그냥 기다리면 됨
- [ ] **Fazier** — https://fazier.com/submit — 배지는 홈 푸터에 배포 완료
      ⚠️ DR > 0 조건 — 신규 도메인이라 현재 DR 0. PH/SaaSHub 링크가 Ahrefs에 잡히는
      **2026년 8월경 재시도** (DR 확인: https://ahrefs.com/website-authority-checker)

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

## 블로그 → 툴 역링크 ✅ 완료 (2026-07-08)

툴 → 블로그, 블로그 → 툴 양방향 완료. 아래 10개 글에 15개 툴 링크 삽입됨.
사용한 스크립트: `02_Autoblog_StackFreeks_Wordpress/insert_tool_links.py` (멱등 —
새 글/새 매핑 추가 시 PLAN에 항목 넣고 재실행하면 됨. 드라이런 기본, --apply로 적용)

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
