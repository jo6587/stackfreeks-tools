# Htpasswd Generator

> Live: https://tools.stackfreeks.com/tools/htpasswd-generator/

Generate .htpasswd file entries for Apache and Nginx basic auth. Supports bcrypt, MD5-APR, SHA1, and plain formats. Client-side only.

## Features
- bcrypt (cost factor 10, recommended)
- MD5-APR ($apr1$ format)
- SHA1 ({SHA} prefix)
- Plain (with security warning)
- Multiple user entries in one output
- No password sent to server

## Tech Stack
- Pure HTML/CSS/JavaScript
- bcryptjs (CDN, client-side only)
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools
[tools.stackfreeks.com](https://tools.stackfreeks.com)
