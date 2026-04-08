# Visual PDF Audit Toolkit and Workflow

This workflow is for cases where PDF text extraction is corrupted and we need visual page reading.

## Toolkit used in this repo

- `magick` (ImageMagick): render PDF pages to high-resolution PNG images.
- `tesseract`: optional OCR fallback for specific pages if needed.
- LLM image reading: read rendered PNG pages directly for visual verification.

## Why this workflow

- `miracles/miracles-original.pdf` has a damaged text layer in this environment.
- Direct text extraction is unreliable.
- Rendering pages as images avoids text-layer corruption and lets us verify the original scan visually.

## Directory layout

- Rendered pages: `ai/pdf-audit/pages/`
- Progressive audit notes: `ai/MIRACLE_TRANSLATION_AUDIT_2.md`

## Commands

### 1) Check total PDF pages

```bash
magick identify -format "%n\n" "miracles/miracles-original.pdf" | awk 'NR==1{print $1}'
```

### 2) Render one page (example: page 1)

```bash
magick -density 300 "miracles/miracles-original.pdf[0]" -quality 100 "ai/pdf-audit/pages/miracles-original-p001.png"
```

### 3) Render multiple pages (example range 70-80, 1-indexed)

```bash
for p in $(seq 70 80); do
  idx=$((p-1))
  out=$(printf "ai/pdf-audit/pages/miracles-original-p%03d.png" "$p")
  magick -density 300 "miracles/miracles-original.pdf[$idx]" -quality 100 "$out"
done
```

### 4) Optional OCR fallback for one rendered page

```bash
tesseract "ai/pdf-audit/pages/miracles-original-p074.png" "ai/pdf-audit/pages/miracles-original-p074" -l eng
```

This produces `ai/pdf-audit/pages/miracles-original-p074.txt`.

## Section-to-page targeting strategy

1. Use `miracles/miracles-raw.txt` to locate section anchors and approximate internal book page labels.
2. Convert approximate target pages plus neighbors (usually `target-2` to `target+2`).
3. Compare visual English page content against `miracles/miracles-cn.md`.
4. Write findings incrementally to `ai/MIRACLE_TRANSLATION_AUDIT_2.md`.

## Progressive-write rule

- Always append results in small batches.
- Never wait for the full pass before writing.
- Each batch should include: section id, original English excerpt, intended meaning, Chinese rendering summary, and verified verdict.
