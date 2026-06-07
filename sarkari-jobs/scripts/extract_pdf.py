#!/usr/bin/env python3
"""Extract text from downloaded Sarkari Jobs PDFs."""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

try:
    import pdfplumber
except Exception as exc:  # pragma: no cover - runtime dependency guard
    pdfplumber = None
    PDFPLUMBER_ERROR = exc
else:
    PDFPLUMBER_ERROR = None

try:
    from pypdf import PdfReader
except Exception as exc:  # pragma: no cover
    PdfReader = None
    PYPDF_ERROR = exc
else:
    PYPDF_ERROR = None

try:
    import pytesseract
    from pdf2image import convert_from_path
except Exception as exc:  # pragma: no cover
    pytesseract = None
    convert_from_path = None
    OCR_ERROR = exc
else:
    OCR_ERROR = None

ROOT = Path(__file__).resolve().parents[2]
PDF_DIR = ROOT / 'sarkari-jobs' / 'pdfs'
EXTRACT_DIR = ROOT / 'sarkari-jobs' / 'extracted-text'
RAW_DIR = Path(__file__).resolve().parent / 'raw'


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_json(path: Path):
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return []


def normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text or '').strip()


def extract_with_pdfplumber(pdf_path: Path) -> str:
    if pdfplumber is None:
        raise RuntimeError(f'pdfplumber unavailable: {PDFPLUMBER_ERROR}')
    text_parts = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ''
            if page_text.strip():
                text_parts.append(page_text)
    return '\n'.join(text_parts)


def extract_with_pypdf(pdf_path: Path) -> str:
    if PdfReader is None:
        raise RuntimeError(f'pypdf unavailable: {PYPDF_ERROR}')
    reader = PdfReader(str(pdf_path))
    parts = []
    for page in reader.pages:
        text = page.extract_text() or ''
        if text:
            parts.append(text)
    return '\n'.join(parts)


def extract_with_ocr(pdf_path: Path) -> str:
    if pytesseract is None or convert_from_path is None:
        raise RuntimeError(f'OCR dependencies unavailable: {OCR_ERROR}')
    if shutil.which('tesseract') is None:
        raise RuntimeError('tesseract binary not found in PATH')
    images = convert_from_path(str(pdf_path), dpi=180)
    parts = [pytesseract.image_to_string(img) for img in images]
    return '\n'.join(parts)


def extract_text(pdf_path: Path) -> str:
    attempts = [
        ('pdfplumber', extract_with_pdfplumber),
        ('pypdf', extract_with_pypdf),
    ]
    last_error = None
    for label, fn in attempts:
        try:
            text = fn(pdf_path)
            cleaned = normalize_text(text)
            if cleaned:
                return text
        except Exception as exc:
            last_error = f'{label}: {exc}'

    if pytesseract and convert_from_path:
        try:
            text = extract_with_ocr(pdf_path)
            if normalize_text(text):
                return text
        except Exception as exc:
            last_error = f'ocr: {exc}'

    raise RuntimeError(last_error or 'no text could be extracted')


def main() -> None:
    ensure_dir(EXTRACT_DIR)
    if not PDF_DIR.exists():
        print('[extract] No PDFs directory found; nothing to extract')
        return

    raw_files = sorted(RAW_DIR.glob('*.json'))
    if not raw_files:
        print('[extract] No raw notification files found; nothing to extract')
        return

    items = []
    for raw_file in raw_files:
        items.extend(load_json(raw_file))

    written = 0
    skipped = 0
    failed = 0

    for item in items:
        item_id = item.get('id')
        pdf_path = PDF_DIR / f'{item_id}.pdf'
        if not pdf_path.exists():
            skipped += 1
            continue

        output_path = EXTRACT_DIR / f'{item_id}.txt'
        if output_path.exists() and output_path.stat().st_size > 0:
            written += 1
            continue

        try:
            text = extract_text(pdf_path)
            output_path.write_text(text, encoding='utf-8')
            written += 1
            print(f'[extract] OK {item_id} -> {output_path.name} ({len(text.split())} words)')
        except Exception as exc:
            failed += 1
            print(f'[extract] FAIL {item_id}: {exc}', file=sys.stderr)

    print(f'[extract] Summary: written={written}, skipped={skipped}, failed={failed}')


if __name__ == '__main__':
    main()
