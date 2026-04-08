#!/usr/bin/env python3
"""
Convert OCR'd book text into clean Markdown.

Usage: python3 convert.py input.txt output.md

Handles:
- Page headers/footers (repeated book title + page numbers)
- OCR line-break hyphens
- Numbered section headings (e.g. "4.\nHealing of Leg Ailments")
- Part headings (e.g. "Part III")
- Named sub-headings (e.g. "Editor's Preface")
- Paragraph re-joining across line breaks
- Collapsing excessive whitespace
- Common OCR underscore artifacts (a_, has_)
"""

import re
import sys


def detect_running_headers(text):
    """Auto-detect repeated page header/footer patterns (title + page number)."""
    # Find lines that are just a number (page numbers)
    # Find lines that repeat frequently and look like headers
    lines = text.split('\n')
    line_counts = {}
    for line in lines:
        stripped = line.strip()
        # Normalize: remove leading/trailing digits (page numbers)
        normalized = re.sub(r'^\d+\s*', '', stripped)
        normalized = re.sub(r'\s*\d+$', '', normalized)
        normalized = normalized.strip()
        if 10 < len(normalized) < 80 and normalized.isupper() or normalized.istitle():
            line_counts[normalized] = line_counts.get(normalized, 0) + 1

    # Lines appearing 2+ times are likely running headers
    return [h for h, count in line_counts.items() if count >= 2]


def clean_ocr_text(text):
    """Fix common OCR artifacts."""
    # Fix underscore-joined words (OCR artifact)
    text = re.sub(r'(\w)_\s', r'\1 ', text)
    # Fix soft hyphens at line breaks: "word-\n  rest" -> "wordrest"
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    # Same-line OCR hyphens: "Ven- eration" -> "Veneration" (lowercase continuation)
    text = re.sub(r'(\w)- ([a-z])', r'\1\2', text)
    return text


def remove_running_headers(text, headers=None):
    """Remove auto-detected or provided running headers and page numbers."""
    if headers is None:
        headers = detect_running_headers(text)

    for header in headers:
        # Match the header with optional surrounding page numbers
        escaped = re.escape(header)
        text = re.sub(
            rf'\n\s*\d*\s*{escaped}\s*\d*\s*\n', '\n', text, flags=re.IGNORECASE
        )
        text = re.sub(
            rf'\n\s*{escaped}\s+\d+\s*\n', '\n', text, flags=re.IGNORECASE
        )
        text = re.sub(
            rf'\n\s*\d+\s+{escaped}\s*\n', '\n', text, flags=re.IGNORECASE
        )

    # Remove standalone page numbers on their own line
    text = re.sub(r'\n\s*\d{1,4}\s*\n', '\n', text)

    # Remove lines that are just "NUMBER ALLCAPS WORDS" or "ALLCAPS WORDS NUMBER"
    # (common page header/footer pattern)
    text = re.sub(r'\n\s*\d{1,4}\s+[A-Z][A-Z\s]{10,}\s*\n', '\n', text)
    text = re.sub(r'\n\s*[A-Z][A-Z\s]{10,}\s+\d{1,4}\s*\n', '\n', text)

    return text


def convert_headings(text):
    """Convert common heading patterns to Markdown headings."""

    # "Part X\n SUBTITLE" or "Part X" alone -> # Part X: Subtitle
    def part_heading(m):
        part = m.group(1).strip()
        subtitle = m.group(2).strip().replace('\n', ' ') if m.group(2) else ''
        subtitle = re.sub(r'\s+', ' ', subtitle)
        # Fix OCR "Ill" -> "III" etc.
        part = re.sub(r'\bIll\b', 'III', part)
        part = re.sub(r'\bIl\b', 'II', part)
        if subtitle:
            # Title-case properly (handle apostrophes and small words)
            words = subtitle.title().split()
            small = {'A','An','And','As','At','But','By','For','In','Nor','Of','On','Or','So','The','To','Up','Yet'}
            subtitle = ' '.join(w if i == 0 else (w if w not in small else w.lower()) for i, w in enumerate(words))
            subtitle = re.sub(r"'S\b", "'s", subtitle)
            subtitle = re.sub(r"'S\b", "'s", subtitle)
            return f'\n# {part}: {subtitle}\n'
        return f'\n# {part}\n'

    text = re.sub(
        r'(?:^|\n)\s*(Part\s+[IVXivx]+|Part\s+\d+|Part\s+I[lI]+)\s*\n((?:[A-Z][^\n]*\n)*?[A-Z][^\n]*)\s*\n\s*\n',
        part_heading, text, flags=re.MULTILINE
    )
    text = re.sub(
        r'\n\s*(Part\s+[IVXivx]+|Part\s+\d+|Part\s+I[lI]+)\s*\n',
        part_heading, text
    )

    # Numbered headings: "4.\nHealing of Leg Ailments" -> "## 4. Healing of Leg Ailments"
    def numbered_heading(m):
        num = m.group(1)
        title = m.group(2).strip()
        # Join if title spans multiple lines
        title = re.sub(r'\s*\n\s*', ' ', title)
        return f'\n## {num}. {title}\n'

    text = re.sub(
        r'\n\s*(\d{1,3})\.\s*\n\s*([A-Z][\w\s,\'\'\-]+(?:\n[\w\s,\'\'\-]+)*)\n',
        numbered_heading, text
    )

    # Standalone title-case or ALL-CAPS lines that look like section headers
    # (between blank lines, short, not a sentence)
    def maybe_heading(m):
        title = m.group(1).strip()
        # Skip if it looks like a normal sentence (has a period mid-text)
        if '.' in title[:-1]:
            return m.group(0)
        if title.isupper() and len(title) > 5:
            title = title.title()
        return f'\n### {title}\n'

    text = re.sub(
        r'\n\n\s*([A-Z][\w\s\'\'\-]{4,60})\s*\n\n',
        maybe_heading, text
    )

    return text


def rejoin_paragraphs(text):
    """Rejoin lines that were broken by OCR/page formatting into proper paragraphs."""
    lines = text.split('\n')
    result = []

    for line in lines:
        stripped = line.strip()
        if stripped == '':
            result.append('')
        elif stripped.startswith('#'):
            result.append(stripped)
        elif stripped.startswith('>'):
            result.append(stripped)
        elif stripped.startswith('- ') or stripped.startswith('* '):
            result.append(stripped)
        else:
            # Join to previous line if it's a continuation
            if (result
                    and result[-1] != ''
                    and not result[-1].startswith('#')
                    and not result[-1].startswith('>')
                    and not result[-1].endswith(':')
                    ):
                result[-1] += ' ' + stripped
            else:
                result.append(stripped)

    return '\n'.join(result)


def final_cleanup(text):
    """Final whitespace and formatting cleanup."""
    # Collapse 3+ newlines into 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Clean multiple spaces
    text = re.sub(r'  +', ' ', text)
    # Ensure headings have blank lines around them
    text = re.sub(r'([^\n])\n(#{1,3} )', r'\1\n\n\2', text)
    text = re.sub(r'(#{1,3} .+)\n([^\n#])', r'\1\n\n\2', text)
    return text.strip() + '\n'


def convert(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    text = clean_ocr_text(text)
    text = remove_running_headers(text)
    text = convert_headings(text)
    text = rejoin_paragraphs(text)
    text = final_cleanup(text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Converted: {input_path} -> {output_path}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.txt output.md")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2])
