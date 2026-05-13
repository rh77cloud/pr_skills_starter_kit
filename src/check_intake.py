#!/usr/bin/env python3
"""Check a PR intake Markdown file for blank fields."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


FIELD_RE = re.compile(r"^\s*-\s+([^:\n]+):\s*(.*)$")
PLACEHOLDER_RE = re.compile(r"\[[^\]]+\]|Yes / No|Approved / Conditionally Approved / Rejected")


def find_missing_fields(path: Path) -> list[str]:
    missing: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        match = FIELD_RE.match(line)
        if not match:
            continue
        field, value = match.groups()
        value = value.strip()
        if not value or PLACEHOLDER_RE.search(value):
            missing.append(f"line {line_number}: {field}")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a PR intake Markdown file for blank fields.")
    parser.add_argument("intake_file", type=Path, help="Path to the completed intake Markdown file.")
    args = parser.parse_args()

    if not args.intake_file.exists():
        print(f"Intake file not found: {args.intake_file}", file=sys.stderr)
        return 2

    missing = find_missing_fields(args.intake_file)
    if not missing:
        print(f"OK: no obvious blank intake fields found in {args.intake_file}")
        return 0

    print(f"Missing or placeholder intake fields found in {args.intake_file}:")
    for item in missing:
        print(f"- {item}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
