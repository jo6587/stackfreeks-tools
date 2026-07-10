# Fail2ban Jail Generator

> Live: https://tools.stackfreeks.com/tools/fail2ban-jail-generator/

Generate a complete fail2ban `jail.local` configuration for SSH, Nginx, Apache, Postfix, vsftpd, and WordPress — with install and apply commands included.

## Features

- 8 selectable jails: sshd, nginx-http-auth, nginx-limit-req, nginx-botsearch, apache-auth, postfix, vsftpd, wordpress
- Common settings: maxretry slider (1–10), bantime presets (10m / 1h / 24h / 1w / permanent), findtime, ignoreip whitelist
- Syntax-highlighted output with copy and download (`jail.local`) buttons
- Ready-to-run install & apply commands (`apt install fail2ban`, `systemctl restart fail2ban`, `fail2ban-client status`)
- English / Korean language toggle

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
