# PHP-FPM pm.max_children Calculator

> Live: https://tools.stackfreeks.com/tools/php-fpm-max-children-calculator/

Calculate PHP-FPM `pm.max_children` and the spare-server settings from your server RAM, the memory other services need, and your measured worker size. The tool generates a ready-to-paste `www.conf` pool block.

## Features

- Formula `floor((RAM − reserved) × (1 − buffer) ÷ worker size)`, printed on the page with your numbers filled in
- Separate reservations for the OS, MySQL/MariaDB, Redis/Memcached and other services
- `ps … | awk` one-liner (with a copy button) to measure the average PHP-FPM worker RSS
- `pm = static / dynamic / ondemand` selector that changes the generated config
- Spare servers rule of thumb: start = min_spare = 25%, max_spare = 75% of max_children
- Reverse mode: minimum total RAM for a target `pm.max_children`
- English / Korean UI

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
