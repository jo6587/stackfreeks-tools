# LLM GPU Cost Calculator

> Live: https://tools.stackfreeks.com/tools/llm-gpu-cost-calculator/

Self-hosted GPU vs. LLM API cost comparison for inference. Enter your monthly request
volume and token sizes to see self-hosted monthly cost, API monthly cost, break-even
volume, and cost per million tokens.

## Features

- Self-hosted GPU cost from request volume, output tokens, GPU $/hr, throughput, and utilization
- API cost from editable $/1M input and $/1M output pricing
- Break-even request volume and a plain-language verdict
- Self-host cost per 1M tokens
- 6 GPU presets (A100 40GB/80GB, H100, L40S, RTX 4090, RTX 3090) with editable $/hr and tokens/sec
- EN / KO bilingual UI
- Transparent, commented formulas

## Formulas

- GPU-hours needed = (requests × output tokens) / (throughput × utilization × 3600)
- Self-hosted cost = max(GPU-hours needed, 730) × GPU $/hr  _(assumes one GPU runs 24/7)_
- API cost = requests × (input/1M × $in + output/1M × $out)
- Break-even volume = (730 × GPU $/hr) / API cost per request

## Tech Stack

- Pure HTML/CSS/JavaScript
- No build tools, no dependencies
- Deployed on Cloudflare Pages

## Part of StackFreeks Tools

[tools.stackfreeks.com](https://tools.stackfreeks.com)
