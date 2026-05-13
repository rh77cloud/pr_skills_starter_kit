#!/usr/bin/env python3
"""Replace PR report sections in a DOCX copy using reviewed Markdown drafts.

This helper is intentionally semi-automated. It preserves the source DOCX as the
template, keeps existing section heading paragraphs, and replaces body paragraphs
between recognized section headings with reviewed Markdown text.

Human review is required after generation, especially for reports with complex
tables, figures, comments, tracked changes, headers/footers, or section breaks.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
import re
import shutil
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
XML_NS = "http://www.w3.org/XML/1998/namespace"
ET.register_namespace("w", W_NS)

SECTION_FILES = {
    "1.3": "1_3_risk_rating.md",
    "2.1.1": "2_1_1_development_data.md",
    "2.1.2": "2_1_2_implementation_data.md",
    "2.1.3": "2_1_3_model_framework.md",
    "2.1.4": "2_1_4_assumptions_limitations.md",
    "2.1.5": "2_1_5_mathematical_structure_variables.md",
    "2.1.6": "2_1_6_ongoing_monitoring.md",
    "2.1.7": "2_1_7_model_documentation.md",
    "2.1.8": "2_1_8_governance_controls.md",
}

SECTION_HEADING_RE = re.compile(r"^(1\.3|2\.1\.[1-8])(?:\s|\b)")
MARKDOWN_HEADING_RE = re.compile(r"^#{1,6}\s+")


def w_tag(name: str) -> str:
    return f"{{{W_NS}}}{name}"


def paragraph_text(paragraph: ET.Element) -> str:
    pieces: list[str] = []
    for text_node in paragraph.iter(w_tag("t")):
        if text_node.text:
            pieces.append(text_node.text)
    return "".join(pieces).strip()


def paragraph_section(paragraph: ET.Element) -> str | None:
    match = SECTION_HEADING_RE.match(paragraph_text(paragraph))
    if match:
        return match.group(1)
    return None


def clean_markdown_line(line: str) -> str:
    line = MARKDOWN_HEADING_RE.sub("", line.strip())
    line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
    line = re.sub(r"\*([^*]+)\*", r"\1", line)
    line = re.sub(r"`([^`]+)`", r"\1", line)
    return line.strip()


def markdown_paragraphs(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    paragraphs: list[str] = []
    buffer: list[str] = []

    for raw_line in text.splitlines():
        line = clean_markdown_line(raw_line)
        if not line:
            if buffer:
                paragraphs.append(" ".join(buffer).strip())
                buffer = []
            continue
        if SECTION_HEADING_RE.match(line):
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        buffer.append(line)

    if buffer:
        paragraphs.append(" ".join(buffer).strip())

    return [paragraph for paragraph in paragraphs if paragraph]


def make_paragraph(text: str, style_source: ET.Element | None) -> ET.Element:
    paragraph = ET.Element(w_tag("p"))
    if style_source is not None:
        source_ppr = style_source.find(w_tag("pPr"))
        if source_ppr is not None:
            paragraph.append(deepcopy(source_ppr))

    run = ET.SubElement(paragraph, w_tag("r"))
    text_node = ET.SubElement(run, w_tag("t"))
    text_node.set(f"{{{XML_NS}}}space", "preserve")
    text_node.text = text
    return paragraph


def load_docx_xml(path: Path) -> tuple[dict[str, bytes], ET.ElementTree]:
    with zipfile.ZipFile(path, "r") as docx:
        contents = {name: docx.read(name) for name in docx.namelist()}
    tree = ET.ElementTree(ET.fromstring(contents["word/document.xml"]))
    return contents, tree


def write_docx(contents: dict[str, bytes], tree: ET.ElementTree, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    contents = dict(contents)
    contents["word/document.xml"] = ET.tostring(
        tree.getroot(),
        encoding="utf-8",
        xml_declaration=True,
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp_path = Path(tmp.name)

    try:
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as docx:
            for name, data in contents.items():
                docx.writestr(name, data)
        shutil.move(str(tmp_path), output_path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def replace_sections(template_docx: Path, section_dir: Path, output_docx: Path) -> int:
    contents, tree = load_docx_xml(template_docx)
    body = tree.getroot().find(f".//{w_tag('body')}")
    if body is None:
        print("Could not find DOCX body.", file=sys.stderr)
        return 2

    children = list(body)
    headings: list[tuple[ET.Element, str]] = []
    for child in children:
        if child.tag != w_tag("p"):
            continue
        section = paragraph_section(child)
        if section:
            headings.append((child, section))

    if not headings:
        print("No supported section headings found. Expected headings like '2.1.1' or '1.3'.", file=sys.stderr)
        return 1

    replacements = 0
    heading_elements = [heading for heading, _ in headings]
    for heading, section in reversed(headings):
        section_file = section_dir / SECTION_FILES.get(section, "")
        if not section_file.exists():
            continue

        current_children = list(body)
        original_index = current_children.index(heading)
        later_heading_indexes = [
            current_children.index(item)
            for item in heading_elements
            if item in current_children and current_children.index(item) > original_index
        ]
        end_index = min(later_heading_indexes) if later_heading_indexes else len(current_children)

        style_source = None
        for candidate in current_children[original_index + 1 : end_index]:
            if candidate.tag == w_tag("p"):
                style_source = candidate
                break

        for child in current_children[original_index + 1 : end_index]:
            body.remove(child)

        insert_at = list(body).index(current_children[original_index]) + 1
        for paragraph in reversed(markdown_paragraphs(section_file)):
            body.insert(insert_at, make_paragraph(paragraph, style_source))

        replacements += 1

    if replacements == 0:
        print(f"No matching section draft files found in {section_dir}", file=sys.stderr)
        return 1

    write_docx(contents, tree, output_docx)
    print(f"Wrote semi-automated DOCX draft to {output_docx}")
    print(f"Replaced {replacements} section(s). Human review is required before delivery.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replace recognized PR sections in a DOCX copy using reviewed Markdown drafts."
    )
    parser.add_argument("template_docx", type=Path, help="Prior/latest PR report DOCX to use as the template.")
    parser.add_argument("section_dir", type=Path, help="Directory containing reviewed section Markdown files.")
    parser.add_argument("output_docx", type=Path, help="Output DOCX draft path.")
    args = parser.parse_args()

    if not args.template_docx.exists():
        print(f"Template DOCX not found: {args.template_docx}", file=sys.stderr)
        return 2
    if not args.section_dir.exists():
        print(f"Section directory not found: {args.section_dir}", file=sys.stderr)
        return 2

    return replace_sections(args.template_docx, args.section_dir, args.output_docx)


if __name__ == "__main__":
    raise SystemExit(main())
