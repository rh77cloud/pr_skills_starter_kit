#!/usr/bin/env python3
"""Extract plain text from a DOCX file for agent review."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import zipfile
import xml.etree.ElementTree as ET


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def paragraph_text(paragraph: ET.Element) -> str:
    pieces: list[str] = []
    for node in paragraph.iter():
        if node.tag == f"{{{NS['w']}}}t" and node.text:
            pieces.append(node.text)
        elif node.tag == f"{{{NS['w']}}}tab":
            pieces.append("\t")
        elif node.tag == f"{{{NS['w']}}}br":
            pieces.append("\n")
    return "".join(pieces).strip()


def extract_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as docx:
        xml_bytes = docx.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    paragraphs = []
    for paragraph in root.findall(".//w:p", NS):
        text = paragraph_text(paragraph)
        if text:
            paragraphs.append(text)
    return "\n\n".join(paragraphs)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract plain text from a DOCX file.")
    parser.add_argument("docx_file", type=Path, help="Path to the DOCX file.")
    parser.add_argument("-o", "--output", type=Path, help="Optional output text file.")
    args = parser.parse_args()

    if not args.docx_file.exists():
        print(f"DOCX file not found: {args.docx_file}", file=sys.stderr)
        return 2

    text = extract_docx_text(args.docx_file)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote extracted text to {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
