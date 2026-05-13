#!/usr/bin/env python3
"""Extract plain text from a PDF file for agent review."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import Any


def load_pdf_reader() -> Any:
    try:
        from pypdf import PdfReader

        return PdfReader
    except ImportError:
        pass

    try:
        from PyPDF2 import PdfReader

        return PdfReader
    except ImportError as exc:
        raise RuntimeError(
            "PDF extraction requires either 'pypdf' or 'PyPDF2'. "
            "Install one of them with: python -m pip install pypdf"
        ) from exc


def extract_pdf_text(path: Path) -> str:
    PdfReader = load_pdf_reader()
    reader = PdfReader(str(path))
    page_text: list[str] = []

    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()
        if text:
            page_text.append(f"--- Page {index} ---\n{text}")

    return "\n\n".join(page_text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract plain text from a PDF file.")
    parser.add_argument("pdf_file", type=Path, help="Path to the PDF file.")
    parser.add_argument("-o", "--output", type=Path, help="Optional output text file.")
    args = parser.parse_args()

    if not args.pdf_file.exists():
        print(f"PDF file not found: {args.pdf_file}", file=sys.stderr)
        return 2

    try:
        text = extract_pdf_text(args.pdf_file)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote extracted text to {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
