# Periodic Review Workflow

## Overview

The PR report workflow updates a prior report into a current-cycle report. It is intentionally section-by-section so each conclusion can be tied to evidence and reviewed before moving to the next section.

## Step 1: Clone and Open

Clone the repository and open it in VS Code:

```bash
git clone https://github.com/rh77cloud/pr_skills_starter_kit.git
cd pr_skills_starter_kit
code .
```

## Step 2: Prepare Local Evidence

Keep confidential evidence outside the repository, or in an ignored local folder. This repository includes `local_inputs.example/` as a safe folder template. Copy it to `local_inputs/`:

```bash
cp -R local_inputs.example local_inputs
```

Recommended local evidence folders include:

```text
local_inputs/
  prior_pr_report/
  model_documentation/
  ogm_1lod/
  ogm_2lod/
  findings/
  management_responses/
  prior_validation/
```

Do not commit confidential evidence to git.

## Step 3: Complete Intake

Copy `templates/intake_template.md` into a working file, such as:

```text
outputs/INV_XXXX/intake.md
```

Fill in the inventory number, model name, cycle periods, material paths, findings, and the section to update first.

Optionally check for obvious blanks:

```bash
python src/check_intake.py outputs/INV_XXXX/intake.md
```

If source materials are DOCX files, optionally extract text for easier agent review:

```bash
python src/extract_docx_text.py local_inputs/prior_pr_report/prior_pr.docx -o outputs/INV_XXXX/source_text/prior_pr.txt
```

If source materials are PDF files, such as a prior validation report, optionally extract text:

```bash
python src/extract_pdf_text.py local_inputs/prior_validation/prior_validation_report.pdf -o outputs/INV_XXXX/source_text/prior_validation_report.txt
```

PDF extraction requires either `pypdf` or `PyPDF2`. If your work computer does not already have one installed, use:

```bash
python -m pip install pypdf
```

## Step 4: Start the Agent Session

Use this opening prompt with Gemini:

```text
Read GEMINI.md, AGENTS.md, and skills/pr_report_orchestrator/SKILL.md.
Use the completed intake file at outputs/INV_XXXX/intake.md.
Help me update Section 2.1.1 first.
Ask for any missing inputs before drafting.
```

## Step 5: Update Sections 2.1.1 Through 2.1.8

For each section:

1. Confirm what changed in the current cycle.
2. Confirm additional key discussion points.
3. Confirm relevant findings or observations.
4. Confirm whether the prior conclusion remains appropriate.
5. Review current-cycle evidence.
6. Draft report-ready language.
7. Save or paste the reviewed section into the working output.

Use:

- `templates/section_update_prompt.md` for Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
- `templates/ogm_prompt.md` for Section 2.1.6.

For OGM graphs and tables, use the 2LOD OGM assessment as the guided source. Paste important exhibits into the 2LOD assessment file and add reviewer notes using `templates/ogm_graph_table_notes_template.md`. The agent should use those notes to update the PR discussion instead of guessing from visual appearance alone.

Recommended reviewed section filenames:

```text
outputs/INV_XXXX/sections/
  1_3_risk_rating.md
  2_1_1_development_data.md
  2_1_2_implementation_data.md
  2_1_3_model_framework.md
  2_1_4_assumptions_limitations.md
  2_1_5_mathematical_structure_variables.md
  2_1_6_ongoing_monitoring.md
  2_1_7_model_documentation.md
  2_1_8_governance_controls.md
```

## Step 6: Draft Risk Rating Section 1.3

Draft Section 1.3 only after Sections 2.1.1 through 2.1.8 are updated. Use `templates/risk_rating_prompt.md`.

The risk rating should summarize:

- Approval conclusion.
- Model method and use.
- Data and framework conclusions.
- Assumptions, limitations, variables, and structure conclusions.
- Ongoing monitoring and 2LOD assessment.
- Documentation, governance, and controls.
- Findings and impact on continued use.

## Step 7: Human Review

The generated report language must be reviewed by a qualified validator. Human review is required for evidence sufficiency, findings, approval conclusion, and final risk rating.

## Optional: Assemble Reviewed Sections

After human review, assemble the Markdown section files:

```bash
python src/assemble_report.py outputs/INV_XXXX/sections outputs/INV_XXXX/pr_report_draft.md
```
