# Overview 

## What this project does

This project scrapes discussion data from Autohome for thesis research. It uses Selenium to load target pages, extracts structured post and comment text, normalizes the data into tabular form, and writes the results to local files for downstream analysis. The repository is organized as a small Python package with a CLI, tests, and documentation.

## How it works

1. **List page parsing**  
   The scraper opens forum or listing pages and collects candidate post URLs.

2. **Detail page parsing**  
   Each post page is loaded in Selenium, and the scraper extracts post-level fields and any visible comments.

3. **Deduplication and normalization**  
   Records are normalized into a stable schema, keyed by post and comment identifiers to reduce duplicate rows.

4. **Output writing**  
   Structured records are written to CSV, and run metadata is saved for traceability and reproducibility.

# Quickstart

### Prerequisites
- Python 3.10+
- Chrome/Chromium (Selenium will use it)

For full instructions on how to run the scraper, configuration options, and examples, see:
➡️ [Usage Guide](USAGE.md)

### Install
```bash
git clone https://github.com/wmeikle33/Thesis-Webscraper.git
cd Thesis-Webscraper
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -e .
pip install -e .[dev]
thesis-webscraper --help

```

```bash

thesis-webscraper run \
  --section used-cars \
  --pages 10 \
  --out-dir data \
  --headless \
  --delay-ms 1200 \
  --jitter 0.4 \
  --max-retries 2 \
  --resume \
  --verbose

```

## What it outputs

After a successful run, the scraper writes data to:
./data/ (default output directory)
posts.csv — forum post-level data
comments.csv — comment-level data (if applicable)
run_metadata.json — run info (timestamp, args, counts, errors)

# Schema

## posts.csv

```bash

post_id (string) — unique ID (from URL or page)
url (string)
title (string, UTF-8)
body (string, UTF-8)
author (string)
created_at (string / ISO timestamp if available)
scraped_at (string / ISO timestamp)
source (string) — e.g., autohome

```

## comments.csv

```bash

post_id (string) — foreign key to posts.csv
comment_id (string)
comment_text (string, UTF-8)
comment_author (string)
comment_created_at (string)
scraped_at (string)

```

## Repository Structure

The project is organized into the following directories:

## Repository structure

```text
.
├── .github/workflows/   # CI configuration
├── data/                # Output data and sample artifacts
├── docs/                # Additional project documentation
├── src/                 # Python package source code
├── tests/               # Automated tests and fixtures
├── notebooks/    
├── Changelog.md
├── LICENSE
├── MIGRATING.md
├── README.md
├── USAGE.md
└── pyproject.toml

```
