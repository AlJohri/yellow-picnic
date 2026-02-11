#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = ["beautifulsoup4", "browser-cookie3", "lxml", "pandas", "requests"]
# ///

import json
import sys
from pathlib import Path

from download import download
from parse import parse
from analyze import analyze

html, date = download()
meals = parse(html, date)

if not meals:
    print("Error: no meals parsed", file=sys.stderr)
    sys.exit(1)

output_dir = Path(date)
output_dir.mkdir(exist_ok=True)

(output_dir / "page.html").write_text(html)
print(f"Downloaded to {output_dir}/page.html ({len(html)} bytes)")

(output_dir / "data.json").write_text(json.dumps(meals, indent=2) + "\n")
print(f"Wrote {len(meals)} meals to {output_dir}/data.json")

df = analyze(meals)
df.to_csv(output_dir / "analysis.csv", index=False)
print(df.to_string(index=False))
