# stjohnshanghaibook

This repository contains OCR source text and converted Markdown for the *Book of St John of Shanghai*.

## Repository Layout

- `script/convert.py`: OCR-to-Markdown conversion script
- `full/full-raw.txt`: raw OCR text for the full book
- `full/full.md`: converted Markdown output
- `miracles/miracles-raw.txt`: raw OCR text for the miracles section
- `miracles/miracles.md`: converted Markdown output

## What the Converter Does

`script/convert.py` cleans OCR artifacts and formats content into readable Markdown. It handles:

- repeated running headers/footers and standalone page numbers
- OCR hyphenation and underscore artifacts
- numbered headings and part headings
- paragraph line rejoining
- whitespace normalization

## Usage

From the repository root:

```bash
python3 script/convert.py input.txt output.md
```

Examples for this repo:

```bash
python3 script/convert.py full/full-raw.txt full/full.md
python3 script/convert.py miracles/miracles-raw.txt miracles/miracles.md
```

## Current Status

The converter has been run for both source files, and these outputs are available:

- `full/full.md`
- `miracles/miracles.md`
