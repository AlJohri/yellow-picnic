# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Yellow Picnic is a Python CLI tool that downloads, parses, and analyzes weekly meal data from the Yellow Picnic meal subscription service. It extracts nutritional macro information and scores meals based on target macro ratios for weight loss.

## Running

```bash
mise run all          # runs the full pipeline: download → parse → analyze
uv run main.py        # equivalent direct invocation
```

Uses `uv` for dependency management with PEP 723 inline script metadata (dependencies declared in `main.py` header). Uses `mise` as the task runner. No separate requirements file.

## Architecture

Three-stage ETL pipeline orchestrated by `main.py`:

1. **download.py** — Authenticates via Chrome cookies (`browser_cookie3`) and fetches HTML from the Yellow Picnic subscription API
2. **parse.py** — Extracts meals from HTML using BeautifulSoup CSS selectors; returns `(date_string, list_of_meal_dicts)` where each meal has name, description, ingredients, and macros for three diet goals (loss/maintain/gain)
3. **analyze.py** — Filters to a target diet goal, calculates protein/carbs and protein/fat ratios, scores against target macros (130P/47C/44F), and returns a sorted pandas DataFrame

Output is written to a date-named directory (e.g. `2026-02-15/`) containing `page.html`, `data.json`, and `analysis.csv`.

## Notes

- No test suite currently exists
- No linting/formatting configuration
- Authentication requires Chrome cookies for yellowpicnic.com (user must be logged in via Chrome)
