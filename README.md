# PR Skills Starter Kit

This repository contains agent-ready Markdown skills, context files, templates, and workflow notes for drafting and refreshing Model Risk Management periodic review (PR) report sections.

The goal is to help an AI assistant update a prior PR report into a current-cycle PR report while preserving validator judgment, prior report structure, evidence discipline, and formal Model Risk voice.

## What This Includes

```text
.
├── AGENTS.md
├── GEMINI.md
├── README.md
├── docs/
│   ├── evidence_requirements.md
│   ├── project_definition.md
│   ├── section_map.md
│   └── workflow.md
├── examples/
│   ├── sample_intake.md
│   └── sample_section_2_1_1_output.md
├── local_inputs.example/
│   ├── findings/
│   ├── management_responses/
│   ├── model_documentation/
│   ├── ogm_1lod/
│   ├── ogm_2lod/
│   ├── prior_pr_report/
│   └── prior_validation/
├── outputs/
│   └── .gitkeep
├── skills/
│   ├── pr_report_orchestrator/
│   │   └── SKILL.md
│   ├── pr_section_update/
│   │   └── SKILL.md
│   ├── pr_ogm_assessment/
│   │   └── SKILL.md
│   └── pr_risk_rating/
│       └── SKILL.md
├── src/
│   ├── assemble_report.py
│   ├── check_intake.py
│   └── extract_docx_text.py
└── templates/
    ├── intake_template.md
    ├── ogm_prompt.md
    ├── risk_rating_prompt.md
    └── section_update_prompt.md
```

## Key Files

- `AGENTS.md`: General agent instructions and repository workflow.
- `GEMINI.md`: Gemini context file for Gemini CLI and Gemini-assisted agent sessions.
- `docs/workflow.md`: Clone-and-use workflow for VS Code and Gemini.
- `docs/section_map.md`: Standard section map used by this repository.
- `docs/evidence_requirements.md`: Evidence checklist by section.
- `templates/intake_template.md`: Intake form to complete before drafting.
- `templates/section_update_prompt.md`: Reusable prompt for Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
- `templates/ogm_prompt.md`: Reusable prompt for Section 2.1.6.
- `templates/risk_rating_prompt.md`: Reusable prompt for Section 1.3.
- `local_inputs.example/`: Safe example folder structure for confidential source evidence.
- `src/`: Lightweight helper scripts for checking intake, extracting DOCX text, and assembling section drafts.

## Skills

- `pr_report_orchestrator`: Coordinates the full PR update workflow, intake, evidence review, section sequencing, and routing to the right drafting skill.
- `pr_section_update`: Updates Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
- `pr_ogm_assessment`: Updates Section 2.1.6 and ongoing monitoring subsections.
- `pr_risk_rating`: Updates Section 1.3 Risk Rating after the supporting sections are completed.

## Intended Workflow

1. Clone the repository and open it in VS Code.
2. Ask Gemini or another agent to read `GEMINI.md` and `AGENTS.md`.
3. Provide the prior PR report or similar report guidance.
4. Provide current-cycle materials, including model documentation, 1LOD ongoing monitoring materials, 2LOD assessment materials, and findings, if any.
5. Complete `templates/intake_template.md`.
6. Update Sections 2.1.1 through 2.1.8 one section at a time.
7. Draft Section 1.3 Risk Rating after the supporting sections have been reviewed.
8. Have a human validator review all conclusions, findings, approvals, and evidence sufficiency.

## VS Code and Gemini Workflow

Clone the repo on your work computer:

```bash
git clone https://github.com/rh77cloud/pr_skills_starter_kit.git
cd pr_skills_starter_kit
code .
```

Then start with this prompt in Gemini:

```text
Read GEMINI.md, AGENTS.md, and skills/pr_report_orchestrator/SKILL.md.
Use templates/intake_template.md to help me prepare the PR intake.
After intake is complete, help me update Section 2.1.1 first.
Ask for missing inputs before drafting.
```

