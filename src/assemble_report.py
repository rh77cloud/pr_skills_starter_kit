#!/usr/bin/env python3
"""Assemble reviewed Markdown section drafts into one Markdown report draft."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


DEFAULT_ORDER = [
    "1_3_risk_rating.md",
    "2_1_1_development_data.md",
    "2_1_2_implementation_data.md",
    "2_1_3_model_framework.md",
    "2_1_4_assumptions_limitations.md",
    "2_1_5_mathematical_structure_variables.md",
    "2_1_6_ongoing_monitoring.md",
    "2_1_7_model_documentation.md",
    "2_1_8_governance_controls.md",
]


def assemble_sections(section_dir: Path, output_file: Path) -> int:
    if not section_dir.exists():
        print(f"Section directory not found: {section_dir}", file=sys.stderr)
        return 2

    parts: list[str] = []
    missing: list[str] = []
    for filename in DEFAULT_ORDER:
        path = section_dir / filename
        if not path.exists():
            missing.append(filename)
            continue
        parts.append(path.read_text(encoding="utf-8").strip())

    if not parts:
        print(f"No recognized section files found in {section_dir}", file=sys.stderr)
        return 1

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Wrote assembled report draft to {output_file}")

    if missing:
        print("Missing optional section files:")
        for filename in missing:
            print(f"- {filename}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble reviewed Markdown section drafts.")
    parser.add_argument("section_dir", type=Path, help="Directory containing reviewed section Markdown files.")
    parser.add_argument("output_file", type=Path, help="Output Markdown report path.")
    args = parser.parse_args()
    return assemble_sections(args.section_dir, args.output_file)


if __name__ == "__main__":
    raise SystemExit(main())
