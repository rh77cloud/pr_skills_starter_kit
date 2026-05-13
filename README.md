# PR Skills Starter Kit

This repository contains a starter set of Codex-style Markdown skills for drafting and refreshing Model Risk Management periodic review (PR) report sections.

The goal is to help an AI assistant update PR report language consistently while preserving validator judgment, prior report structure, evidence discipline, and formal Model Risk voice.

## What This Includes

```text
.
├── AGENTS.md
├── README.md
└── skills/
    ├── pr_report_orchestrator/
    │   └── SKILL.md
    ├── pr_section_update/
    │   └── SKILL.md
    ├── pr_ogm_assessment/
    │   └── SKILL.md
    └── pr_risk_rating/
        └── SKILL.md
```

## Skills

- `pr_report_orchestrator`: Coordinates the full PR update workflow, intake, evidence review, section sequencing, and routing to the right drafting skill.
- `pr_section_update`: Updates Sections 2.1.1 through 2.1.5, 2.1.7, and 2.1.8.
- `pr_ogm_assessment`: Updates Section 2.1.6 and ongoing monitoring subsections.
- `pr_risk_rating`: Updates Section 1.3 Risk Rating after the supporting sections are completed.

## Intended Workflow

1. Open the repository in Codex.
2. Ask Codex to read `AGENTS.md`.
3. Provide the prior PR report or similar report guidance.
4. Provide current-cycle materials, including model documentation, 1LOD ongoing monitoring materials, 2LOD assessment materials, and findings, if any.
5. Update Sections 2.1.1 through 2.1.8 one section at a time.
6. Draft Section 1.3 Risk Rating after the supporting sections have been reviewed.
7. Have a human validator review all conclusions, findings, approvals, and evidence sufficiency.

## Example Prompt

```text
Read AGENTS.md and use skills/pr_report_orchestrator/SKILL.md.
I am updating a Tier II PR report.
First ask me for the required intake information, then help me update Section 2.1.1 using skills/pr_section_update/SKILL.md.
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

- Add an intake form for collecting PR inputs.
- Add prompt templates for each section.
- Add example source materials and sample generated outputs.
- Add checks for missing required inputs before drafting.
- Add a report assembly workflow that combines reviewed sections into a single draft.

## Uploading to GitHub

From this folder, initialize git and push to a new GitHub repository:

```bash
cd /Users/RuiStation/Documents/Playground/pr_skills_starter_kit
git init
git add .
git commit -m "Initial commit"
gh repo create pr_skills_starter_kit --private --source=. --remote=origin --push
```

Use `--public` instead of `--private` if the repository should be public.