For confidential model evidence, keep source files outside the repository or in a local ignored folder. Do not commit model reports, production data, finding appendices, or internal documentation.

To create the ignored local input folder on your work machine:

```bash
cp -R local_inputs.example local_inputs
```

Then place confidential files under `local_inputs/`.

## Helper Scripts

Check whether a completed intake file still has obvious blank fields:

```bash
python src/check_intake.py outputs/INV_XXXX/intake.md
```

Extract text from a DOCX file for easier agent review:

```bash
python src/extract_docx_text.py local_inputs/prior_pr_report/prior_pr.docx -o outputs/INV_XXXX/source_text/prior_pr.txt
```

Assemble reviewed Markdown section drafts into one Markdown report draft:

```bash
python src/assemble_report.py outputs/INV_XXXX/sections outputs/INV_XXXX/pr_report_draft.md
```

## Required Intake Information

For a typical PR update, prepare the following inputs:

- Whether this is the first PR report for the model.
- Inventory number.
- Model name.
- Model tier.
- Current cycle period.
- Prior cycle period.
- Prior PR report or similar PR guidance.
- Current model documentation.
- Current-cycle 1LOD ongoing monitoring materials.
- Current-cycle 2LOD ongoing monitoring assessment.
- Findings appendix or finding descriptions, if applicable.
- Management responses or remediation updates, if applicable.
- Target section to update first.

Use `templates/intake_template.md` to collect this information.

## Section Mapping

| Report Section | Skill | Focus |
| --- | --- | --- |
| 2.1.1 Development Data | `pr_section_update` | Development sample, recalibration data, representativeness, and continued appropriateness. |
| 2.1.2 Implementation Data | `pr_section_update` | Production data sources, feeds, transformations, lineage, and data quality controls. |
| 2.1.3 Model Framework | `pr_section_update` | Methodology, approved use, scope, and whether changes require validation. |
| 2.1.4 Model Assumptions and Limitations | `pr_section_update` | Assumptions, limitations, compensating controls, and risk appetite. |
| 2.1.5 Mathematical Structure and Variables | `pr_section_update` | Formulas, variables, segmentation, calibration mechanics, and analytical structure. |
| 2.1.6 Ongoing Monitoring | `pr_ogm_assessment` | Monitoring plan, test results, thresholds, breaches, and 2LOD assessment. |
| 2.1.7 Model Documentation | `pr_section_update` | Documentation completeness, accuracy, currency, and standards compliance. |
| 2.1.8 Governance and Controls | `pr_section_update` | Data controls, manual processes, implementation controls, change management, and governance. |
| 1.3 Risk Rating | `pr_risk_rating` | Overall PR conclusion and risk rating narrative. |

## Drafting Guardrails

- Do not invent facts, findings, test results, evidence, or conclusions.
- Ask for current-cycle changes before drafting a section unless they were already provided.
- Preserve the prior report structure, tone, and validator voice.
- Refresh dates, cycle periods, evidence references, model name, and inventory number.
- Avoid verbatim reuse from the prior report.
- Incorporate relevant findings in the section where they apply.
- Draft Section 1.3 only after Sections 2.1.1 through 2.1.8 are updated.

## Human Review Required

These skills support drafting, but they do not replace validator judgment. A qualified reviewer should approve:

- Final report conclusions.
- Finding severity and status.
- Approval, conditional approval, or rejection decisions.
- Whether a model change requires new validation.
- Whether evidence is sufficient.
- Whether controls are effective.

## Recommended Next Build Steps

- Add sanitized examples for Sections 2.1.2 through 2.1.8 and 1.3.
- Add optional VS Code task files for common workflows.

## Uploading to GitHub

This repository is designed to be cloned and reused. If you fork or create a new version, initialize git and push to a new GitHub repository:

```bash
cd /path/to/pr_skills_starter_kit
git init
git add .
git commit -m "Initial commit"
gh repo create pr_skills_starter_kit --private --source=. --remote=origin --push
```

Use `--public` instead of `--private` if the repository should be public.
