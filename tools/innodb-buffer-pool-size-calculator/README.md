# InnoDB Buffer Pool Size Calculator

> Live: https://tools.stackfreeks.com/tools/innodb-buffer-pool-size-calculator/

Work out `innodb_buffer_pool_size` from server RAM after the OS, PHP-FPM, Redis, the web server and worst-case connection buffers take their share, and copy a `[mysqld]` block for MySQL 8.4, MySQL 8.0 or MariaDB 10.5+.

## Features

- Separate reservations for OS, PHP-FPM, Redis, web server and other services
- Per-connection memory (max_connections × default per-thread buffers for the selected version)
- Size rounded down to a multiple of chunk size × instances, with the formula printed
- Dedicated-server toggle with the MySQL `innodb_dedicated_server` value (128 MB / 50% / 75%) for comparison
- Memory breakdown bar and a warning when the total exceeds RAM
- Version-aware `[mysqld]` snippet (no instances line for MariaDB, no removed variables)
- Reverse mode: RAM needed to cache your InnoDB data, with the information_schema query to measure it
- English / Korean UI, light and dark mode

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
