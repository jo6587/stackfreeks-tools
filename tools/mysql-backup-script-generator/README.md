# MySQL Backup Script Generator

> Live: https://tools.stackfreeks.com/tools/mysql-backup-script-generator/

Generate a ready-to-use `mysqldump` backup shell script for MySQL/MariaDB — gzip compression, retention cleanup, optional rsync remote transfer, timestamped filenames, and cron schedule presets.

## Features

- Configurable DB name, DB user, and backup directory (defaults to `/var/backups/mysql`)
- Optional gzip compression of the dump
- Timestamped filenames (`YYYY-MM-DD_HHMMSS`) to avoid overwriting previous backups
- Automatic cleanup of local backups older than N days via `find -mtime -delete`
- Optional rsync transfer to a remote host/path for off-site backups
- Cron schedule presets (daily 2 AM, every 6 hours, weekly Sunday 3 AM) with an editable crontab expression field
- Generates install instructions covering `chmod +x`, the crontab line, and safely handling credentials via `~/.my.cnf`
- Copy and download buttons for both the script and the install instructions

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
