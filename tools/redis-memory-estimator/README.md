# Redis Memory Estimator

> Live: https://tools.stackfreeks.com/tools/redis-memory-estimator/

Estimate how much RAM Redis needs for your dataset based on key count, data type (String, Hash, List, Set, Sorted Set), and average value/element size — then get a matching Vultr VPS plan recommendation.

## Features

- Supports all 5 core Redis data types with type-specific per-key and per-element overhead
- Accounts for Redis internal overhead (dictEntry, robj headers, SDS strings, hash table buckets, skiplist nodes) and typical jemalloc allocation rounding
- Instant MB/GB memory estimate with a full breakdown (raw bytes, Redis overhead, allocator rounding)
- Suggested Vultr Cloud Compute plan sized with headroom for snapshotting and connection buffers
- EN/KO bilingual UI

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
