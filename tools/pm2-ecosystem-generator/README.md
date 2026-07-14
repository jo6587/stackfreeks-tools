# PM2 Ecosystem Config Generator

> Live: https://tools.stackfreeks.com/tools/pm2-ecosystem-generator/

Generate a ready-to-use PM2 `ecosystem.config.js` file for your Node.js app — instances, cluster/fork mode, environment variables, watch mode, and max_memory_restart, plus the deploy commands to run it.

## Features

- App name, script path, instances (number or "max" for all CPU cores), and exec_mode (fork/cluster)
- Add/remove environment variables (KEY=value pairs)
- Toggle watch mode and autorestart, set an optional max_memory_restart threshold
- Presets for Express API, Next.js, and NestJS
- One-click copy/download of `ecosystem.config.js`
- Generated deploy commands: `pm2 start`, `pm2 save`, `pm2 startup`, `pm2 logs`, `pm2 monit`

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
