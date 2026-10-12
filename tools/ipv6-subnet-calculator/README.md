# IPv6 Subnet Calculator

> Live: https://tools.stackfreeks.com/tools/ipv6-subnet-calculator/

Split any IPv6 prefix into child subnets (e.g. how many /64s are in a /56) and list every subnet, with exact BigInt counts, RFC 5952 compressed and expanded forms, the ip6.arpa reverse zone and the address type.

## Features

- Exact subnet and address counts (2^n and the full integer, BigInt math, never rounded)
- Network, first and last address, prefix mask
- Paged list of child subnets for any child prefix, "jump to subnet #N", copy page, CSV export (up to 65,536 rows per file)
- RFC 5952 compressed form, fully expanded form, ip6.arpa reverse zone (with non-nibble prefixes handled)
- Address type from the IANA special-purpose registry (global unicast, ULA, link-local, multicast, loopback, documentation, ...)
- Warnings for child prefixes longer than /64 (SLAAC) and prefixes off a nibble boundary (reverse DNS)
- Parses `::` shorthand and IPv4-embedded forms (`::ffff:192.0.2.1`), with inline errors for invalid input
- English / Korean UI, light and dark mode

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
