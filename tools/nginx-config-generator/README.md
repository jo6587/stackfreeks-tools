# Nginx Config Generator

**Live tool:** [tools.stackfreeks.com/tools/nginx-config-generator/](https://tools.stackfreeks.com/tools/nginx-config-generator/)

Generate ready-to-use nginx server block configs in seconds. Fill out the form, copy or download your config — no manual editing required.

## Features

- **Live preview** — config updates instantly as you type
- **SSL support** — generates HTTP→HTTPS redirect block + HTTPS server block with Let's Encrypt paths
- **PHP-FPM** — adds `location ~ \.php$` block with `fastcgi_pass unix:/run/php/php8.1-fpm.sock;`
- **Reverse proxy** — adds full `proxy_pass` block with headers for Node.js / Python / any upstream
- **Gzip compression** — adds gzip block with sensible defaults
- **Static file caching** — `expires 30d` for images, CSS, JS, fonts
- **WWW redirect** — configurable: www → non-www, non-www → www, or none
- **Copy button** — clipboard copy with "Copied!" feedback
- **Download button** — saves config as `nginx.conf`

## Mutual exclusion

PHP-FPM and Proxy Pass cannot be active simultaneously (they conflict on `location /`). Selecting one automatically deselects the other.

## Tech

Pure HTML/CSS/JS — no build step, no dependencies, runs entirely in the browser.

## Usage

1. Enter your domain name (e.g. `example.com`)
2. Set root directory (default: `/var/www/html`)
3. Toggle SSL, PHP-FPM, proxy pass, gzip, caching as needed
4. Copy or download the generated config
5. Place at `/etc/nginx/sites-available/your-domain`, symlink to `sites-enabled/`, then `nginx -t && systemctl reload nginx`
