# Apache MaxRequestWorkers Calculator

> Live: https://tools.stackfreeks.com/tools/apache-maxrequestworkers-calculator/

Size Apache `MaxRequestWorkers` and `ServerLimit` for the prefork, worker or event MPM from server RAM, per-service reservations and the measured Apache process size.

## Features

- MPM-aware math: prefork (one process per request) vs worker/event (processes × ThreadsPerChild, rounded down to a multiple of ThreadsPerChild, ServerLimit = ceil(MaxRequestWorkers ÷ ThreadsPerChild))
- Separate reservations for OS, MySQL/MariaDB, PHP-FPM and other services, with a safety headroom
- Formula printed with your numbers plugged in
- Warnings: prefork above 256 needs ServerLimit raised, ThreadsPerChild above ThreadLimit, ServerLimit hard limits
- Peak memory breakdown bar, with an optional check of your current MaxRequestWorkers
- Copy-ready `<IfModule mpm_*_module>` block and a `ps` one-liner to measure process size
- Reverse mode: RAM needed for a target number of concurrent requests
- English / Korean

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
