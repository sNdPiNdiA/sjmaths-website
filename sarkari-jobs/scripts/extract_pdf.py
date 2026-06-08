#!/usr/bin/env python3
"""
Sarkari Jobs - PDF text extractor.

For every downloaded PDF in sarkari-jobs/pdfs/, extract text to
sarkari-jobs/extracted-text/<id>.txt using pdfplumber. If pdfplumber
returns little or no usable text (scanned image, image-only pages),
fall back to Tesseract OCR via pdf2image.

Idempotent: skips PDFs that already have a corresponding .done marker.
"""

from __future__ import annotations

import os
import sys
import json
import time
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[extract] %(message)s",
)
log = logging.getLogger("extract")

ROOT = Path(__file__).resolve().parents[2]  # sjmaths-website/
SCRIPTS_DIR = ROOT / "sarkari-jobs" / "scripts"
PDF_DIR = ROOT / "sarkari-jobs" / "pdfs"
EXTRACT_DIR = ROOT / "sarkari-jobs" / "extracted-text"
RAW_DIR = SCRIPTS_DIR / "raw"
PARSED_DIR = SCRIPTS_DIR / "parsed"
QUARANTINE_DIR = SCRIPTS_DIR / "quarantine"

MIN_TEXT_LENGTH = 200
MAX_OCR_PAGES = 25
MAX_PDF_BYTES = 50 * 1024 * 1024


def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        log.warning("could not parse %s: %s", path, exc)
        return default


def extract_with_pdfplumber(pdf_path: Path) -> str:
    import pdfplumber  # imported lazily so missing dep is reported cleanly

    chunks: list[str] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for i, page in enumerate(pdf.pages):
            try:
                text = page.extract_text() or ""
            except Exception as exc:  # noqa: BLE001
                log.warning("pdfplumber failed on page %d: %s", i + 1, exc)
                text = ""
            chunks.append(text)
    return "\n\n".join(chunks)


def extract_with_ocr(pdf_path: Path) -> str:
    from pdf2image import convert_from_path  # type: ignore
    import pytesseract  # type: ignore

    images = convert_from_path(str(pdf_path), dpi=200, last_page=MAX_OCR_PAGES)
    page_texts: list[str] = []
    for i, img in enumerate(images):
        try:
            txt = pytesseract.image_to_string(img, lang="eng+hin")
        except Exception as exc:  # noqa: BLE001
            log.warning("tesseract failed on page %d: %s", i + 1, exc)
            txt = ""
        page_texts.append(txt)
    return "\n\n".join(page_texts)


def find_pdfs() -> list[Path]:
    if not PDF_DIR.exists():
        return []
    return sorted(p for p in PDF_DIR.glob("*.pdf") if p.is_file())


def process_pdf(pdf_path: Path) -> dict:
    id_ = pdf_path.stem
    text_path = EXTRACT_DIR / f"{id_}.txt"
    done_marker = EXTRACT_DIR / f"{id_}.done"
    attempted_marker = EXTRACT_DIR / f"{id_}.attempted"
    fallback_marker = EXTRACT_DIR / f"{id_}.ocr"

    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)

    if text_path.exists() and done_marker.exists():
        return {"id": id_, "status": "skipped-complete"}

    if not attempted_marker.exists():
        attempted_marker.write_text(time.strftime("%Y-%m-%dT%H:%M:%S%z"), encoding="utf-8")

    size = pdf_path.stat().st_size
    if size > MAX_PDF_BYTES:
        log.warning("%s: size %d > cap, marking for quarantine", id_, size)
        return {"id": id_, "status": "skipped-too-large", "size": size}

    t0 = time.time()
    text = ""
    used_ocr = False
    error = None

    try:
        text = extract_with_pdfplumber(pdf_path)
    except Exception as exc:  # noqa: BLE001
        log.warning("%s: pdfplumber error: %s", id_, exc)
        error = str(exc)

    if len(text.strip()) < MIN_TEXT_LENGTH:
        log.info("%s: pdfplumber text too short (%d chars), trying OCR", id_, len(text.strip()))
        try:
            ocr_text = extract_with_ocr(pdf_path)
            if len(ocr_text.strip()) > len(text.strip()):
                text = ocr_text
                used_ocr = True
        except Exception as exc:  # noqa: BLE001
            log.warning("%s: OCR error: %s", id_, exc)
            if not error:
                error = f"ocr: {exc}"

    text_path.write_text(text, encoding="utf-8")
    done_marker.write_text(
        json.dumps(
            {
                "id": id_,
                "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "bytes": size,
                "chars": len(text),
                "usedOcr": used_ocr,
            }
        ),
        encoding="utf-8",
    )
    if used_ocr:
        fallback_marker.write_text("1", encoding="utf-8")

    elapsed = round(time.time() - t0, 1)
    log.info(
        "%s: %d chars in %ss (ocr=%s) -> %s",
        id_, len(text), elapsed, used_ocr, text_path.relative_to(ROOT),
    )
    return {"id": id_, "status": "ok", "chars": len(text), "elapsed": elapsed, "ocr": used_ocr, "error": error}


def collect_pdf_ids_from_raw() -> set[str]:
    if not RAW_DIR.exists():
        return set()
    ids: set[str] = set()
    for f in sorted(RAW_DIR.glob("*.json"), reverse=True)[:3]:  # last 3 days
        data = load_json(f, [])
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("id"):
                    ids.add(item["id"])
    return ids


def clean_orphan_outputs(known_ids: set[str]) -> int:
    """Remove parsed/quarantine/extracted files for IDs that are no longer in recent raw data.

    Helps keep the output dir from accumulating dead IDs across runs.
    """
    removed = 0
    for folder in (PARSED_DIR, QUARANTINE_DIR, EXTRACT_DIR):
        if not folder.exists():
            continue
        for p in folder.iterdir():
            if not p.is_file():
                continue
            if p.name.startswith("."):
                continue
            stem = p.stem.split(".", 1)[0]
            if "." in p.name:
                stem = p.stem
            if stem in {"gitkeep"}:
                continue
            if known_ids and stem not in known_ids and "_" not in stem:
                # heuristic: an id is a hyphenated portal+hash string
                if "-" in stem and len(stem) >= 8:
                    p.unlink(missing_ok=True)
                    removed += 1
    return removed


def main() -> int:
    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
    pdfs = find_pdfs()
    log.info("found %d PDFs in %s", len(pdfs), PDF_DIR.relative_to(ROOT))

    if not pdfs:
        log.info("nothing to extract; downstream steps will operate on title-only data")
        return 0

    ok = 0
    skipped = 0
    failed = 0
    for pdf in pdfs:
        try:
            r = process_pdf(pdf)
        except Exception as exc:  # noqa: BLE001
            log.error("%s: unexpected error: %s", pdf.name, exc)
            failed += 1
            continue
        s = r.get("status")
        if s == "ok":
            ok += 1
        else:
            skipped += 1

    log.info("Summary: ok=%d skipped=%d failed=%d", ok, skipped, failed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
