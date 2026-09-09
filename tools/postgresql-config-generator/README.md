# PostgreSQL Config Generator

> Live: https://tools.stackfreeks.com/tools/postgresql-config-generator/

A PGTune-style `postgresql.conf` tuner. Enter your RAM, CPU cores, storage type, PostgreSQL version, workload and expected max connections, and get a tuned config snippet with a one-click Copy button — plus a matched Vultr plan for the RAM you entered.

## Features

- Generates `shared_buffers`, `effective_cache_size`, `work_mem`, `maintenance_work_mem`, `wal_buffers`, `min_wal_size` / `max_wal_size`, `checkpoint_completion_target`, `default_statistics_target`, `random_page_cost`, `effective_io_concurrency`, `max_connections` and parallel worker settings
- Ports the well-known PGTune formulas (25% RAM shared_buffers, 75% effective_cache_size, connection-derived work_mem, etc.)
- Per-workload profiles: Web app, OLTP, Data warehouse, Desktop, Mixed
- Storage-aware planner cost constants (SSD/NVMe, HDD, Network/SAN)
- PostgreSQL 14 / 15 / 16 / 17
- Copy button + matched Vultr Cloud Compute / Managed Database plan
- EN / KO bilingual UI

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
