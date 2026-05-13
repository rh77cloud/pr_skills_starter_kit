# Source Helpers

This folder contains lightweight helper scripts for running the PR drafting workflow.

The scripts are intentionally simple and dependency-light so they are easy to run on a work computer.

- `check_intake.py`: Checks a completed intake Markdown file for obvious blank fields.
- `extract_docx_text.py`: Extracts plain text from a DOCX file.
- `extract_pdf_text.py`: Extracts plain text from a PDF file using `pypdf` or `PyPDF2`.
- `assemble_report.py`: Combines reviewed Markdown sections into one Markdown report draft.
- `replace_docx_sections.py`: Copies a prior PR DOCX template and replaces recognized section bodies with reviewed Markdown drafts.
