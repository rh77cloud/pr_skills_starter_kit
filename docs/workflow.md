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

Keep confidential evidence outside the repository, or in an ignored local folder. Recommended local evidence folders include:

```text
local_inputs/
  prior_pr/
  model_documentation/
  ogm_1lod/
  ogm_2lod/
  findings/
  management_responses/
```

Do not commit confidential evidence to git.

## Step 3: Complete Intake

Copy `templates/intake_template.md` into a working file, such as:

```text
outputs/INV_XXXX/intake.md
```

Fill in the inventory number, model name, cycle periods, material paths, findings, and the section to update first.

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
