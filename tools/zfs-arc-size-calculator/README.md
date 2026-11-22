# ZFS ARC Size Calculator

> Live: https://tools.stackfreeks.com/tools/zfs-arc-size-calculator/

Work out `zfs_arc_max` from RAM, pool size and server role (Proxmox / VM host, dedicated NAS, mixed), with the exact byte value and copy-ready commands.

## Features

- Recommended `zfs_arc_max` in GiB and exact bytes, with the formula shown using your numbers
- Proxmox wiki storage rule (2 GiB + 1 GiB per TiB), NAS and mixed starting points
- ARC capped at RAM minus a reserve for VMs, containers and the OS; "RAM left" shown
- Same-RAM comparison: Proxmox VE 8.1+ installer default, OpenZFS 2.2 and 2.3+ defaults, default `zfs_arc_min`
- `zfs_arc_min` warning and extra line when the max would be ignored
- Copyable `/etc/modprobe.d/zfs.conf`, `update-initramfs`, runtime `/sys/module` and verify commands
- GiB ↔ bytes converter with share of RAM
- English / Korean

## Sources

- Proxmox VE wiki, ZFS on Linux: https://pve.proxmox.com/wiki/ZFS_on_Linux
- OpenZFS zfs(4) man pages: https://openzfs.github.io/openzfs-docs/man/v2.2/4/zfs.4.html, https://openzfs.github.io/openzfs-docs/man/v2.3/4/zfs.4.html

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
