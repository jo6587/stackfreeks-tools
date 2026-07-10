# Systemd Service Generator

> Live: https://tools.stackfreeks.com/tools/systemd-service-generator/

Generate a complete systemd `.service` unit file for your app — ExecStart, restart policy, environment variables, and ready-to-run install commands.

## Features

- Presets for Node.js, Python, Go binary, and Java jar — one click auto-fills the form
- Service type select: simple / forking / oneshot / notify
- Restart policy (no / on-failure / always) with RestartSec
- Unlimited Environment= key/value pairs plus optional EnvironmentFile
- Generated install commands: daemon-reload, `enable --now`, status, `journalctl -u` follow
- Copy to clipboard or download as `[name].service`
- Inline ini/shell syntax highlighting
- English / Korean UI toggle

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
